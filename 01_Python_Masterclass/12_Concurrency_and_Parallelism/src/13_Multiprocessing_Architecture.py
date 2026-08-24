# 🌟 ================================================================================= 🌟
# 🚀               Module 13: MULTIPROCESSING & TRUE PARALLELISM
# 🌟 ================================================================================= 🌟

import time
import multiprocessing
import concurrent.futures
from PIL import Image, ImageFilter

# ====================================================================================
# 🧠 CONCEPT 1: THE MULTIPROCESSING MODULE (The Old, Manual Way)
# ====================================================================================
# Why Multiprocessing? 
# For CPU-Bound tasks (like number crunching or image processing), the CPU is working 
# at 100% capacity. It never enters a "Wait State," so it NEVER releases the GIL.
# Threading fails here. The solution is Multiprocessing: bypassing the GIL by 
# creating entirely separate Python processes, each with its own memory, its own GIL, 
# and its own dedicated CPU Core.

print("\n--- 1. MULTIPROCESSING (Manual Way) ---")
start = time.perf_counter()

def do_something(seconds=1):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')

if __name__ == '__main__':
    # ❓ QUESTION: Why do we pass the function name (target=do_something) and not do_something()?
    # 🧠 EXPLANATION: If you write `do_something()`, Python will execute the function IMMEDIATELY 
    # right there on the main thread and pass its RETURN VALUE to the Process. We don't want that. 
    # We want to pass the "Function Object" itself so the child process can execute it later.

    # 🛠️ Creating Process Objects
    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_something)

    # 🚀 Starting Processes
    p1.start()
    p2.start()

    # ❓ QUESTION: Why did it only print time (0.00004 sec) when I didn't use join()?
    # 🧠 EXPLANATION: Just like threading, `.start()` only tells the OS to begin the process 
    # in the background. The Main Process DOES NOT WAIT. It instantly zooms past to the finish line.
    
    # ⚓ Joining Processes
    p1.join() 
    p2.join()

finish = time.perf_counter()
print(f"Manual Processing finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCEPT 2: RUNNING MULTIPLE PROCESSES IN A LOOP
# ====================================================================================
print("--- 2. MULTIPLE PROCESSES IN A LOOP ---")
start = time.perf_counter()

if __name__ == '__main__':
    processes = []
    
    for _ in range(10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        processes.append(p)

    # ❓ QUESTION: Why didn't we just run `p.join()` inside the first loop?
    # 🧠 EXPLANATION: If you put `p.join()` in the first loop, the code will:
    # 1. Start Process 1
    # 2. WAIT for Process 1 to completely finish (because of join)
    # 3. Then Start Process 2...
    # You would destroy the parallel execution! It would run synchronously taking 10 seconds.
    # By separating the loops, we START all 10 simultaneously, and THEN we wait for all of them.
    for process in processes: 
        process.join()

finish = time.perf_counter()
print(f"10 Processes Loop finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCEPT 3: PASSING ARGUMENTS AND THE "PICKLE" MYSTERY
# ====================================================================================
print("--- 3. PASSING ARGUMENTS (The Pickle Concept) ---")
start = time.perf_counter()

if __name__ == '__main__':
    processes = []
    for _ in range(10):
        # ❓ QUESTION: Why did Corey Schafer mention "Pickle" here? I can pass objects anywhere!
        # 🧠 EXPLANATION (System Architecture Level):
        # In Threading, all threads share the SAME RAM (Memory). They can easily read the same variables.
        # But in Multiprocessing, the OS creates 10 completely SEPARATE memory spaces. 
        # Process 2 cannot look inside the RAM of Process 1! 
        # So, how do we send the argument `[1.5]` from the Main Process to the Child Process?
        # Python uses a module called `pickle`. It serializes (converts) your data into a byte-stream, 
        # sends it over an OS pipe to the new process, and "unpickles" it there. 
        # (This means you CANNOT pass un-picklable objects like Database Connections or open files to a Process).
        p = multiprocessing.Process(target=do_something, args=[1.5]) 
        p.start()
        processes.append(p)

    for process in processes: 
        process.join()

finish = time.perf_counter()
print(f"Arguments passed finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCEPT 4: CONCURRENT.FUTURES (ProcessPoolExecutor)
# ====================================================================================
# The modern, highly abstracted way to handle multiprocessing without manual joins.

print("--- 4. CONCURRENT.FUTURES (as_completed) ---")
start = time.perf_counter()

def do_something_future(seconds):
    print(f'Future Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(do_something_future, sec) for sec in secs]
        
        # ❓ QUESTION: Why use as_completed()? What happens without it?
        # 🧠 EXPLANATION: 
        # Look at the 'secs' list. The 5-second process is submitted FIRST. The 1-second is LAST.
        # If we didn't use `as_completed` and just looped over `results` normally, our loop would 
        # BLOCK at the 5-second future. It would wait 5 whole seconds before printing anything, 
        # completely ignoring that the 1, 2, 3, and 4-second processes finished early!
        # `as_completed()` is an iterator that YIELDS a future the exact millisecond it finishes, 
        # regardless of the order it was submitted. The 1-second result will print first!
        for f in concurrent.futures.as_completed(results): 
            print(f.result())

finish = time.perf_counter()
print(f"as_completed finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCEPT 5: THE MAP FUNCTION & ERROR HANDLING
# ====================================================================================
print("--- 5. CONCURRENT.FUTURES (map method) ---")
start = time.perf_counter()

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        
        # `map` automatically submits the tasks and returns the results in the ORIGINAL order 
        # (unlike as_completed). It is the cleanest way to write parallel code.
        results = executor.map(do_something_future, secs)
        
        # ❓ QUESTION: How and why do we use try-except here?
        # 🧠 EXPLANATION: 
        # If one of your child processes crashes (e.g., division by zero), it DOES NOT throw an error 
        # when you submit it. The error is stored inside the result object. 
        # The exception is only raised when you actually try to RETRIEVE the result from the iterator.
        for result in results: 
            try:
                # The exception is thrown right here on this line if the process failed
                print(result)
            except Exception as e:
                print(f"A process failed with error: {e}")

finish = time.perf_counter()
print(f"Map method finished in {round(finish - start, 2)} second(s).\n")


# ====================================================================================
# 🧠 CONCEPT 6: REAL-WORLD PRACTICAL EXAMPLE (CPU Bound)
# ====================================================================================
print("--- 6. REAL WORLD: MASS IMAGE PROCESSING ---")
# 🧠 AI EXPLANATION: Why Multiprocessing here and not Threading?
# Processing high-resolution images (GaussianBlur, changing dimensions) is heavy MATH. 
# The CPU is crunching pixels at 100% capacity. There is no "Wait State." 
# If we used Threading, the GIL would bottleneck the entire program. Multiprocessing unlocks all CPU cores.

# Note: Ensure you have a 'processed' folder created in your directory for this to work.
img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

def process_image(img_name):
    # This block requires heavy CPU ALU (Arithmetic Logic Unit) calculation
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail((1200, 1200))
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

if __name__ == '__main__':
    t1_img = time.perf_counter()
    
    # Bypassing the GIL to process images simultaneously across multiple CPU cores
    if img_names: # Guard to prevent errors if the list is empty
        with concurrent.futures.ProcessPoolExecutor() as executor:
            executor.map(process_image, img_names)

    t2_img = time.perf_counter()
    print(f'Real-World Image Processing finished in {round(t2_img-t1_img, 2)} sec')

# 🌟 ================================================================================= 🌟