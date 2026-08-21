# 📚 Python Library Management System (Enterprise-Level Console Application)

## 🌟 Overview
Welcome to the **Library Management System (LMS)**! This is a robust, highly scalable, and fully functional console-based application built entirely from scratch using **Core Python**. Spanning over 2,600 lines of meticulously structured code, this system completely bypasses external database dependencies (like SQL or MongoDB) by utilizing a custom-engineered **File I/O Database Engine**. 

It is designed to manage the end-to-end workflow of a modern library, facilitating seamless interactions between **Administrators** and standard **Users (Guests)**. From real-time fine calculation based on date-time logic to dynamic cross-platform database initialization, this project showcases advanced problem-solving and software architecture skills.

---

## 🚀 Key Features & Functionalities

### 1. Dual-Portal Authentication System
* **Secure Sign-Up & Sign-In:** Distinct login portals for Administrators and Guests.
* **Smart Data Loading:** User session data (Name, Email, Mobile, Login ID) is dynamically fetched from the File I/O system and loaded into active object attributes upon successful login.
* **Profile Management:** Users and Admins can view, edit, and safely delete their profiles. The system handles the cleanup of respective records automatically.

### 2. Administrator Capabilities (Superuser)
* **Inventory Management:** Add new books, update existing book quantities, or completely remove books from the library catalog.
* **User Monitoring:** View the complete list of registered users.
* **Borrowing Oversight:** Track which user has borrowed which book, including timestamps.

### 3. Guest/User Capabilities
* **Extensive Search Engine:** Users can search the library catalog for specific books using intuitive inputs.
* **Borrowing System:** Users can borrow books (up to a predefined limit). The system actively checks library stock and automatically deducts the quantity upon a successful borrow.
* **Return & Fine Calculation:** Real-time calculation of overdue fines. If a user exceeds the allotted borrowing period, the system calculates the exact penalty based on the current date using the `datetime` module.
* **Return All:** A master switch for users to securely return all borrowed books at once.

### 4. Custom File I/O Database Engine (The Brain)
* **No SQL Required:** Data is persistently stored across three primary text files: `books.txt`, `users.txt`, and `borrowedbooks.txt`.
* **Cross-Platform & Self-Healing:** The system uses Python's `os` module to automatically detect the host operating system, dynamically build absolute paths, and auto-generate the `database` directory and text files if they do not exist. 
* **Data Masking & Parsing:** Advanced string manipulation (like `.strip()`, `.split()`) is used to parse delimited text data into usable Python objects without crashing.

---

## 🏗️ System Architecture & OOP Concepts

This software heavily relies on the principles of **Object-Oriented Programming (OOP)** to maintain a clean, modular, and DRY (Don't Repeat Yourself) codebase.

* **Inheritance:** The system employs Hierarchical and Multiple Inheritance. Parent classes like `Account` and `CommonWork` hold universal attributes (like database paths and search algorithms), which are elegantly inherited by the `Admin` and `User` child classes.
* **Polymorphism:** The main `Menu` acts as a dynamic factory. Depending on user input, the `self.current_person` variable morphs into either a `User()` or `Admin()` object, dynamically changing the system's behavior and access privileges.
* **Encapsulation:** Sensitive data and methods are compartmentalized. Validation checks prevent unauthorized access or accidental data corruption.
* **Exception Handling:** Extensive `try-except` blocks are deployed throughout the software to catch `ValueError`, `FileNotFoundError`, and `IndexError`, ensuring the system never crashes abruptly during runtime.

---

## 💻 Tech Stack
* **Language:** Python 3.x
* **Libraries Used:** 
  * `os` (For dynamic pathing and directory creation)
  * `datetime` (For real-time fine calculation and borrowing logs)
  * `sys` (For controlled system exits)
* **Database:** Custom `.txt` File Handling (CRUD operations via Python)
* **Version Control:** Git & GitHub (Data protected via `.gitignore`)

---

## ⚙️ Installation & Usage

Since this software uses a self-initializing database, setting it up on your local machine is incredibly simple.

**Step 1:** Clone the repository
> `git clone https://github.com/lokendra-kushwaha/Python-Learning.git`

**Step 2:** Navigate to the project directory
> `cd Python-Learning`

**Step 3:** Run the main application
> `python library_management_system.py`

*(Note: Replace `library_management_system.py` with your actual main python file name).*

Upon the first execution, the system will automatically create a secure `database` folder in the root directory to store all persistent data.

---

## 🛡️ Testing & QA (Quality Assurance)
This software has undergone rigorous manual testing phases:
* **Phase 1 (Happy Path):** Verified the complete end-to-end lifecycle (Registration -> Borrowing -> Returning -> Logout).
* **Phase 2 (Negative Testing):** System resilience tested against empty inputs, invalid data types, logic bypassing (e.g., trying to return books immediately after sign-up without logging in), and missing database files. 

---

## 🔮 Future Scope
While this is a fully functional backend system, future updates may include:
1. **Graphical User Interface (GUI):** Implementing `Tkinter` or `PyQt` for a modern, clickable interface.
2. **Database Migration:** Upgrading the File I/O system to `SQLite` or `MySQL` for faster querying.
3. **Email Notifications:** Integrating `smtplib` to send automated overdue warnings to users.

---
*Developed with ❤️ and countless cups of coffee by Lokendra Kushwaha.*