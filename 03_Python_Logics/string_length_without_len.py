def calculate_length(string):
    """
    Calculates the length of a string without using Python's built-in len() function.

    Logic:
        Initializes a counter variable to 0. A for loop iterates through the string 
        character by character, incrementing the counter by 1 for every iteration.

    Args:
        string (str): A standard string whose length needs to be calculated.

    Returns:
        int: The total length (number of characters) of the string.
    """
    string_length = 0
    for char in string:
        string_length += 1
        
    return string_length

if __name__ == "__main__":

    # Testing calculate_length function
    text2 = 'Lokendra Kushwaha'
    print(f"Length of '{text2}':", calculate_length(text2))