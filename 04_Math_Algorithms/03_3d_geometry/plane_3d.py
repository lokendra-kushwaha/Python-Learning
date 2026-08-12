# Adding the custom Vector module folder path to sys.path
# This allows importing Point and Vector classes from external files without errors
import sys
sys.path.append(r"L:/Python/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")
from math import sqrt
from vectors import Vector, Point
from advance_vectors import angle_between, cross_product, dot_product
from line_3d import CartesianLine, VectorLine

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
    

def check_point_on_plane(n: Vector, d: float, target_point: Point) -> bool:
    """
    Checks whether a specific 3D point lies on a given plane.

    Parameters:
        n (Vector): Normal vector of the plane.
        d (float): The constant distance value of the plane's equation.
        target_point (Point): The point (x, y, z) to be checked.

    Returns:
        bool: True if the point lies on the plane, False otherwise.
    """
    lhs = (n.a * target_point.x) + (n.b * target_point.y) + (n.c * target_point.z)
    if abs(lhs - d) < 1e-5:
        return True
    else:
        return False
    
def get_intercept_form(A: float, B: float, C: float, D: float):
    """
    Converts a Cartesian equation of a plane (Ax + By + Cz + D = 0) 
    into Intercept form (x/a + y/b + z/c = 1).

    Parameters:
        A (float): Coefficient of x.
        B (float): Coefficient of y.
        C (float): Coefficient of z.
        D (float): The constant term.

    Returns:
        str: Formatted string of the Intercept form, or an error message for edge cases.
    """
    if D == 0:
        return "Plane passes through the origin. Intercept form does not exist."
    
    if A == 0 or B == 0 or C == 0:
        return "Plane is parallel to an axis. Valid Intercept form cannot be generated."
    
    a = -D / A
    b = -D / B
    c = -D / C

    return f"x/({a}) + y/({b}) + z/({c}) = 1".replace("+ -", "- ")

def get_plane_through_intersection(n1: Vector, d1: float, n2: Vector, d2: float) -> str:
    """
    Generates the equation of a plane passing through the intersection of two given planes.

    Parameters:
        n1 (Vector): Normal vector of the first plane.
        d1 (float): Constant term of the first plane.
        n2 (Vector): Normal vector of the second plane.
        d2 (float): Constant term of the second plane.

    Returns:
        str: The family of planes equation using lambda (\u03BB).
    """
    return f"(xi + yj + zk).[({n1}) - \u03BB({n2})] = {d1} + \u03BB{d2}".replace("\u03BB-", "-\u03BB")

def are_lines_coplaner(vec_line1: VectorLine = None, vec_line2: VectorLine = None, cart_line1: CartesianLine = None, cart_line2: CartesianLine = None):
    """
    Checks if two given 3D lines are coplanar (lie on the same plane).
    Supports checking for both Vector Lines and Cartesian Lines.

    Parameters:
        vec_line1 (VectorLine, optional): First line in vector format.
        vec_line2 (VectorLine, optional): Second line in vector format.
        cart_line1 (CartesianLine, optional): First line in cartesian format.
        cart_line2 (CartesianLine, optional): Second line in cartesian format.

    Returns:
        bool: True if the lines are coplanar, False otherwise.
    """
    if vec_line1 is not None and vec_line2 is not None:
        a1 = Vector(vec_line1.A.x, vec_line1.A.y, vec_line1.A.z)
        a2 = Vector(vec_line2.A.x, vec_line2.A.y, vec_line2.A.z)

        if dot_product(Vector.substraction(a2, a1), cross_product(vec_line1.b, vec_line2.b)) == 0:
            return True
        else:
            return False
        
    if cart_line1 is not None and cart_line2 is not None:
        a1 = Vector(cart_line1.A.x, cart_line1.A.y, cart_line1.A.z)
        a2 = Vector(cart_line2.A.x, cart_line2.A.y, cart_line2.A.z)

        b1 = Vector(cart_line1.b.a, cart_line1.b.b, cart_line1.b.c)
        b2 = Vector(cart_line2.b.a, cart_line2.b.b, cart_line2.b.c)

        if dot_product(Vector.substraction(a2, a1), cross_product(b1, b2)) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    print("\n--- Testing Plane 3D Engine ---\n")

    # Creating some dummy test data
    n_cap = Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14))
    n_vec = Vector(2, 3, 4)
    v1 = Vector(1, -1, 2)
    v2 = Vector(2, 0, 1)

    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = Point(7, 8, 0)

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

    print("3. Point on Plane Check:")
    print(f"Is Point {p2} on the plane? ->", check_point_on_plane(n=n_vec, d=20, target_point=p2))
    print("-" * 30)

    print("4. Intercept Form:")
    print(get_intercept_form(A=2, B=3, C=4, D=-12))
    print("-" * 30)

    print("5. Plane through Intersection:")
    print(get_plane_through_intersection(n1=v1, d1=4, n2=v2, d2=-5))
    print("-" * 30)

    print("6. Coplanar Lines Check:")
    # Assuming VectorLine and CartesianLine can be initialized empty or with default data for testing
    vec_l1 = VectorLine()
    vec_l2 = VectorLine()
    print("Vector Line 1:", vec_l1)
    print("Vector Line 2:", vec_l2)
    print("Are Vector Lines Coplanar? ->", are_lines_coplaner(vec_line1=vec_l1, vec_line2=vec_l2))
    print("\n")
    
    cart_l1 = CartesianLine()
    cart_l2 = CartesianLine()
    print("Cartesian Line 1:", cart_l1)
    print("Cartesian Line 2:", cart_l2)
    print("Are Cartesian Lines Coplanar? ->", are_lines_coplaner(cart_line1=cart_l1, cart_line2=cart_l2))
    print("-" * 30)