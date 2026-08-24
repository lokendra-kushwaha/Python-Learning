"""
Trigonometric Operations Module for the Math Engine.

This module introduces advanced transcendental mathematical functions 
(Sine, Cosine, Tangent, Cotangent, etc.) into the Abstract Syntax Tree (AST).

Each class represents a specific trigonometric operation and implements:
1. An AST node structure for building complex equations.
2. The standard analytical calculus derivative using the Chain Rule.
"""

from core.primitives import MathNode, Constant
from operations.arithmetic import Multiply, Divide, Power


class Sin(MathNode):
    """
    Represents the mathematical Sine function.
    Mathematical Concept: $\sin(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the sine function.
    """

    def __init__(self, argument):
        """
        Initializes the Sine node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the sine function.
        """
        return f"sin({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the sine function.
        (Note: Advanced trigonometric identities can be added here in the future).

        Returns:
            Sin: A new Sine node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Sin(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Trigonometric Chain Rule.
        
        Calculus Rule:
            $d/dx [\sin(u)] = \cos(u) \cdot u'$

        Returns:
            Multiply: The analytical derivative representing the rule.
        """
        return Multiply(
            Cos(self.argument), 
            self.argument.derive()
        )
    

class Cos(MathNode):
    """
    Represents the mathematical Cosine function.
    Mathematical Concept: $\cos(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the cosine function.
    """

    def __init__(self, argument):
        """
        Initializes the Cosine node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the cosine function.
        """
        return f"cos({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the cosine function.

        Returns:
            Cos: A new Cosine node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Cos(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Trigonometric Chain Rule.
        
        Calculus Rule:
            $d/dx [\cos(u)] = -\sin(u) \cdot u'$

        Returns:
            Multiply: The analytical derivative representing the rule.
        """
        return Multiply(
            Multiply(
                Constant(-1), 
                Sin(self.argument)
            ),
            self.argument.derive()
        )
    

class Tan(MathNode):
    """
    Represents the mathematical Tangent function.
    Mathematical Concept: $\tan(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the tangent function.
    """

    def __init__(self, argument):
        """
        Initializes the Tangent node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument
    
    def __repr__(self):
        """
        Returns the string representation of the tangent function.
        """
        return f"tan({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the tangent function.

        Returns:
            Tan: A new Tangent node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Tan(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Quotient/Chain Rule formula.
        
        Calculus Rule:
            $d/dx [\tan(u)] = \sec^2(u) \cdot u' = \frac{u'}{\cos^2(u)}$

        Returns:
            Divide: The analytical derivative of the tangent function.
        """
        # Numerator: u'
        numerator = self.argument.derive()
        
        # Denominator: cos^2(u)
        denominator = Power(Cos(self.argument), Constant(2))
        
        return Divide(
            numerator, 
            denominator
        )


class Cot(MathNode):
    """
    Represents the mathematical Cotangent function.
    Mathematical Concept: $\cot(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the cotangent function.
    """

    def __init__(self, argument):
        """
        Initializes the Cotangent node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the cotangent function.
        """
        return f"cot({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the cotangent function.

        Returns:
            Cot: A new Cotangent node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Cot(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the standard Chain Rule.
        
        Calculus Rule:
            $d/dx [\cot(u)] = -\csc^2(u) \cdot u' = \frac{-u'}{\sin^2(u)}$

        Returns:
            Divide: The analytical derivative of the cotangent function.
        """
        return Divide(
            Multiply(
                Constant(-1), 
                self.argument.derive()
            ),
            Power(
                Sin(self.argument), 
                Constant(2)
            )
        )


class Sec(MathNode):
    """
    Represents the mathematical Secant function.
    Mathematical Concept: $\sec(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the secant function.
    """

    def __init__(self, argument):
        """
        Initializes the Secant node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the secant function.
        """
        return f"sec({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the secant function.

        Returns:
            Sec: A new Secant node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Sec(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Trigonometric Chain Rule.
        
        Calculus Rule:
            $d/dx [\sec(u)] = \sec(u) \cdot \tan(u) \cdot u'$

        Returns:
            Multiply: The analytical derivative of the secant function.
        """
        return Multiply(
            Multiply(
                Sec(self.argument), 
                Tan(self.argument)
            ),
            self.argument.derive()
        )
    

class Cosec(MathNode):
    """
    Represents the mathematical Cosecant function.
    Mathematical Concept: $\csc(f(x))$

    Attributes:
        argument (MathNode): The inner expression/angle of the cosecant function.
    """

    def __init__(self, argument):
        """
        Initializes the Cosecant node.

        Args:
            argument (MathNode): The inner expression.
        """
        self.argument = argument

    def __repr__(self):
        """
        Returns the string representation of the cosecant function.
        """
        return f"cosec({self.argument})"
    
    def simplify(self):
        """
        Simplifies the inner argument of the cosecant function.

        Returns:
            Cosec: A new Cosecant node with a simplified argument.
        """
        sim_arg = self.argument.simplify()
        return Cosec(sim_arg)
    
    def derive(self):
        """
        Calculates the derivative using the Trigonometric Chain Rule.
        
        Calculus Rule:
            $d/dx [\csc(u)] = -\csc(u) \cdot \cot(u) \cdot u'$

        Returns:
            Multiply: The analytical derivative of the cosecant function.
        """
        return Multiply(
            Multiply(
                Constant(-1),
                Multiply(
                    Cosec(self.argument), 
                    Cot(self.argument)
                )
            ),
            self.argument.derive()
        )