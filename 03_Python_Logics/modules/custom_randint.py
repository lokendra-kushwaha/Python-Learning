"""
Custom Random Integer Generator
-------------------------------
A script that simulates a random integer generator using Python sets.
"""
import time
import os

def random_randint(start: int, end: int) -> int:
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
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("The starting and end values can only be integers.")
    
    if start > end:
        raise ValueError("Start value cannot be greater than the end value.")

    # 1. Creating the Salt: Generating a unique identifier for every process.
    # We are combining the Process ID (PID) and the current time.
    salt = f"{os.getpid()}_{time.time()}"

    # ---------------------------------------------------------
    # ❌ The Old Method - Why it failed in multiprocessing:
    # When 100 processes ran simultaneously, all of them had the exact same 
    # strings (like "5", "6"). Python's hashing algorithm placed these identical 
    # strings in the exact same memory positions across all isolated processes.
    # Therefore, pop() threw out the exact same number 100 times.
    #
    # random_set = {str(num) for num in range(start, end + 1)}
    # return int(random_set.pop())
    # ---------------------------------------------------------

    # ✅ The New Method - Using Salting
    # Here, we attach our unique salt to the end of the number (e.g., "5***1234_17000.55").
    # This makes the string completely unique for every single process, forcing 
    # Python's hashing engine to shuffle them into random, unpredictable positions.
    random_set = {f"{num}***{salt}" for num in range(start, end + 1)}
    
    # Extracting an arbitrary element from the set
    popped_item = random_set.pop()

    # Splitting the string to remove the salt (garbage data) and retrieving the original number
    original_num = popped_item.split("***")[0]
    
    return int(original_num)

if __name__ == "__main__":
    start_val = 4
    end_val = 20
    
    result = random_randint(start_val, end_val)
    print(f"Custom random number between {start_val} and {end_val}: {result}")