"""
3D Geometry Base Core
---------------------
This module serves as the foundational engine for 3D geometric operations.
It handles Direction Ratios and the calculation of Direction Cosines from both 
individual vector components and between two points in 3D space.
"""
# Adding the custom Vector module folder path to sys.path
import sys
sys.path.append(r"L:/01_AI_and_Data_Science/Python-Learning/04_Math_Algorithms/02_Vector_Algebra")
from vectors import Vector, Point
from random import randint

#================================================================================================
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

#=================================================================================================

class DirectionRatio:
    """
    A class to represent the Direction Ratios (a, b, c) of a vector or a line.
    If no specific values are provided during initialization, it assigns 
    random integers between -10 and 10.
    """
    def __init__(self, a: float = None, b: float = None, c: float = None, data=None):
        """
        Initializes the Direction Ratio object.
        
        Parameters:
        a (float, optional): The x-component ratio.
        b (float, optional): The y-component ratio.
        c (float, optional): The z-component ratio.
        data (any, optional): Placeholder for any additional data handling.
        """
        if a is not None and b is not None and c is not None:
            validate_type('a', a, (float, int))
            validate_type('b', b, (float, int))
            validate_type('c', c, (float, int))

            self.a = a
            self.b = b
            self.c = c

        else:
            # Generate random direction ratios if inputs are missing
            self.a = randint(-10, 10)
            self.b = randint(-10, 10)
            self.c = randint(-10, 10)

    def __str__(self) -> str:
        """
        Returns the string representation of the Direction Ratios as a tuple.
        """
        dic_ratios = (self.a, self.b, self.c)
        return str(dic_ratios)
    
    def __repr__(self):
        return self.__str__()
    
    def dic_cosine(self) -> Vector:
        """
        Calculates the Direction Cosines (l, m, n) based on the current Direction Ratios.
        
        Returns:
        Vector: A Unit Vector representing the direction cosines. 
                Returns a zero vector if the magnitude is 0 to avoid DivisionByZero error.
        """ 
        magnitude = (self.a**2 + self.b**2 + self.c**2)**0.5
        # Crash protection: If magnitude is zero, return a zero Vector
        if magnitude == 0:
            return 0, 0, 0
        
        l_val = self.a / magnitude
        m_val = self.b / magnitude
        n_val = self.c / magnitude

        return Vector(l_val, m_val, n_val)

    
def dic_cosine_of_a_line_segment(p1:Point, p2:Point) -> Vector:
    """
    Calculates the Direction Cosines of a line passing through two specific points.
    
    Parameters:
    p1 (Point): The starting point of the line.
    p2 (Point): The ending point of the line.
    
    Returns:
    Vector: A Unit Vector containing the calculated direction cosines (l, m, n).
    """
    validate_type('p1', p1, Point)
    validate_type('p2', p2, Point)
    
    magnitude = ((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)**0.5

    # Crash protection: Check if both points are at the exact same location
    if magnitude == 0:
        return Vector(0, 0, 0)
        
    l_val = (p2.x - p1.x) / magnitude
    m_val = (p2.y - p1.y) / magnitude
    n_val = (p2.z - p1.z) / magnitude

    return Vector(l_val, m_val, n_val)

# Test Execution Block
if __name__ == "__main__":
    
    print("--- Testing DirectionRatio Class ---")
    d = DirectionRatio()
    print(f"Random Direction Ratios: {d}")
    print(f"Calculated Direction Cosines: {d.dic_cosine()}\n")

    print("--- Testing Two Points Global Function ---")
    # Assuming the Point class initializes with random coordinates if left empty
    p1 = Point() 
    p2 = Point()
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Direction Cosines between p1 and p2: {dic_cosine_of_a_line_segment(p1, p2)}")