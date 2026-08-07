import random
print("-"*100)
print(f"Love Calculator - How much is he/she into you?")
print("-"*100,"\n")

yName = input("Enter Your Name: ")
pName = input("Enter Your Partner Name: ")
love = random.randint(1,100)
print("\n")
userInput = input("Calculate (type: 1): ").title()
if userInput == "Calculate":
    print(f"\nLove Percentage between both ({yName.title()} & {pName.title()}) of You!")
    print(f"{love}%")

else:
    print("Please Enter Valid Input!")