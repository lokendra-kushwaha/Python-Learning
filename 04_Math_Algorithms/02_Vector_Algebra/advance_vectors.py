import math
from vectors import Vector

def dot_product(v1:  Vector, v2: Vector) -> float:
    """
    Calculates the scalar dot product of two vectors.
    Formula: (a1 * a2) + (b1 * b2) + (c1 * c2)
    
    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.
        
    Returns:
        float: The resulting scalar value.
    """
    return (v1.a * v2.a) + (v1.b * v2.b) + (v1.c * v2.c)

def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calculates the vector cross product of two vectors.
    Produces a new vector that is perpendicular to both input vectors.
    
    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.
        
    Returns:
        Vector: A new Vector object representing the cross product.
    """
    new_a = v1.b*v2.c - v1.c*v2.b
    new_b = -(v1.a*v2.c - v1.c*v2.a)
    new_c = v1.a*v2.b - v1.b*v2.a
    return Vector(new_a, new_b, new_c)

def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calculates the angle between two vectors in degrees.
    Formula: cos(theta) = (v1 . v2) / (|v1| * |v2|)
    
    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.
        
    Returns:
        float: The angle in degrees, rounded to 2 decimal places.
    """
    cos_theta = dot_product(v1, v2)/(v1.magnitude()*v2.magnitude())
    angle_in_radian = math.acos(cos_theta)
    angle_in_degree = math.degrees(angle_in_radian)

    return angle_in_degree

def vector_projection(v1: Vector, v2: Vector) -> float:
    """
    Calculates the scalar projection of vector v1 onto vector v2.
    Formula: (v1 . v2) / |v2|
    
    Args:
        v1 (Vector): The vector to be projected.
        v2 (Vector): The vector on which the projection is made.
        
    Returns:
        float: The scalar length of the projection, rounded to 2 decimal places.
    """
    return round(dot_product(v1, v2)/v2.magnitude(), 2)

def scalar_triple_product(v1: Vector, v2: Vector, v3: Vector) -> float:
    """
    Calculates the scalar triple product of three vectors.
    Geometrically represents the volume of the parallelepiped formed by the three vectors.
    Formula: v1 . (v2 x v3)
    
    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.
        v3 (Vector): The third vector.
        
    Returns:
        float: The resulting scalar volume.
    """
    return dot_product(v1, cross_product(v2, v3))

def vector_triple_product(v1: Vector, v2: Vector, v3: Vector) -> Vector:
    """
    Calculates the vector triple product of three vectors.
    Formula: v1 x (v2 x v3)
    
    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.
        v3 (Vector): The third vector.
        
    Returns:
        Vector: A new Vector object representing the final result.
    """
    return cross_product(v1, cross_product(v2, v3))

def vector_rotation(v1):
    """
    [WORK IN PROGRESS]
    Rotates a vector in 3D space using rotation matrices or quaternions.
    """
    pass

def shortest_distance_in_3D(v1):
    """
    [WORK IN PROGRESS]
    Calculates the shortest distance between 3D geometrical components (e.g., lines or planes).
    """
    pass

if __name__ == "__main__":
    v1 = Vector()
    v2 = Vector()
    v3 = Vector()
    print('v1 =', v1)
    print('v2 =', v2)
    print('v3 =', v3)

    print("Dot product of v1 and v2 -: ", dot_product(v1, v2))
    print("Projection of vector v1 on v2 -: ", vector_projection(v1, v2))
    print("Angle between vector v1 and vector v2 -: ", angle_between(v1, v2))
    print("Cross product of v1 and v2 -: ", cross_product(v1, v2))
    print("Scalor triple product of v1, v2, and v3 -: ", scalar_triple_product(v1, v2, v3))
    print("Vector triple product of v1, v2, and v3 -: ", vector_triple_product(v1, v2, v3))