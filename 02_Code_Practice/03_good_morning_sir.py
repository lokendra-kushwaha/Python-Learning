"""
Topic: Time Module and If-Else Conditions
Goal: To create a dynamic greeting script that wishes the user based on the current system time.
"""

#==================================================================================================
#                               Good Morning Sir (Exercise) - Version 1
#==================================================================================================

import time

# Getting the current hour in 24-hour format
timestamp = time.strftime('%H')
# timestamp = int(input("Enter time : "))

# Checking the hour to determine the correct greeting
if (int(timestamp) > 12 and int(timestamp) < 16):
    print("Good Afternoon, Sir")

elif (int(timestamp) > 16):
    print("Good Evening, Sir")

else:
    print("Good Morning, Sir")


#==================================================================================================
#                               Good Morning Sir (Exercise) - Version 2 (Improved)
#==================================================================================================

import time

# Printing exact current time for reference
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))
name = input("Enter Your Name : ")
print(timestamp)

# timestamp1 = int(time.strftime('%M'))
# print(timestamp1)

# timestamp2 = int(time.strftime('%S'))
# print(timestamp2)

# Using Python's chained comparison (e.g., 0 < timestamp < 12) for cleaner logic
# And using .title() to ensure the user's name is properly capitalized
if(0 < timestamp < 12):
    print("Good Morning,", name.title())
elif(12 <= timestamp <= 16):
    print("Good Afternoon,", name.title())
elif(16 < timestamp <= 24):
    print("Good Evening,", name.title())