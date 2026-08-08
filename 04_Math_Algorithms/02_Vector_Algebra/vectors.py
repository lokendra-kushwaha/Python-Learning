from random import randint

def clean_vector(raw_str):
    clean_str = raw_str.replace("+ -", "-")
    return clean_str

class Vector:

    def __init__(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            self.a = a
            self.b = b
            self.c = c

        else:
            self.a = randint(-10, 10)
            self.b = randint(-10, 10)
            self.c = randint(-10, 10)

    def __str__(self):
        return clean_vector(f"{self.a}i + {self.b}j + {self.c}k")

    def magnitude(self):
        str_mag =  f"{(self.a**2 + self.b**2 + self.c**2)**0.5:.2f}"
        return float(str_mag)
    
    def addition(self, other):
        new_a, new_b, new_c = self.a + other.a, self.b + other.b, self.c + other.c
        return Vector(new_a, new_b, new_c)
    
    def substraction(self, other):
        new_a, new_b, new_c = self.a - other.a, self.b - other.b, self.c - other.c   
        return Vector(new_a, new_b, new_c)
    
    def unit_vector(self):
        mag = self.magnitude()
        new_a, new_b, new_c = round(self.a/mag, 2), round(self.b/mag, 2), round(self.c/mag, 2)

        return Vector(new_a, new_b, new_c)

    def scalor_multiply(self, scalor):
        new_a, new_b, new_c = scalor*self.a, scalor*self.b, scalor*self.c
        return Vector(new_a, new_b, new_c)
    
    def is_collinear(self, other):
        condition_1 = self.a*other.b == self.b*other.a
        condition_2 = self.b*other.c == self.c*other.b
        condition_3 = self.a*other.c == self.c*other.a
        if condition_1 and condition_2 and condition_3:
            return "Both are collinear vectors."
        
        else:
            return "Vectors are not collinear."
    
    def is_equal(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return "Both are equal vectors."
        
        else:
            return "Vectors are not equal."
        
    def get_direction_ratios(self):
        a, b, c = self.a, self.b, self.c
        return [a, b, c]
    
    def get_dic_cos(self):
        mag = self.magnitude()
        cos = []
        for ratios in self.get_direction_ratios():
            cos.append(round(ratios/mag, 2))

        return cos

    def section_vector(self, other, m, n, is_internal=True):
        if m == 0 and n == 0:
            return "Error: Ratio 0:0 is invalid."
        
        if is_internal:
            if m + n == 0:
                return "Error: (m + n) cann't zero in Internal division."

            new_a = round((other.a*m + self.a*n)/(m + n), 2)
            new_b = round((other.b*m + self.b*n)/(m + n), 2)
            new_c = round((other.c*m + self.c*n)/(m + n), 2)

            return Vector(new_a, new_b, new_c)
        
        else:          
            if m == n:
                return "Error: n and m can not be same in External Division."
            
            new_a = round((other.a*m - self.a*n)/(m - n), 2)
            new_b = round((other.b*m - self.b*n)/(m - n), 2)
            new_c = round((other.c*m - self.c*n)/(m - n), 2)
            
            return Vector(new_a, new_b, new_c)


class Point(Vector):
    
    def __init__(self, x1=None, y1=None, z1=None):
        if x1 is not None and y1 is not None and z1 is not None:
            self.x, self.y, self.z = x1, y1, z1

        else:
            self.x, self.y, self.z = randint(-10, 10), randint(-10, 10), randint(-10, 10)

    def __str__(self):
        x, y, z = self.x, self.y, self.z
        return f"{x, y, z}"
    
    def vector_joining_two_points(self, other):
        new_a = other.x - self.x
        new_b = other.y - self.y
        new_c = other.z - self.z

        return Vector(new_a, new_b, new_c)

if __name__ == "__main__":
    v1 = Vector()
    v2 = Vector()
    print(v1)
    print(v2)

    print(v1.magnitude())
    print(v1.addition(v2))
    print(v1.substraction(v2))
    print(v1.unit_vector())
    print(v1.scalor_multiply(2))
    print(v1.is_collinear(v2))
    print(v1.is_equal(v2))
    print(v1.get_direction_ratios())
    print(v1.get_dic_cos())
    print(v1.section_vector(v2, 1, 3, is_internal=False))

    p1 = Point(1, 2, 3)
    p2 = Point(2, 3, 4)
    print(p1)
    print(p2)

    print(p1.vector_joining_two_points(p2))
    print(p1.vector_joining_two_points(p2))