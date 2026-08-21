from elements import Variable, Constant
from basic_rules import Power

x = Variable('x')
power_val = -3

equation = Power(x, power_val)
print(equation)
print(equation.derive())
print(equation.derive().left)
print(equation.derive().right)