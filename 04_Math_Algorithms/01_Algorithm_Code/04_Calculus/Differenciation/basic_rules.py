from elements import Constant, Variable

class Multiply:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.left}*{self.right}"
    
    def derive(self):
        pass


class Power:

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        return f"{self.base}^{self.exponent}"
    
    def derive(self):
        new_exponent = Constant(self.exponent - 1)

        new_power_term = Power(self.base, new_exponent)

        return Multiply(self.exponent, new_power_term)
    

class Expression:
    
    def __init__(self, *args):
        self.element = args

    def __repr__(self):
        ex = ''
        for element in self.element:
            ex = ex + f' + {str(element)}'.replace('+ -', '- ')
        
        return ex
    
    def derive(self):
        
        new_ex = []
        for item in self.element:
            term = item.derive()

            new_ex.append(term)

        return Expression(*new_ex)

exp = Expression(Constant(2), Constant(-2), Power('x', 2), Power('-x', -2), Constant(10), Variable('x'))
print(exp.derive())

# ml = Expression(Power('x', 3))
# print(ml.derive())
# print(ml.derive().left)
# print(ml.derive().right)

var = Expression(Variable('x'))
print(var.derive())
var2 = var.derive()
print(var2.derive())

eq2 = exp.derive()
print(eq2.derive())