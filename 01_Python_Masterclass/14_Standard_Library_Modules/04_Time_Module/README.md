# ⏳ The time Module: Timekeeping & Benchmarking

## 📌 Overview
The time module is essential for scheduling tasks, converting time formats for databases/logs, and accurately measuring the performance (benchmarking) of your Python code.

## 🚀 Core Capabilities
*   **The Epoch:** Understanding computer time, which counts seconds starting from January 1, 1970 (time.time()).
*   **Timezones:** Differentiating between Local Time (for users) and UTC Time (for global servers).
*   **String Formatting:** 
    *   strftime: Converts a Time Object into a readable string (for logs).
    *   strptime: Parses a string back into a Time Object (for databases).
*   **Thread Suspension:** Pausing code execution using time.sleep().
*   **Benchmarking:** Measuring absolute code execution speed.

## ⚡ Benchmarking Best Practices
Never use time.time() to measure how fast your code runs, as it can be affected by system clock updates. 
*   Use **time.perf_counter()** for real-world execution time.
*   Use **time.process_time()** to measure purely the CPU effort (ignores sleep delays).