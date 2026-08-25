# 📊 Student Result Management System

This folder contains two iterations of a command-line based Python application designed to manage, save, and retrieve student academic records. 

Including both versions here demonstrates the evolution of the code—starting from a basic functional script to a more robust version with global data tracking and error handling.

## 📂 Project Files & Evolution

### 1. Version 1: Basic Result Tracker (result_management1.0.0.py)
The initial version focuses on fundamental File I/O operations and dictionary manipulations.
* **Unique ID Generation:** Creates a unique login ID for every new student.
* **Result Calculation:** Accepts marks for multiple subjects and calculates the total and percentage.
* **Personal File Handling:** Saves individual student records in uniquely named .txt files.
* **Retrieval System:** Allows returning students to view their saved results using their Unique ID.

### 2. Version 2: Advanced Tracker with Analytics (result_management1.0.1.py)
The upgraded version builds upon the first one by introducing a global tracking mechanism and better error handling.
* **Global Score Tracker:** Introduces a centralized file (maxMinMarks.txt) to continuously track the total marks of all registered students.
* **Max/Min Analytics:** Allows users to instantly fetch the Highest and Lowest scores across the entire system.
* **Improved Menu & Error Handling:** Features a refined user interface, cleaner loops, and try-except blocks to prevent crashes during incorrect inputs or missing files.

## 🧠 Concepts Demonstrated
* File Handling (Read/Write/Append modes)
* Dictionaries & Lists for data storage
* String Manipulation & Formatting
* Error Handling (try-except blocks)
* Algorithm logic for finding Maximum and Minimum values.

## 🚀 How to Run
1. Ensure you have Python installed on your system.
2. Clone the repository and navigate to this folder.
3. Run either of the scripts using the terminal:
   ``bash
   python result_management_system1.0.0.py
   # OR
   python result_management_system1.0.1.py
``
4. Follow the on-screen terminal prompts to interact with the system.