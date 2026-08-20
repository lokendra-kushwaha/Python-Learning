# 📇 Contact Management System

A purely file-based CRUD (Create, Read, Update, Delete) application built during my early days of learning Python. This project demonstrates how to manage persistent data using the os module and standard text files before diving into actual databases.

## ✨ Core Features
* **Authentication Simulation:** Generates a personalized User ID for session management.
* **CRUD Operations:**
  * **Create:** Add new contacts (Name, Mobile, Email, Address, Relation).
  * **Read:** View a master list of all contacts or search for a specific person.
  * **Update:** Dynamically overwrite existing contact files with new information.
  * **Delete:** Securely remove a contact's text file using Python's os.remove() method.
* **Dynamic Directory Creation:** Automatically creates a Contact_Files folder in the current directory to safely store all generated .txt files without cluttering the root folder.

## 🧠 Technical Skills Showcased
* Extensive use of Python's **File I/O** (Read, Write, and Append modes).
* Interacting with the Operating System via the **os module**.
* Building interactive, multi-layered terminal menus using while loops and conditionals.

## 🚀 How to Run
1. Clone this repository to your local machine.
2. Run the script from your terminal:
   ``bash
   python contact_manager.py
``
3. Follow the on-screen prompts to register an ID and manage your contacts!