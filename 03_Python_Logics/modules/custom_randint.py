"""
Custom Random Integer Generator
-------------------------------
A script that simulates a random integer generator using Python sets.
"""

def custom_random_randint(start: int, end: int) -> int:
    """
    Generates a pseudo-random integer within a given range using Set popping.

    How it works:
    It creates a set of string representations of numbers in the range. 
    Since sets are unordered and strings use hash randomization in Python, 
    popping an element returns an arbitrary item, simulating randomness.

    Note:
        This is a conceptual logic demonstrating Python's string hash 
        randomization. It is memory-intensive for large ranges (O(N) time 
        and space complexity) and is not meant for production use. Python's 
        built-in random.randint() runs in O(1) time and is highly optimized.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.

    Returns:
        int: A pseudo-randomly selected integer from the range.
        
    Raises:
        ValueError: If the start value is greater than the end value or not both of integers.
    """
    if not isinstance(start, int):
        raise ValueError("The starting and end values can only be integers.")
    
    if not isinstance(end, int):
        raise ValueError("The starting and end values can only be integers.")
    
    if start > end:
        raise ValueError("Start value cannot be greater than the end value.")

    
    # Creating a set of strings to utilize Python's string hash randomization
    random_set = {str(num) for num in range(start, end + 1)}
    
    # Popping an arbitrary element and converting it back to integer
    return int(random_set.pop())


if __name__ == "__main__":
    start_val = 4
    end_val = 20
    
    result = custom_random_randint(start_val, end_val)
    print(f"Custom random number between {start_val} and {end_val}: {result}")