from core.container import Expression
from core.primitives import Constant, Variable
from operations.arithmetic import Power, Multiply, Add

exp1 = Expression(Power('x', Constant(2)), Power('-x', Constant(-2)))
print(exp1.derive())

x = Variable('x')
equ = 5 * x**2 + 3 * x + 2
print('original eq - ', equ)
print(equ.derive().simplify())

eq2 = x**3 - x**2
print(eq2.derive().simplify())


eq3 = x**3 / (-4)**0.5
print(eq3.derive().simplify())