# My First Python Program
print("Lokendra Kushwaha is Great.")

# Calculation on two numbers using arithmetic operators
x = 10
y = 6
print(x, "+", y, "=", x + y)
print(x, "-", y, "=", x - y)
print(x, "x", y, "=", x * y)
print(x, "/", y, "=", x / y)
print(x, "//", y, "=", x // y, "(Floor Division)")
print(x, "%", y, "=", x % y, "(Modulus)")

# Good Morning Sir (Exercise)

import time

timestamp = time.strftime('%H')
# timestamp = int(input("Enter time : "))

if (int(timestamp) > 12 and int(timestamp) < 16):
    print("Good Afternoon, Sir")

elif (int(timestamp) > 16):
    print("Good Evening, Sir")

else:
    print("Good Morning, Sir")

 # if-else Exersize (Good Morning Sir)

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
name = input("Enter Your Name : ")
print(timestamp)

# timestamp1 = int(time.strftime('%M'))
# print(timestamp1)

# timestamp2 = int(time.strftime('%S'))
# print(timestamp2)

if(0 < timestamp < 12):
    print("Good Morning,", name.title())
elif(12 <= timestamp <= 16):
    print("Good Afternoon,", name.title())
elif(16 < timestamp <= 24):
    print("Good Evening,", name.title())