# 🚀 Python OOPs: Architecture & System Design Masterclass

Welcome to the **Advanced Python OOPs** module! This repository doesn't just cover textbook definitions of Object-Oriented Programming; it dives deep into **System Architecture, Memory Management, and Enterprise-Level Design**. 

Here, we decode *how* CPython handles objects under the hood, how classes interact chemically and physically, and how to design scalable systems using industry-standard UML logic.

---

## 📂 Folder Structure

    05_OPPs_Concepts/
    │
    ├── 📂 Concepts/ (The Practical Engine)
    │   ├── 01_classes_and_objects.py                  # Basics, __init__, self, and object lifecycle
    │   ├── 02_encapsulation_and_static_vars.py        # Core state management & security
    │   └── 03_inheritance_polymorphism_abstraction.py # Architecture, MRO, and API Contracts
    │
    └── 📂 Notes/ (The Blueprint & Documentation)
        ├── Classes_Objects_and_Self.md                # Memory blocks, self, & Garbage Collection
        ├── Encapsulation_and_State_Architecture.md    # Name Mangling, Pass-by-Reference
        └── Class_Relationships_and_Abstraction.md     # UML ASCII Diagrams, MRO, Interfaces

---

## 🔥 Key Highlights & What's Inside

Unlike standard OOP tutorials, this module treats you like a **System Architect**. Key topics covered include:

*   **⚙️ Classes, Objects & self:** Decoding how physical memory blocks are allocated, the true identity of the self parameter, and how constructors (__init__) bootstrap the object.
*   **🛡️ Encapsulation & The "Bouncer" Logic:** We don't just "hide data." We explore **Name Mangling** (_ClassName__var) and how Getters/Setters act as strict security checkpoints to prevent system crashes.
*   **🏗️ Class Relationships (UML Perfect):** Custom ASCII diagrams visualizing:
    *   **Aggregation (Has-A):** Shown with proper strict Diamond Notation (<>--------->).
    *   **Inheritance (Is-A):** Shown with proper Hollow Triangle Notation (---------|>).
*   **🧠 Memory & State:** Deep dive into the illusion of Reference Variables, Object Mutability, and the strict isolation between Instance Variables (Object-Level) and Static Variables (Class-Level).
*   **💎 The Diamond Problem Decoded:** Understanding Python's C3 Linearization Algorithm and how **Method Resolution Order (MRO)** perfectly resolves multiple inheritance conflicts.
*   **🏛️ Abstraction as an API Contract:** Why Abstract Base Classes (ABC) are strictly enforced by Senior Architects to ensure Junior Developers follow structural rules.

---

## 🛠️ How to Use This Module

1.  **Read the Blueprints First:** Start with the .md files in the Notes/ folder. They contain the ASCII UML diagrams and "Under the Hood" architectural explanations.
2.  **Run the Engine:** Open the .py scripts in the Concepts/ folder. The code is heavily commented with emojis, highlighting the exact moments where concepts like Method Overriding and Pass-by-Reference take action.

---
*Built with ❤️ for those who don't just write code, but engineer systems.*