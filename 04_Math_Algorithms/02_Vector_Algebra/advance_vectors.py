import math
from vectors import Vector

def dot_product(v1:  Vector, v2: Vector) -> float:
    return (v1.a * v2.a) + (v1.b * v2.b) + (v1.c * v2.c)

def cross_product(v1: Vector, v2: Vector) -> Vector:
    new_a = v1.b*v2.c - v1.c*v2.b
    new_b = -(v1.a*v2.c - v1.c*v2.a)
    new_c = v1.a*v2.b - v1.b*v2.a
    return Vector(new_a, new_b, new_c)

def angle_between(v1: Vector, v2: Vector) -> float:
    cos_theta = dot_product(v1, v2)/(v1.magnitude()*v2.magnitude())
    angle_in_radian = math.acos(cos_theta)
    angle_in_degree = math.degrees(angle_in_radian)

    return  round(angle_in_degree, 2)

def vector_projection(v1: Vector, v2: Vector) -> float:
    return round(dot_product(v1, v2)/v2.magnitude(), 2)

def scalar_triple_product(v1: Vector, v2: Vector, v3: Vector) -> float:
    return dot_product(v1, cross_product(v2, v3))

def vector_triple_product(v1: Vector, v2: Vector, v3: Vector) -> Vector:
    return cross_product(v1, cross_product(v2, v3))

def vector_rotation(v1):
    pass

def shortest_distance_in_3D(v1):
    pass


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