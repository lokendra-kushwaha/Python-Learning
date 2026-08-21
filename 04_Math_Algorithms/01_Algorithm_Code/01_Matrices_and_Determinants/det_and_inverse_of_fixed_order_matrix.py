from random import randint

class Matrix:
    """
    A specialized, high-speed Matrix engine designed for fixed-order matrices (specifically 1x1, 2x2, and 3x3).
    It uses hardcoded mathematical formulas for O(1) time complexity, avoiding the overhead of recursion
    or deep loops.
    
    Attributes:
        row (int): The number of rows in the matrix.
        col (int): The number of columns in the matrix.
        matrix (list): A 2D list containing the actual mathematical data.
    """
    def __init__(self, m, n, data=None):
        """
        Initializes the Matrix object.

        If specific data is provided, it creates a matrix with that data. 
        Otherwise, it generates a matrix filled with random numbers between -10 and 10.

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
        Utility function to print the matrix row by row.
        Adds a dashed line at the bottom for clean visual separation in the terminal.

        Returns:
            str: The formatted string representation of the matrix.
        """
        matrix = ''
        for row in self.matrix:
            matrix += str(row) + '\n'
        matrix += '-'*20
        return matrix
    
    def determinant(self):
        """
        Calculates the determinant of 1x1, 2x2, and 3x3 matrices using direct formulas.

        Logic: 
            - Validates if the matrix is square.
            - 1x1 Edge Case: Returns the single element directly.
            - For 2x2: Applies formula (a11*a22) - (a12*a21).
            - For 3x3: Expands along the first row calculating the minor for each element.

        Returns:
            int, float, or str: The determinant value, or an error string if the matrix is not square.
        """
        if self.col != self.row:
            return "Determinant can not be find."
        
        if self.col == 1 and self.row == 1:
            return self.matrix[0][0]
         
        if self.col == 2 and self.row == 2:
            a11, a12 = self.matrix[0][0], self.matrix[0][1]
            a21, a22 = self.matrix[1][0], self.matrix[1][1]

            return (a11 * a22) - (a12 * a21)
        
        if self.col == 3 and self.row == 3:
            a11, a12, a13 = self.matrix[0][0], self.matrix[0][1], self.matrix[0][2]
            a21, a22, a23 = self.matrix[1][0], self.matrix[1][1], self.matrix[1][2]
            a31, a32, a33 = self.matrix[2][0], self.matrix[2][1], self.matrix[2][2]

            i = (a22 * a33) - (a23 * a32)
            j = (a21 * a33) - (a23 * a31)
            k = (a21 * a32) - (a22 * a31)

            return (a11*i - a12*j + a13*k)

    def fraction(self, num, den):
        """
        Helper method to format a fraction as a string.

        Args:
            num (int/float): The numerator.
            den (int/float): The denominator.

        Returns:
            str: A formatted fraction string (e.g., '5/2').
        """
        return   "{}/{}".format(num, den)
    
    def inverseMatrix(self):
        """
        Calculates the Inverse of 1x1, 2x2, and 3x3 matrices using the Adjoint method.

        Step-by-Step Logic:
            1. Square Check: Ensures the matrix is an n x n square.
            2. 1x1 Matrix: Calculates the reciprocal of the single element.
            3. Hardcoded Unpacking: Maps matrix elements to variables for fast O(1) processing.
            4. Determinant Check: If the determinant is 0, it returns a singularity error.
            5. Cofactors & Adjoint: Calculates cofactors and transposes them to form the Adjoint matrix.
            6. Final Inverse: Multiplies every element in adjA by (1 / det) and rounds to 2 decimals.

        Returns:
            Matrix or str: A new Matrix object containing the inversed matrix data, 
                           or an error string if the matrix is singular or non-square.
        """
        if self.col != self.row:
            return "Non-singular of matrix doesn't exist. (Not a square matrix)"
        
        if self.row == 1 and self.col == 1:
            if self.matrix[0][0] == 0:
                return "This is a singular Matrix. (Determinant = 0)"

            inverse_Matrix = [[round(1/self.matrix[0][0], 2)]]
            return Matrix(self.row, self.col, data=inverse_Matrix)
         
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

            inverse_Matrix = [[round(element*1/det, 2) for element in row] for row in adjA]
            # for rows in adjA:
            #     new_row = []
            #     for element in rows:
            #         new_row.append(element*1/det)

            #     inverse_Matrix.append(new_row)
            return Matrix(self.row, self.col, data=inverse_Matrix)
            
        if self.col == 3 and self.row == 3:
            a11, a12, a13 = self.matrix[0][0], self.matrix[0][1], self.matrix[0][2]
            a21, a22, a23 = self.matrix[1][0], self.matrix[1][1], self.matrix[1][2]
            a31, a32, a33 = self.matrix[2][0], self.matrix[2][1], self.matrix[2][2]

            A11, A12, A13 = (a22*a33 - a23*a32), -(a21*a33 - a23*a31), (a21*a32 - a22*a31)
            A21, A22, A23 = -(a12*a33 - a13*a32), (a11*a33 - a13*a31), -(a11*a32 - a12*a31)
            A31, A32, A33 = (a12*a23 - a13*a22), -(a11*a23 - a13*a21), (a11*a22 - a12*a21)

            det = a11*A11 + a12*A12 + a13*A13
            if det == 0:
                print("This is a singular Matrix. (Determinant = 0)")
                return
            
            adjA = [[A11, A21, A31], [A12, A22, A32], [A13, A23, A33]]

            inverse_Matrix = [[round(element*1/det, 2) for element in row] for row in adjA]
            
            return Matrix(self.row, self.col, data=inverse_Matrix)

if __name__ == "__main__":          
    m1 = Matrix(2, 2)
    m2 = Matrix(3, 3)
    print(m1)
    print(m2)
    print('Determinant :', m1.determinant(), '\n')
    print('Determinant :', m2.determinant())

    print("\nInverse of 1st martix - ")
    print(m1.inverseMatrix())

    print("\nInverse of 2nd martix - ")
    print(m2.inverseMatrix())