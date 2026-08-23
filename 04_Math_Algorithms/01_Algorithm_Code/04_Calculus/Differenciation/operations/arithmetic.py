from core.primitives import MathNode, Constant, Variable

class Power(MathNode):

    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        return f"{self.base}^{self.exponent}"
    
    def simplify(self):

        sim_base = self.base.simplify()
        sim_exponent = self.exponent.simplify()

        if isinstance(sim_exponent, Constant) and sim_exponent.value == 0:
            return Constant(1)
        
        if isinstance(sim_exponent, Constant) and sim_exponent.value == 1:
            return sim_base

        if isinstance(sim_base, Constant) and isinstance(sim_exponent, Constant):
            return Constant(sim_base.value ** sim_exponent.value)
        
        if type(sim_base).__name__ == 'Power':
            if isinstance(sim_base.exponent, Constant) and isinstance(sim_exponent, Constant):
                new_exp = Constant(sim_base.exponent.value * sim_exponent.value)
                return Power(sim_base.base, new_exp)
        
        return Power(sim_base, sim_exponent)
    
    def derive(self):
        new_exponent = Constant(self.exponent.value - 1)

        new_power_term = Power(self.base, new_exponent)

        return Multiply(self.exponent, new_power_term)
    

class Add(MathNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} + {self.right})"
    
    def simplify(self):
        
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        if isinstance(sim_left, Constant) and sim_left.value == 0:
            return sim_right
        
        if isinstance(sim_right, Constant) and sim_right.value == 0:
            return sim_left
        
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value + sim_right.value)
        
        return Add(sim_left, sim_right)
    
    def derive(self):
        return Add(self.left.derive(), self.right.derive())
    

class Subtract(MathNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"({self.left} - {self.right})"
    
    def simplify(self):
        
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        if isinstance(sim_left, Constant) and sim_left.value == 0:
            return Multiply(Constant(-1), sim_right)
        
        if isinstance(sim_right, Constant) and sim_right.value == 0:
            return sim_left
        
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value - sim_right.value)
        
        return Subtract(sim_left, sim_right)
    
    def derive(self):
        return Subtract(self.left.derive(), self.right.derive())


class Multiply(MathNode):

    def __init__(self, left, right):
        self.left = left
        self.right = right


    def __repr__(self):
        return f"({self.left}*{self.right})"
    
    
    def simplify(self):
        
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        if (isinstance(sim_right, Constant) and sim_right.value == 0) or (isinstance(sim_left, Constant) and sim_left.value == 0):
            return Constant(0)
        
        if isinstance(sim_right, Constant) and sim_right.value == 1:
            return sim_left
        
        if isinstance(sim_left, Constant) and sim_left.value == 1:
            return sim_right
        
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value * sim_right.value)
        
        return Multiply(sim_left, sim_right)

    def derive(self):

        left = Multiply(self.left, self.right.derive())
        right = Multiply(self.left.derive(), self.right)

        return Add(left, right)


class Divide(MathNode):

    def __init__(self, num, den):
        self.num = num
        self.den = den

    
    def __repr__(self):
        return f"({self.num}/{self.den})"


    def simplify(self):
        
        sim_num = self.num.simplify()
        sim_den = self.den.simplify()
        
        if isinstance(sim_den, Constant) and sim_den.value == 0:
            raise ValueError("Math Error")
        
        if (isinstance(sim_num, Constant) and sim_num.value == 0):
            return Constant(0)
        
        if isinstance(sim_den, Constant) and sim_den.value == 1:
            return sim_num
        
        if isinstance(sim_num, Constant) and isinstance(sim_den, Constant):
            return Constant(sim_num.value / sim_den.value)
        
        if (isinstance(sim_num, Constant) and sim_num.value == 1) and (isinstance(sim_den, Constant) and sim_den.value == 1):
            return Constant(1)
        
        
        return Divide(sim_num, sim_den)
    

    def derive(self):

        term1 = Multiply(self.num.derive(), self.den)
        term2 = Multiply(self.num, self.den.derive())
        
        numerator = Subtract(term1, term2)
        denominator = Power(self.den, Constant(2))

        return Divide(numerator, denominator)