from core.primitives import MathNode, Constant, Variable

class Power(MathNode):

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        return f"{self.base}^{self.exponent}"
    
    def derive(self):
        new_exponent = Constant(self.exponent.value - 1)

        new_power_term = Power(self.base, new_exponent)

        return Multiply(self.exponent, new_power_term)
    

class Multiply(MathNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def __repr__(self):
        return f"({self.left}*{self.right})"
    
    
    def derive(self):
        left = Multiply(self.left, self.right.derive())
        right = Multiply(self.left.derive(), self.right)

        return Add(left, right)


class Add(MathNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} + {self.right})"
    
    def derive(self):
        return Add(self.left.derive(), self.right.derive())