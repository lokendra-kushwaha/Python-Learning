"""
3D Vector Geometry Engine
-------------------------
A pure Python module built from scratch to handle 3D Lines and Planes 
using Vector Algebra. It provides classes for Cartesian and Vector representations
and functions to calculate intersections, angles, distances, and projections.

Dependencies: Custom vectors and line_3d modules.
"""

# Adding the custom Vector module folder path to sys.path
# This allows importing Point and Vector classes from external files without errors
import sys
# Make sure to adjust this path according to your local setup
sys.path.append(r"L:/01_AI_and_Data_Science/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")
from warnings import warn
from typing import Union, Tuple
from math import sqrt, degrees, acos, asin
from random import randint

# Importing your custom classes and functions
from vectors import Vector, Point
from advance_vectors import cross_product, dot_product, vector_triple_product
from line_3d import CartesianLine, VectorLine


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


class CartesianPlane:
    """
    Represents a 3D Plane in Cartesian Form: Ax + By + Cz = D.

    This class automatically normalizes the plane equation upon initialization.
    The coefficients (A, B, C) are converted into direction cosines, ensuring 
    that the normal vector (A, B, C) is always a unit vector, and D represents 
    the exact perpendicular distance from the origin to the plane.

    Attributes:
        A (float): The normalized x-coefficient of the plane's normal vector.
        B (float): The normalized y-coefficient of the plane's normal vector.
        C (float): The normalized z-coefficient of the plane's normal vector.
        D (float): The normalized constant, representing perpendicular distance from origin.
    """
    def __init__(self, A: float = None, B: float = None, C: float = None, D: float = None):
        """
        Initializes the CartesianPlane and normalizes the coefficients.

        If all parameters are provided, it normalizes them by dividing by the 
        magnitude of the normal vector. If parameters are missing, it generates 
        a random normalized plane for testing purposes.

        Args:
            A (float, optional): x-coefficient.
            B (float, optional): y-coefficient.
            C (float, optional): z-coefficient.
            D (float, optional): Constant term.

        Raises:
            ValueError: If the magnitude of the given normal vector is zero 
                        (i.e., A=0, B=0, C=0).
        """
        if A is not None and B is not None and C is not None and D is not None:
            validate_type('A', A, (int, float))
            validate_type('B', B, (int, float))
            validate_type('C', C, (int, float))
            validate_type('D', D, (int, float))

            mag = sqrt(A**2 + B**2 + C**2)
            if mag == 0:
                raise ValueError("A, B, and C cannot all be zero.")
            self.A = A / mag
            self.B = B / mag
            self.C = C / mag
            self.D = D / mag
        else:
            A, B, C, D = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
            mag = sqrt(A**2 + B**2 + C**2)
            self.A = A / mag
            self.B = B / mag
            self.C = C / mag
            self.D = D / mag

    @classmethod
    def from_point_and_normal(cls, pt: Point, n: Vector):
        """
        Creates a CartesianPlane using a point on the plane and a normal vector.

        Mathematical Formula:
        $$ A(x - x_1) + B(y - y_1) + C(z - z_1) = 0 $$
        Expanding this gives:
        $$ Ax + By + Cz = Ax_1 + By_1 + Cz_1 = D $$

        Args:
            pt (Point): A point (x1, y1, z1) lying on the plane.
            n (Vector): A normal vector (A, B, C) perpendicular to the plane.

        Returns:
            CartesianPlane: A new, automatically normalized CartesianPlane object.
        """
        validate_type('pt', pt, Point)
        validate_type('n', n, Vector)

        A, B, C = n.a, n.b, n.c
        # Calculating the constant D = (A*x1 + B*y1 + C*z1)
        D = (A * pt.x) + (B * pt.y) + (C * pt.z)
        # Passing raw values to init, which will handle the normalization
        return cls(A = A, B = B, C = C, D = D )
    
    @classmethod
    def from_three_points(cls, p1: Point, p2: Point, p3:Point):
        """
        Creates a CartesianPlane passing through three non-collinear points.

        It derives the normal vector by taking the cross product of two vectors 
        lying on the plane (formed by the three points). Then, it uses one of 
        the points to calculate the constant distance 'D'.

        Mathematical Formula:
        $$ \vec{n} = \vec{AB} \times \vec{AC} $$
        $$ D = \vec{n} \cdot \vec{A} $$

        Args:
            p1 (Point): First point on the plane.
            p2 (Point): Second point on the plane.
            p3 (Point): Third point on the plane.

        Returns:
            CartesianPlane: A new, automatically normalized CartesianPlane object.
        """
        validate_type('p1', p1, Point)
        validate_type('p2', p2, Point)
        validate_type('p3', p3, Point)

        vec_a = Vector(p1.x, p1.y, p1.z)
        vec_b = Vector(p2.x, p2.y, p2.z)
        vec_c = Vector(p3.x, p3.y, p3.z)

        # Cross product generates the normal vector (A, B, C)
        normal_vec = cross_product((vec_b - vec_a), (vec_c - vec_a))

        # D is essentially the dot product of the normal vector and point p1
        A, B, C = normal_vec.a, normal_vec.b, normal_vec.c

        D = (A * p1.x) + (B * p1.y) + (C * p1.z)

        return cls(A = A, B = B, C = C, D = D)


    def __str__(self):
        """Returns the string representation of the plane."""
        # Using f-string formatting with sign specifier is optional here, 
        # but returning your clean version.
        return f"{self.A}x + {self.B}y + {self.C}z = {self.D}".replace("+ -", "- ")
    
    def __repr__(self):
        """Returns the representation of the object when inside a container."""
        return self.__str__()


class VectorPlane:
    """
    Represents a 3D Plane in Vector Form: r.n = d.

    This class automatically normalizes the plane equation upon initialization.
    The normal vector 'n' is always converted and stored as a unit vector (n-cap), 
    and 'd' represents the exact perpendicular distance from the origin.

    Attributes:
        n (Vector): The normalized unit normal vector of the plane.
        d (float): The normalized perpendicular distance from the origin.
    """
    def __init__(self, n: Vector = None, d: float = None):
        """
        Initializes the VectorPlane and normalizes the given parameters.

        Args:
            n (Vector, optional): A normal vector perpendicular to the plane.
            d (float, optional): The scalar distance associated with the normal vector.

        Raises:
            ValueError: If the provided normal vector is a zero vector.
        """
        if n is not None and d is not None:
            validate_type('n', n, Vector)
            validate_type('d', d, (float, int))

            mag = Vector.magnitude(n)
            if mag == 0:
                raise ValueError("Normal vector cannot be a zero vector.")
            
            # 🔥 Normalizing: Store as unit vector
            self.n = Vector.unit_vector(n)
            
            # 🔥 Distance divided by the original magnitude, not the new unit vector's magnitude
            self.d = d / mag

        else:
            n_rand = Vector() # Assumes default creates a random non-zero vector
            mag_rand = Vector.magnitude(n_rand)
            self.n = Vector.unit_vector(n_rand)
            self.d = randint(1, 10) / mag_rand

    @classmethod
    def from_point_and_normal(cls, A: Point, n: Vector):
        """
        Creates a VectorPlane using a point on the plane and a normal vector.

        Mathematical Formula:
        $$ (\vec{r} - \vec{a}) \cdot \vec{n} = 0 $$
        Expanding gives:
        $$ \vec{r} \cdot \vec{n} = \vec{a} \cdot \vec{n} = d $$

        Args:
            A (Point): A positional point lying on the plane.
            n (Vector): A normal vector perpendicular to the plane.

        Returns:
            VectorPlane: A new, automatically normalized VectorPlane object.
        """
        validate_type('A', A, Point)
        validate_type('n', n, Vector)

        vec_a = Vector(A.x, A.y, A.z)

        # d is the dot product of the position vector and the normal vector
        d_val = dot_product(vec_a, n)

        return cls(n = n, d = d_val)
    
    @classmethod
    def from_three_points(cls, A: Point, B: Point, C: Point):
        """
        Creates a VectorPlane passing through three non-collinear points.

        Generates the normal vector using the cross product of two directional 
        vectors on the plane. The scalar distance 'd' is then derived using 
        the dot product of one point and the generated normal vector.

        Mathematical Formula:
        $$ \vec{n} = \vec{AB} \times \vec{AC} $$
        $$ d = \vec{a} \cdot \vec{n} $$

        Args:
            A (Point): First positional point on the plane.
            B (Point): Second positional point on the plane.
            C (Point): Third positional point on the plane.

        Returns:
            VectorPlane: A new, automatically normalized VectorPlane object.
        """
        validate_type('A', A, Point)
        validate_type('B', B, Point)
        validate_type('C', C, Point)

        a_vec = Vector(A.x, A.y, A.z)
        b_vec = Vector(B.x, B.y, B.z)
        c_vec = Vector(C.x, C.y, C.z)

        # Normal vector generated via Cross Product
        normal_vec = cross_product((b_vec - a_vec), (c_vec - a_vec))

        # Scalar distance generated via Dot Product
        d_val = dot_product(a_vec, normal_vec)

        return cls(n=normal_vec, d=d_val)
    
    def __str__(self):
        """Returns the string representation of the vector plane."""
        # Note: self.n is ALREADY a unit vector because of init,
        # so we don't need to call Vector.unit_vector(self.n) again here!
        return f"(xi + yj + zk).({self.n}) = {self.d}"
    
    def __repr__(self):
        """Returns the representation of the object when inside a container."""
        return self.__str__()


def get_vector_equation(d:float = None, n:Vector = None, A:Point = None, B:Point = None, C:Point = None) -> VectorPlane | str:
    """
    Generates the Vector equation of a Plane.
    It can handle 3 forms: Normal Form, Point-Normal Form, and Three-Point Form.

    Parameters:
        d (float, optional): Perpendicular distance of the plane from the origin.
        n (Vector, optional): Normal vector perpendicular to the plane.
        A (Point, optional): First position vector/point on the plane.
        B (Point, optional): Second position vector/point on the plane.
        C (Point, optional): Third position vector/point on the plane.

    Returns:
        str: A string representing the vector equation of the plane.
    """
    # Case 1: Normal Form -> r.n = d
    if d is not None and n is not None:
        validate_type('d', d, (float, int))
        validate_type('n', n, Vector)

        if Vector.magnitude(n) == 1:
            return VectorPlane(n = n, d = d)
        else:
            return VectorPlane(n = Vector.unit_vector(n), d = d/Vector.magnitude(n))
    
    # Case 2: Point-Normal Form -> (r - a).n = 0
    elif n is not None and A is not None:
        validate_type('n', n, Vector)
        validate_type('A', A, Point)

        return f"[(x - {A.x})i + (y - {A.y})j + (z - {A.z})k].({n}) = 0".replace("- -", "+ ")
    
    # Case 3: Three-Point Form -> (r - a).(AB x AC) = 0
    elif A is not None and B is not None and C is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)
        validate_type('C', C, Point)
        
        a_vec = Vector(A.x, A.y, A.z)
        b_vec = Vector(B.x, B.y, B.z)
        c_vec = Vector(C.x, C.y, C.z)

        # Cross product of vectors AB and AC gives the normal vector
        normal_vec = cross_product((b_vec - a_vec), (c_vec - a_vec))
        return f"[(x - {A.x})i + (y - {A.y})j + (z - {A.z})k].({normal_vec}) = 0".replace("- -", "+ ")
    
    else:
        raise ValueError(
            "Ambiguous arguments definition. You must provide a complete parameter set "
            "e.g., either valid Distance - Vector OR Distance - Point OR 3 Points."
        )

def get_cartesian_equation(d:float = None, n:Vector = None, A:Point = None, B:Point = None, C:Point = None) -> CartesianPlane | str:
    """
    Generates the Cartesian equation of a Plane (Ax + By + Cz = D).
    It can handle 3 forms: Normal Form, Point-Normal Form, and Three-Point Form.

    Parameters:
        d (float, optional): Perpendicular distance of the plane from the origin.
        n (Vector, optional): Normal vector (direction ratios A, B, C).
        A (Point, optional): First point (x1, y1, z1) on the plane.
        B (Point, optional): Second point (x2, y2, z2) on the plane.
        C (Point, optional): Third point (x3, y3, z3) on the plane.

    Returns:
        str: A string representing the cartesian equation of the plane.
    """
    if d is not None and n is not None:
        validate_type('d', d, (float, int))
        validate_type('n', n, Vector)

        if Vector.magnitude(n) == 1:
            return CartesianPlane(A=n.a, B=n.b, C=n.c, D=d)
        else:
            return CartesianPlane(A=n.a, B=n.b, C=n.c, D=d/Vector.magnitude(n))
        
    elif n is not None and A is not None:
        validate_type('n', n, Vector)
        validate_type('A', A, Point)

        return f"{n.a}x + {n.b}y + {n.c}z - {n.a*A.x + n.b*A.y + n.c*A.z} = 0".replace("- -", "+ ")
    
    elif A is not None and B is not None and C is not None:
        validate_type('A', A, Point)
        validate_type('B', B, Point)
        validate_type('C', C, Point)

        M11 = ((B.y - A.y)*(C.z - A.z) - (C.y - A.y)*(B.z - A.z))
        M12 = ((B.x - A.x)*(C.z - A.z) - (B.z - A.z)*(C.x - A.x))
        M13 = ((B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x))
        return f"{M11:+}x {M12:+}y {M13:+}z {- A.x*M11 + A.y*M12 - A.z*M13} = 0".replace("+ -", "- ")
    
    else:
        raise ValueError(
            "Ambiguous arguments definition. You must provide a complete parameter set "
            "e.g., either valid Distance - Vector OR Distance - Point OR 3 Points."
        )

def check_point_on_plane(plane: VectorPlane, target_point: Point) -> bool:
    """
    Checks whether a specific 3D point lies on a given Vector Plane.

    Parameters:
        plane (VectorPlane): The plane object to test against.
        target_point (Point): The 3D point (x, y, z) to be checked.

    Returns:
        bool: True if the point lies exactly on the plane, False otherwise.
    """
    validate_type('plane', plane, VectorPlane)
    validate_type('target_point', target_point, Point)

    lhs = (plane.n.a * target_point.x) + (plane.n.b * target_point.y) + (plane.n.c * target_point.z)
    if abs(lhs - plane.d) < 1e-5:
        return True

    return False


def get_intercept_form(plane: CartesianPlane) -> str:
    """
    Converts a given CartesianPlane object into Intercept form (x/a + y/b + z/c = 1).

    Parameters:
        plane (CartesianPlane): The plane object to convert.

    Returns:
        str: Formatted string of the Intercept form, or an error message for edge cases.
    """
    validate_type('plane', plane, CartesianPlane)

    A, B, C, D = plane.A, plane.B, plane.C, plane.D

    if D == 0:
        return "Plane passes through the origin. Intercept form does not exist."
    
    if A == 0 or B == 0 or C == 0:
        return "Plane is parallel to an axis. Valid Intercept form cannot be generated."
    
    a, b, c = -D / A, -D / B, -D / C

    return f"x/({a}) + y/({b}) + z/({c}) = 1".replace("+ -", "- ")


def get_plane_through_intersection(plane1: VectorPlane, plane2: VectorPlane) -> str:
    """
    Generates the family of planes equation passing through the intersection of two VectorPlanes.

    Parameters:
        plane1 (VectorPlane): The first intersecting plane.
        plane2 (VectorPlane): The second intersecting plane.

    Returns:
        str: The family of planes equation using lambda (\u03BB).
    """
    validate_type('plane1', plane1, VectorPlane)
    validate_type('plane2', plane2, VectorPlane)

    return f"(xi + yj + zk).[({plane1.n}) - \u03BB({plane2.n})] = {plane1.d} + \u03BB{plane2.d}".replace("\u03BB-", "-\u03BB")


def get_line_through_intersection(plane1: VectorPlane, plane2: VectorPlane) -> VectorLine:
    """
    Calculates the vector equation of the intersection line of two planes.

    This function determines the line where two non-parallel planes intersect.
    The direction vector of the line is found using the cross product of the 
    two planes' normal vectors. A point on the line is derived using the 
    vector triple product.

    Args:
        plane1 (VectorPlane): The first plane object containing normal vector (n) and distance (d).
        plane2 (VectorPlane): The second plane object containing normal vector (n) and distance (d).

    Returns:
        str: A formatted string representing the vector equation of the line 
             in the format "(xi + yj + zk) = a + λ(b)".
             If the planes are parallel (cross product is zero), it returns 
             a string indicating that no intersection line exists.
    """
    validate_type('plane1', plane1, VectorPlane)
    validate_type('plane2', plane2, VectorPlane)

    vec_b = cross_product(plane1.n, plane2.n)
    if Vector.squareMagnitude(vec_b) == 0:
        warn("Both planes are parallel, so intersection line doesn't exists.")
        return None
    
    vec_a = vector_triple_product((plane1.d * plane2.n - plane2.d * plane1.n), plane1.n, plane2.n)/(Vector.magnitude(vec_b))**2
    
    return VectorLine(a=vec_a, b=vec_b)

def get_line_plane_intersection(plane: VectorPlane, line: VectorLine) -> Vector:
    """
    Finds the exact intersection point of a vector line and a vector plane.

    This function calculates the 3D position vector where a given line pierces 
    through a plane. It substitutes the line's equation into the plane's 
    equation to solve for the scalar parameter (lambda), and then uses that 
    lambda to find the exact intersection point.

    Args:
        plane (VectorPlane): The plane surface object.
        line (VectorLine): The line object containing a point (a) and direction (b).

    Returns:
        Vector: A Vector object representing the exact intersection point (position vector).
        str: If the line's direction is perpendicular to the plane's normal 
             (dot product is 0), it returns a string message indicating the line 
             is parallel to the plane and does not intersect.
    """
    validate_type('plane', plane, VectorPlane)
    validate_type('plane', line, VectorLine)

    denominator = dot_product(line.b, plane.n)
    if denominator == 0:
        warn("No unique intersection point. The line is strictly parallel to the plane OR completely lies on it.")
        return None
    
    lam = (plane.d - dot_product(line.a, plane.n)) / denominator

    intersection_point = line.a + (line.b * lam)
    return intersection_point 
    

def are_lines_coplaner(vec_line1: VectorLine = None, vec_line2: VectorLine = None, cart_line1: CartesianLine = None, cart_line2: CartesianLine = None) -> bool:
    """
    Checks if two given 3D lines are coplanar (lie on the exact same plane).
    Supports checking for both VectorLine objects and CartesianLine objects.

    Parameters:
        vec_line1, vec_line2 (VectorLine, optional): Lines in vector format.
        cart_line1, cart_line2 (CartesianLine, optional): Lines in cartesian format.

    Returns:
        bool: True if the lines are coplanar, False otherwise.
    """
    if vec_line1 is not None and vec_line2 is not None:
        validate_type('vec_line1', vec_line1, VectorLine)
        validate_type('vec_line2', vec_line2, VectorLine)

        a1 = vec_line1.a
        a2 = vec_line2.a

        if dot_product((a2 - a1), cross_product(vec_line1.b, vec_line2.b)) == 0:
            return True
        
        return False
        
    elif cart_line1 is not None and cart_line2 is not None:
        validate_type('cart_line1', cart_line1, CartesianLine)
        validate_type('cart_line2', cart_line2, CartesianLine)

        a1 = Vector(cart_line1.A.x, cart_line1.A.y, cart_line1.A.z)
        a2 = Vector(cart_line2.A.x, cart_line2.A.y, cart_line2.A.z)

        b1 = Vector(cart_line1.b.a, cart_line1.b.b, cart_line1.b.c)
        b2 = Vector(cart_line2.b.a, cart_line2.b.b, cart_line2.b.c)

        if dot_product(a2 - a1, cross_product(b1, b2)) == 0:
            return True
        
        return False

    else:
        raise ValueError(
            "Ambiguous plane definition. You must provide a complete parameter set "
            "e.g., either valid VectorLine OR a CartesianLine."
        )


def angle_between_planes(cart_plane1: CartesianPlane = None, cart_plane2: CartesianPlane = None, vec_plane1: VectorPlane = None, vec_plane2: VectorPlane = None) -> float:
    """
    Calculates the shortest angle between two planes.
    Accepts either two CartesianPlane objects or two VectorPlane objects.

    Returns:
        float: The angle in degrees.
    """

    costheta = 0.0
    if vec_plane1 is not None and vec_plane2 is not None:
        validate_type('vec_plane1', vec_plane1, VectorPlane)
        validate_type('vec_plane2', vec_plane2, VectorPlane)

        costheta =  dot_product(vec_plane1.n, vec_plane2.n) / (Vector.magnitude(vec_plane1.n) * Vector.magnitude(vec_plane2.n))

    elif cart_plane1 is not None and cart_plane2 is not None:
        validate_type('cart_plane1', cart_plane1, CartesianPlane)
        validate_type('cart_plane2', cart_plane2, CartesianPlane)

        n1 = Vector(cart_plane1.A, cart_plane1.B, cart_plane1.C)
        n2 = Vector(cart_plane2.A, cart_plane2.B, cart_plane2.C)
        costheta = dot_product(n1, n2) / (Vector.magnitude(n1) * Vector.magnitude(n2))

    else:
        raise ValueError(
            "Ambiguous plane definition. You must provide a complete parameter set "
            "e.g., either valid VectorPlanes OR a CartesianPlanes."
        )
    
    # Clamping to avoid domain errors
    costheta = max(-1.0, min(1.0, costheta))
    angle_in_radian = acos(costheta)
    angle_in_degree = degrees(angle_in_radian)

    return angle_in_degree


def distance_between_point_and_plane(cart_plane: CartesianPlane = None, vec_plane: VectorPlane = None, P: Point = None) -> float:
    """
    Calculates the shortest (perpendicular) distance from a point to a plane.

    Parameters:
        cart_plane (CartesianPlane, optional): Target plane in cartesian format.
        vec_plane (VectorPlane, optional): Target plane in vector format.
        P (Point): The point in 3D space.

    Returns:
        float: Absolute perpendicular distance.
    """
    vec_a = Vector(P.x, P.y, P.z)

    if vec_plane is not None:
        validate_type('vec_plane', vec_plane, VectorPlane)
        validate_type('P', P, Point)

        distance = (dot_product(vec_a, vec_plane.n) - vec_plane.d) / Vector.magnitude(vec_plane.n)

    elif cart_plane is not None:
        validate_type('cart_plane', cart_plane, CartesianPlane)
        distance = (dot_product(vec_a, Vector(cart_plane.A, cart_plane.B, cart_plane.C)) - cart_plane.D) / Vector.magnitude(Vector(cart_plane.A, cart_plane.B, cart_plane.C))
    
    else:
        raise ValueError(
            "Ambiguous plane or point definition. You must provide a complete parameter set "
            "e.g., either valid VectorPlane - Point OR CartesianPlane - Point."
        )

    return abs(distance)


def distance_between_planes(plane1: VectorPlane, plane2: VectorPlane) -> float:
    """
    Calculates the minimum perpendicular distance between two parallel planes.

    This function first verifies if the two planes are parallel by checking 
    the square magnitude of their cross product. If they intersect, the distance 
    is zero. If they are parallel, it calculates a scaling factor (lambda) to 
    align their normal vectors, avoiding any directional sign traps, and then 
    computes the exact absolute distance between them.

    Args:
        plane1 (VectorPlane): The first plane object containing normal vector (n) and distance (d).
        plane2 (VectorPlane): The second plane object containing normal vector (n) and distance (d).

    Returns:
        float: The absolute minimum distance between the two parallel planes.
        str: A message indicating that the planes intersect (distance is 0) 
             if their normal vectors are not parallel.
    """
    validate_type('plane1', plane1, VectorPlane)
    validate_type('plane2', plane2, VectorPlane)

    cross_vec = cross_product(plane1.n, plane2.n)

    # Fail-fast validation: Check if planes are parallel
    if Vector.squareMagnitude(cross_vec) != 0:
        warn("Planes are intersecting. Returning shortest distance as 0.0")
        return 0.0
    
    # Calculate lambda (scaling factor) using the 'a' (x-component) of the normal vectors
    lam = plane1.n.a / plane2.n.a

    # Apply the derived universal distance formula
    distance = (plane1.d - lam*plane2.d)/Vector.magnitude(plane1.n)
    return abs(distance)


def angle_between_line_and_plane(vec_line: VectorLine = None, cart_line: CartesianLine = None, vec_plane: VectorPlane = None, cart_plane: CartesianPlane = None) -> float:
    """
    Calculates the angle of intersection between a 3D line and a plane.

    Returns:
        float: The angle in degrees.
    """
    sintheta = 0.0
    if vec_line is not None and vec_plane is not None:
        validate_type('vec_line', vec_line, VectorLine)
        validate_type('vec_plane', vec_plane, VectorPlane)

        sintheta = dot_product(vec_plane.n, vec_line.b) / (Vector.magnitude(vec_plane.n) * Vector.magnitude(vec_line.b))
    
    elif cart_line is not None and cart_plane is not None:
        validate_type('cart_line', cart_line, CartesianLine)
        validate_type('cart_plane', cart_plane, CartesianPlane)

        sintheta = dot_product(cart_plane.n, cart_line.b) / (Vector.magnitude(cart_plane.n) * Vector.magnitude(cart_line.b))

    else:
        raise ValueError(
            "Ambiguous plane - line definition. You must provide a complete parameter set "
            "e.g., either valid VectorPlane - VectorLine OR CartesianPlane - CartesianLine."
        )

    # Clamping to avoid domain errors
    sintheta = max(-1.0, min(1.0, sintheta))
    angle_in_radian = asin(sintheta)
    angle_in_degree = degrees(angle_in_radian)

    return angle_in_degree


def get_foot_of_perpendicular(plane: VectorPlane, A: Point) -> Point:
    """
    Finds the exact coordinate (Point) on the plane where a perpendicular 
    dropped from point A intersects it.

    Parameters:
        plane (CartesianPlane): The plane surface.
        A (Point): The point in 3D space.

    Returns:
        Point: The exact coordinates of the foot of the perpendicular.
    """
    validate_type('plane', plane, VectorPlane)
    validate_type('A', A, Point)

    vec_n = plane.n
    lam = (plane.d - (vec_n.a*A.x + vec_n.b*A.y + vec_n.c*A.z))/(vec_n.a*vec_n.a + vec_n.b*vec_n.b + vec_n.c*vec_n.c)

    foot = Point(A.x + vec_n.a*lam, A.y + vec_n.b*lam, A.z + vec_n.c*lam)
    return foot

def get_image_point(original_point: Point, foot_of_perpendicular:Point) -> Point:
    """
    Calculates the image (reflection) of a point across a plane or line.

    This function uses the geometric principle that the foot of the 
    perpendicular acts as the exact midpoint between the original object 
    and its reflection. It calculates the image using the vector formula: 
    Image = 2 * Foot - Original.

    Args:
        original_point (Point): The original point (object) in 3D space.
        foot_of_perpendicular (Point): The exact point where the perpendicular 
                                       from the original point touches the surface.

    Returns:
        Point: A new Point object representing the exact coordinates of 
               the reflected image.
    """
    validate_type('original_point', original_point, Point)
    validate_type('foot_of_perpendicular', foot_of_perpendicular, Point)

    F = foot_of_perpendicular
    P = original_point

    # Utilizing Dunder/Magic methods (mul, sub) of the Point class
    image_of_P = (2 * F) - P

    return image_of_P


def get_angle_bisecter_planes(plane1: VectorPlane, plane2: VectorPlane) -> Union[VectorPlane, Tuple[VectorPlane, VectorPlane]]:
    """
    Calculates the angle bisector plane(s) between two given VectorPlanes.

    This function determines the locus of points equidistant from both planes. 
    If the planes are parallel (cross product of normals is zero), it returns 
    a single mid-parallel plane. If they intersect, it returns two bisector 
    planes (one for the acute angle, one for the obtuse angle).

    Mathematical Formulas Used:
    - For parallel planes (Mid-Plane): 
      Distance: $$ d_{mid} = \frac{d_1 + d_2}{2} $$
    - For intersecting planes (Bisectors): 
      Normal: $$ \hat{n}_{new} = \hat{n}_1 \pm \hat{n}_2 $$
      Distance: $$ d_{new} = d_1 \pm d_2 $$
      (Note: Assumes plane1.n and plane2.n are already unit vectors)

    Args:
        plane1 (VectorPlane): The first target plane.
        plane2 (VectorPlane): The second target plane.

    Returns:
        VectorPlane | tuple[VectorPlane, VectorPlane]: 
            - A single VectorPlane object if the original planes are parallel.
            - A tuple of two VectorPlane objects (plus_bisector, minus_bisector) 
              if the original planes are intersecting.
    """
    validate_type('plane1', plane1, VectorPlane)
    validate_type('plane2', plane2, VectorPlane)

    cross_prod = cross_product(plane1.n, plane2.n)

    if Vector.squareMagnitude(cross_prod) == 0:
        warn("Planes are parallel. Returning a single Mid-Parallel Plane.")

        n_cap = Vector.unit_vector(plane1.n)
        d_mid = (plane1.d + plane2.d) / 2

        return VectorPlane(n=n_cap, d=d_mid)

    else:
        # Note: For strict mathematical accuracy, ensure plane.n is a unit vector 
        # before this addition/subtraction. Your VectorPlane class design handles this!
        bisector_minus = VectorPlane(n=plane1.n - plane2.n, d=plane1.d - plane2.d)
        bisector_plus = VectorPlane(n=plane1.n + plane2.n, d=plane1.d + plane2.d)
        
        return bisector_minus, bisector_plus


def get_projection_of_line(plane: VectorPlane, line: VectorLine) -> VectorLine:
    """
    Calculates the 3D projection (shadow) of a given line onto a plane.

    The function computes a new line that lies perfectly flat on the target plane.
    It resolves the original line's direction vector to remove its perpendicular 
    component relative to the plane. For the position vector, it utilizes the 
    exact intersection point, or falls back to the foot of the perpendicular 
    if the line is strictly parallel to the plane.

    Mathematical Formula Used (Vector Resolution):
    $$ \vec{b}_{proj} = \vec{b} - (\vec{b} \cdot \hat{n})\hat{n} $$
    Where b is the line's direction and n-cap is the plane's unit normal.

    Args:
        plane (VectorPlane): The surface plane on which the projection is cast.
        line (VectorLine): The original 3D line floating in space.

    Returns:
        VectorLine: A new VectorLine object representing the perfectly 
                    projected line lying on the plane.
    """
    validate_type('plane', plane, VectorPlane)
    validate_type('line', line, VectorLine)

    n_cap = Vector.unit_vector(plane.n)
    dot_val = dot_product(line.b, n_cap)

    # Deriving the projected direction vector
    b_proj = line.b - (n_cap * dot_val)

    # Deriving the starting position point
    a_proj = get_line_plane_intersection(plane, line)

    # Fallback logic for parallel lines (Intersection returns None)
    if a_proj is None:
        a_proj = get_foot_of_perpendicular(plane, line.a)

    return VectorLine(a=a_proj, b=b_proj)


# ==========================================
#              TESTING BLOCK
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 INITIALIZING 3D MATH ENGINE TESTING 🚀")
    print("="*50 + "\n")

    # Creating core testing components
    from math import sqrt # Just in case
    n_cap = Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14))
    n_vec = Vector(2, 3, 4)
    
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = Point(7, 8, 0)

    # Assuming these initialize with some default or test values
    vec_pl1 = VectorPlane()
    vec_pl2 = VectorPlane()
    cart_pl1 = CartesianPlane()
    cart_pl2 = CartesianPlane()
    vec_line1 = VectorLine()
    vec_line2 = VectorLine()

    print("--- [ Generated Objects ] ---")
    print(f"Vector Plane 1:    {vec_pl1}")
    print(f"Vector Plane 2:    {vec_pl2}")
    print(f"Cartesian Plane 1: {cart_pl1}")
    print(f"Cartesian Plane 2: {cart_pl2}")
    print(f"Vector Line 1:     {vec_line1}")
    print(f"Vector Line 2:     {vec_line2}\n")

    print("--- [ 1. Equation Generators ] ---")
    print("1. Vector Equations:")
    print("Normal Form:       ", get_vector_equation(n=n_cap, d=5))
    print("Point-Normal Form: ", get_vector_equation(n=n_vec, A=p1))
    print("Three-Point Form:  ", get_vector_equation(A=p1, B=p2, C=p3))
    print("-" * 30)

    print("2. Cartesian Equations:")
    print("Normal Form:       ", get_cartesian_equation(n=n_cap, d=5))
    print("Point-Normal Form: ", get_cartesian_equation(n=n_vec, A=p1))
    print("Three-Point Form:  ", get_cartesian_equation(A=p1, B=p2, C=p3))
    print("-" * 30 + "\n")

    print("--- [ 2. Core Mechanics Test ] ---")
    print(f"> Is Point p1 on Vector Plane 1?   -> {check_point_on_plane(plane=vec_pl1, target_point=p1)}")
    print(f"> Intercept Form (Cart. Plane 1):  {get_intercept_form(plane=cart_pl1)}")
    print(f"> Intersection Family Equation:    {get_plane_through_intersection(plane1=vec_pl1, plane2=vec_pl2)}\n")

    print("--- [ 3. Distances & Angles ] ---")
    print(f"> Angle between Vector Planes:     {angle_between_planes(vec_plane1=vec_pl1, vec_plane2=vec_pl2):.2f}°")
    print(f"> Angle between Cartesian Planes:  {angle_between_planes(cart_plane1=cart_pl1, cart_plane2=cart_pl2):.2f}°")
    print(f"> Dist (Point p1 to Cart Plane 1): {distance_between_point_and_plane(cart_plane=cart_pl1, P=p1):.4f} units\n")

    print("--- [ 4. Advanced Geometry ] ---")
    foot_point = get_foot_of_perpendicular(plane=vec_pl1, A=p1)
    print(f"> Foot of Perpendicular (p1 to VP1): ({foot_point.x:.2f}, {foot_point.y:.2f}, {foot_point.z:.2f})\n")
    
    print("--- [ 5. Intersections, Reflections & Distances ] ---")
    
    # 1. Reflection / Image Point
    image_pt = get_image_point(original_point=p1, foot_of_perpendicular=foot_point)
    print(f"> Image of Point p1 (Reflection):  {image_pt}")

    # 2. Line through intersection of two planes
    intersect_line_eq = get_line_through_intersection(plane1=vec_pl1, plane2=vec_pl2)
    print(f"> Line of Intersection (Planes):   {intersect_line_eq}")

    # 3. Line and Plane Intersection
    line_plane_pt = get_line_plane_intersection(plane=vec_pl1, line=vec_line1)
    print(f"> Line-Plane Intersection Point:   {line_plane_pt}")

    # 4. Distance between two planes
    plane_dist = distance_between_planes(plane1=vec_pl1, plane2=vec_pl2)
    if isinstance(plane_dist, (float, int)):
        print(f"> Distance Between Planes:         {plane_dist:.4f} units")
    else:
        print(f"> Distance Between Planes:         {plane_dist}")


    print("\n--- [ 6. Ultimate Boss Level Features ] ---")
    
    # Angle Bisectors
    bisectors = get_angle_bisecter_planes(plane1=vec_pl1, plane2=vec_pl2)
    print(f"> Angle Bisector Planes:           {bisectors}")

    # Projection of Line
    proj_line = get_projection_of_line(plane=vec_pl1, line=vec_line1)
    print(f"> Projection of Line on Plane:     {proj_line}")


    print("\n--- [ 7. Factory Methods Validation (Classmethods) ] ---")
    
    # VectorPlane Factory Methods
    vx = VectorPlane.from_point_and_normal(A=p1, n=n_vec)
    print(f"> VectorPlane (Point + Normal):    {vx}")

    vxx = VectorPlane.from_three_points(A=p1, B=p2, C=p3)
    print(f"> VectorPlane (Three Points):      {vxx}")

    # CartesianPlane Factory Methods
    cx = CartesianPlane.from_point_and_normal(pt=p1, n=n_vec)
    print(f"> CartesianPlane (Point + Normal): {cx}")

    cxx = CartesianPlane.from_three_points(p1=p1, p2=p2, p3=p3)
    print(f"> CartesianPlane (Three Points):   {cxx}")


    print("\n" + "="*50)
    print("✅ 3D ENGINE TESTING COMPLETE ✅")
    print("="*50 + "\n")