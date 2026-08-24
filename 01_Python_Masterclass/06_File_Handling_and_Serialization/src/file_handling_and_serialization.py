# 🌟 ======================================================================= 🌟
# 🚀                       FILE HANDLING & SERIALIZATION
# 🌟 ======================================================================= 🌟

# 📚 SOME THEORY -->
# Types of data used for I/O:
# - Text - '12345' as a sequence of unicode chars
# - Binary - 12345 as a sequence of bytes of its binary equivalent

# Hence there are 2 file types to deal with
# - Text files - All program files are text files
# - Binary Files - Images, music, video, exe files

# How File I/O is done in most programming languages
# - Open a file
# - Read/Write data
# - Close the file

# ✍️ ======================================================================= ✍️
# 📝 WRITING TO A FILE --->
# ✍️ ======================================================================= ✍️

# Case 1 - If the file is not present
f = open('Python/sample.txt','w')
f.write('Hello world')
f.close()
# since file is closed hence this will not work
# f.write('hello') # 🚨 Output -> I/O operation on closed file.

# Write multiline strings
f = open('Python/sample.txt','w')
f.write('hello world')
f.write('\nhow are you?')
f.close()

# Case 2 - If the file is already present
f = open('Python/sample.txt','w')
f.write('Lokendra Kushwaha')
f.close()


# 🧠 EXPLANATION: How exactly open() works under the hood (CPython & Memory)?
# -------------------------------------------------------------------------
# When you call `open()`, CPython sends a system request to your Operating System (OS).
# 1. The OS locates the file on the hard drive (HDD/SSD) and creates a "File Descriptor" (a pointer) in the RAM. The entire file is NOT loaded; only the reference is.
# 2. Buffer Memory: When you execute `f.write()`, the data does not go to the hard drive immediately because HDDs are very slow. Instead, CPython collects this data in a small temporary space in the RAM called a "Buffer".
# 3. f.close(): When you close the file, the OS "flushes" all the collected data from the Buffer directly into the hard drive and cuts the RAM connection.
# (If you don't close the file, your data might remain stuck in the RAM buffer and never actually get saved to the hard drive!)
# -------------------------------------------------------------------------


# Problem with 'w' mode --> Old content gets deleted
# Solution -> Introducing Append mode ('a')
f = open('Python/sample.txt','a')
f.write('\nI am fine')
f.close()

# Write lines --> To write multiple lines
L = ['hello\n','hi\n','how are you\n','I am fine']

f = open('Python/sample.txt','w')
f.writelines(L)
f.close()


# 📖 ======================================================================= 📖
# 🔍 READING FROM FILES --->
# 📖 ======================================================================= 📖

# -> using read() -: Reads the entire file at once
f = open('Python/sample.txt','r')
s = f.read()
print(s)
f.close()

# Why do we close the file?
# 1. When we work with a file, we load it into RAM. If we don't do `f.close()`, it stays in memory until the garbage collector removes it.
# 2. Someone else might access the file because it is still open in RAM, and they could modify it. (Reason - Safety/File Locking).

# Reading upto n chars
f = open('Python/sample.txt','r')
s = f.read(10)
print(s)
f.close()

# readline() -> to read line by line
f = open('Python/sample.txt','r')
print(f.readline(), end='')
print(f.readline(), end='')
f.close()

# 💡 This is used when we have massive amounts of data in a file and we do not want to load it all into RAM at once.

# Reading entire file using readline
f = open('Python/sample.txt','r')

while True:
  data = f.readline()
  if data == '':
    break
  else:
    print(data, end='')

f.close()


# 🛡️ ======================================================================= 🛡️
# 🏗️ USING CONTEXT MANAGER (WITH KEYWORD)
# 🛡️ ======================================================================= 🛡️
# - It's a good idea to close a file after usage as it will free up the resources
# - If we dont close it, garbage collector would close it
# - `with` keyword closes the file as soon as the usage is over

with open('Python/sample.txt','w') as f:
  f.write('Lokendra Kushwaha')

# f.write('hello') # 🚨 Output -> I/O operation on closed file.

# try f.read() now
with open('Python/sample.txt','r') as f:
  print(f.readline())


# Moving within a file -> 10 char then 10 char
with open('Python/sample.txt','r') as f:
  print(f.read(10))
  print(f.read(10)) # Reading the next 10 characters, not from the top
  print(f.read(10))
  print(f.read(10))


# 💡 Benefit of read(chunk)? -> to load a big file in memory efficiently
big_L = ['hello world ' for i in range(1000)]

with open('Python/big.txt','w') as f:
  f.writelines(big_L)

with open('Python/big.txt','r') as f:
  chunk_size = 10
  while len(f.read(chunk_size)) > 0:
    print(f.read(chunk_size), end='***')
    f.read(chunk_size)


# 🎯 ======================================================================= 🎯
# 🧭 SEEK() AND TELL() FUNCTIONS
# 🎯 ======================================================================= 🎯

with open('Python/sample.txt','r') as f:
  print(f.read(10))
  print(f.tell()) # Tells you the current position of the Cursor/Buffer
  f.seek(0)       # Used to move the Cursor to a specific position
  print(f.read(10))
  print(f.tell())

# seek during write ->
with open('Python/sample.txt','w') as f:
  f.write('Hello')
  f.seek(0)
  f.write('Xa') # Overwrites 'He' with 'Xa' -> Result is 'Xallo'


# 🖼️ ======================================================================= 🖼️
# 💾 WORKING WITH BINARY FILES & OTHER DATA TYPES
# 🖼️ ======================================================================= 🖼️

# Problems with working in text mode:
# - can't work with binary files like images
# - not good for other data types like int/float/list/tuples

# working with binary file (Text mode will fail)
# with open('Python/image.jpg','r') as f:
#     f.read()
# 🚨 Output -> UnicodeDecodeError: 'charmap' codec can't decode byte 0x81...

# Correct way: working with binary file ('rb' and 'wb')
with open('Python/image.jpg','rb') as f:
  with open('Python/image_copy.jpg','wb') as wf:
    wf.write(f.read())


# Working with other data types
# with open('Python/sample.txt','w') as f:
#   f.write(5)
# 🚨 Error - write() argument must be str, not int. You can only write string data directly.

with open('Python/sample.txt','w') as f:
  f.write('5')

with open('Python/sample.txt','r') as f:
  print(int(f.read()) + 5)


# More complex data
d = {
    'name':'nitish',
    'age':33,
    'gender':'male'
}

# with open('Python/sample.txt','w') as f:
#   f.write(d) 
# 🚨 Output -> write() argument must be str, not dict. You must convert it to a string first.

with open('Python/sample.txt','w') as f:
  f.write(str(d)) 

with open('Python/sample.txt','r') as f:
    str_data = f.read()
    print(str_data)
    print(type(str_data))
    
    # print(dict(str_data)) # 🚨 Output : dictionary update sequence element #0 has length 1... 
    # A string representation of a dict cannot be converted back directly using dict().

    # We can convert a stringified dict back to a dict data type using the eval() function, but this is a security risk.
    dict_data = eval(str_data)
    print(type(dict_data))


# 🌐 ======================================================================= 🌐
# 🧩 SERIALIZATION & DESERIALIZATION (JSON)
# 🌐 ======================================================================= 🌐

# - **Serialization** - process of converting python data types to JSON format
# - **Deserialization** - process of converting JSON to python data types

# 🧠 EXPLANATION: What is JSON?
# JSON (JavaScript Object Notation) is a universal data format understood by almost every programming language.
# In simple terms: JSON is a bridge. If Python needs to send data to a Java backend or a JavaScript frontend, it cannot send a native Python List or Dictionary. JSON is a standardized text format that servers worldwide can parse and understand.

# Serialization using json module (List) -->
import json

L = [1,2,3,4]
with open('Python/demo.json','w') as f:
    json.dump(L, f)

# Dict
d = {
    'name':'Lokendra',
    'age':20,
    'gender':'male'
}
with open('Python/demo.json','w') as f:
  json.dump(d, f, indent=4)

# Deserialization
with open('Python/demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d)) # Resolves the issue we faced earlier with standard write/read.

# Serialize and deserialize Tuple
t = (1,2,3,4,5)

with open('Python/demo.json','w') as f:
  json.dump(t, f)

with open('Python/demo.json','r') as f:
  t = json.load(f)
  print(t)
  print(type(t)) 

# 🧠 EXPLANATION: Why did the Tuple turn into a List?
# The JSON format does not have a concept of Tuples or Sets. It only supports Arrays (`[]`). 
# When Python serializes a Tuple, the JSON module converts it into a JSON Array. 
# When you deserialize it back, Python reads that Array and automatically maps it to its default sequence type, which is a List.
# (Note: JSON cannot serialize Sets at all and will throw a TypeError directly).


# Serialize and deserialize a nested dict
d = {
    'student':'nitish',
    'marks':[23,14,34,45,56]
}

with open('Python/demo.json','w') as f:
  json.dump(d, f)


# 🧬 ======================================================================= 🧬
# 🧑‍💻 CUSTOM OBJECTS SERIALIZATION
# 🧬 ======================================================================= 🧬

class Person:
  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

person = Person('Lokendra','Kushwaha',20,'male')

# 🚨 json.dump(person, f) -> TypeError: Object of type Person is not JSON serializable
# Python's inbuilt data types can be serialized automatically, but custom objects cannot.
# You have to explicitly tell the JSON module HOW to serialize it using a custom formatting function.

# As a String
def show_object_str(person):
    if isinstance(person, Person):
        return "name -> {} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)

with open('Python/demo.json','w') as f:
    json.dump(person, f, default=show_object_str)

# As a Dict (Best Practice)
def show_object_dict(person):
    if isinstance(person, Person):
        return {'name':person.fname + ' ' + person.lname, 'age':person.age, 'gender':person.gender}

with open('Python/demo.json','w') as f:
    json.dump(person, f, default=show_object_dict, indent=4)

# Deserializing
with open('Python/demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))

# If we want to serialize our custom object exactly as it is, and deserialize it later 
# to use its methods just like a normal object, JSON cannot do this natively. 


# 🥒 ======================================================================= 🥒
# 🚀 PICKLING (PYTHON SPECIFIC SERIALIZATION)
# 🥒 ======================================================================= 🥒
# `Pickling` is the process whereby a Python object hierarchy is converted into a byte stream, and 
# `unpickling` is the inverse operation, whereby a byte stream (from a binary file or bytes-like
# object) is converted back into an object hierarchy.

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display_info(self):
    print('Hi my name is', self.name, 'and I am ', self.age, 'years old')

p = Person2('Lokendra', 20)

# Pickle Dump (Write Binary) -->
import pickle
with open('Python/person.pkl', 'wb') as f:
    pickle.dump(p, f)

# Pickle Load (Read Binary) -->
with open('Python/person.pkl', 'rb') as f:
    p = pickle.load(f)

p.display_info() 

# 🧠 EXPLANATION: Error on Pickling after commenting out the Class
# Doubt: "I don't know why I can't access my object after commenting out my class..."
# Answer: The Pickle module does NOT save the actual *code* (the blueprint) of the class; it only saves the *data* (the state of the object).
# When you unpickle the file, Python searches your current code for the `Person2` class blueprint so it can map the data back into it. 
# If you comment out or delete the class, Python gets confused and throws an error: `module '__main__' has no attribute 'Person2'`.
# Your assumption was 100% correct: In real-world enterprise applications, we write the class in a separate module (like `models.py`) and simply `import` it wherever we need to unpickle the object!


# ⚖️ ======================================================================= ⚖️
# 🆚 PICKLE VS JSON
# ⚖️ ======================================================================= ⚖️
# - Pickle lets the user store data in binary format (Python Specific - retains object architecture). 
# - JSON lets the user store data in a human-readable text format (Universal across all languages, but loses object properties).

# 🌟 ======================================================================= 🌟
#               END OF FILE I/O AND SERIALIZATION MASTERCLASS
# 🌟 ======================================================================= 🌟