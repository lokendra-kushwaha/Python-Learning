def two_sum_basic(numbers: list, target: int) -> tuple:
    """
    Finds two numbers in a list that add up to a specific target.
    
    This is the basic approach. It iterates through the list and checks 
    if the required difference exists in the remaining part of the list.
    While it works perfectly, slicing the list and searching within it 
    gives it a time complexity of O(N^2).

    Args:
        numbers (list): A list of integers.
        target (int): The target sum we want to achieve.

    Returns:
        tuple: A tuple containing the two numbers (num1, num2) if found, else None.
    """
    for i in range(len(numbers) - 1):
        x = target - numbers[i]
        # Searching in the remaining list slice
        if x in numbers[i+1:]:
            return numbers[i], x
            
    return None


def two_sum_optimized(numbers: list, target: int) -> tuple:
    """
    Finds two numbers in a list that add up to a specific target optimally.
    
    This is the advanced approach using a Set. Since Python sets use 
    hash tables, checking if the required difference exists takes O(1) 
    average time. This brings the overall time complexity down to O(N), 
    making it extremely fast for large datasets.

    Args:
        numbers (list): A list of integers.
        target (int): The target sum we want to achieve.

    Returns:
        tuple: A tuple containing the two numbers (num1, num2) if found, else None.
    """
    history = set()
    
    for num in numbers:
        x = target - num
        # O(1) lookup time using set hashing
        if x in history:
            return x, num
        
        # Add the current number to history for future lookups
        history.add(num)
        
    return None


if __name__ == "__main__":
    # Testing Basic Approach
    numbers_1 = [5, 80, 2, 100, -30, 4]
    target_1 = 82
    result_1 = two_sum_basic(numbers_1, target_1)
    
    if result_1:
        print(f"Basic Approach: {result_1[0]} + {result_1[1]} = {target_1}")
        
    # Testing Optimized Approach
    numbers_2 = [5, 80, 2, 100, -30, 4, 4]
    target_2 = 102 
    result_2 = two_sum_optimized(numbers_2, target_2)
    
    if result_2:
        print(f"Optimized Approach: {result_2[0]} + {result_2[1]} = {target_2}")