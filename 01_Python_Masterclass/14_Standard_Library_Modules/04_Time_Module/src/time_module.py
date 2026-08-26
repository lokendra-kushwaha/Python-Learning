"""
====================================================================================
⏳ STANDARD LIBRARY: THE 'time' MODULE (Deep Dive)
====================================================================================
Description: The 'time' module provides various time-related functions. 
             It is essential for scheduling tasks (sleeping), converting time 
             formats (for logs/databases), and benchmarking code performance.

Pro Tip: Different OS (Windows/Linux) handle time slightly differently, but 
         this module provides a unified interface for the developer.
====================================================================================
"""

import time

def section_divider(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")

# 🟢 1. THE EPOCH (The Beginning of Computer Time)
# ====================================================================================
section_divider("1. THE EPOCH (Computer's Birthday)")
"""
What is the Epoch?
Computers don't understand "August 2026". They count time in SECONDS starting 
from a specific point called the "Epoch" (January 1, 1970, 00:00:00 UTC).
"""
# time.time() returns the number of seconds passed since January 1, 1970.
current_seconds = time.time()
print(f"-> Seconds since Epoch (Jan 1, 1970): {current_seconds}")

# time.ctime() converts those raw seconds into a human-readable string
print(f"-> Human Readable Time (ctime)      : {time.ctime(current_seconds)}")


# 🟢 2. TIME STRUCTS (Local Time vs UTC Time)
# ====================================================================================
section_divider("2. TIME STRUCTURES (Local vs UTC)")
"""
Servers are often located in different countries. To avoid confusion, 
servers use UTC (Coordinated Universal Time), while users see Local Time.
"""
# 1. Local Time (Based on your computer's timezone, e.g., IST in India)
local_time_obj = time.localtime()
print(f"-> Local Time Object: {local_time_obj}")
print(f"   Year: {local_time_obj.tm_year}, Month: {local_time_obj.tm_mon}, Day: {local_time_obj.tm_mday}")

# 2. UTC Time (Global Standard Time)
utc_time_obj = time.gmtime()
print(f"\n-> UTC Time Object  : {utc_time_obj}")
print(f"   (Notice the difference in hours if you are not in the UK!)")


# 🟢 3. TIME FORMATTING (For Logs & Databases)
# ====================================================================================
section_divider("3. FORMATTING: strftime & strptime")
"""
- strftime (String Format Time): Converts a Time Object into a Custom String.
- strptime (String Parse Time): Converts a Custom String back into a Time Object.
"""
# --- A. Formatting (strftime) ---
# Directives: %Y (Year), %m (Month), %d (Day), %H (Hour 24), %I (Hour 12), %p (AM/PM)
formatted_time = time.strftime("%Y-%m-%d | %I:%M:%S %p", local_time_obj)
print(f"-> Custom Formatted String (strftime) : {formatted_time}")

# --- B. Parsing (strptime) ---
# Used heavily in Data Science when reading dates from a CSV or Database
database_date_string = "25 August 2026"
parsed_time_obj = time.strptime(database_date_string, "%d %B %Y")
print(f"-> Parsed from String (strptime)      : {parsed_time_obj.tm_year}-{parsed_time_obj.tm_mon}-{parsed_time_obj.tm_mday}")


# 🟢 4. PAUSING EXECUTION (Sleep)
# ====================================================================================
section_divider("4. PAUSING THE THREAD (Sleep)")
"""
time.sleep() halts the execution of the CURRENT thread. 
(Note: In advanced Asyncio, we NEVER use time.sleep, we use asyncio.sleep instead!)
"""
print("-> Going to sleep for 1.5 seconds...")
time.sleep(1.5)
print("-> Woke up!")

# 🟢 5. BENCHMARKING (The Architect's Tool)
# ====================================================================================
section_divider("5. CODE BENCHMARKING (perf_counter vs time)")

"""
Question: "How do you measure the execution speed of your code?"
Wrong Answer: time.time() -> It can be affected if the OS updates the system clock during execution.
Right Answer: time.perf_counter() -> A clock with the highest available resolution, strictly for measuring durations.
"""

# Let's test how fast Python can create a list of 5 million numbers
print("-> Benchmarking List Comprehension (5 Million items)...")

start_time = time.perf_counter()

# The Heavy Task
massive_list = [x * 2 for x in range(5_000_000)]

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"-> ⏱️ Task completed in: {execution_time:.4f} seconds")


# 🟢 6. PROCESS TIME (CPU Time vs Wall Time)
# ====================================================================================
section_divider("6. PROCESS TIME (CPU Load)")
"""
time.process_time() measures only the time the CPU spent EXECUTING your code.
It ignores sleep() time! This is crucial to know if your code is slow because 
of CPU calculations or because of network/sleep delays.
"""
start_cpu = time.process_time()
start_wall = time.perf_counter()

print("-> Calculating heavy math and then sleeping for 1 second...")
_ = [x ** 2 for x in range(1_000_000)] # Heavy CPU work
time.sleep(1) # Network delay / Idle time

end_cpu = time.process_time()
end_wall = time.perf_counter()

print(f"   ⏱️ Wall Time (Real world time passed) : {end_wall - start_wall:.4f} seconds")
print(f"   🔥 CPU Time (Actual processing time)  : {end_cpu - start_cpu:.4f} seconds (Ignores the 1s sleep!)")


print("\n" + "=" * 70)
print("🎯 CONCLUSION: You are now a master of Time & Performance Benchmarking!")
print("=" * 70)