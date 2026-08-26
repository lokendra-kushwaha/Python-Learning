"""
======================================================================
Core Statistics Module Tester & Integration Script
======================================================================

This script tests the functionality and performance of our custom 
Statistics Engine. It specifically evaluates:
1. The custom Vector data container.
2. Central Tendency measures: Mean, Median, and Mode.
3. Execution time for processing 100,000 items.

It also handles dynamic path resolution to import custom logic 
modules from different project directories.
"""

import sys
import os
import time
import random
import concurrent.futures

# =========================================================
# PATH CONFIGURATION (Dynamic Imports)
# =========================================================
# Setting up paths so Python can find our custom modules across folders
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Linking the external '03_Python_Logics' folder to import custom_randint
logic_dir = os.path.abspath(os.path.join(current_dir, "../../../..", "03_Python_Logics", "modules"))
print(f"Logic Directory Linked: {logic_dir}\n")
sys.path.append(logic_dir)

# =========================================================
# CUSTOM IMPORTS
# =========================================================
import custom_randint  # type: ignore
from core.vector import Vector
from descriptive.central import mean, median, mode


# =========================================================
# DATA GENERATION FUNCTIONS
# =========================================================
def create_data(_):
    """Worker function to generate a single random number."""
    return custom_randint.random_randint(1, 100)

def get_data():
    """Generates 100,000 numbers using Multiprocessing (without chunking)."""
    items = range(100_000)
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(create_data, items)
        return list(results)


# =========================================================
# MAIN EXECUTION & STATS TESTING
# =========================================================
def main():
    print("🚀 INITIATING STATS ENGINE TEST 🚀")
    print("Generating data and calculating metrics...\n")
    
    start = time.perf_counter()
    
    # 1. Generate 100,000 items using list comprehension
    data2 = [custom_randint.random_randint(1, 100) for _ in range(100_000)]
    
    # =====================================================
    # 🧪 CUSTOM STATISTICS MODULE TESTING BLOCK 🧪
    # =====================================================
    
    # Test 1: Loading data into our secure Vector container
    vec = Vector(data2)
    
    # Test 2: Calculating Mean
    mean_data = mean(vec)
    print(f"✅ Calculated Mean:   {mean_data}")

    # Test 3: Calculating Median
    median_data = median(vec)
    print(f"✅ Calculated Median: {median_data}")

    # Test 4: Calculating Mode(s)
    mode_data = mode(vec)
    print(f"✅ Calculated Mode:   {mode_data}")
    
    # =====================================================
    
    end = time.perf_counter()
    
    print("\n========================================")
    print(f"⏱️  Total Execution Time: {end - start:.4f} seconds")
    print("========================================")

if __name__ == "__main__":
    main()   