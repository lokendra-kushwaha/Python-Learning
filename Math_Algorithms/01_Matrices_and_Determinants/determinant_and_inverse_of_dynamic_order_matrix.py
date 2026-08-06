from random import randint

class Matrix:
    """
    A dynamic Matrix engine to  generate randomly matrices and perform complex linear algebra operations
    like finding the determinant and inverse of matrix using recursion.
    """
    def __init__(self, n, m):
        """
        Initializes the Matrix object with random integers.

        Parameters:
            n (int): Number of columns (based on inner loop).
            m (int): Number of rows (based on outer loop).

        logic: 
            Uses list comprehension to generate an 'm x n' matrix.
            Fills each position with a random integer between 1 and 9.
        """
        self.row = n
        self.col = m
        self.matrix = [[randint(1, 9) for i in range(self.row)] for j in range(self.col)]

    def display_matrix(self):
        """
        Utility function to print the matrix in a clean, readable format.

        Logic:
            Iterates through each row of the matrix and prints it as a list.
            Adds a dashed line at the end to separate multiple outputs visually. 
        """
        for row in self.matrix:
            print(row)
        print('-'*10)

    def get_determinant(self):
        """
        Wrapper (Manager) function to calculate the determinant of the matrix.

        Logic:
            1. Validation: Mathematically, a determinant can only be calculated for a square matrix (where rows == columns). 
               It checks this first.
            2. 1x1 Edge Case: If it's a 1x1 matrix, it directly returns the single element (as the deteminant of a 1x1 matrix is the number itself).
            3. Delegation: If validation passes, it passes the original matrix to the private recursive engine ('recursive_det')
               for calculation.

        Returns:
            int/float: The final determinant value.
            str: Error message if the matrix is not square.
        """
        
        if self.row != self.col:
            return "Determinant only exists for square matrices."
        
        if self.col == 1 and self.row == 1:
            return self.matrix[0][0]

        return self.recursive_det(self.matrix)

    def recursive_det(self, matrix):
        """
        The core Recursive Engine to calculate the determinant of an N x N matrix.

        Parameters:
            matrix (List of Lists): The matrix (or sub-matrix) to be evaluated.

        Step-by_Step Logic Breakdown:
            1. Base Case: If the matrix shrinks down to a 2x2 order, it stops recursion and uses the direct
               formula: (a11 * a22) - (a12 * a21).
            2. Expansion Loop: Iterates through each element of the FIRST row (index j).
            3. Sign Alternation: Calculates the mathematical sign (+, -, +, -) using (-1)**j.
            4. Sub-Matrix Creation (The Slicing Magic): 
               - Skips the first row using 'matrix[1:]'
               - Removes the current column 'j' using list slicing 'row[:j] + row[j+1:]'.
            5. Recursive Call: Multiplies the sign, the element, and the determinant of the newly created sub_matrix (which calls this function again).

        Returns:
            int: The calculated determinant of the passed matrix. 
        """

        if len(matrix) == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        
        ans = 0
        for j in range(len(matrix)):
            element = matrix[0][j]
            sign = (-1)**j

            sub_matrix = []
            for row in matrix[1:]:
                cut_row = row[:j] + row[j+1:]
                sub_matrix.append(cut_row)

            ans += sign * element * self.recursive_det(sub_matrix)

        return ans
    
    def get_inverse_matrix(self):
        """
        Wrapper function to calculate and print the inverse of a matrix.

        This function acts as the manager. It first validates if the matrix is a square matrix.
        To save computational power and avoid deep recursion for simple case, it directly handles the edge cases.
        - 1x1 Matrix: Directly prints the reciprocal of the single element.
        - 2x2 Matrix: Uses the direct formula (Adjoint / Determinant) for O(1) time complexity.

        For matrices of order 3x3  or higher, it delegates the heavy lifting to the recursive 'inverseMatrix' helper function.
        """
        if self.row != self.col:
            print("Non-singular matrix only exists for square matrices.")
            return
        
        if self.row == 1 and self.col == 1:
            for i in self.matrix:
                for j in i:
                    print([1/j])
            return
        
        if self.col == 2 and self.row == 2:
            a11, a12 = self.matrix[0][0], self.matrix[0][1]
            a21, a22 = self.matrix[1][0], self.matrix[1][1]

            det=  (a11 * a22) - (a12 * a21)
            if det == 0:
                print("This is a singular Matrix. (Determinant = 0)")
                return

            A11, A12 = a22, -a21
            A21, A22 = -a12, a11
            adjA = [[A11, A21], [A12, A22]]

            inverse_Matrix = [[element*1/det for element in row] for row in adjA]
            for row in inverse_Matrix:
                print(row)
            return

        return self.inverseMatrix(self.matrix)
    
    def inverseMatrix(self, matrix):
        """
        Recursive engine to find the inverse of an N x N matrix (Order 3 or higher).

        Step-by-Step Logic Breakdown:
        1. Co-factor Calculation: Iterates through every elements of the matrix. Uses Python list slicing
           to eliminate the current row and column, creating a smaller 'sub_matrix'.
        2. Minor & Sign: Calls 'recursive_det' on the sub_matrix to get the minor, and multiplies it by (-1)^(row+col) to get the
           correct co-factor.
        3. Smart Determinant: Instead of recalculating the entire determinant from scratch it dynamically calculates it
           by multiplying the first row's elements with their respective co-factors.
        4. Adjoint Matrix (adjA): Transposes the co-factor matrix (swap rows with columns)
        5. Final Inverse: Multiplies every element of the Adjoint matrix by (1 / determinant) and prints the final rows.

        Returns:
            None (Prints the final inverted matrix rows directly).
        """
        co_factor_matrix = []
        for m, j in enumerate(matrix):
            co_factor_row = []
            for a in range(len(j)):
                sign = (-1)**(m + a)

                sub_matrix = []
                for row in matrix[:m] + matrix[m+1:]:
                    cut_row = row[:a] + row[a+1:]
                    sub_matrix.append(cut_row)

                co_factor_row.append(sign * self.recursive_det(sub_matrix))
            
            co_factor_matrix.append(co_factor_row)
        
        res = 0
        for n, i in enumerate(co_factor_matrix[0]):
            res += i*matrix[0][n]

        det = res
        if det == 0:
            print("This is a singular Matrix. (Determinant = 0)")
            return

        adjA = []
        for j in range(len(co_factor_matrix)):
            new_row = []
            for i in range(len(co_factor_matrix)):
                new_row.append(co_factor_matrix[i][j])

            adjA.append(new_row)

        inverse_Matrix = [[element*1/det for element in row] for row in adjA]
        
        for row in inverse_Matrix:
            print(row)
        return

m1 = Matrix(2, 2)
m1.display_matrix()
print("Determinant of martix - ")
print(m1.get_determinant())


print("\n")
m1 = Matrix(4, 4)
m1.display_matrix()
print("Inverse of martix - ")
m1.get_inverse_matrix()