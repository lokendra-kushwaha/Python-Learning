from core.container import Expression
from core.primitives import Constant, Variable
from operations.arithmetic import Power, Multiply, Add

exp1 = Expression(Power('x', Constant(2)), Power('-x', Constant(-2)))
print(exp1.derive())

x = Variable('x')

equ = 5 * x**2 + 3 * x + 2
print('original eq - ', equ)
print(equ.derive())

equ1 = x*x*x
print(equ1.derive())

equ2 = x**3
print(equ2.derive())