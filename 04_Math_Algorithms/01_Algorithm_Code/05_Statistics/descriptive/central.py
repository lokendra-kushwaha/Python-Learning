import sys
import os

# =========================================================
# PATH CONFIGURATION (Dynamic Imports)
# =========================================================
# Setting up paths so Python can find our custom modules across folders
current_dir = os.path.dirname(os.path.abspath(__file__))
# Linking the external '03_Python_Logics' folder to import custom_randint
logic_dir = os.path.abspath(os.path.join(current_dir, "../../../..", "03_Python_Logics", "built_in_functions"))
print(f"Logic Directory Linked: {logic_dir}\n")
sys.path.append(logic_dir)

import custom_sum, custom_sorted, custom_len, custom_max # type: ignore

"""
Descriptive Statistics: Measures of Central Tendency.

This module provides functional tools to identify the center or typical 
value of a given dataset (Vector). It includes calculations for the Mean 
(mathematical average) and Median (positional average).

These functions are designed to operate strictly on the custom Vector 
data container.
"""

def mean(vector):
    """
    Calculates the arithmetic mean (average) of a dataset.
    
    Mathematical Formula:
        $\mu = \frac{1}{N} \sum_{i=1}^{N} x_i$
        Where $N$ is the total number of elements, and $x_i$ represents each value.

    Args:
        vector (Vector): The input data container containing numerical values.

    Raises:
        ValueError: If the vector is empty (division by zero prevention).

    Returns:
        float: The calculated mean of the dataset.
    """
    n = custom_len.custom_len(vector)
    
    if n == 0:
        raise ValueError("Math Error: Cannot calculate the mean of an empty dataset.")
        
    return custom_sum.sum_with_reduce(vector) / n


def median(vector):
    """
    Calculates the median (middle value) of a dataset.
    
    The function first sorts the data in ascending order. If the dataset 
    has an odd number of elements, it returns the exact middle value. 
    If it has an even number of elements, it returns the average of the 
    two central values.

    Args:
        vector (Vector): The input data container.

    Raises:
        ValueError: If the vector is empty.

    Returns:
        float or int: The median value of the dataset.
    """
    n = custom_len.custom_len(vector)
    
    if n == 0:
        raise ValueError("Math Error: Cannot calculate the median of an empty dataset.")

    # Sorting the data to find the positional center
    sorted_data = custom_sorted.merge_sort(vector)
    
    # Finding the middle index using floor division
    mid_index = n // 2

    # Case 1: Odd number of elements
    if n % 2 != 0:
        return sorted_data[mid_index]
    
    # Case 2: Even number of elements
    else:
        left_mid = sorted_data[mid_index - 1]
        right_mid = sorted_data[mid_index]
        return (left_mid + right_mid) / 2.0
    

def mode(vector):
    """
    Calculates the mode (most frequent value or values) of a dataset.
    
    This function counts the frequency of each distinct number in the dataset. 
    It is designed to handle unimodal, bimodal, and multimodal distributions 
    by returning all values that share the highest frequency.

    Args:
        vector (Vector): The input data container.

    Raises:
        ValueError: If the vector is empty.

    Returns:
        list: A list containing the mode(s) of the dataset. 
    """
    if custom_len.custom_len(vector) == 0:
        raise ValueError("Math Error: Cannot calculate the mode of an empty dataset.")

    # Step 1: Count the frequency of each number
    counts = {}
    for item in vector:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            
    # Step 2: Find the maximum frequency
    max_count = custom_max.custom_max(counts.values())
    
    # Step 3: Extract all numbers that have the maximum frequency
    modes = []
    for number, freq in counts.items():
        if freq == max_count:
            modes.append(number)
            
    return modes
