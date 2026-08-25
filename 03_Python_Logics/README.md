# 🐍 03_Python_Logics: Under the Hood

Welcome to the **03_Python_Logics** workspace! This directory is dedicated to reverse-engineering Python. Instead of relying on built-in magic, this is where I rebuild Python's core functionalities entirely from scratch to deeply understand algorithmic thinking and internal mechanics.

## 📂 Dynamic Folder Structure
This repository is designed to scale automatically as I decode more concepts. It is categorized logically based on Python's core components:

*   **built_in_functions/**: Replicating core Python functions (like determining lengths, finding extremes, or custom console printing) using pure raw logic, loops, and system-level interactions.
*   **strings/**: Ground-up implementations of string manipulation methods. Here, custom slicing and iterations replace standard built-in text methods to show exactly how string processing works.
*   **modules/**: Custom simulations of standard library features (e.g., probability and math generators) to understand how high-level modules operate behind the scenes.

## 🧠 Core Philosophy
*   **Zero Magic:** If Python has a built-in method for it, the goal here is to build it manually and understand the "why" and "how".
*   **Algorithmic Focus:** Prioritizing time and space complexity. This space is used to experiment with performance limits (understanding practically why O(1) is better than O(N)).
*   **Deep Learning:** This isn't just about getting the correct output; it's about reverse-engineering the engine that produces the output.

## 🚀 How to Explore
Feel free to dive into any subdirectory and run the scripts individually. Each file is an independent logic experiment.

```bash
python built_in_functions/custom_print.py
```