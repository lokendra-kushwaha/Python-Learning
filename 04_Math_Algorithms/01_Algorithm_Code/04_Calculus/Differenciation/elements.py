class Constant:
    
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def derive(self):
        return Constant(0)
    
class Variable:

    def __init__(self, var):
        self.var = var

    def __repr__(self):
        return str(self.var)

    def derive(self):
        return Constant(1)    