# 🌟 ================================================================================= 🌟
# 🚀                 Module 12: MULTITHREADING & SYSTEM ARCHITECTURE
# 🌟 ================================================================================= 🌟

import time
import threading
import concurrent.futures
import requests

# ====================================================================================
# 🧠 THE FOUNDATION: I/O BOUND vs CPU BOUND (Memory & Hardware Level)
# ====================================================================================
# Before understanding Threading, you must understand what your CPU is actually doing.
#
# 🔴 CPU Bound Tasks:
# - What it is: Tasks that require heavy number crunching (e.g., mathematical loops, 
#   Machine Learning, 3D Rendering).
# - Memory/Hardware Level: The CPU's ALUs (Arithmetic Logic Units) are working at 100% 
#   capacity. It is sweating. 
# - Solution: Threading DOES NOT work here. You need `multiprocessing` to use multiple cores.
#
# 🟢 I/O Bound Tasks (Input/Output):
# - What it is: Tasks that wait for external operations to finish (e.g., reading/writing 
#   to a file system, network operations, downloading from the internet).
# - Memory/Hardware Level: The CPU sends a request to the Network Card or Hard Drive and 
#   then literally does NOTHING. It sits completely idle (0% usage) waiting for the data 
#   to arrive. This idle time is a massive waste of processing power.
# - Solution: Multithreading! We use this "waiting time" to start other tasks.


print("\n--- 1. SYNCHRONOUS EXECUTION (The Normal Way) ---")
# 🧠 EXPLANATION: Synchronous means executing one after the other. 
# The CPU must wait for the first task to finish completely before looking at the second task.

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    # When Python hits time.sleep(1), the CPU enters an "Idle/Wait State". 
    # It stares at the wall for 1 second.
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()
print(f"Normal execution finished in {round(finish - start, 2)} second(s).\n")
# Output: ~2 seconds. (1 second for the first + 1 second for the second).


# ====================================================================================
# 🌉 THE BRIDGE: WHY WAS THREADING INVENTED? (The "Aha!" Moment)
# ====================================================================================
# 🧠 DEEP EXPLANATION:
# Why did the synchronous code above take 2 seconds? 
# When the first function reached `time.sleep(1)`, our CPU literally went "IDLE". 
# It stared at the wall for 1 full second and did not read the upcoming code. 
# When the first wait ended, it started the second function and stared at the wall again. 
# 
# Computer Scientists realized: "The CPU operates in Nano-seconds. Letting it sit idle 
# like this is an insult to the hardware!"
# 
# This is exactly where THREADING was born.
# The core concept of Threading is "CONCURRENCY" (Context Switching).
# It means instructing the CPU: "While the first function is waiting for the internet 
# or sleeping (Wait State), do not sit idle! Instantly context-switch and start 
# executing the second function!"
# This way, the CPU cleverly overlaps the wait times of both functions simultaneously, 
# dropping the total execution time from 2 seconds down to 1 second.


# ====================================================================================
# 🧠 INTRODUCING THE THREADING MODULE (The Manual OS-Level Way)
# ====================================================================================
print("--- 2. MULTITHREADING MODULE (Manual Way) ---")

start = time.perf_counter()

def do_something():
    print('Sleeping 1 second...')
    # When Python hits time.sleep(1), the CPU enters an "Idle/Wait State". 
    # It stares at the wall for 1 second.
    time.sleep(1)
    print('Done Sleeping...')

# We are creating "Thread Objects". 
# Memory Level: The Operating System allocates a dedicated chunk of RAM (Stack memory) 
# for each of these workers.
t1 = threading.Thread(target=do_something) 
t2 = threading.Thread(target=do_something)

# 🚀 Starting the Threads
t1.start()
t2.start()

# ❓ QUESTION: Why did it finish in 0.001 seconds when we didn't use join()?
# 🧠 EXPLANATION: 
# When you execute `t1.start()`, the Main Python Thread (the main script) tells the OS: 
# "Hey, start running t1 in the background."
# The crucial part is: The Main Thread DOES NOT WAIT for t1 to finish! 
# It instantly moves to the next line (`t2.start()`), and then instantly moves to the 
# timer calculation at the bottom. The background threads are still sleeping, but the 
# script has already printed the "Finished in..." statement. 

# ⚓ Joining the Threads (The Fix)
t1.join()
t2.join()

# ❓ QUESTION: How did join() give the correct time?
# 🧠 EXPLANATION: 
# `.join()` is a "Blocking" method. It literally tells the Main Python Thread: 
# "Stop executing the rest of the script. Do not move forward until t1 and t2 have 
# completely finished their execution and merged back into the main process."
# This forces the timer to wait until the 1-second sleep is actually over.

finish = time.perf_counter()
print(f"Manual Threading finished in {round(finish - start, 2)} second(s).\n")
# Output: ~1 second. Because both threads slept at the EXACT SAME TIME (Concurrency).


# ====================================================================================
# 🧠 RUNNING MULTIPLE THREADS IN A LOOP
# ====================================================================================
print("--- 3. MULTIPLE THREADS IN A LOOP ---")
start = time.perf_counter()

threads = []
# Creating 10 threads dynamically
for _ in range(10):
    t = threading.Thread(target=do_something)
    t.start()
    threads.append(t) # We must save them to a list so we can join them later

# We cannot join inside the first loop, otherwise it will wait for the first thread 
# to finish before starting the second one (defeating the purpose of threading).
for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"10 Threads Loop finished in {round(finish - start, 2)} second(s).\n")
# Output: Still ~1 second! 10 tasks were executed in the time it takes to do 1 task.


# ====================================================================================
# 🧠 PASSING ARGUMENTS TO THREADS
# ====================================================================================
print("--- 4. THREADING WITH ARGUMENTS ---")
start = time.perf_counter()

def do_something_args(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

threads = []
for _ in range(10):
    # We use the 'args' parameter. It MUST be an iterable (like a list or tuple).
    t = threading.Thread(target=do_something_args, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"Arguments Threading finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCURRENT.FUTURES (The Modern Abstraction - Python 3.2+)
# ====================================================================================
# ❓ QUESTION: What is concurrent.futures and why didn't they just update threading?
# 🧠 EXPLANATION: 
# The `threading` module is highly manual. If you have 10,000 URLs to download, 
# creating 10,000 OS-level threads will consume massive amounts of RAM and crash your CPU 
# due to "Context Switching Overhead". 
# `concurrent.futures` introduces a "ThreadPool". Instead of creating a new thread for 
# every task, it creates a pool of (e.g., 10) reusable threads. When a thread finishes 
# a task, it picks up the next one. It is vastly superior for memory management.

print("--- 5. CONCURRENT.FUTURES (Submit Method) ---")
start = time.perf_counter()

def do_something_future(seconds):
    print(f'Future Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Future Done Sleeping...{seconds}' # Returning instead of printing

# 'with' acts as a Context Manager. It automatically joins and cleans up threads when done.
with concurrent.futures.ThreadPoolExecutor() as executor:
    # submit() schedules a function to be executed and returns a "Future" object.
    # A Future is a promise: "I am executing in the background, check me later for the result."
    f1 = executor.submit(do_something_future, 1) 
    f2 = executor.submit(do_something_future, 1)
    
    # .result() waits for the thread to finish and captures the return value.
    print(f1.result()) 
    print(f2.result())

finish = time.perf_counter()
print(f"Submit execution finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCURRENT.FUTURES (Using as_completed in a Loop)
# ====================================================================================
print("--- 6. CONCURRENT.FUTURES (as_completed) ---")
start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    # List comprehension to submit 10 tasks
    results = [executor.submit(do_something_future, 1) for _ in range(10)]
    
    # as_completed() is an iterator. It yields the Future objects the exact moment 
    # they finish executing, regardless of the order they were submitted in.
    for f in concurrent.futures.as_completed(results):
        print(f.result()) 

finish = time.perf_counter()
print(f"as_completed Loop finished in {round(finish - start, 2)} second(s).\n")
# ❓ QUESTION: Why did this take 2 seconds in my original code?
# 🧠 EXPLANATION: In your original script, you created the `start` variable at the VERY 
# TOP of the script, and the `finish` variable at the VERY BOTTOM. It was adding the time 
# of ALL previous functions together! By resetting `start = time.perf_counter()` before 
# each block in this script, you will see it correctly takes ~1 second.


# ====================================================================================
# 🧠 CONCURRENT.FUTURES (Varying Wait Times)
# ====================================================================================
print("--- 7. CONCURRENT.FUTURES (Varying Times) ---")
start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = [executor.submit(do_something_future, sec) for sec in secs]
    
    # Because of as_completed, the 1-second thread will print first, even though 
    # the 5-second thread was submitted first!
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()
print(f"Varying times finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCURRENT.FUTURES (The map() Function - Industry Standard)
# ====================================================================================
# ❓ QUESTION: Why use map()? Is it a higher-order function?
# 🧠 EXPLANATION: 
# Yes! `map()` is a higher-order function because it takes another function as an argument.
# We use `map()` because it completely eliminates the need for loops, `submit()`, 
# and `as_completed()`. It automatically applies the iterable to the function, manages 
# the thread pooling, and returns the results IN THE EXACT ORDER they were passed, 
# (unlike as_completed which returns them as they finish).

print("--- 8. CONCURRENT.FUTURES (Using map) ---")
start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # One line of code replaces the entire loop and submission process.
    results = executor.map(do_something_future, secs)
    
    for result in results:
        print(result)

finish = time.perf_counter()
print(f"Map method finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 REAL-WORLD PRACTICAL EXAMPLE (Network I/O Bound Task)
# ====================================================================================
print("--- 9. REAL WORLD IMPLEMENTATION (Image Downloader) ---")

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()

def download_image(img_url):
    # 🧠 CPU Wait Time #1: Waiting for the internet server to respond.
    img_bytes = requests.get(img_url).content
    
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    
    # 🧠 CPU Wait Time #2: Waiting for the Hard Drive to write the physical file.
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

# Using ThreadPoolExecutor to drastically reduce the I/O wait times.
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

t2 = time.perf_counter()
print(f'Real-World Download finished in {round(t2-t1, 2)} seconds')

# 🌟 ================================================================================= 🌟