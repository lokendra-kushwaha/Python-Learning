import sys

def my_print(*args, sep=' ', end='\n'):
    """
    A custom implementation of Python's built-in print() function.

    This function works exactly like the real print(). It takes multiple 
    arguments, joins them with a separator (sep), appends an end character 
    (end) at the last, and then writes directly to the system's standard 
    output (sys.stdout).

    Args:
        *args: All the values or variables that need to be printed.
        sep (str, optional): The string inserted between values. Defaults to a space (' ').
        end (str, optional): The string appended after the last value. Defaults to a newline ('\n').
        
    Returns:
        None: This function does not return anything; it only outputs to the screen.
    """
    # Joining all arguments into a string with the separator
    text = sep.join(str(arg) for arg in args)
    
    # Adding the end character (like a newline) at the end
    text += end

    # Writing directly to the system's output stream
    sys.stdout.write(text)

if __name__ == "__main__":
    l = [1, 2, 3]
    
    # Testing 1: With custom separator and newline
    my_print('lokendra kushwaha', 'kushwaha', sep='***', end='\n')
    
    # Testing 2: With custom separator and no newline
    my_print('lokendra kushwaha', 'kushwaha', sep='***', end='')