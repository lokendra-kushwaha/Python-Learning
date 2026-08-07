from random import randint

class Matrix:
    """
    A specialized, high-speed Matrix engine designed for fixed-order matrices (specifically 2x2 and 3x3).
    It uses hardcoded mathematical formulas for $O(1)$ time complexity, avoiding the overhead of recursion
    or deep loops.
    """
    def __init__(self, n, m):
        """
        Initializes the Matrix object with random integers.

        Parameters:
            n (int): Number of columns (inner list length).
            m (int): Number of rows (outer list length).

        Logic:
            Generates a matrix filled with random numbers between 1 and 9.
            (Note: Based on the first comprehension, this creates a matrix with 'm' rows and 'n' columnc).
        """
        self.row = n
        self.col = m
        self.matrix = [[randint(1, 9) for i in range(self.col)] for j in range(self.row)]

    def display_matrix(self):
        """
        Utility function to print the matrix row by row.
        Adds a dashed line at the bottom for clean visual separation in the terminal.
        """
        for row in self.matrix:
            print(row)
        print('-'*10)

    def determinant(self):
        """
        Calculates the determinant of 2x2 and 3x3 matrices using direct formulas.

        Logic: 
            - Validates if the matrix is square.
            - 1x1 Edge Case: If it's a 1x1 matrix, it directly returns the single element (as the deteminant of a 1x1 matrix is the number itself).
            - For 2x2: Applies (a11*a22) - (a12*a21).
            - For 3x3: Expands along the first row. Calculates the minor for each element (i, j, k) and
              applies formula: a11(i) - a12(j) + a13(k)

        Returns:
            int/float: The determinant value. or an error string if not square.
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
        Helper method to format a fraction as a string (e.g., '5/2')
        Can be used to display exact fractional values of an inverse matrix.
        """
        return   "{}/{}".format(num, den)
    
    def inverseMatrix(self):
        """
        Calculates and prints the Inverse of 2x2 and 3x3 matrices using the Adjoint method.

        Step-by-Step Logic:
            1. Square Check: Ensures the matrix is an n x n square.
            2. 1x1 Matrix: Directly prints the reciprocal of the single element.
            3. Hardcoded Unpacking: Maps matrix elements to variables (a11, a12, etc.) for extremely fast processing.
            4. Determinant & Singularity Check: If determinant is 0, the matrix is singular (inverse doesn't exist).
            5. Cofactors & Adjoint: Calculates cofactors (A11, A12.....) and arranges them directly in transposed order to form the Adjoint matrix (adjA).
            6. Final Inverse: Multiplies every elementin adjA by (1 / det) and prints the result.

        Returns:
            None (Prints thefinal inversed matrix or an error message.)

        """
        if self.col != self.row:
            return "Non-singular of matrix doesn't exist. (Not a square matrix)"
        
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
            # for rows in adjA:
            #     new_row = []
            #     for element in rows:
            #         new_row.append(element*1/det)

            #     inverse_Matrix.append(new_row)

            for row in inverse_Matrix:
                print(row)
            return
            
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

            inverse_Matrix = [[element*1/det for element in row] for row in adjA]

            for row in inverse_Matrix:
                print(row)
            return
            
m1 = Matrix(2, 2)
m2 = Matrix(3, 3)
m1.display_matrix()
m2.display_matrix()
print('Determinant :', m1.determinant(), '\n')
print('Determinant :', m2.determinant())

print("\nInverse of 1st martix - ")
m1.inverseMatrix()

print("\nInverse of 2nd martix - ")
m2.inverseMatrix()