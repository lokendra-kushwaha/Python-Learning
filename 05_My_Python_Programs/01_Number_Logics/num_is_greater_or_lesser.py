# A Python Program Which Finds a Number Greater or Lesser When User Gives Two Random Numbers.

while True:
    try:
        num1 = int(input("Enter First Number : "))
    except:
        continue
    break

while True:
    try:
        num2 = int(input("Enter Second Number : "))
    except:
        continue
    break

if (num1==num2):
    print("\nBoth numbers are equal.")

elif (num1>num2):
    print("\nAnswer -: ")
    print(num1, "is Greater than", num2, ".") 
    print(num2, "is Lesser than", num1, ".")

else:
    print("\nAnswer -: ")
    print(num2, "is Greater than", num1,  ".")
    print(num1, "is Lesser than", num2, ".")