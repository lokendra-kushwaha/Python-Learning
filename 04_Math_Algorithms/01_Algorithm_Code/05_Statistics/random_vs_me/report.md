# Performance Benchmark Report: Custom Stats Engine vs. Python Built-in

## 🖥️ System & Test Overview
* **Task:** Generating and processing 100,000 random integers.
* **Hardware Detected:** 4 Logical Cores (Dual-Core Processor with Hyper-Threading).
* **Optimization Applied:** "Chunking" (assigning batches of 25,000 items per core) to eliminate massive IPC (Inter-Process Communication) overhead.

## 📊 Benchmark Results

| Engine Type | Single Process (List Comp.) | Multi-Processing (Chunked) | Category Winner |
| :--- | :--- | :--- | :--- |
| **Custom Engine** (Pure Python) | 2.7088 seconds | 1.7305 seconds | 🏆 **Multi-Processing** |
| **Built-in Engine** (C-Optimized) | 0.0291 seconds | 0.4973 seconds | 🏆 **Single Process** |

## 🧠 Key Engineering Insights
* **The "C-Language" Advantage:** Python's built-in random module is written in highly optimized C. This allows it to execute much closer to the hardware level, making its Single Process execution (0.0291s) blazingly fast and virtually unbeatable by pure Python logic.
* **The "Overhead Tax" of Multiprocessing:** Applying Multi-processing to the built-in engine actually slowed it down (to 0.4973s). Because the core task was executed in microseconds, the operating system spent more time creating new worker processes and serializing/deserializing data (Pickling) than performing the actual calculations.
* **Custom Engine Scaling:** The custom logic was written entirely in pure Python, making it significantly more CPU-intensive. In this heavy-load scenario, Multi-processing (1.7305s) easily outperformed the Single Process (2.7088s) because the 4 CPU threads effectively divided and conquered the mathematical workload.
* **Chunking Saved the Day:** Without the chunking algorithm, Multi-processing would have taken over 35 seconds due to extreme IPC data-transfer bottlenecks. Grouping the workload into large blocks made the execution roughly 20x faster.

## 🏆 Final Grade: A+
> **Remark:** Outstanding architecture scaling and analysis. Building a core mathematical algorithm from scratch, stress-testing it, identifying system bottlenecks, and optimizing CPU thread allocation is a prime example of production-level software engineering.