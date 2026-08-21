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
    """
    Represents a 3D line in Cartesian (symmetric) form.
    Equation format: (x - x1)/a = (y - y1)/b = (z - z1)/c
    
    Attributes:
        A (Point): A point that the line passes through (x1, y1, z1).
        b (Vector): The direction vector of the line (a, b, c).
    """

    def __init__(self, A: 'Point' = None, b: 'Vector' = None):
        """
        Initializes a CartesianLine object.

        Args:
            A (Point, optional): A point on the line. Defaults to origin Point(0,0,0).
            b (Vector, optional): The direction vector. Defaults to null Vector(0,0,0).
        """
        if A is not None and b is not None:
            validate_type('A', A, Point)
            validate_type('b', b, Vector)
            
            mag_b_sq = (b.a ** 2) + (b.b ** 2) + (b.c ** 2)
            if mag_b_sq == 0:
                raise ValueError("Direction vector of the line cannot be a zero vector.")
            
            self.A = A
            self.b = b
        
        else:          
            self.A = Point()
            self.b = Vector()

    @classmethod
    def from_two_points(cls, A: 'Point', B: 'Point'):
        """
        Creates a CartesianLine from two given points.
        The direction vector is calculated as (B - A).

        Args:
            A (Point): The starting point of the line.
            B (Point): Another point on the line.

        Returns:
            CartesianLine: A new CartesianLine instance.
        """
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        # Direction vector 'b' is the difference between point B and point A coordinates
        vec_b = Vector(B.x - A.x, B.y - A.y, B.z - A.z)

        return cls(A=A, b=vec_b)

    def __str__(self):
        """
        Returns the string representation of the Cartesian equation.
        
        Returns:
            str: The formatted equation string.
        """
        # The replace("- -", "+ ") is a neat trick! 
        # If A.x is -5, f-string makes it "(x - -5)". The replace changes it to "(x + 5)"
        return f"(x - {self.A.x})/{self.b.a} = (y - {self.A.y})/{self.b.b} = (z - {self.A.z})/{self.b.c}".replace("- -", "+ ")


class VectorLine:
    """
    Represents a 3D line in Vector form.
    Equation format: r = a + \u03BB(b)
    Where 'a' is the position vector of a point, and 'b' is the direction vector.
    
    Attributes:
        a (Vector): The position vector of a known point on the line.
        b (Vector): The direction vector parallel to the line.
    """

    def __init__(self, a: 'Vector' = None, b: 'Vector' = None):
        """
        Initializes a VectorLine object.

        Args:
            a (Vector, optional): Position vector of a point on the line.
            b (Vector, optional): Direction vector of the line.
        """
        if a is not None and b is not None:
            validate_type('a', a, Vector)
            validate_type('b', b, Vector)

            mag_b_sq = (b.a ** 2) + (b.b ** 2) + (b.c ** 2)
            if mag_b_sq == 0:
                raise ValueError("Direction vector of the line cannot be a zero vector.")
            
            self.a = a
            self.b = b
        
        else:
            self.a = Vector()
            self.b = Vector()

    @classmethod
    def from_two_points(cls, A: 'Point', B: 'Point'):
        """
        Creates a VectorLine from two given points.

        Args:
            A (Point): The starting point.
            B (Point): The ending point to determine direction.

        Returns:
            VectorLine: A new VectorLine instance.
        """
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        # Position vector 'a' is just the coordinates of point A
        vec_a = Vector(A.x, A.y, A.z)
        # Direction vector 'b' is the difference between B and A
        vec_b = Vector(B.x - A.x, B.y - A.y, B.z - A.z) # Fixed a bug here: was B.z - B.z

        return cls(a=vec_a, b=vec_b)
     
    def __str__(self):
        """
        Returns the string representation of the Vector equation.
        
        Returns:
            str: The formatted vector equation.
        """
        # replace("+ -", "- ") cleans up negative components, e.g., "5i + -3j" becomes "5i - 3j"
        return f"xi + yj + zk = {self.a} + \u03BB({self.b})".replace("+ -", "- ")
    
    def __repr__(self):
        """Returns the developer-friendly string representation."""
        return self.__str__()


def get_vector_equation(A: 'Point' = None, b: 'Vector' = None, B: 'Point' = None) -> str:
    """
    Generates the Vector Equation of a 3D line as a string.
    
    Args:
        A (Point, optional): The starting point on the line (Position Vector).
        b (Vector, optional): The vector parallel to the line.
        B (Point, optional): The second point on the line (used if 'b' is not provided).
    
    Returns:
        str: A clean and formatted string representation of the vector equation.
        
    Raises:
        ValueError: If a valid combination of arguments (Point+Vector or Point+Point) is not provided.
    """
    # Scenario 1: Point and Direction Vector given (r = a + \u03BBb)
    if b is not None and B is None:
        validate_type('A', A, Point)
        validate_type('b', b, Vector)
        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({b})".replace("+ -", "- ")
    
    # Scenario 2: Two Points given (r = a + \u03BB(b - a))
    if b is None and B is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)
        return f"{A.x}i + {A.y}j + {A.z}k + \u03BB({B.x - A.x}i + {B.y - A.y}j + {B.z - A.z}k)".replace("+ -", "- ")

    raise ValueError(
        "Ambiguous arguments. Provide either (A: Point, b: Vector) OR (A: Point, B: Point)."
    )


def get_cartesian_equation(A: 'Point' = None, b: 'Vector' = None, B: 'Point' = None) -> str:
    """
    Generates the Cartesian Equation of a 3D line as a string.
    
    Args:
        A (Point, optional): The starting point on the line (x1, y1, z1).
        b (Vector, optional): The vector providing Direction Ratios (a, b, c).
        B (Point, optional): The second point used to calculate Direction Ratios.
    
    Returns:
        str: A formatted string of the Cartesian equation.
        
    Raises:
        ValueError: If proper argument pairs are not supplied.
    """
    # Scenario 1: Point and Direction Ratios given
    if b is not None and B is None:
        validate_type('A', A, Point)
        validate_type('b', b, Vector)
        
        return f"(x - {A.x})/{b.a} = (y - {A.y})/{b.b} = (z - {A.z})/{b.c}".replace("- -", "+ ")

    # Scenario 2: Two Points given (Direction ratios are x2-x1, y2-y1, z2-z1)
    if b is None and B is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)

        dx, dy, dz = B.x - A.x, B.y - A.y, B.z - A.z
        return f"(x - {A.x})/{dx} = (y - {A.y})/{dy} = (z - {A.z})/{dz}".replace("- -", "+ ")

    raise ValueError(
        "Ambiguous arguments. Provide either (A: Point, b: Vector) OR (A: Point, B: Point)."
    )


def get_point_on_line(line: VectorLine, lambda_val: float) -> 'Point':
    """
    Calculates a specific Point on the line by plugging in a value for Lambda (\u03BB).
    Formula used: Point = a + \u03BB(b)
    
    Args:
        line (VectorLine): The line on which we want to find the point.
        lambda_val (float): The scalar value multiplier for the direction vector.
    
    Returns:
        Point: The calculated coordinates of the new point.
    """
    validate_type('line', line, VectorLine)
    validate_type('lambda_val', lambda_val, (float, int))

    # Calculate new x, y, z by scaling the direction vector and adding to the position vector
    new_x = line.a.a + (lambda_val * line.b.a)
    new_y = line.a.b + (lambda_val * line.b.b)
    new_z = line.a.c + (lambda_val * line.b.c)
    
    return Point(new_x, new_y, new_z)


def get_angle_between_lines(line1: VectorLine, line2: VectorLine) -> float:
    """
    Calculates the angle between two 3D lines.
    The angle between two lines is identical to the angle between their direction vectors (b1 and b2).
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
    
    Returns:
        float: The angle between the two lines in degrees/radians.
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    # Angle only depends on direction vectors
    return angle_between(line1.b, line2.b)
    

def get_distance_between_lines(line1: VectorLine, line2: VectorLine) -> float:
    """
    Calculates the shortest distance between two 3D lines. 
    It checks whether the lines are parallel or skew, and applies the respective formula.
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
    
    Returns:
        float: The absolute shortest distance between the two lines.
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)
    
    a1, b1 = line1.a, line1.b
    a2, b2 = line2.a, line2.b
    
    # The magnitude of the cross product of the direction vectors
    # If this is 0, the vectors are parallel.
    mag_cross = Vector.magnitude(cross_product(b1, b2))
    
    if mag_cross != 0:
        # Skew Lines Formula: |(b1 x b2) \u2022 (a2 - a1)| / |b1 x b2|
        numerator = dot_product(cross_product(b1, b2), (a2 - a1))
        return get_absolute_value(numerator / mag_cross)
    else:
        # Parallel Lines Formula: |b1 x (a2 - a1)| / |b1|
        numerator = Vector.magnitude(cross_product(b1, (a2 - a1)))
        return get_absolute_value(numerator / Vector.magnitude(b1))


def get_foot_of_perpendicular(P: 'Point', line: 'VectorLine') -> 'Point':
    """
    Calculates the Foot of the Perpendicular dropped from a Point to a 3D line.
    
    Args:
        P (Point): The external point.
        line (VectorLine): The target line.
        
    Returns:
        Point: The exact coordinates of the foot on the line.
        
    Raises:
        ValueError: If the direction vector of the line is a zero vector.
    """
    validate_type('P', P, Point)
    validate_type('line', line, VectorLine)

    a = line.a  # Position vector of the line
    b = line.b  # Direction vector of the line
    
    # Create a vector from the line's position vector 'a' to the external point 'P'
    vec_p_minus_a = Vector(P.x - a.a, P.y - a.b, P.z - a.c)
    
    # Calculate the dot product of (p - a) and the direction vector 'b'
    dot_num = (vec_p_minus_a.a * b.a) + (vec_p_minus_a.b * b.b) + (vec_p_minus_a.c * b.c)
    
    # Calculate the squared magnitude of the direction vector 'b'
    mag_b_sq = (b.a ** 2) + (b.b ** 2) + (b.c ** 2)
    
    if mag_b_sq == 0:
        raise ValueError("Direction vector of the line cannot be a zero vector.")
        
    # Find the scalar multiplier (Lambda)
    lambda_val = dot_num / mag_b_sq
    
    # Substitute lambda back into the line equation to find the exact point
    return get_point_on_line(line, lambda_val)


def get_distance_point_to_line(P: 'Point', line: 'VectorLine') -> float:
    """
    Calculates the shortest (perpendicular) distance from a Point to a Line.
    
    Args:
        P (Point): The external point.
        line (VectorLine): The target line.
        
    Returns:
        float: The absolute shortest distance.
    """
    validate_type('P', P, Point)
    validate_type('line', line, VectorLine)

    # Retrieve the foot of the perpendicular
    F = get_foot_of_perpendicular(P, line)
    
    # Create a vector connecting the original point and the foot
    vec_PF = Vector(F.x - P.x, F.y - P.y, F.z - P.z)
    
    # Return the magnitude of this vector
    return Vector.magnitude(vec_PF)


def get_image_of_point(P: 'Point', line: 'VectorLine') -> 'Point':
    """
    Calculates the image (reflection) of a Point across a 3D line.
    
    The foot of the perpendicular (F) acts as the midpoint between 
    the original point (P) and its image (P'). 
    Derived formula: P' = 2F - P.
    
    Args:
        P (Point): The original point to be reflected.
        line (VectorLine): The line acting as a mirror.
        
    Returns:
        Point: The coordinates of the reflected image point.
    """
    validate_type('P', P, Point)
    validate_type('line', line, VectorLine)

    # Calculate the midpoint (Foot of Perpendicular)
    F = get_foot_of_perpendicular(P, line)
    
    # Apply the midpoint theorem logic across all axes
    image_x = (2 * F.x) - P.x
    image_y = (2 * F.y) - P.y
    image_z = (2 * F.z) - P.z
    
    return Point(image_x, image_y, image_z)

def is_parallel(line1: 'VectorLine', line2: 'VectorLine') -> bool:
    """
    Determines if two 3D lines are parallel.
    
    Two lines are parallel if their direction vectors are scalar multiples 
    of each other. Mathematically, the magnitude of their cross product 
    must be exactly zero.
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
        
    Returns:
        bool: True if the lines are parallel, False otherwise.
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    b1 = line1.b
    b2 = line2.b
    
    # Calculate the cross product of the direction vectors
    cross_prod = cross_product(b1, b2)
    
    # Check if the magnitude of the cross product is zero
    return Vector.magnitude(cross_prod) == 0


def is_perpendicular(line1: 'VectorLine', line2: 'VectorLine') -> bool:
    """
    Determines if two 3D lines are perpendicular to each other.
    
    Two lines are perpendicular if the angle between them is 90 degrees.
    Mathematically, the dot product of their direction vectors must be zero.
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
        
    Returns:
        bool: True if the lines are perpendicular, False otherwise.
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    b1 = line1.b
    b2 = line2.b
    
    # Calculate the dot product of the direction vectors
    dot_val = dot_product(b1, b2)
    
    # Check if the dot product evaluates to zero
    return dot_val == 0


def is_skew(line1: 'VectorLine', line2: 'VectorLine') -> bool:
    """
    Determines if two 3D lines are skew.
    
    Skew lines are lines that do not intersect and are not parallel 
    (i.e., they are not coplanar). Mathematically, this is true if the 
    scalar triple product of the vector connecting their position points 
    and their two direction vectors is non-zero.
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
        
    Returns:
        bool: True if the lines are skew, False otherwise.
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    a1, b1 = line1.a, line1.b
    a2, b2 = line2.a, line2.b
    
    # Step 1: Vector connecting the position points of both lines
    vec_a_diff = Vector(a2.a - a1.a, a2.b - a1.b, a2.c - a1.c)
    
    # Step 2: Cross product of the two direction vectors
    cross_b = cross_product(b1, b2)
    
    # Step 3: Dot product of vec_a_diff and the cross product
    scalar_triple_product = dot_product(vec_a_diff, cross_b)
    
    # If the scalar triple product is not zero, the lines are skew
    return scalar_triple_product != 0


def get_intersection_point(line1: 'VectorLine', line2: 'VectorLine') -> Point | None:
    """
    Calculates the intersection point of two 3D lines, if it exists.
    
    Logic:
    Equates the parametric equations of the two lines for the X and Y axes 
    to solve for the scalars (lambda for line1, mu for line2). 
    Checks if these scalars satisfy the Z axis equation. If they do, the 
    lines intersect, and the point is calculated. Otherwise, they are skew.
    
    Args:
        line1 (VectorLine): The first line.
        line2 (VectorLine): The second line.
        
    Returns:
        Point: The exact intersection point.
        None: If the lines are parallel or skew (do not intersect).
    """
    validate_type('line1', line1, VectorLine)
    validate_type('line2', line2, VectorLine)

    # First, quickly check if they are skew or parallel
    if is_skew(line1, line2) or is_parallel(line1, line2):
        return None  # They will never intersect

    a1, b1 = line1.a, line1.b
    a2, b2 = line2.a, line2.b

    # Setup linear equations using X and Y coordinates:
    # Equation 1 (X): a1.a + lambda * b1.a = a2.a + mu * b2.a
    # Equation 2 (Y): a1.b + lambda * b1.b = a2.b + mu * b2.b
    
    # Rearranged to standard form: A*lambda + B*mu = C
    # (b1.a)*lambda + (-b2.a)*mu = (a2.a - a1.a)
    # (b1.b)*lambda + (-b2.b)*mu = (a2.b - a1.b)
    
    A1, B1, C1 = b1.a, -b2.a, a2.a - a1.a
    A2, B2, C2 = b1.b, -b2.b, a2.b - a1.b
    
    # Cramer's Rule for solving 2x2 system of linear equations
    determinant = (A1 * B2) - (A2 * B1)
    
    # If determinant is 0, the X and Y components are parallel (should be caught by is_parallel)
    if determinant == 0:
        return None
        
    # Solve for lambda
    lambda_val = ((C1 * B2) - (C2 * B1)) / determinant
    
    # Calculate the exact point using lambda_val on line1
    # Reusing our existing robust function!
    return get_point_on_line(line1, lambda_val)


if __name__ == "__main__":
    # --- Example Usage and Testing ---
    print("\n" + "="*50)
    print("🚀 3D Geometry Module Initialization")
    print("="*50)
    
    p1 = Point()
    p2 = Point()
    
    v1 = Vector()
    v2 = Vector()

    vec_line1 = VectorLine()
    vec_line2 = VectorLine()

    lx = VectorLine.from_two_points(A=p1, B=p2)
    print("Vector Line from 2 Points:", lx)

    cx = CartesianLine.from_two_points(A=p1, B=p2)
    print("Cartesian Line from 2 Points:", cx)

    print("\n[Generated Test Objects]")
    print(f"Point 1 (p1): {p1}")
    print(f"Point 2 (p2): {p2}")
    print(f"Vector 1 (v1): {v1}")
    print(f"Vector 2 (v2): {v2}")
    print(f"Vector Line 1: {vec_line1}")
    print(f"Vector Line 2: {vec_line2}")

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
    print(f"Distance : {get_distance_between_lines(line1=vec_line1, line2=vec_line2)}")

    print("\n" + "-"*50)
    print("5. Point and Line Interactions")
    print("-" * 50)
    print(f"Foot of Perpendicular : {get_foot_of_perpendicular(P=p1, line=vec_line1)}")
    print(f"Perpendicular Distance: {get_distance_point_to_line(P=p1, line=vec_line1):.4f}")
    print(f"Image of Point        : {get_image_of_point(P=p1, line=vec_line1)}")

    print("\n" + "-"*50)
    print("6. Line Comparisons (Boolean Checks)")
    print("-" * 50)
    print(f"Are Lines Parallel?      : {is_parallel(line1=vec_line1, line2=vec_line2)}")
    print(f"Are Lines Perpendicular? : {is_perpendicular(line1=vec_line1, line2=vec_line2)}")

    print("\n" + "-"*50)
    print("7. Intersection of Two Lines")
    print("-" * 50)
    print(f"Intersection Point       : {get_intersection_point(line1=vec_line1, line2=vec_line2)}")
    
    # End of testing block
    print("="*50 + "\n")