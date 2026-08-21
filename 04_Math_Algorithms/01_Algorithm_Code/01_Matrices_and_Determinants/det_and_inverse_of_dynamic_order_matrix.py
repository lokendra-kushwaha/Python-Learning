from random import randint

class Matrix:
    """
    A dynamic Matrix engine to generate random matrices and perform complex linear algebra operations
    like finding the determinant and inverse of an N x N matrix using recursion.
    
    Attributes:
        row (int): The number of rows in the matrix.
        col (int): The number of columns in the matrix.
        matrix (list): A 2D list containing the actual mathematical data.
    """
    def __init__(self, m, n, data=None):
        """
        Initializes the Matrix object.

        If specific data is provided, it creates a matrix with that data. 
        Otherwise, it generates an 'm x n' matrix filled with random integers between -10 and 10.

        Args:
            m (int): Number of rows (outer list length).
            n (int): Number of columns (inner list length).
            data (list, optional): A predefined 2D list to initialize the matrix. Defaults to None.
        """
        self.row = m
        self.col = n
        
        if data is not None:
            self.matrix = data

        else:
            self.matrix = [[randint(-10, 10) for i in range(self.col)] for j in range(self.row)]

    def __str__(self):
        """
        Utility function to print the matrix in a clean, readable format.

        Returns:
            str: The matrix formatted row by row with a dashed separator line at the end.
        """
        matrix = ''
        for row in self.matrix:
            matrix += str(row) + '\n'
        matrix += '-'*20
        return matrix

    def get_determinant(self):
        """
        Wrapper (Manager) function to calculate the determinant of the matrix.

        Logic:
            1. Validation: Checks if the matrix is square (rows == columns).
            2. 1x1 Edge Case: Returns the single element directly.
            3. Delegation: Passes the matrix to the private recursive engine ('recursive_det') for N x N calculation.

        Returns:
            int, float, or str: The final determinant value, or an error message if the matrix is not square.
        """
        
        if self.row != self.col:
            return "Determinant only exists for square matrices."
        
        if self.col == 1 and self.row == 1:
            return self.matrix[0][0]

        return self.recursive_det(self.matrix)

    def recursive_det(self, matrix):
        """
        The core Recursive Engine to calculate the determinant of an N x N matrix.

        Step-by-Step Logic Breakdown:
            1. Base Case: If the matrix shrinks to 2x2, it applies the direct formula: (a11 * a22) - (a12 * a21).
            2. Expansion Loop: Iterates through each element of the FIRST row (index j).
            3. Sign Alternation: Calculates the mathematical sign (+, -, +, -) using (-1)**j.
            4. Sub-Matrix Creation: Creates a minor by skipping the first row and removing the current column 'j'.
            5. Recursive Call: Multiplies the sign, element, and the recursive determinant of the sub-matrix.

        Args:
            matrix (list): A 2D list representing the matrix (or sub-matrix) to be evaluated.

        Returns:
            int/float: The calculated determinant of the passed matrix. 
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
        Wrapper function to calculate the inverse of a matrix.

        Logic:
            - Validates if the matrix is a square matrix.
            - Handles 1x1 and 2x2 edge cases directly for O(1) time complexity.
            - For matrices of order 3x3 or higher, it delegates the heavy lifting to the recursive 'inverseMatrix' helper function.

        Returns:
            Matrix or str: A new Matrix object containing the inverted data, or an error string if singular/non-square.
        """
        if self.row != self.col:
            return "Non-singular matrix only exists for square matrices."
        
        if self.row == 1 and self.col == 1:
            if self.matrix[0][0] == 0:
                return "This is a Singular Matrix. (Deteminant = 0)"
            
            matrix = [[round(1/self.matrix[0][0], 2)]]
            return Matrix(self.row, self.col, data=matrix)
        
        if self.col == 2 and self.row == 2:
            a11, a12 = self.matrix[0][0], self.matrix[0][1]
            a21, a22 = self.matrix[1][0], self.matrix[1][1]

            det=  (a11 * a22) - (a12 * a21)
            if det == 0:
                return "This is a singular Matrix. (Determinant = 0)"
                

            A11, A12 = a22, -a21
            A21, A22 = -a12, a11
            adjA = [[A11, A21], [A12, A22]]

            inverse_Matrix = [[round(element*1/det, 2) for element in row] for row in adjA]

            return Matrix(self.row, self.col, data=inverse_Matrix)

        return Matrix(self.row, self.col, data=self.inverseMatrix(self.matrix))
    
    def inverseMatrix(self, matrix):
        """
        Recursive engine to find the inverse of an N x N matrix (Order 3 or higher).

        Step-by-Step Logic Breakdown:
            1. Co-factor Calculation: Iterates through every element, creating a sub-matrix by eliminating the current row and column.
            2. Minor & Sign: Calls 'recursive_det' on the sub-matrix and applies (-1)^(row+col) to get the co-factor.
            3. Smart Determinant: Dynamically calculates the determinant using the first row's elements and their co-factors.
            4. Adjoint Matrix: Transposes the co-factor matrix (swaps rows with columns).
            5. Final Inverse: Multiplies every element of the Adjoint matrix by (1 / determinant).

        Args:
            matrix (list): A 2D list representing the matrix to be inverted.

        Returns:
            list or None: A 2D list representing the inverted matrix data, or None if the determinant is 0.
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

        inverse_Matrix = [[round(element*1/det, 2) for element in row] for row in adjA]

        return inverse_Matrix

if __name__ == "__main__":
    m1 = Matrix(2, 2)
    print(m1)
    print("Determinant of martix - ")
    print(m1.get_determinant())

    print("\n")
    m1 = Matrix(4, 4)
    print(m1)
    print("Inverse of martix - ")
    print(m1.get_inverse_matrix())