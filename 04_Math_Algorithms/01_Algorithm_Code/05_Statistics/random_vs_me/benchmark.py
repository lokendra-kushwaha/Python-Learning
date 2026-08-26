"""
======================================================================
Performance Benchmarking: Custom Stats Engine vs Python Built-in
======================================================================

This script serves as a stress test for data generation and CPU utilization.
It compares a custom pure-Python random logic against Python's C-optimized 
built-in 'random' module. 

It tests 4 scenarios to demonstrate the impact of IPC (Inter-Process 
Communication) overhead and why Single-Process List Comprehensions 
often beat Multiprocessing for lightweight tasks.
"""
import sys
import os
current_dir = os.path.dirname(os.fspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

logic_dir = os.path.abspath(os.path.join(current_dir, "../../../..", "03_Python_Logics", "modules"))
print(logic_dir)
sys.path.append(logic_dir)

import time
# Importing the custom random module.
try:
    import custom_randint # type: ignore
except ImportError:
    print("Warning: custom_randint.py module not found.")
import random
from core.vector import Vector
from descriptive.central import mean, median, mode
import multiprocessing
from concurrent.futures import ProcessPoolExecutor


# ---------------------------------------------------------
# Multiprocessing Workers (Using the 'Chunking' Method)
# ---------------------------------------------------------
# Why chunking? Sending 100,000 individual tasks to CPU cores causes 
# massive IPC overhead (taking 30+ seconds). Instead, we send a "chunk" 
# of tasks to each core, reducing communication delays drastically.

def custom_chunk_worker(chunk_size):
    """Generates a chunk of data using the custom pure-Python randint."""
    return [custom_randint.random_randint(1, 100) for _ in range(chunk_size)]

def builtin_chunk_worker(chunk_size):
    """Generates a chunk of data using Python's C-optimized random module."""
    return [random.randint(1, 100) for _ in range(chunk_size)]

# ---------------------------------------------------------
# Main Execution Benchmark
# ---------------------------------------------------------
def main():
    TOTAL_ITEMS = 100_000
    cpu_cores = multiprocessing.cpu_count()
    
    # Calculate how many items each CPU core should process
    chunk_size = TOTAL_ITEMS // cpu_cores
    chunks_list = [chunk_size] * cpu_cores 
    
    print("==================================================")
    print(f"🚀 CPU BENCHMARK | Items: {TOTAL_ITEMS} | Cores: {cpu_cores} 🚀")
    print("==================================================\n")

    # ---------------------------------------------------------
    # ROUND 1: Custom Engine (Pure Python Logic)
    # ---------------------------------------------------------
    print("--- ROUND 1: CUSTOM ENGINE ---")
    
    # Case 1: Standard List Comprehension (Single Core)
    start_time = time.perf_counter()
    data1 = [custom_randint.random_randint(1, 100) for _ in range(TOTAL_ITEMS)]
    time1 = time.perf_counter() - start_time
    print(f"Case 1 (Custom + Single Process): {time1:.4f} seconds")

    # Case 2: Multiprocessing using Chunks (Multi-Core)
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=cpu_cores) as executor:
        results = executor.map(custom_chunk_worker, chunks_list)
    
    # Flatten the returned list of lists into a single 1D list
    data2 = [num for chunk in results for num in chunk]
    time2 = time.perf_counter() - start_time
    print(f"Case 2 (Custom + Multi-Process):  {time2:.4f} seconds\n")

    # ---------------------------------------------------------
    # ROUND 2: Built-in Engine (C-Language Optimized)
    # ---------------------------------------------------------
    print("--- ROUND 2: BUILT-IN ENGINE ---")
    
    # Case 3: Standard List Comprehension (Single Core)
    # Note: This is usually the fastest due to C-level optimizations.
    start_time = time.perf_counter()
    data3 = [random.randint(1, 100) for _ in range(TOTAL_ITEMS)]
    time3 = time.perf_counter() - start_time
    print(f"Case 3 (Built-in + Single Process): {time3:.4f} seconds")

    # Case 4: Multiprocessing using Chunks (Multi-Core)
    # Note: Slower than Case 3 due to the OS overhead of creating processes.
    start_time = time.perf_counter()
    with ProcessPoolExecutor(max_workers=cpu_cores) as executor:
        results = executor.map(builtin_chunk_worker, chunks_list)
        
    data4 = [num for chunk in results for num in chunk]
    time4 = time.perf_counter() - start_time
    print(f"Case 4 (Built-in + Multi-Process):  {time4:.4f} seconds\n")

if __name__ == '__main__':
    main()