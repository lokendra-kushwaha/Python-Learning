"""
Core Arithmetic Operations Module for the Math Engine.

This module defines the fundamental mathematical operations (Addition, 
Subtraction, Multiplication, Division, and Exponentiation) as nodes in 
an Abstract Syntax Tree (AST). 

Each class in this module is responsible for:
1. Representing a specific algebraic operation.
2. Providing algebraic simplification rules (e.g., x + 0 = x, x * 1 = x).
3. Implementing its respective calculus derivation rule (e.g., Product Rule, Power Rule).
"""

from core.primitives import MathNode, Constant
import math

class Power(MathNode):
    """
    Represents an exponentiation operation (base raised to an exponent).
    Mathematical Concept: f(x)^n

    Attributes:
        base (MathNode): The base expression (e.g., 'x' in x^2).
        exponent (MathNode): The power expression (e.g., '2' in x^2).
    """

    def __init__(self, base, exponent):
        """
        Initializes the Power node.

        Args:
            base (MathNode): The base of the power operation.
            exponent (MathNode): The exponent/power.
        """
        self.base = base
        self.exponent = exponent

    def __repr__(self):
        """
        Returns the string representation of the power operation.
        """
        return f"{self.base}^{self.exponent}"
    
    def simplify(self):
        """
        Simplifies the exponentiation operation using standard algebraic rules.

        Rules Applied:
            1. Zero Exponent: x^0 = 1
            2. Identity Exponent: x^1 = x
            3. Constant Evaluation: c1^c2 = c3 (e.g., 2^3 = 8)
            4. Power of a Power: (x^a)^b = x^(a * b)

        Returns:
            MathNode: The most simplified form of the expression.
        """
        sim_base = self.base.simplify()
        sim_exponent = self.exponent.simplify()

        # Rule 1: x^0 = 1
        if isinstance(sim_exponent, Constant) and sim_exponent.value == 0:
            return Constant(1)
        
        # Rule 2: x^1 = x
        if isinstance(sim_exponent, Constant) and sim_exponent.value == 1:
            return sim_base

        # Rule 3: Both base and exponent are constants
        if isinstance(sim_base, Constant) and isinstance(sim_exponent, Constant):
            return Constant(sim_base.value ** sim_exponent.value)
        
        # Rule 4: (x^a)^b = x^(a * b)
        if type(sim_base).__name__ == 'Power':
            if isinstance(sim_base.exponent, Constant) and isinstance(sim_exponent, Constant):
                new_exp = Constant(sim_base.exponent.value * sim_exponent.value)
                return Power(sim_base.base, new_exp)
        
        return Power(sim_base, sim_exponent)
    
    def derive(self):
        """
        Calculates the derivative using the Power Rule combined with the Chain Rule.
        
        Calculus Rule:
            d/dx [u^n] = n * u^(n-1) * u'
            
        Note: This implementation currently assumes the exponent 'n' is a Constant.

        Returns:
            Multiply: The analytical derivative of the power expression.
        """
        # Step 1: Calculate the new exponent (n - 1)
        new_exponent = Constant(self.exponent.value - 1)

        # Step 2: Create the new base term u^(n-1)
        new_power_term = Power(self.base, new_exponent)

        # Step 3: Multiply the original exponent by the new base term: n * u^(n-1)
        power_rule = Multiply(
            self.exponent, 
            new_power_term
        )
        
        # Step 4: Apply Chain Rule by multiplying with the derivative of the base: u'
        return Multiply(
            power_rule, 
            self.base.derive()
        )  


class Add(MathNode):
    """
    Represents a mathematical addition operation.
    Mathematical Concept: f(x) + g(x)

    Attributes:
        left (MathNode): The left operand.
        right (MathNode): The right operand.
    """

    def __init__(self, left, right):
        """
        Initializes the Add node.

        Args:
            left (MathNode): The left operand of the addition.
            right (MathNode): The right operand of the addition.
        """
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Returns the string representation of the addition with protective parentheses.
        """
        return f"({self.left} + {self.right})"
    
    def simplify(self):
        """
        Simplifies the addition operation.

        Rules Applied:
            1. Identity Property (Left): 0 + x = x
            2. Identity Property (Right): x + 0 = x
            3. Constant Evaluation: c1 + c2 = c3

        Returns:
            MathNode: The simplified expression.
        """
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        # Rule 1: 0 + x = x
        if isinstance(sim_left, Constant) and sim_left.value == 0:
            return sim_right
        
        # Rule 2: x + 0 = x
        if isinstance(sim_right, Constant) and sim_right.value == 0:
            return sim_left
        
        # Rule 3: Pre-compute if both are constants
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value + sim_right.value)
        
        return Add(sim_left, sim_right)
    
    def derive(self):
        """
        Calculates the derivative using the Sum Rule.
        
        Calculus Rule:
            d/dx [f(x) + g(x)] = f'(x) + g'(x)

        Returns:
            Add: The sum of the derivatives of the left and right operands.
        """
        return Add(self.left.derive(), self.right.derive())


class Subtract(MathNode):
    """
    Represents a mathematical subtraction operation.
    Mathematical Concept: f(x) - g(x)

    Attributes:
        left (MathNode): The minuend (value being subtracted from).
        right (MathNode): The subtrahend (value to subtract).
    """

    def __init__(self, left, right):
        """
        Initializes the Subtract node.

        Args:
            left (MathNode): The left operand.
            right (MathNode): The right operand.
        """
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Returns the string representation of the subtraction operation.
        """
        return f"({self.left} - {self.right})"
    
    def simplify(self):
        """
        Simplifies the subtraction operation.

        Rules Applied:
            1. Zero Left: 0 - x = -x (Converted to -1 * x)
            2. Zero Right: x - 0 = x
            3. Constant Evaluation: c1 - c2 = c3

        Returns:
            MathNode: The simplified expression.
        """
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        # Rule 1: 0 - x = -1 * x
        if isinstance(sim_left, Constant) and sim_left.value == 0:
            return Multiply(Constant(-1), sim_right)
        
        # Rule 2: x - 0 = x
        if isinstance(sim_right, Constant) and sim_right.value == 0:
            return sim_left
        
        # Rule 3: Pre-compute if both are constants
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value - sim_right.value)
        
        return Subtract(sim_left, sim_right)
    
    def derive(self):
        """
        Calculates the derivative using the Difference Rule.
        
        Calculus Rule:
            d/dx [f(x) - g(x)] = f'(x) - g'(x)

        Returns:
            Subtract: The difference between the derivatives of the operands.
        """
        return Subtract(self.left.derive(), self.right.derive())


class Multiply(MathNode):
    """
    Represents a mathematical multiplication operation.
    Mathematical Concept: f(x) * g(x)

    Attributes:
        left (MathNode): The left multiplier.
        right (MathNode): The right multiplier.
    """

    def __init__(self, left, right):
        """
        Initializes the Multiply node.

        Args:
            left (MathNode): The first operand.
            right (MathNode): The second operand.
        """
        self.left = left
        self.right = right

    def __repr__(self):
        """
        Returns the string representation of the multiplication.
        """
        return f"({self.left}*{self.right})"
    
    def simplify(self):
        """
        Simplifies the multiplication operation.

        Rules Applied:
            1. Zero Property: 0 * x = 0  OR  x * 0 = 0
            2. Identity Property (Right): x * 1 = x
            3. Identity Property (Left): 1 * x = x
            4. Constant Evaluation: c1 * c2 = c3

        Returns:
            MathNode: The simplified expression.
        """
        sim_left = self.left.simplify()
        sim_right = self.right.simplify()

        # Rule 1: Zero multiplication yields zero
        if (isinstance(sim_right, Constant) and sim_right.value == 0) or \
           (isinstance(sim_left, Constant) and sim_left.value == 0):
            return Constant(0)
        
        # Rule 2: x * 1 = x
        if isinstance(sim_right, Constant) and sim_right.value == 1:
            return sim_left
        
        # Rule 3: 1 * x = x
        if isinstance(sim_left, Constant) and sim_left.value == 1:
            return sim_right
        
        # Rule 4: Pre-compute constants
        if isinstance(sim_left, Constant) and isinstance(sim_right, Constant):
            return Constant(sim_left.value * sim_right.value)
        
        return Multiply(sim_left, sim_right)

    def derive(self):
        """
        Calculates the derivative using the standard Product Rule.
        
        Calculus Rule:
            d/dx [u * v] = (u * v') + (u' * v)

        Returns:
            Add: The sum of the two components derived from the Product Rule.
        """
        # Component 1: u * v'
        left = Multiply(self.left, self.right.derive())
        
        # Component 2: u' * v
        right = Multiply(self.left.derive(), self.right)

        # Result: (u * v') + (u' * v)
        return Add(left, right)


class Divide(MathNode):
    """
    Represents a mathematical division operation.
    Mathematical Concept: $f(x) / g(x)$

    Attributes:
        num (MathNode): The numerator (the dividend or top value).
        den (MathNode): The denominator (the divisor or bottom value).
    """

    def __init__(self, num, den):
        """
        Initializes the Divide node.

        Args:
            num (MathNode): The numerator expression.
            den (MathNode): The denominator expression.
        """
        self.num = num
        self.den = den

    def __repr__(self):
        """
        Returns the string representation of the division operation.
        """
        return f"({self.num}/{self.den})"

    def simplify(self):
        """
        Simplifies the division operation using standard algebraic rules.

        Rules Applied:
            1. Zero Denominator Error: x / 0 is mathematically undefined.
            2. Zero Numerator: 0 / x = 0 (assuming x != 0).
            3. Identity Property: x / 1 = x.
            4. Constant Evaluation: c1 / c2 = c3.

        Raises:
            ValueError: If the denominator simplifies to a constant 0.

        Returns:
            MathNode: The simplified division expression.
        """
        sim_num = self.num.simplify()
        sim_den = self.den.simplify()
        
        # Rule 1: Division by zero check
        if isinstance(sim_den, Constant) and sim_den.value == 0:
            raise ValueError("Math Error: Division by zero is undefined.")
        
        # Rule 2: 0 / x = 0
        if isinstance(sim_num, Constant) and sim_num.value == 0:
            return Constant(0)
        
        # Rule 3: x / 1 = x
        if isinstance(sim_den, Constant) and sim_den.value == 1:
            return sim_num
        
        # Rule 4: Pre-compute if both are constants
        if isinstance(sim_num, Constant) and isinstance(sim_den, Constant):
            return Constant(sim_num.value / sim_den.value)
        
        # Rule 5: 1 / 1 = 1 (Redundant but safe fallback)
        if (isinstance(sim_num, Constant) and sim_num.value == 1) and \
           (isinstance(sim_den, Constant) and sim_den.value == 1):
            return Constant(1)
        
        return Divide(sim_num, sim_den)
    
    def derive(self):
        """
        Calculates the derivative using the standard Quotient Rule.
        
        Calculus Rule:
            $d/dx [u / v] = \frac{u'v - uv'}{v^2}$

        Returns:
            Divide: The analytical derivative representing the Quotient Rule.
        """
        # Term 1: u' * v
        term1 = Multiply(self.num.derive(), self.den)
        
        # Term 2: u * v'
        term2 = Multiply(self.num, self.den.derive())
        
        # Numerator: (u'v) - (uv')
        numerator = Subtract(term1, term2)
        
        # Denominator: v^2
        denominator = Power(self.den, Constant(2))

        # Final Result: [(u'v) - (uv')] / [v^2]
        return Divide(numerator, denominator)


class Exp(MathNode):
    """
    Represents an exponential function with base 'e' (Euler's number).
    Mathematical Concept: $e^{f(x)}$

    Attributes:
        argument (MathNode): The exponent expression applied to base 'e'.
    """
    
    def __init__(self, argument):
        """
        Initializes the Exponential node.

        Args:
            argument (MathNode): The power to which 'e' is raised.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the exponential function.
        """
        return f"e^{self.argument}"
    
    def simplify(self):
        """
        Simplifies the exponential function.

        Rules Applied:
            1. Zero Exponent: $e^0 = 1$
            2. Identity Exponent: $e^1 = e$ (returns the mathematical constant e)

        Returns:
            MathNode: The simplified exponential expression.
        """
        sim_arg = self.argument.simplify()

        if isinstance(sim_arg, Constant):
            # Rule 1: e^0 = 1
            if sim_arg.value == 0:
                return Constant(1)
            
            # Rule 2: e^1 = e
            elif sim_arg.value == 1:
                return Constant(math.e)
        
        return Exp(sim_arg)
            
    def derive(self):
        """
        Calculates the derivative using the Exponential Chain Rule.
        
        Calculus Rule:
            $d/dx [e^u] = e^u \cdot u'$

        Returns:
            Multiply: The derivative of the exponential function.
        """
        # Returns: e^u * d(u)/dx
        return Multiply(self, self.argument.derive())
    

class Log(MathNode):
    """
    Represents a natural logarithm function (base 'e').
    Mathematical Concept: $\ln(f(x))$

    Attributes:
        argument (MathNode): The inner expression of the logarithm.
    """
    
    def __init__(self, argument):
        """
        Initializes the Natural Logarithm node.

        Args:
            argument (MathNode): The value inside the logarithm.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the natural logarithm.
        """
        return f"ln({self.argument})"
    
    def simplify(self):
        """
        Simplifies the natural logarithm function.

        Rules Applied:
            1. Logarithm of 1: $\ln(1) = 0$
            2. Logarithm of base e: $\ln(e) = 1$

        Returns:
            MathNode: The simplified logarithmic expression.
        """
        sim_arg = self.argument.simplify()

        if isinstance(sim_arg, Constant):
            # Rule 1: ln(1) = 0
            if sim_arg.value == 1:
                return Constant(0)
            
            # Rule 2: ln(e) = 1
            if math.isclose(sim_arg.value, math.e):
                return Constant(1)
            
        return Log(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Logarithmic Chain Rule.
        
        Calculus Rule:
            $d/dx [\ln(u)] = \frac{1}{u} \cdot u' = \frac{u'}{u}$

        Returns:
            Divide: The derivative of the natural logarithm.
        """
        # Returns: d(u)/dx / u
        return Divide(self.argument.derive(), self.argument)