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
sys.path.append(r"L:/01_AI_and_Data_Science/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")

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
    

def validate_type(var_name: str, var_value: any, expected_type: tuple | type):
    """
    Validates if a variable matches the expected class type based on its string name.

    This helper function bypasses Python's strict memory address checking by 
    comparing the names of the classes. It prevents 'ghost class' errors when 
    reloading modules in active environments.

    Args:
        var (Any): The variable or object whose type needs to be checked.
        expected_type (type): The class/type that the variable is expected to be.
        var_name (str): The name of the variable (used to format the error message).

    Raises:
        TypeError: If the class name of var does not match the class name 
                   of expected_type.
    """
    if not isinstance(var_value, expected_type):
        if isinstance(expected_type, tuple):
            expected_name = " or ".join([t.__name__ for t in expected_type])
        else:
            expected_name = expected_type.__name__
            
        raise TypeError(f"Expected '{var_name}' to be {expected_name}, got {type(var_value).__name__} instead.")

#================================================================================================

class CartesianLine:

    def __init__(self, A: Point = None , b: Vector = None):
        if A is not None and b is not None:
            validate_type('A', A, Point)
            validate_type('b', b, Vector)
            self.A = A
            self.b = b
        else:
            self.A = Point()
            self.b = Vector()

    @classmethod
    def from_two_points(cls, A: Point, B: Point):
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        vec_b = Vector(B.x - A.x, B.y - A.y, B.z - A.z)

        return cls(A = A, b = vec_b)

    def __str__(self):
        return f"(x - {self.A.x})/{self.b.a} = (y - {self.A.y})/{self.b.b} = (z - {self.A.z})/{self.b.c}".replace("- -", "+ ")


class VectorLine:

    def __init__(self, a: Vector = None, b: Vector = None):
        if a is not None and b is not None:
            validate_type('a', a, Vector)
            validate_type('b', b, Vector)
            
            self.a = a
            self.b = b
        else:
            self.a = Vector()
            self.b = Vector()


    @classmethod
    def from_two_points(cls, A: Point, B: Point):
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        vec_a = Vector(A.x, A.y, A.z)
        vec_b = Vector(B.x - A.x, B.y - A.y, B.z - B.z)

        return cls(a = vec_a, b = vec_b)

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
        validate_type('A', A, Point)
        validate_type('b', b, Vector)

        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({b})".replace("+ -", "- ")
    
     # Condition 2: When two Points (A and B) are provided
    if b is None and B is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({B.x - A.x}i + {B.y - A.y}j + {B.z - A.z}k)".replace("+ -", "- ")

    else:
        raise ValueError(
            "Ambiguous arguments definition. You must provide a complete parameter set "
            "e.g., either valid Point - Vector OR Point - Point."
        )


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
        validate_type('A', A, Point)
        validate_type('b', b, Vector)

        val_a = b.a
        val_b = b.b
        val_c = b.c
        x1, y1, z1 = A.x, A.y, A.z

        return f"(x - {x1})/{val_a} = (y - {y1})/{val_b} = (z - {z1})/{val_c}".replace("- -", "+ ")
        # Using replace("- -", "+ ") to ensure negative coordinates are printed correctly 

    # Condition 2: When two Points (A and B) are provided   
    if b is None and B is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        x1, y1, z1 = A.x, A.y, A.z
        x2, y2, z2 = B.x, B.y, B.z

        return f"(x - {x1})/{x2 - x1} = (y - {y1})/{y2 - y1} = (z - {z1})/{z2 - z1}".replace("- -", "+ ")

    else:
        raise ValueError(
            "Ambiguous arguments definition. You must provide a complete parameter set "
            "e.g., either valid Point - Vector OR Point - Point."
        )


def get_point_on_line(line: VectorLine, lambda_val: float) -> Point:
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
    validate_type('line', line, VectorLine)
    validate_type('lambda_val', lambda_val, (float, int))

    vec_a = line.a
    vec_b = line.b
    new_x = vec_a.a + lambda_val*vec_b.a
    new_y = vec_a.b + lambda_val*vec_b.b
    new_z = vec_a.c + lambda_val*vec_b.c
    return Point(new_x, new_y, new_z)


def get_angle_between_lines(line1: VectorLine, line2: VectorLine) -> float:
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
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    b1 = line1.b
    b2 = line2.b

    return angle_between(b1, b2)
    
def get_distance_between_lines(line1: VectorLine, line2: VectorLine) -> float:
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
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)
    
    a1 = line1.a
    a2 = line2.a

    b1 = line1.b
    b2 = line2.b
    
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
    
    v1 = Vector()
    v2 = Vector()

    vec_line1 = VectorLine()
    vec_line2 = VectorLine()

    lx = VectorLine.from_two_points(A=p1, B=p2)
    print(lx)

    cx = CartesianLine.from_two_points(A=p1, B=p2)
    print(cx)

    print("\n[Generated Test Objects]")
    print(f"Point 1 (p1): {p1}")
    print(f"Point 2 (p2): {p2}")
    print(f"Vector 1 (v1): {v1}")
    print(f"Vector 2 (v2): {v2}")
    print(f"Vector Line (vec_line1): {vec_line1}")
    print(f"Vector Line (vec_line2): {vec_line2}")

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
    print(f"Point : {get_point_on_line(line=vec_line1, lambda_val=2)}")

    print("\n" + "-"*50)
    print("3. Angle Between Two Lines")
    print("-" * 50)
    print(f"Angle : {get_angle_between_lines(line1=vec_line1, line2=vec_line2)}°")

    print("\n" + "-"*50)
    print("4. Shortest Distance Between Two Lines")
    print("-" * 50)
    print(f"Distance (Skew)       : {get_distance_between_lines(line1=vec_line1, line2=vec_line2)}")
    print("="*50 + "\n")