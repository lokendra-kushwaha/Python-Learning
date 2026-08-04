#==================================================================================================
#                               My First Python Program
#==================================================================================================

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

#==================================================================================================
#                               Good Morning Sir (Exercise)
#==================================================================================================

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

#==================================================================================================
#                            Armstrong Number Finder in a Range    
#==================================================================================================

# Armstrong Number Finder in a Range
"""
This program tell a number is an Armsrong number or not in a given range.
Input: The progran take two input first is starting no. and second is last no.
Execution: First we extract all no. from the range then calculate the digits in no. one by one and then calculates the sum of all digits power of total digits and we compare the sum with the number if sum is equal to number then number is an Armstrong number.
Ex. A no. in range (1 - 10) between -> 10
Digits in 10 -> 2
Armstron sum -> 1^2 + 0^2 = 2 != 10 (Not an Armstrong no.)
"""
StartNumberInString = input("Enter Starting Number: ")
EndNumberInString = input("Enter Ending Number: ")

for number in range(int(StartNumberInString),int(EndNumberInString)+1):
    string_number = str(number)
    lenth = len(string_number)

    armstrong_sum = 0
    for digit in str(number):
        string_digit = str(digit)
        powerOfdigit = int(string_digit)**lenth
        armstrong_sum = armstrong_sum + powerOfdigit

    if armstrong_sum == int(number): 
            print(number,"is an Armstrong Number.")

#==================================================================================================
#                            Armstrong Number Checker    
#==================================================================================================

"""
This program tell a number is an Armsrong number or not in a given range.
Input: The progran take two input first is starting no. and second is last no.
Execution: First we extract all no. from the range then calculate the digits in no. one by one and then calculates the sum of all digits power of total digits and we compare the sum with the number if sum is equal to number then number is an Armstrong number.
Ex. Given no. -> 10
Digits in 10 -> 2
Armstron sum -> 1^2 + 0^2 = 2 != 10 (Not an Armstrong no.)
"""

numberInString = input("Enter Your Number: ")
armstrong_sum = 0
for i in numberInString:
    number = int(i)
    cube = number**len(numberInString)
    armstrong_sum = armstrong_sum + cube

if armstrong_sum == int(numberInString):
    print("This is a Armstrong Number.👌")

else:
    print("This is not a Armstrong Number.🤦")