"""
====================================================================================
🌐 STANDARD LIBRARY: THE 'json' MODULE
====================================================================================
Description: JSON (JavaScript Object Notation) is the universal language of the web.
             The 'json' module allows Python to convert its native objects (like 
             dictionaries and lists) into JSON strings (Serialization) and vice versa 
             (Deserialization). 

Real-World Use Case: 
Reading configuration files, saving application states, and communicating with APIs.
====================================================================================
"""

import json
import os

def section_divider(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")

# 🟢 1. SERIALIZATION: Python to JSON String (dumps)
# ====================================================================================
section_divider("1. SERIALIZATION: Python Dict -> JSON String (json.dumps)")

python_developer = {
    "name": "Lokendra",
    "role": "System Architect",
    "skills": ["Python", "Asyncio", "APIs"],
    "is_active": True,
    "salary": None  # Python's None will become JSON's null
}

print("-> Original Python Dictionary:")
print(type(python_developer))

# dumps() stands for "Dump to String"
# indent=4 makes it highly readable (pretty-printing)
json_string = json.dumps(python_developer, indent=4, sort_keys=True)

print("\n-> Converted JSON String (Notice True became true, None became null):")
print(json_string)
print(f"Type: {type(json_string)}")


# 🟢 2. DESERIALIZATION: JSON String to Python (loads)
# ====================================================================================
section_divider("2. DESERIALIZATION: JSON String -> Python Dict (json.loads)")

api_response_string = '{"server": "AWS", "status": 200, "data_loaded": true}'

# loads() stands for "Load from String"
python_dict = json.loads(api_response_string)

print("-> Parsed Python Dictionary:")
print(python_dict)
print(f"-> Accessing Data directly: Server Status is {python_dict['status']}")


# 🟢 3. FILE I/O: Writing and Reading JSON Files (dump & load)
# ====================================================================================
section_divider("3. FILE I/O: Working with JSON Files (dump & load)")

file_path = "developer_config.json"

# A. Writing to a file using json.dump() (No 's' at the end!)
with open(file_path, "w") as file:
    json.dump(python_developer, file, indent=4)
print(f"   [+] Data successfully written to {file_path}")

# B. Reading from a file using json.load() (No 's' at the end!)
with open(file_path, "r") as file:
    loaded_data = json.load(file)
print(f"   [+] Data read from file: {loaded_data['name']} is a {loaded_data['role']}")

# Cleanup the file to keep workspace clean
os.remove(file_path)
print(f"   [-] Cleaned up {file_path}")


# 🟢 4. Handling Unsupported Objects
# ====================================================================================
section_divider("4. PRO LEVEL: Handling Unsupported Objects")
"""
JSON only supports basic data types (str, int, float, bool, list, dict).
If you try to convert a custom Class object or a DateTime object, it will CRASH!
Here is how Senior Developers fix it.
"""

class Server:
    def __init__(self, ip, active):
        self.ip = ip
        self.active = active

my_server = Server("192.168.1.1", True)

# json.dumps(my_server) # ❌ This would throw a TypeError!

# ✅ The Fix: Convert the object's internal dictionary (dict) to JSON
safe_json = json.dumps(my_server.__dict__, indent=4)

print("-> Safely converted a Custom Python Object into JSON:")
print(safe_json)


print("\n" + "=" * 70)
print("🎯 CONCLUSION: You can now communicate with any API in the world!")
print("=" * 70)