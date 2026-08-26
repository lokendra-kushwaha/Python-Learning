from functools import reduce

def sum_with_reduce(my_list):
    """
    Calculates the sum of a list using the reduce function.

    This method uses functional programming paradigms and Python's C-backend
    optimized reduce function along with a lambda to aggregate the list elements.
    
    Time Complexity: O(N) where N is the number of elements in the list.
    Space Complexity: O(1)

    Args:
        my_list (list): A list of numerical values (int or float).

    Returns:
        int or float: The total sum of all elements in the list.
    """
    return reduce(lambda x, y: x + y, my_list)


def sum_with_while(my_list):
    """Calculates the sum of a list using a manual while loop.

    This method manually controls the index variable to iterate through
    the list. It is highly customizable for skipping elements if needed,
    but is more verbose than other methods.
    
    Time Complexity: O(N) where N is the number of elements in the list.
    Space Complexity: O(1)

    Args:
        my_list (list): A list of numerical values.

    Returns:
        int or float: The total sum of all elements in the list.
    """
    i = 0
    total = 0
    while i < len(my_list):
        total += my_list[i]
        i += 1
    return total


def sum_with_for(my_list):
    """Calculates the sum of a list using a Pythonic for loop.

    This method iterates directly over the values of the list rather than
    using indices. This is the most readable and standard Pythonic approach,
    eliminating the risk of index out-of-bounds errors.
    
    Time Complexity: O(N) where N is the number of elements in the list.
    Space Complexity: O(1)

    Args:
        my_list (list): A list of numerical values.

    Returns:
        int or float: The total sum of all elements in the list.
    """
    total = 0
    for num in my_list:
        total += num
    return total


# ==========================================
# Testing & Benchmarking Block
# ==========================================
if __name__ == "__main__":
    test_data = [1, 2, 3, 4]
    
    print("--- Custom Sum Benchmark ---")
    print(f"1. Reduce Sum : {sum_with_reduce(test_data)}")
    print(f"2. While Sum  : {sum_with_while(test_data)}")
    print(f"3. For Sum    : {sum_with_for(test_data)}")