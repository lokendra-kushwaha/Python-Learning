"""
Custom Sorted Function
----------------------
A script that reverse-engineers Python's built-in sorted() function.
It returns a new sorted list from the items in any iterable.
"""

from typing import Iterable, List, Any

def custom_sorted(iterable: Iterable) -> List[Any]:
    """
    Returns a new sorted list from the items in the given iterable.

    How it works:
    This function uses the Bubble Sort algorithm. It first converts the 
    input iterable into a new list to ensure it doesn't modify the original 
    data (exactly how the built-in sorted() works). Then, it repeatedly 
    steps through the list, compares adjacent elements, and swaps them 
    if they are in the wrong order.

    Args:
        iterable (Iterable): A sequence or collection to be sorted (list, string, tuple, etc.).

    Returns:
        List[Any]: A new list containing all items from the iterable in ascending order.

    Examples:
        >>> custom_sorted([5, 80, 2, 4, 3, 1, 100])
        [1, 2, 3, 4, 5, 80, 100]
        >>> custom_sorted('python')
        ['h', 'n', 'o', 'p', 't', 'y']
    """
    # Convert iterable to a new list to avoid modifying the original object
    # This also allows it to handle strings, tuples, etc.
    result_list = list(iterable)
    n = len(result_list)

    for j in range(n):
        # (n - 1 - j) optimizes the loop since the last j elements are already sorted
        for i in range(n - 1 - j):
            if result_list[i] > result_list[i + 1]:
                # Swap the elements
                result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]

    return result_list

if __name__ == "__main__":
    # Testing with a list
    original_numbers = [5, 80, 2, 4, 3, 1, 100]
    sorted_numbers = custom_sorted(original_numbers)
    
    print(f"Original List: {original_numbers}")
    print(f"Sorted List:   {sorted_numbers}\n")

    # Testing with a string
    text = "lokendra"
    sorted_text = custom_sorted(text)
    
    print(f"Original String: '{text}'")
    print(f"Sorted String:   {sorted_text}")