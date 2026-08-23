# 🧮 Range Sum Logic: The Tale of Two Methods

This folder contains a single Python script that perfectly captures my evolution as a programmer. It tackles a simple problem—calculating the sum of even and odd numbers in a range—using two wildly different approaches.

## 🤣 The "Over-Engineered" Approach (Method 1)
In an attempt to mathematically optimize the code using a step of 2 in the loop (`range(num1, num2, 2)`), I ended up creating a complex beast. 
Because the starting and ending numbers could be any combination of even/odd, I had to manually write `if-elif` blocks for all 4 possible combinations:
1. Even to Even
2. Even to Odd
3. Odd to Odd
4. Odd to Even

It's a mathematical nightmare, but it works flawlessly!

## ✨ The "Clean" Approach (Method 2)
The realization that the simplest logic is often the best. This method simply loops through every number in the range one by one (`range(num1, num2 + 1)`), checks if it is divisible by 2 using the modulo operator (`%`), and sorts it into the respective sum variable. 

**Lesson Learned:** Let the computer do the heavy lifting. Clean, readable code is always better than complex, brute-forced logic!