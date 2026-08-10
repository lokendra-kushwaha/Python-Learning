"""
Advanced 3D Geometry Module
---------------------------
This module handles calculations related to 3D Lines.
It provides functionalities to generate Vector and Cartesian equations of a 3D Line.

This engine supports two initialization methods:
1. Point + Parallel Vector (Given a point 'A' and a parallel vector 'b')
2. Two Points (Given two points 'A' and 'B' on the line)
"""
# Adding the custom Vector module folder path to sys.path
# This allows importing Point and Vector classes from external files without errors
import sys
sys.path.append(r"L:/Python/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")
from vectors import Vector
from vectors import Point
from geometry_3d import DirectionRatio


def get_vector_equation(A:Point = None, b:Vector = None, B:Point = None) -> str:
    """
    Generates the Vector Equation of a 3D line.
    
    Parameters:
    A (Point): The starting point on the line (Position Vector).
    b (Vector, optional): The vector parallel to the line.
    B (Point, optional): The second point on the line (used if 'b' is not provided).
    
    Returns:
    str: A clean and formatted string representation of the vector equation.
    """
    # Condition 1: When a Point (A) and a Parallel Vector (b) are provided
    if b is not None and B is None:
        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({b})".replace("+ -", "- ")
    
     # Condition 2: When two Points (A and B) are provided
    if b is None and B is not None:
        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({B.x - A.x}i + {B.y - A.y}j + {B.z - A.z}k)".replace("+ -", "- ")

def get_cartesian_equation(A:Point = None, b:Vector = None, B:Point = None) -> str:
    """
    Generates the Cartesian Equation of a 3D line.
    
    Parameters:
    A (Point): The starting point on the line (x1, y1, z1).
    b (Vector, optional): The vector providing Direction Ratios (a, b, c).
    B (Point, optional): The second point used to calculate Direction Ratios.
    
    Returns:
    str: A formatted string of the Cartesian equation.
    """
    # Condition 1: When a Point and a Parallel Vector (b) are provided
    if b is not None and B is None:
        val_a = b.a
        val_b = b.b
        val_c = b.c
        x1, y1, z1 = A.x, A.y, A.z

        return f"(x - {x1})/{val_a} = (y - {y1})/{val_b} = (z - {z1})/{val_c}".replace("- -", "+ ")
        # Using replace("- -", "+ ") to ensure negative coordinates are printed correctly 

    # Condition 2: When two Points (A and B) are provided   
    if b is None and B is not None:
        x1, y1, z1 = A.x, A.y, A.z
        x2, y2, z2 = B.x, B.y, B.z

        return f"(x - {x1})/{x2 - x1} = (y - {y1})/{y2 - y1} = (z - {z1})/{z2 - z1}".replace("- -", "+ ")

def get_point_on_line(A:Point = None, b:Vector = None, B:Point = None, lambda_val:float = None) -> Vector:
    """
    Calculates a new Point (as a Vector) on the line for a specific value of Lambda.
    This is the main function for mathematical computations.
    
    Parameters:
    A (Point): The starting point.
    b (Vector, optional): The parallel vector.
    B (Point, optional): The second point.
    lambda_val (float): The constant scalar value for Lambda.
    
    Returns:
    Vector: The position vector of the newly calculated point.
    """
    # Condition 1: Point and Vector method
    if b is not None and B is None:
        new_x = A.x + lambda_val*b.a
        new_y = A.y + lambda_val*b.b
        new_z = A.z + lambda_val*b.c
        return Vector(new_x, new_y, new_z)

     # Condition 2: Two Points method
    if b is None and B is not None :
        new_x = A.x + lambda_val*(B.x - A.x)
        new_y = A.y + lambda_val*(B.y - A.y)
        new_z = A.z + lambda_val*(B.z - A.z)
        return Vector(new_x, new_y, new_z)

if __name__ == "__main__":
    p1 = Point()
    p2 = Point()
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    b = Vector()

    print("Vector Eqaution - ", get_vector_equation(A=p1, b=b))
    print("Vector Eqaution - ", get_vector_equation(A=p1, B=p2))
    print("Cartisian Eqaution - ", get_cartesian_equation(A=p1, b=b))
    print("Cartisian Eqaution - ", get_cartesian_equation(A=p1, B=p2))
    print(get_point_on_line(A=p1, b=b, lambda_val=2))
    print(get_point_on_line(A=p1, B=p2, lambda_val=2))