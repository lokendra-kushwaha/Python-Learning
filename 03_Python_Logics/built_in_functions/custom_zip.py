"""
Custom Zip Function
-------------------
A script that reverse-engineers Python's built-in zip() function for two lists.
It pairs elements from both lists up to the length of the shorter list.
"""

from typing import List, Tuple, Any

def custom_zip(l1: List[Any], l2: List[Any]) -> List[Tuple[Any, Any]]:
    """
    Pairs corresponding elements from two lists sequentially.

    How it works:
    It compares the lengths of the two input lists to find the shorter one.
    Then, it uses a for loop to iterate up to that length, taking elements 
    from both lists at the same index and packing them into a tuple.

    Args:
        l1 (List[Any]): The first list.
        l2 (List[Any]): The second list.

    Returns:
        List[Tuple[Any, Any]]: A list of tuples, where each tuple contains 
                               paired elements from l1 and l2.

    Examples:
        >>> custom_zip([1, 2, 3], ['a', 'b', 'c'])
        [(1, 'a'), (2, 'b'), (3, 'c')]
    """
    pairs = []
    
    # Check which list is smaller to avoid IndexError
    if len(l1) <= len(l2):
        for i in range(len(l1)):
            pairs.append((l1[i], l2[i]))
        return pairs
    else:
        for i in range(len(l2)):
            pairs.append((l1[i], l2[i]))
        return pairs


if __name__ == "__main__":
    # Testing the custom zip function
    l3 = [1, 2, 3, 4, 5]
    l4 = [-1, -2, -3, -4, 5]
    
    zipped_result = custom_zip(l3, l4)
    print("Paired Data:", zipped_result)

    # Performing calculations just like the real zip
    addition_result = [i + j for i, j in custom_zip(l3, l4)]
    print("Addition using custom_zip:", addition_result)