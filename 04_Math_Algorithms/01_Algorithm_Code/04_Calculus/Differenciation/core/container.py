"""
Legacy Expression Container Module.

This module contains an older, list-based approach to managing mathematical 
expressions. While the newer Abstract Syntax Tree (AST) approach directly 
handles operations, this container class groups multiple independent terms 
together and derives them iteratively. 

It is preserved for historical context and alternative logic implementation.
"""

def clean_output_string(raw_string):
    """
    Cleans up formatting artifacts from the generated mathematical string.

    Args:
        raw_string (str): The unformatted mathematical expression string.

    Returns:
        str: The cleaned string with proper mathematical signs.
    """
    # Fixes instances where adding a negative term creates '+ -'
    fixed_signs = raw_string.replace('+ -', '- ')
    
    # Removes redundant '+ 0' artifacts from the output
    final_string = fixed_signs.replace(' + 0', '')

    return final_string


class Expression:
    """
    A container class representing a mathematical expression as a collection of terms.
    
    Instead of building a strict binary tree of operations, this class takes 
    multiple mathematical nodes (terms) and treats them as a single polynomial-style 
    equation linked by addition.

    Attributes:
        terms (tuple): A collection of MathNode objects representing individual terms.
    """
    
    def __init__(self, *terms):
        """
        Initializes the Expression container.

        Args:
            *terms (MathNode): An arbitrary number of mathematical terms unpacked as a tuple.
        """
        self.terms = terms

    def __repr__(self):
        """
        Returns the string representation of the full expression.
        Iterates through all terms, joins them with addition signs, and 
        cleans up the final formatting.
        """
        formatted_string = ''
        
        for term in self.terms:
            # Append each term with a plus sign, adjusting for negative terms dynamically
            formatted_string += f' + {str(term)}'.replace('+ -', '- ')
        
        # Strip the leading ' + ' if it exists at the very beginning of the string
        if formatted_string.startswith(' + '):
            formatted_string = formatted_string[3:]
            
        return clean_output_string(formatted_string)
    
    def derive(self):
        """
        Calculates the derivative of the entire expression iteratively.
        
        Calculus Rule:
            The derivative of a sum of terms is the sum of their individual derivatives.
            $d/dx [f(x) + g(x) + ...] = f'(x) + g'(x) + ...$

        Returns:
            Expression: A new Expression container holding all the derived terms.
        """
        derived_terms = []
        
        for term in self.terms:
            derived_term = term.derive()
            derived_terms.append(derived_term)

        # Unpack the list back into arguments using the '*' operator
        return Expression(*derived_terms)