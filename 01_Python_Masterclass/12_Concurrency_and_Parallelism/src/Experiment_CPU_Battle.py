# 🌟 ================================================================================= 🌟
# 🥊 EXPERIMENT: THE ULTIMATE CPU BATTLE (Sync vs Multiprocessing vs Threading)
# 🌟 ================================================================================= 🌟
"""
🎯 THE ARCHITECT'S LESSONS FROM THIS EXPERIMENT:

1. THE GIL REALITY (Why Threading failed here):
   Threading provides the "Illusion of Parallelism". It only works when tasks have "Wait Times". 
   For continuous heavy math (CPU-Bound), the GIL never drops. Hence, Threading performs exactly 
   like Synchronous code.

2. IS THE GIL FLEXIBLE? (The Smart Release Mechanism):
   You might think Python made the GIL "flexible" to allow Threading. 
   Technically, the GIL is strictly locked during math/CPU tasks. However, the CPython 
   interpreter is designed with a "Smart Release" mechanism (Py_BEGIN_ALLOW_THREADS). 
   The exact millisecond your code hits a waiting period (I/O Bound like time.sleep 
   or network calls), Python deliberately DROPS the GIL, allowing other threads to run. 
   This is why Threading works beautifully for I/O, but fails for CPU-bound tasks.

3. THE ULTIMATE "WHY": WHY DOES THE GIL EXIST AT ALL?
   If the GIL makes multithreading useless for CPU tasks, why did Python creators build it? 
   The answer is Memory Safety (Reference Counting). 
   
   - The Problem: Python manages memory using 'Reference Counting'. Every variable tracks how 
     many places are using it. If we had True Parallelism (no GIL), two threads might try to 
     access or modify the same variable's reference count at the exact same microsecond.
     
   - The Crash: Due to a 'Race Condition', the count would get corrupted. It might drop to -1 
     causing a fatal 'Segmentation Fault' (C-level crash), or delete the memory while another 
     thread is still reading it. The GIL is the "Master Lock" that prevents this disaster by 
     forcing threads to access memory one at a time.
     
   - Why not just remove the Garbage Collector? We can't! RAM is limited. If the Garbage 
     Collector doesn't constantly delete unused variables (where reference count == 0), the 
     system's RAM will fill up in minutes, causing a catastrophic 'Memory Leak' and freezing 
     the entire computer. The GIL is the necessary price we pay for automated memory safety!

4. THE MULTIPROCESSING CHEAT CODE (Multiple Interpreters = Multiple GILs):
   How does Multiprocessing bypass the GIL? By fooling it! 
   Python doesn't break the original GIL. Instead, the OS spawns entirely NEW Python Interpreters 
   for each CPU core. If you have 4 cores, you get 4 separate Python interpreters in memory. 
   Each interpreter gets its own isolated RAM and its own personal GIL. 
   Since they don't share memory, they don't fight for the same lock. True Parallelism achieved!

5. THE PICKLE BOTTLENECK (IPC - Inter Process Communication):
   Because Multiprocessing uses isolated interpreters, they cannot share variables directly. 
   If a worker returns a massive object, the OS spends huge time serializing (Pickling) that data 
   to send it across to the main interpreter. 
   Rule: Do heavy calculations in the worker, but return minimal data!

6. THE WINDOWS SPAWN RULE (if __name__ == '__main__'):
   Windows doesn't use "fork" to copy processes; new interpreters import your script from top to bottom. 
   Always wrap execution code in `if __name__ == '__main__'` to prevent recursive Fork Bombs.
"""

import time
import sys
import concurrent.futures

# Increasing recursion limit just in case, though we are using a loop here
sys.setrecursionlimit(2000)

# ====================================================================================
# 🧠 THE CPU-BOUND FUNCTION
# ====================================================================================
def heavy_math(num):
    """A purely continuous CPU-Bound task with zero I/O wait."""
    ans = 1
    for i in range(1, num):
        ans *= i
        
    # 🚨 CRITICAL ARCHITECTURE DECISION:
    # Returning 'ans' (a massive number) would choke the IPC pipeline because the OS 
    # has to 'pickle' (serialize) it to send it back from the worker to the main process. 
    # To measure pure CPU speed, we return a tiny integer.
    return 1 


# ====================================================================================
# 🏁 THE BATTLEGROUND
# ====================================================================================
if __name__ == "__main__":
    
    # 100 tasks of calculating the factorial of 50,000
    numbers = [50000 for _ in range(100)] 
    
    print("\n🔥 THE ULTIMATE CPU BATTLE 🔥\n")

    # ---------------------------------------------------------
    # 1. SYNCHRONOUS (1 Core, 1 GIL)
    # ---------------------------------------------------------
    print("1. Starting Synchronous Test (Linear Execution)...")
    start_sync = time.perf_counter()
    
    for n in numbers:
        heavy_math(n)
        
    print(f"✅ Synchronous time = {time.perf_counter() - start_sync:.2f} seconds\n")

    # ---------------------------------------------------------
    # 2. MULTIPROCESSING (All Cores, Multiple GILs)
    # ---------------------------------------------------------
    # Here, the workload is distributed across true hardware cores. 
    # No GIL bottleneck. Time should drop significantly (e.g., 2.5x faster).
    print("2. Starting Multiprocessing Test (True Parallelism)...")
    start_multi = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(heavy_math, numbers)
        
    print(f"🚀 Multiprocessing time = {time.perf_counter() - start_multi:.2f} seconds\n")

    # ---------------------------------------------------------
    # 3. THREADING (1 Core, 1 GIL + Overhead)
    # ---------------------------------------------------------
    # Since there are no "wait states" in heavy_math, the GIL remains locked by one thread.
    # The OS desperately tries to context-switch, wasting time. 
    # Result: It acts like Synchronous code, proving Threading fails for CPU Bound tasks.
    print("3. Starting Threading Test (Illusion of Parallelism)...")
    start_thread = time.perf_counter()
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(heavy_math, numbers)
        
    print(f"🐢 Threading time = {time.perf_counter() - start_thread:.2f} seconds\n")

    print("-" * 60)
    print("🎯 CONCLUSION: Threads for I/O Bound. Processes for CPU Bound!")
    print("-" * 60)
    
# 🌟 ================================================================================= 🌟