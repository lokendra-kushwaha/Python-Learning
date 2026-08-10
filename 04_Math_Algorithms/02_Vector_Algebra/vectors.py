from random import randint

def clean_vector(raw_str):
    """
    Cleans the string representation of a vector by formatting negative signs properly.
    Example: Converts '2i + -3j' to '2i -3j'.
    
    Args:
        raw_str (str): The raw formatted vector string.
        
    Returns:
        str: A mathematically clean vector string.
    """
    clean_str = raw_str.replace("+ -", "- ")
    return clean_str

class Vector:
    """
    A class to represent a 3D Vector (ai + bj + ck) and perform vector algebra operations.
    """
    def __init__(self, a=None, b=None, c=None):
        """
        Initializes the Vector object.

        Args:
            a (int/float, optional): i-cap component.
            b (int/float, optional): j-cap component.
            c (int/float, optional): k-cap component.
            
        Note: If no arguments are passed, it generates a random vector with values between -10 and 10.
        """
        if a is not None and b is not None and c is not None:
            self.a = a
            self.b = b
            self.c = c

        else:
            self.a = randint(-10, 10)
            self.b = randint(-10, 10)
            self.c = randint(-10, 10)

    def __str__(self) -> str:
        """Returns the standard string representation of the vector (e.g., 2i + 3j - 4k)."""
        return clean_vector(f"{self.a}i + {self.b}j + {self.c}k")

    def magnitude(self: Vector) -> float:
        """
        Calculates the length (magnitude) of the vector.
        
        Returns:
            float: The magnitude rounded to 2 decimal places.
        """
        str_mag =  f"{(self.a**2 + self.b**2 + self.c**2)**0.5:.2f}"
        return float(str_mag)
    
    def addition(self: Vector, other: Vector) -> Vector:
        """
        Adds another vector to the current vector.
        
        Args:
            other (Vector): The vector to be added.
            
        Returns:
            Vector: A new Vector object representing the sum.
        """
        new_a, new_b, new_c = self.a + other.a, self.b + other.b, self.c + other.c
        return Vector(new_a, new_b, new_c)
    
    def substraction(self: Vector, other: Vector) -> Vector:
        """
        Subtracts another vector from the current vector.
        
        Args:
            other (Vector): The vector to subtract.
            
        Returns:
            Vector: A new Vector object representing the difference.
        """
        new_a, new_b, new_c = self.a - other.a, self.b - other.b, self.c - other.c   
        return Vector(new_a, new_b, new_c)
    
    def unit_vector(self: Vector) -> Vector:
        """
        Calculates the unit vector (a vector of length 1) in the same direction.
        
        Returns:
            Vector: A new Vector object representing the unit vector.
        """
        mag = self.magnitude()
        new_a, new_b, new_c = round(self.a/mag, 2), round(self.b/mag, 2), round(self.c/mag, 2)

        return Vector(new_a, new_b, new_c)

    def scalor_multiply(self: Vector, scalor: int) -> Vector:
        """
        Multiplies the vector by a scalar number.
        
        Args:
            scalor (int/float): The number to multiply with.
            
        Returns:
            Vector: A new scaled Vector object.
        """
        new_a, new_b, new_c = scalor*self.a, scalor*self.b, scalor*self.c
        return Vector(new_a, new_b, new_c)
    
    def is_collinear(self: Vector, other: Vector) -> str:
        """
        Checks if two vectors are collinear (parallel) by comparing their direction ratios.
        
        Args:
            other (Vector): The vector to compare with.
            
        Returns:
            str: Message indicating whether they are collinear or not.
        """
        condition_1 = self.a*other.b == self.b*other.a
        condition_2 = self.b*other.c == self.c*other.b
        condition_3 = self.a*other.c == self.c*other.a
        if condition_1 and condition_2 and condition_3:
            return "Both are collinear vectors."
        
        else:
            return "Vectors are not collinear."
    
    def is_equal(self: Vector, other: Vector) -> str:
        """
        Checks if two vectors have exactly the same components.
        
        Args:
            other (Vector): The vector to compare with.
            
        Returns:
            str: Message indicating whether they are equal or not.
        """
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return "Both are equal vectors."
        
        else:
            return "Vectors are not equal."
        
    def get_direction_ratios(self: Vector) -> list:
        """
        Retrieves the direction ratios (scalar components) of the vector.
        
        Returns:
            list: A list containing [a, b, c].
        """
        a, b, c = self.a, self.b, self.c
        return [a, b, c]
    
    def get_dic_cos(self: Vector) -> int:
        """
        Calculates the direction cosines of the vector.
        
        Returns:
            list: A list containing [l, m, n] representing the direction cosines.
        """
        mag = self.magnitude()
        cos = []
        for ratios in self.get_direction_ratios():
            cos.append(round(ratios/mag, 2))

        return cos

    def section_vector(self: Vector, other: Vector, m: int, n: int, is_internal=True) -> Vector:
        """
        Finds the position vector of a point that divides the line joining 
        the current vector and the 'other' vector in the ratio m:n.
        
        Args:
            other (Vector): The terminal vector.
            m (int/float): Ratio part 1.
            n (int/float): Ratio part 2.
            is_internal (bool): True for internal division, False for external. Defaults to True.
            
        Returns:
            Vector or str: A new Vector object if successful, or an Error string for invalid ratios.
        """
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
    """
    A class to represent a 3D coordinate point (x, y, z).
    Inherits from Vector to utilize vector-based logic for geometry.
    """
    def __init__(self, x=None, y=None, z=None):
        """
        Initializes the 3D Point.
        
        Args:
            x1 (int/float, optional): X-coordinate.
            y1 (int/float, optional): Y-coordinate.
            z1 (int/float, optional): Z-coordinate.
            
        Note: If coordinates are not provided, generates a random point between -10 and 10.
        """
        if x is not None and y is not None and z is not None:
            self.x, self.y, self.z = x, y, z

        else:
            self.x, self.y, self.z = randint(-10, 10), randint(-10, 10), randint(-10, 10)

    def __str__(self: Point) -> str:
        """Returns the point in standard coordinate format: (x, y, z)."""
        x, y, z = self.x, self.y, self.z
        return f"{x, y, z}"
    
    def vector_joining_two_points(self: Point, other: Point) -> Vector:
        """
        Calculates the vector directed from the current point to another point.

        Args:
            other (Point): The destination Point.
        
        Returns:
            Vector: A new Vector object representing the directed segment.
        """
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