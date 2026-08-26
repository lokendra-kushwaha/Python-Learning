"""
Core Data Container Module for the Statistics Library.

This module provides the foundational data structure (Vector) used across 
the entire statistics engine. It acts similarly to a 1-Dimensional NumPy array, 
ensuring data integrity, type checking, and providing built-in iteration 
and indexing capabilities.
"""

class Vector:
    """
    A 1-Dimensional data container for statistical calculations.

    This class strictly accepts numerical data (integers and floats). 
    It serves as the base input for all descriptive and inferential 
    statistical functions.

    Attributes:
        data (list): The validated list of numerical values.
    """

    def __init__(self, data_list):
        """
        Initializes the Vector and validates the input data.

        Args:
            data_list (list or tuple): A sequence of numerical values.

        Raises:
            TypeError: If any element in the input is not an int or float.
            ValueError: If the input list is empty.
        """
        if not data_list:
            raise ValueError("Data Input Error: Vector cannot be empty.")

        self.data = []
        for index, item in enumerate(data_list):
            if not isinstance(item, (int, float)):
                raise TypeError(f"Type Error at index {index}: Expected int or float, got {type(item).name}.")
            self.data.append(item)

    def __repr__(self):
        """
        Returns the string representation of the Vector.
        """
        return f"Vector({self.data})"

    def __len__(self):
        """
        Returns the total number of elements in the Vector.
        Allows the use of the standard Python len() function.
        
        Example: len(my_vector)
        
        Returns:
            int: The count of elements.
        """
        return len(self.data)

    def __getitem__(self, index):
        """
        Enables indexing and slicing on the Vector object.
        Allows users to access data points exactly like a normal list.
        
        Example: my_vector[0] or my_vector[:3]

        Args:
            index (int or slice): The index or range to access.

        Returns:
            int, float, or list: The accessed data point(s).

        Raises:
            IndexError: If the index is not integer value.
        """
        if not isinstance(index, int):
            raise IndexError(f"Index Error: Expected int, got {type(index).__name__}.")
        
        return self.data[index]