class MathNode:
    """
    The Base Class (Blueprint) for all mathematical expressions in the engine.
    
    This class serves as the foundation for our Abstract Syntax Tree (AST). Its primary 
    purpose is to overload standard Python mathematical operators (+, -, *, /, **) 
    using Magic Methods. Instead of immediately computing a value, these methods 
    build an equation tree. For example, 'x + 2' becomes Add(Variable('x'), Constant(2)).

    Methods:
        The 'simplify' and 'derive' methods are meant to be overridden by each specific 
        child class (e.g., Add, Multiply, Sin) to apply their unique mathematical rules.
    """

    def __add__(self, other):
        """
        Overloads the addition operator (+).
        Mathematical Concept: f(x) + g(x)

        If a user adds a MathNode to a standard Python numeric type (int, float, complex), 
        this method automatically type-casts that number into our engine's Constant node.

        Args:
            other (MathNode, int, float, complex): The value being added.

        Returns:
            Add: A new Add node representing the sum of both values.
        """
        from operations.arithmetic import Add

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Add(self, other)
    
    
    def __radd__(self, other):
        """
        Overloads the right-side addition operator.
        
        Handles cases like '5 + x' where the integer appears first. Since addition 
        is commutative (A + B = B + A), this method reverses the order and falls back 
        to the standard __add__ method.

        Args:
            other: The left-side value (e.g., an integer or float).

        Returns:
            Add: A new Add node.
        """
        return self.__add__(other)
    

    def __sub__(self, other):
        """
        Overloads the subtraction operator (-).
        Mathematical Concept: f(x) - g(x)

        Args:
            other (MathNode, int, float, complex): The value to subtract.

        Returns:
            Subtract: A new Subtract node.
        """
        from operations.arithmetic import Subtract

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Subtract(self, other)
    

    def __rsub__(self, other):
        """
        Overloads the right-side subtraction operator.
        
        Handles cases like '5 - x'. Since subtraction is not commutative (A - B != B - A), 
        we cannot simply reverse the order. This ensures the first element is properly 
        type-casted and maintains its position as the left operand.

        Args:
            other: The left-side value (minuend).

        Returns:
            Subtract: A new Subtract node representing (other - self).
        """
        from operations.arithmetic import Subtract

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Subtract(other, self)


    def __neg__(self):
        """
        Overloads the unary negation operator (-).
        Mathematical Concept: -f(x) equates to -1 * f(x)

        When a user writes '-x', this method converts it mathematically into 
        a multiplication operation with a constant of -1.

        Returns:
            Multiply: A node representing (-1 * self).
        """
        from operations.arithmetic import Multiply
        
        return Multiply(Constant(-1), self)


    def __mul__(self, other):
        """
        Overloads the multiplication operator (*).
        Mathematical Concept: f(x) * g(x)

        Args:
            other (MathNode, int, float, complex): The multiplier.

        Returns:
            Multiply: A new Multiply node.
        """
        from operations.arithmetic import Multiply

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Multiply(self, other)
    

    def __rmul__(self, other):
        """
        Overloads the right-side multiplication operator.
        
        Handles equations like '5 * x'. Since multiplication is commutative 
        (A * B = B * A), this directly routes back to the standard __mul__ method.

        Args:
            other: The left-side value.

        Returns:
            Multiply: A new Multiply node.
        """
        return self.__mul__(other)
    

    def __truediv__(self, other):
        """
        Overloads the true division operator (/).
        Mathematical Concept: f(x) / g(x)

        Args:
            other (MathNode, int, float, complex): The denominator.

        Returns:
            Divide: A new Divide node.
        """
        from operations.arithmetic import Divide

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Divide(self, other)


    def __rtruediv__(self, other):
        """
        Overloads the right-side division operator.
        
        Handles equations like '1 / x'. Since division is not commutative 
        (A / B != B / A), the order of operands is strictly maintained.

        Args:
            other: The left-side value (numerator).

        Returns:
            Divide: A new Divide node representing (other / self).
        """
        from operations.arithmetic import Divide

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Divide(other, self)


    def __pow__(self, other):
        """
        Overloads the exponentiation operator (**).
        Mathematical Concept: f(x) ^ g(x)

        Args:
            other (MathNode, int, float, complex): The exponent or power.

        Returns:
            Power: A new Power node.
        """
        from operations.arithmetic import Power

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Power(self, other)
    

    def __rpow__(self, other):
        """
        Overloads the right-side exponentiation operator.
        
        Handles cases like '2 ** x'. Exponents are not commutative (A^B != B^A), 
        so the original order is preserved.

        Args:
            other: The base value.

        Returns:
            Power: A new Power node where the base is 'other' and exponent is 'self'.
        """
        from operations.arithmetic import Power

        if isinstance(other, (int, float, complex)):
            other = Constant(other)

        return Power(other, self)


class Constant(MathNode):
    """
    Represents a Mathematical Constant (e.g., 1, -5, 3.14, math.e, math.pi).
    This acts as a 'Leaf Node' in our Abstract Syntax Tree.

    Attributes:
        value (int, float, complex): The numerical value of the constant.
    """
    
    def __init__(self, value):
        """
        Initializes the Constant node.
        
        Args:
            value (int, float, complex): The assigned numerical value.
        """
        self.value = value


    def __repr__(self): 
        """
        Returns the string representation of the constant for terminal output.
        """
        return str(self.value)


    def simplify(self):
        """
        Simplifies the Constant.
        
        Since a constant is already in its simplest mathematical form, 
        it simply returns itself.

        Returns:
            Constant: Self.
        """
        return self


    def derive(self):
        """
        Calculates the derivative of the Constant.
        
        Calculus Rule: The derivative of any constant number is always 0.
        This is because a constant has no rate of change relative to any variable 'x'.
        Rule: d/dx(c) = 0

        Returns:
            Constant: A new Constant node with a value of 0.
        """
        return Constant(0)
    
    
class Variable(MathNode):
    """
    Represents a Mathematical Variable (e.g., 'x', 'y', 'theta').
    This is also a 'Leaf Node' in the Abstract Syntax Tree.

    Attributes:
        name (str): The string identifier for the variable.
    """

    def __init__(self, name):
        """
        Initializes the Variable node.
        
        Args:
            name (str): The name of the variable (e.g., 'x').
        """
        self.name = name


    def __repr__(self):
        """
        Returns the variable's name for terminal output.
        """
        return self.name
    

    def simplify(self):
        """
        Simplifies the Variable.
        
        A standalone variable is already in its simplest form.
        
        Returns:
            Variable: Self.
        """
        return self
    

    def derive(self):
        """
        Calculates the derivative of the Variable with respect to itself.
        
        Calculus Rule: The derivative of a variable with respect to itself is always 1.
        (The rate of change is perfectly linear, 1:1).
        Rule: d/dx(x) = 1
        
        Note: Currently, the engine assumes single-variable calculus, implying derivation 
        is always performed with respect to this variable's name.

        Returns:
            Constant: A new Constant node with a value of 1.
        """
        return Constant(1)