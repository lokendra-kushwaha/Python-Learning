"""
Advanced 3D Geometry Module
---------------------------
This module handles calculations related to 3D Lines.
It provides functionalities to generate Vector and Cartesian equations,
find points, and calculate angles and distances between 3D lines.

This engine supports two initialization methods:
1. Point + Parallel Vector (Given a point 'A' and a parallel vector 'b')
2. Two Points (Given two points 'A' and 'B' on the line)
"""
# Adding the custom Vector module folder path to sys.path
# This allows importing Point and Vector classes from external files without errors
import sys
sys.path.append(r"L:/Python/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")

from vectors import Vector, Point
from advance_vectors import angle_between, cross_product, dot_product 

#================================================================================================
def get_absolute_value(d: float) -> float:
    """
    Returns the absolute (positive) value of a given number.
    Used mathematically to ensure distance calculations are never negative.
    """
    if d >= 0:
        return d
    else:
        return -1 * d
#================================================================================================

class CartesianLine:

    def __init__(self, A: Point = None, a: Vector = None, b: Vector = None):
        if A is not None and b is not None:
            self.A = A
            self.b = b
        else:
            self.A = Point()
            self.b = Vector()

    def __str__(self):
        return f"(x - {self.A.x})/{self.b.a} = (y - {self.A.y})/{self.b.b} = (z - {self.A.z})/{self.b.c}".replace("- -", "+ ")

class VectorLine:

    def __init__(self, a: Vector = None, b: Vector = None):
        if a is not None and b is not None:
            self.a = a
            self.b = b
        else:
            self.a = Vector()
            self.b = Vector()

    def __str__(self):
        return f"xi + yj + zk = {self.a} + \u03BB({self.b})".replace("+ -", "- ")
    
    def __repr__(self):
        return self.__str__(self)

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

def get_angle_between_lines(A1:Point = None, b1:Vector = None, B1:Point = None, A2:Point = None, b2:Vector = None, B2:Point = None) -> float:
    """
    Calculates the angle between two 3D lines. Automatically resolves the direction 
    vectors based on the input combination (Points vs Parallel Vectors).
    
    Parameters:
    A1, A2 (Point): Starting points of Line 1 and Line 2.
    b1, b2 (Vector, optional): Parallel vectors of Line 1 and Line 2.
    B1, B2 (Point, optional): Second points on Line 1 and Line 2.
    
    Returns:
    float: The angle between the two lines (in degrees/radians depending on base utility).
    """
    if B1 is None and B2 is None:
        pass
            
    if b1 is None and b2 is None:
        b1_a, b1_b, b1_c = B1.x - A1.x, B1.y - A1.y, B1.z - A1.z
        b2_a, b2_b, b2_c = B2.x - A2.x, B2.y - A2.y, B2.z - A2.z
        b1 = Vector(b1_a, b1_b, b1_c)
        b2 = Vector(b2_a, b2_b, b2_c)
    
    if B1 is None and b2 is None:
        b2_a, b2_b, b2_c = B2.x - A2.x, B2.y - A2.y, B2.z - A2.z
        b2 = Vector(b2_a, b2_b, b2_c)
    
    if b1 is None and B2 is None:
        b1_a, b1_b, b1_c = B1.x - A1.x, B1.y - A1.y, B1.z - A1.z
        b1 = Vector(b1_a, b1_b, b1_c)
    
    return angle_between(b1, b2)
    
def get_distance_between_lines(A1:Point = None, b1:Vector = None, B1:Point = None, A2:Point = None, b2:Vector = None, B2:Point = None) -> float:
    """
    Calculates the shortest distance between two 3D lines. 
    Intelligently handles both Skew Lines and Parallel Lines scenarios.
    
    Parameters:
    A1, A2 (Point): Starting points of Line 1 and Line 2.
    b1, b2 (Vector, optional): Parallel vectors of Line 1 and Line 2.
    B1, B2 (Point, optional): Second points on Line 1 and Line 2.
    
    Returns:
    float: The shortest absolute distance between the two lines.
    """
    a1 = Vector(A1.x, A1.y, A1.z)
    a2 = Vector(A2.x, A2.y, A2.z)

    if B1 is None and B2 is None:
        pass
    
    elif b1 is None and b2 is None:
        b1_a, b1_b, b1_c = B1.x - A1.x, B1.y - A1.y, B1.z - A1.z
        b2_a, b2_b, b2_c = B2.x - A2.x, B2.y - A2.y, B2.z - A2.z
        b1 = Vector(b1_a, b1_b, b1_c)
        b2 = Vector(b2_a, b2_b, b2_c)

    elif B1 is None and b2 is None:
        b2_a, b2_b, b2_c = B2.x - A2.x, B2.y - A2.y, B2.z - A2.z
        b2 = Vector(b2_a, b2_b, b2_c)

    elif b1 is None and B2 is None:
        b1_a, b1_b, b1_c = B1.x - A1.x, B1.y - A1.y, B1.z - A1.z
        b1 = Vector(b1_a, b1_b, b1_c)
    
    mag_cross = Vector.magnitude(cross_product(b1, b2))
    # Skew Lines Condition
    if mag_cross != 0:
        return get_absolute_value(dot_product(cross_product(b1, b2), (a2 - a1)) / mag_cross)
    else:
        return get_absolute_value(Vector.magnitude(cross_product(b1, (a2 - a1))) / Vector.magnitude(b1))
        

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 3D Geometry Module Initialization")
    print("="*50)
    
    # Generate random points and vectors
    p1 = Point()
    p2 = Point()
    p3 = Point()
    p4 = Point()
    
    v1 = Vector()
    v2 = Vector()

    print("\n[Generated Test Objects]")
    print(f"Point 1 (p1): {p1}")
    print(f"Point 2 (p2): {p2}")
    print(f"Point 3 (p3): {p3}")
    print(f"Point 4 (p4): {p4}")
    print(f"Vector 1 (v1): {v1}")
    print(f"Vector 2 (v2): {v2}")

    print("\n" + "-"*50)
    print("1. Line Equations (Vector & Cartesian)")

    print("-" * 50)
    print(f"Vector Eq (Point + Vector)  :  {get_vector_equation(A=p1, b=v1)}")
    print(f"Vector Eq (Two Points)      :  {get_vector_equation(A=p1, B=p2)}")
    print(f"Cartesian Eq (Point + Vector): {get_cartesian_equation(A=p1, b=v1)}")
    print(f"Cartesian Eq (Two Points)    : {get_cartesian_equation(A=p1, B=p2)}")

    print("\n" + "-"*50)
    print("2. Point on Line (Lambda = 2)")
    print("-" * 50)
    print(f"Point (Point + Vector method): {get_point_on_line(A=p1, b=v1, lambda_val=2)}")
    print(f"Point (Two Points method)    : {get_point_on_line(A=p1, B=p2, lambda_val=2)}")

    print("\n" + "-"*50)
    print("3. Angle Between Two Lines")
    print("-" * 50)
    print(f"Angle (Case 1: v1 & v2)      : {get_angle_between_lines(A1=p1, A2=p2, b1=v1, b2=v2)}°")
    print(f"Angle (Case 2: p1-p2 & p3-p4): {get_angle_between_lines(A1=p1, A2=p2, B1=p3, B2=p4)}°")
    print(f"Angle (Case 3: p1-p2 & v2)   : {get_angle_between_lines(A1=p1, B1=p2, A2=p3, b2=v2)}°")
    print(f"Angle (Case 4: v1 & p3-p4)   : {get_angle_between_lines(A1=p1, b1=v1, A2=p3, B2=p4)}°")

    print("\n" + "-"*50)
    print("4. Shortest Distance Between Two Lines")
    print("-" * 50)
    print(f"Distance (Skew Case 1)       : {get_distance_between_lines(A1=p1, A2=p2, b1=v1, b2=v2)}")
    print(f"Distance (Skew Case 2)       : {get_distance_between_lines(A1=p1, A2=p2, B1=p3, B2=p4)}")
    print(f"Distance (Skew Case 3)       : {get_distance_between_lines(A1=p1, B1=p2, A2=p3, b2=v2)}")
    print(f"Distance (Skew Case 4)       : {get_distance_between_lines(A1=p1, b1=v1, A2=p3, B2=p4)}")
    print(f"Distance (Parallel Lines)    : {get_distance_between_lines(A1=p1, b1=v1, A2=p2, b2=v1)}")
    print("="*50 + "\n")