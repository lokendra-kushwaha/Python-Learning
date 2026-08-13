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
sys.path.append(r"L:/Python/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")
from math import sqrt, degrees, acos, asin
from random import randint

# Importing your custom classes and functions
from vectors import Vector, Point
from advance_vectors import cross_product, dot_product
from line_3d import CartesianLine, VectorLine

class CartesianPlane:
    """Represents a 3D Plane in Cartesian Form: Ax + By + Cz = D"""
    def __init__(self, n: Vector = None, d: float = None):
        if n is not None and d is not None:
            self.n = n
            self.d = d
        else:
            self.n = Vector()
            self.d = Vector.magnitude(self.n)*randint(1, 10)

    def __str__(self):
        return f"{self.n.a}x + {self.n.b}y + {self.n.c}z = {self.d}".replace("+ -", "- ")
    

class VectorPlane:
    """Represents a 3D Plane in Vector Form: r.n = d"""
    def __init__(self, n: Vector = None, d: float = None):
        if n is not None and d is not None:
            self.n = n
            self.d = d
        else:
            self.n = Vector()
            self.d = randint(1, 10)

    def __str__(self):
        return f"(xi + yj + zk).({Vector.unit_vector(self.n)}) = {self.d}"

def get_vector_equation(d:float = None, n:Vector = None, A:Point = None, B:Point = None, C:Point = None) -> str:
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
        if Vector.magnitude(n) == 1:
            return f"(xi + yj + zk).({n}) = {d}"
        else:
            return f"(xi + yj + zk).({Vector.unit_vector(n)}) = {d}"
    
    # Case 2: Point-Normal Form -> (r - a).n = 0
    if n is not None and A is not None:
        return f"[(x - {A.x})i + (y - {A.y})j + (z - {A.z})k].({n}) = 0".replace("- -", "+ ")
    
    # Case 3: Three-Point Form -> (r - a).(AB x AC) = 0
    if A is not None and B is not None and C is not None:
        a_vec = Vector(A.x, A.y, A.z)
        b_vec = Vector(B.x, B.y, B.z)
        c_vec = Vector(C.x, C.y, C.z)

        # Cross product of vectors AB and AC gives the normal vector
        normal_vec = cross_product(Vector.substraction(b_vec, a_vec), Vector.substraction(c_vec, a_vec))
        return f"[(x - {A.x})i + (y - {A.y})j + (z - {A.z})k].({normal_vec}) = 0".replace("- -", "+ ")

def get_cartesian_equation(d:float = None, n:Vector = None, A:Point = None, B:Point = None, C:Point = None) -> str:
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
        if Vector.magnitude(n) == 1:
            return f"{n.a}x + {n.b}y + {n.c}z = {d}".replace("+ -", "- ")
        else:
            return f"{n.a}x + {n.b}y + {n.c}z = {Vector.magnitude(n)*d}".replace("+ -", "- ")
        
    if n is not None and A is not None:
        return f"{n.a}x + {n.b}y + {n.c}z - {n.a*A.x + n.b*A.y + n.c*A.z} = 0".replace("- -", "+ ")
    
    if A is not None and B is not None and C is not None:
        M11 = ((B.y - A.y)*(C.z - A.z) - (C.y - A.y)*(B.z - A.z))
        M12 = ((B.x - A.x)*(C.z - A.z) - (B.z - A.z)*(C.x - A.x))
        M13 = ((B.x - A.x)*(C.y - A.y) - (B.y - A.y)*(C.x - A.x))
        return f"{M11}x - {M12}y + {M13}z + {- A.x*M11 + A.y*M12 - A.z*M13} = 0".replace("+ -", "- ")
    

def check_point_on_plane(plane: VectorPlane, target_point: Point) -> bool:
    """
    Checks whether a specific 3D point lies on a given Vector Plane.

    Parameters:
        plane (VectorPlane): The plane object to test against.
        target_point (Point): The 3D point (x, y, z) to be checked.

    Returns:
        bool: True if the point lies exactly on the plane, False otherwise.
    """
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
    A, B, C, D = plane.n.a, plane.n.b, plane.n.c, plane.d

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
    return f"(xi + yj + zk).[({plane1.n}) - \u03BB({plane2.n})] = {plane1.d} + \u03BB{plane2.d}".replace("\u03BB-", "-\u03BB")


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
        a1 = Vector(vec_line1.A.x, vec_line1.A.y, vec_line1.A.z)
        a2 = Vector(vec_line2.A.x, vec_line2.A.y, vec_line2.A.z)

        if dot_product(Vector.substraction(a2, a1), cross_product(vec_line1.b, vec_line2.b)) == 0:
            return True
        
        return False
        
    if cart_line1 is not None and cart_line2 is not None:
        a1 = Vector(cart_line1.A.x, cart_line1.A.y, cart_line1.A.z)
        a2 = Vector(cart_line2.A.x, cart_line2.A.y, cart_line2.A.z)

        b1 = Vector(cart_line1.b.a, cart_line1.b.b, cart_line1.b.c)
        b2 = Vector(cart_line2.b.a, cart_line2.b.b, cart_line2.b.c)

        if dot_product(Vector.substraction(a2, a1), cross_product(b1, b2)) == 0:
            return True
        
        return False


def angle_between_planes(cart_plane1: CartesianPlane = None, cart_plane2: CartesianPlane = None, vec_plane1: VectorPlane = None, vec_plane2: VectorPlane = None) -> float:
    """
    Calculates the shortest angle between two planes.
    Accepts either two CartesianPlane objects or two VectorPlane objects.

    Returns:
        float: The angle in degrees.
    """
    costheta = 0.0
    if vec_plane1 is not None and vec_plane2 is not None:
        costheta =  dot_product(vec_plane1.n, vec_plane2.n) / (Vector.magnitude(vec_plane1.n) * Vector.magnitude(vec_plane2.n))

    if cart_plane1 is not None and cart_plane2 is not None:
        n1 = Vector(cart_plane1.n.a, cart_plane1.n.b, cart_plane1.n.c)
        n2 = Vector(cart_plane2.n.a, cart_plane2.n.b, cart_plane2.n.c)
        costheta = dot_product(n1, n2) / (Vector.magnitude(n1) * Vector.magnitude(n2))

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
        distance = (dot_product(vec_a, vec_plane.n) - vec_plane.d) / Vector.magnitude(vec_plane.n)

    if cart_plane is not None:
        distance = (dot_product(vec_a, cart_plane.n) - cart_plane.d) / Vector.magnitude(cart_plane.n)
    
    return abs(distance)


def angle_between_line_and_plane(vec_line: VectorLine = None, cart_line: CartesianLine = None, vec_plane: VectorPlane = None, cart_plane: CartesianPlane = None) -> float:
    """
    Calculates the angle of intersection between a 3D line and a plane.

    Returns:
        float: The angle in degrees.
    """
    sintheta = 0.0
    if vec_line is not None and vec_plane is not None:
        sintheta = dot_product(vec_plane.n, vec_line.b) / (Vector.magnitude(vec_plane.n) * Vector.magnitude(vec_line.b))
    
    if cart_line is not None and cart_plane is not None:
        sintheta = dot_product(cart_plane.n, cart_line.b) / (Vector.magnitude(cart_plane.n) * Vector.magnitude(cart_line.b))

    # Clamping to avoid domain errors
    sintheta = max(-1.0, min(1.0, sintheta))
    angle_in_radian = asin(sintheta)
    angle_in_degree = degrees(angle_in_radian)

    return angle_in_degree


def get_foot_of_perpendicular(plane: CartesianPlane = None, A: Point = None) -> Point:
    """
    Finds the exact coordinate (Point) on the plane where a perpendicular 
    dropped from point A intersects it.

    Parameters:
        plane (CartesianPlane): The plane surface.
        A (Point): The point in 3D space.

    Returns:
        Point: The exact coordinates of the foot of the perpendicular.
    """
    vec_n = plane.n
    lam = (plane.d - (vec_n.a*A.x + vec_n.b*A.y + vec_n.c*A.z))/(vec_n.a*vec_n.a + vec_n.b*vec_n.b + vec_n.c*vec_n.c)

    foot = Point(A.x + vec_n.a*lam, A.y + vec_n.b*lam, A.z + vec_n.c*lam)
    return foot


# ==========================================
#              TESTING BLOCK
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("🚀 INITIALIZING 3D MATH ENGINE TESTING 🚀")
    print("="*50 + "\n")

    # Creating core testing components
    n_cap = Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14))
    n_vec = Vector(2, 3, 4)
    
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = Point(7, 8, 0)

    vec_pl1 = VectorPlane()
    vec_pl2 = VectorPlane()
    cart_pl1 = CartesianPlane()
    cart_pl2 = CartesianPlane()

    print("--- [ Generated Plane Objects ] ---")
    print(f"Vector Plane 1: {vec_pl1}")
    print(f"Vector Plane 2: {vec_pl2}")
    print(f"Cartesian Plane 1: {cart_pl1}")
    print(f"Cartesian Plane 2: {cart_pl2}\n")

    print("--- [ 1. Equation Generators ] ---")
    print("1. Vector Equations:")
    print("Normal Form:", get_vector_equation(n=n_cap, d=5))
    print("Point-Normal Form:", get_vector_equation(n=n_vec, A=p1))
    print("Three-Point Form:", get_vector_equation(A=p1, B=p2, C=p3))
    print("-" * 30)

    print("2. Cartesian Equations:")
    print("Normal Form:", get_cartesian_equation(n=n_cap, d=5))
    print("Point-Normal Form:", get_cartesian_equation(n=n_vec, A=p1))
    print("Three-Point Form:", get_cartesian_equation(A=p1, B=p2, C=p3))
    print("-" * 30)
    print("\n")

    print("--- [ 2. Core Mechanics Test ] ---")
    print(f"> Is Point {p2} on Vector Plane 1?  -> {check_point_on_plane(plane=vec_pl1, target_point=p2)}")
    print(f"> Intercept Form (Cart. Plane 1):  {get_intercept_form(plane=cart_pl1)}")
    print(f"> Intersection Family Equation:    {get_plane_through_intersection(plane1=vec_pl1, plane2=vec_pl2)}")
    print("\n")

    print("--- [ 3. Distances & Angles ] ---")
    print(f"> Angle between Vector Planes:     {angle_between_planes(vec_plane1=vec_pl1, vec_plane2=vec_pl2):.2f}°")

    print(f"> Angle between Cartesian Planes:  {angle_between_planes(cart_plane1=cart_pl1, cart_plane2=cart_pl2):.2f}°")
    print(f"> Dist (Point p1 to Cart Plane 1): {distance_between_point_and_plane(cart_plane=cart_pl1, P=p1):.4f} units")
    print("\n")

    print("--- [ 4. Advanced Geometry ] ---")
    foot_point = get_foot_of_perpendicular(plane=cart_pl1, A=p1)
    # print(f"> Foot of Perpendicular (p1 to Cart Plane 1): {foot_point}")
    print(f"> Foot of Perpendicular (p1 to Cart Plane 1): ({foot_point.x:.2f}, {foot_point.y:.2f}, {foot_point.z:.2f})")
    
    print("\n" + "="*50)
    print("✅ ENGINE TESTING COMPLETE ✅")
    print("="*50 + "\n")