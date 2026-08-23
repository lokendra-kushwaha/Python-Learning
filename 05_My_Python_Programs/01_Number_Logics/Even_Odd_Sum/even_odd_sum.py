"""
=========================================================
🧮 EVEN & ODD SUM CALCULATOR (THE TALE OF TWO METHODS) 🧮
=========================================================

Description:
    This script calculates the sum of all even and odd numbers within 
    a given range. The beauty of this file lies in the comparison 
    between two completely different approaches written by the same 
    developer during their learning phase.

    - Method 1: The "Over-Engineered Math" Approach (Complex)
    - Method 2: The "Pythonic" Approach (Clean)

Created By: Lokendra Kushwaha
"""

print("=" * 60)
print("             🧮 EVEN & ODD SUM CALCULATOR 🧮             ")
print("=" * 60)

num1 = int(input("\nEnter Your First Number: "))
num2 = int(input("Enter Your Last Number: "))

print("\n" + "=" * 60)
print("🚀 METHOD 1: The 'Over-Engineered Math' Approach")
print("=" * 60)

odd_sum = 0
even_sum = 0

# A condition which checks that num1 is even and num2 also a even number
if num1%2 == 0 and num2%2 == 0:
    for i in range(num1, num2, 2):
        even_sum = even_sum + i
        odd_sum = odd_sum + (i + 1)
    print("The sum of even no. between",num1, "and", num2, ":",even_sum + num2)
    print("The sum of odd no. between",num1, "and", num2, ":",odd_sum)

# A condition which checks that num1 is even and num2 a odd number
elif num1%2 == 0 and num2%2 == 1:
    for i in range(num1, num2, 2):
        even_sum = even_sum + i
        odd_sum = odd_sum + (i + 1)  
    print("The sum of even no. between",num1, "and", num2, ":",even_sum) 
    print("The sum of odd no. between",num1, "and", num2, ":",odd_sum)

# A condition which checks that num1 is odd and num2 also a odd number
elif num1%2 == 1 and num2%2 == 1:
    for i in range(num1, num2, 2):
        even_sum = even_sum + (i+1)
        odd_sum = odd_sum + i
    print("The sum of even no. between",num1, "and", num2, ":",even_sum)
    print("The sum of odd no. between",num1, "and", num2, ":",odd_sum+ num2)

# A condition which checks that num1 is odd and num2 a even number
elif num1%2 == 1 and num2%2 == 0:
    for i in range(num1, num2,2):
        even_sum = even_sum + (i + 1)
        odd_sum = odd_sum + i    
    print("The sum of even no. between",num1, "and", num2, ":",even_sum)
    print("The sum of odd no. between",num1, "and", num2, ":",odd_sum)


print("\n" + "=" * 60)
print("✨ METHOD 2: The Clean 'Pythonic' Approach")
print("=" * 60)

odd_sum_2 = 0
even_sum_2 = 0

# Extract all numbers between range, check condition, and calculate sums.
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        even_sum_2 = even_sum_2 + i 
    else:
        odd_sum_2 = odd_sum_2 + i  

print("The sum of even no. between", num1, "and", num2, ":", even_sum_2)
print("The sum of odd no. between", num1, "and", num2, ":", odd_sum_2)
print("=" * 60)