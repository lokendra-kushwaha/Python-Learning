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
from advance_vectors import cross_product, dot_product, vector_triple_product
from line_3d import CartesianLine, VectorLine


class CartesianPlane:
    """Represents a 3D Plane in Cartesian Form: Ax + By + Cz = D"""
    def __init__(self, A: float = None, B: float = None, C: float = None, D: float = None):
        if A is not None and B is not None and C is not None and D is not None:
            mag = sqrt(A**2 + B**2 + C**2)
            if mag == 0:
                raise ValueError("A, B, C can not be zero.")
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

    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C}z = {self.D}".replace("+ -", "- ")


class VectorPlane:
    """Represents a 3D Plane in Vector Form: r.n = d"""
    def __init__(self, n: Vector = None, d: float = None):
        
        if n is not None and d is not None:
            mag = Vector.magnitude(n)
            if mag == 0:
                raise ValueError("Normal vector cann't be zero vector.")
            
            self.n = n
            self.d = d/Vector.magnitude(self.n)

        else:
            self.n = Vector()
            self.d = randint(1, 10)/Vector.magnitude(self.n)

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
        normal_vec = cross_product((b_vec - a_vec), (c_vec - a_vec))
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
    return f"(xi + yj + zk).[({plane1.n}) - \u03BB({plane2.n})] = {plane1.d} + \u03BB{plane2.d}".replace("\u03BB-", "-\u03BB")


def get_line_through_intersection(plane1: VectorPlane, plane2: VectorPlane) -> str:
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
    vec_b = cross_product(plane1.n, plane2.n)
    if Vector.squareMagnitude(vec_b) == 0:
        return f"Both planes are parallel, so intersection line doesn't exists."
    
    vec_a = f"{vector_triple_product((plane1.d * plane2.n - plane2.d * plane1.n), plane1.n, plane2.n)/(Vector.magnitude(vec_b))**2}"
    
    return f"(xi + yj + zk) = {vec_a} + \u03BB({vec_b})"

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
    denominator = dot_product(line.b, plane.n)
    if denominator == 0:
        return "Line is parallel to the plane. No intersection."
    
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
        a1 = Vector(vec_line1.A.x, vec_line1.A.y, vec_line1.A.z)
        a2 = Vector(vec_line2.A.x, vec_line2.A.y, vec_line2.A.z)

        if dot_product((a2 - a1), cross_product(vec_line1.b, vec_line2.b)) == 0:
            return True
        
        return False
        
    if cart_line1 is not None and cart_line2 is not None:
        a1 = Vector(cart_line1.A.x, cart_line1.A.y, cart_line1.A.z)
        a2 = Vector(cart_line2.A.x, cart_line2.A.y, cart_line2.A.z)

        b1 = Vector(cart_line1.b.a, cart_line1.b.b, cart_line1.b.c)
        b2 = Vector(cart_line2.b.a, cart_line2.b.b, cart_line2.b.c)

        if dot_product(a2 - a1, cross_product(b1, b2)) == 0:
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
        n1 = Vector(cart_plane1.A, cart_plane1.B, cart_plane1.C)
        n2 = Vector(cart_plane2.A, cart_plane2.B, cart_plane2.C)
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
        distance = (dot_product(vec_a, Vector(cart_plane.A, cart_plane.B, cart_plane.C)) - cart_plane.D) / Vector.magnitude(Vector(cart_plane.A, cart_plane.B, cart_plane.C))
    
    return abs(distance)


def distance_between_planes(plane1: VectorPlane, plane2: VectorPlane) -> float | str:
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
    cross_vec = cross_product(plane1.n, plane2.n)

    # Fail-fast validation: Check if planes are parallel
    if Vector.squareMagnitude(cross_vec) != 0:
        return "Both planes intersect each other. Minimum distance is 0."
    
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
        sintheta = dot_product(vec_plane.n, vec_line.b) / (Vector.magnitude(vec_plane.n) * Vector.magnitude(vec_line.b))
    
    if cart_line is not None and cart_plane is not None:
        sintheta = dot_product(cart_plane.n, cart_line.b) / (Vector.magnitude(cart_plane.n) * Vector.magnitude(cart_line.b))

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
    F = foot_of_perpendicular
    P = original_point

    # Utilizing Dunder/Magic methods (mul, sub) of the Point class
    image_of_P = (2 * F) - P

    return image_of_P


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
    vec_line = VectorLine()

    print("--- [ Generated Objects ] ---")
    print(f"Vector Plane 1:    {vec_pl1}")
    print(f"Vector Plane 2:    {vec_pl2}")
    print(f"Cartesian Plane 1: {cart_pl1}")
    print(f"Cartesian Plane 2: {cart_pl2}")
    print(f"Vector Line:       {vec_line}\n")

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
    print(f"> Is Point {p2} on Vector Plane 1?  -> {check_point_on_plane(plane=vec_pl1, target_point=p2)}")
    print(f"> Intercept Form (Cart. Plane 1):  {get_intercept_form(plane=cart_pl1)}")
    print(f"> Intersection Family Equation:    {get_plane_through_intersection(plane1=vec_pl1, plane2=vec_pl2)}\n")

    print("--- [ 3. Distances & Angles ] ---")
    print(f"> Angle between Vector Planes:     {angle_between_planes(vec_plane1=vec_pl1, vec_plane2=vec_pl2):.2f}°")
    print(f"> Angle between Cartesian Planes:  {angle_between_planes(cart_plane1=cart_pl1, cart_plane2=cart_pl2):.2f}°")
    print(f"> Dist (Point p1 to Cart Plane 1): {distance_between_point_and_plane(cart_plane=cart_pl1, P=p1):.4f} units\n")

    print("--- [ 4. Advanced Geometry ] ---")
    foot_point = get_foot_of_perpendicular(plane=vec_pl1, A=p1)
    print(f"> Foot of Perpendicular (p1 to VP1): ({foot_point.x:.2f}, {foot_point.y:.2f}, {foot_point.z:.2f})\n")
    
    print("--- [ 5. Intersections, Reflections & Distances (New) ] ---")
    
    # 1. Reflection / Image Point
    image_pt = get_image_point(original_point=p1, foot_of_perpendicular=foot_point)
    print(f"> Image of Point p1 (Reflection):  {image_pt}")

    # 2. Line through intersection of two planes
    intersect_line_eq = get_line_through_intersection(plane1=vec_pl1, plane2=vec_pl2)
    print(f"> Line of Intersection (Planes):   {intersect_line_eq}")

    # 3. Line and Plane Intersection
    line_plane_pt = get_line_plane_intersection(plane=vec_pl1, line=vec_line)
    print(f"> Line-Plane Intersection Point:   {line_plane_pt}")

    # 4. Distance between two planes
    plane_dist = distance_between_planes(plane1=vec_pl1, plane2=vec_pl2)
    if isinstance(plane_dist, (float, int)):
        print(f"> Distance Between Planes:         {plane_dist:.4f} units")
    else:
        print(f"> Distance Between Planes:         {plane_dist}")


    print("\n" + "="*50)
    print("✅ 3D ENGINE TESTING COMPLETE ✅")
    print("="*50 + "\n")