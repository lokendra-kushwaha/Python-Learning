"""
Public API Wrapper for the Math Engine.

This module provides a clean, user-friendly interface for building 
mathematical equations. Instead of manually instantiating AST classes 
like `Sin(Variable('x'))`, users can write natural Pythonic expressions 
like `sin(x)`.

It also pre-defines standard mathematical constants to prevent users 
from accidentally treating them as variables.
"""

import math
from core.primitives import Constant
from operations.arithmetic import Log, Exp
from operations.trig import Sin, Cos, Tan, Cot, Sec, Cosec

# ==========================================
# FIXED MATHEMATICAL CONSTANTS
# ==========================================
# These constants are instantiated once and treated as immutable leaves in the AST.

e = Constant(math.e)
"""Constant: Represents Euler's number ($e \approx 2.71828...$)."""

pi = Constant(math.pi)
"""Constant: Represents the ratio of a circle's circumference to its diameter ($\pi \approx 3.14159...$)."""


# ==========================================
# TRANSCENDENTAL WRAPPER FUNCTIONS
# ==========================================

def log(argument):
    """
    Creates a natural logarithm (base 'e') expression.
    Mathematical Concept: $\ln(x)$

    Args:
        argument (MathNode, int, float): The inner expression.

    Returns:
        Log: An AST node representing the natural logarithm.
    """
    return Log(argument)


def exp(argument):
    """
    Creates an exponential expression with base 'e'.
    Mathematical Concept: $e^x$

    Args:
        argument (MathNode, int, float): The exponent expression.

    Returns:
        Exp: An AST node representing the exponential function.
    """
    return Exp(argument)


# ==========================================
# TRIGONOMETRIC WRAPPER FUNCTIONS
# ==========================================

def sin(argument):
    """
    Creates a sine trigonometric expression.
    Mathematical Concept: $\sin(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Sin: An AST node representing the sine function.
    """
    return Sin(argument)


def cos(argument):
    """
    Creates a cosine trigonometric expression.
    Mathematical Concept: $\cos(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Cos: An AST node representing the cosine function.
    """
    return Cos(argument)


def tan(argument):
    """
    Creates a tangent trigonometric expression.
    Mathematical Concept: $\tan(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Tan: An AST node representing the tangent function.
    """
    return Tan(argument)


def cot(argument):
    """
    Creates a cotangent trigonometric expression.
    Mathematical Concept: $\cot(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Cot: An AST node representing the cotangent function.
    """
    return Cot(argument)


def sec(argument):
    """
    Creates a secant trigonometric expression.
    Mathematical Concept: $\sec(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Sec: An AST node representing the secant function.
    """
    return Sec(argument)


def cosec(argument):
    """
    Creates a cosecant trigonometric expression.
    Mathematical Concept: $\csc(x)$

    Args:
        argument (MathNode, int, float): The angle/expression.

    Returns:
        Cosec: An AST node representing the cosecant function.
    """
    return Cosec(argument)