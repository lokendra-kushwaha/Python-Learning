class MathNode:

    def __add__(self, other):
        from operations.arithmetic import Add

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Add(self, other)
    
    
    def __radd__(self, other):
        return self.__add__(other)
    

    def __sub__(self, other):
        from operations.arithmetic import Subtract

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Subtract(self, other)
    

    def __rsub__(self, other):
        from operations.arithmetic import Subtract

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Subtract(other, self)


    def __neg__(self):
        from operations.arithmetic import Multiply
        
        return Multiply(Constant(-1), self)


    def __mul__(self, other):
        from operations.arithmetic import Multiply

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return(Multiply(self, other))
    

    def __rmul__(self, other):
        return self.__mul__(other)
    

    def __truediv__(self, other):
        from operations.arithmetic import Divide

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return(Divide(self, other))


    def __rtruediv__(self, other):
        from operations.arithmetic import Divide

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return(Divide(other, self))


    def __pow__(self, other):
        from operations.arithmetic import Power

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Power(self, other)
    

    def __rpow__(self, other):
        from operations.arithmetic import Power

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Power(other, self)


class Constant(MathNode):
    
    def __init__(self, value):
        self.value = value


    def __repr__(self): 
        return str(self.value)


    def simplify(self):
        return self


    def derive(self):
        return Constant(0)
    
    
class Variable(MathNode):

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return self.name
    

    def simplify(self):
        return self
    

    def derive(self):
        return Constant(1) 