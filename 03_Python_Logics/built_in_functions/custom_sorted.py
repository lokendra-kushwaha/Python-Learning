"""
Bubble Sort Algorithm
----------------------
A script that mimics Python's built-in sorted() function using the 
Bubble Sort method. It returns a new sorted list from any iterable.
"""

from typing import Iterable, List, Any

def bubble_sort(iterable: Iterable) -> List[Any]:
    """Sorts an iterable in ascending order using Bubble Sort.

    This algorithm repeatedly steps through the list, compares adjacent 
    elements, and swaps them if they are in the wrong order. It creates 
    a new list to avoid modifying the original data.

    Time Complexity: O(N^2) - Very slow for large datasets.
    Space Complexity: O(N) - Creates a new list in memory.

    Args:
        iterable (Iterable): A sequence or collection to be sorted (e.g., list, string).

    Returns:
        List[Any]: A new list containing all items in ascending order.
    """
    result_list = list(iterable)
    list_length = len(result_list)

    # pass_num controls how many times we traverse the list
    for pass_num in range(list_length):
        # We subtract pass_num because the last elements are already sorted
        for current_index in range(list_length - 1 - pass_num):
            if result_list[current_index] > result_list[current_index + 1]:
                # Swap the elements
                result_list[current_index], result_list[current_index + 1] = \
                    result_list[current_index + 1], result_list[current_index]

    return result_list



def merge_sort(iterable: Iterable) -> List[Any]:
    """
    Sorts an iterable in ascending order using the Merge Sort algorithm.

    This function acts as a wrapper that encapsulates the divide-and-conquer 
    logic. It handles the initial conversion of the iterable into a list 
    and then uses nested helper functions to recursively sort the data without 
    modifying the original input.

    Time Complexity: O(N log N) - Consistently fast across all cases.
    Space Complexity: O(N) - Requires extra space for temporary arrays during the merge phase.

    Args:
        iterable (Iterable): A sequence or collection of comparable items to be sorted 
            (e.g., list, tuple, string).

    Returns:
        List[Any]: A new list containing all items from the input iterable in 
            ascending order.

    Example:
        >>> merge_sort([5, 80, 2, 4, 3, 1, 100])
        [1, 2, 3, 4, 5, 80, 100]
        >>> merge_sort("lokendra")
        ['a', 'd', 'e', 'k', 'l', 'n', 'o', 'r']
    """

    def merge(left: list, right: list) -> list:
        """Helper function to merge two sorted lists into a single sorted list."""
        result = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        # Append any remaining elements
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_recursive(data_list: list) -> list:
        """Helper function to recursively divide and sort the list."""
        if len(data_list) <= 1:
            return data_list
            
        mid = len(data_list) // 2
        left_split = sort_recursive(data_list[:mid])
        right_split = sort_recursive(data_list[mid:])
        
        return merge(left_split, right_split)

    # Convert the iterable to a list and begin the recursive sorting
    return sort_recursive(list(iterable))


# ==========================================
# Testing Block
# ==========================================
if __name__ == "__main__":
    # Test with a list of numbers
    original_numbers = [5, 80, 2, 4, 3, 1, 100]
    print(f"Original List: {original_numbers}")
    print(f"Bubble Sorted: {bubble_sort(original_numbers)}")

    print("-" * 40)

    # Test with a string
    text = "lokendra"
    print(f"Original String: '{text}'")
    print(f"Bubble Sorted:   {bubble_sort(text)}")

    print("-" * 40)

    # Test with a list of numbers
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6, 7, 8, 9, 0, 223, 34, 45]
    print("Original List :", test_numbers)
    print("Merge Sorted  :", merge_sort(test_numbers))
    
    print("-" * 40)
    
    # Test with a string
    test_string = "lokendra"
    print("Original String :", f"'{test_string}'")
    print("Merge Sorted    :", merge_sort(test_string))