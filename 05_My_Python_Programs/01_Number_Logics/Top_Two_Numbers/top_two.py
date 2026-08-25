def get_largest_and_second_largest(numbers: list) -> tuple:
    """
    Finds the largest and second-largest numbers in a given list.

    This function iterates through the list exactly once, making it 
    highly efficient with an O(N) time complexity. It purely relies on 
    logic and avoids using any built-in sorting or max() functions.

    Args:
        numbers (list): A list of numerical values (can include negative numbers).

    Returns:
        tuple: A tuple containing (largest, second_largest).
    """
    # Setting initial values to negative infinity to handle negative numbers as well
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            # Current largest becomes the second largest
            second_largest = largest
            largest = num
            
        elif num > second_largest and num != largest:
            # Update second largest if the number is between largest and second largest
            second_largest = num
            
    return largest, second_largest


if __name__ == "__main__":
    # Test Data
    numbers_list = [5, 80, 2, 4, 3, 1, 100]
    
    # Function Call
    largest_num, second_largest_num = get_largest_and_second_largest(numbers_list)
    
    # Output
    print(f"Largest Number: {largest_num}")
    print(f"Second Largest Number: {second_largest_num}")