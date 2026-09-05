from random import randint

class Matrix:
    """
    A class used to represent and perform mathematical operations on a 2D Matrix.
    
    Attributes:
        col (int): The number of columns in the matrix.
        row (int): The number of rows in the matrix.
        matrix (list): A 2D list containing the actual mathematical data of the matrix.
    """

    def __init__(self, row, col, data=None):
        """
        Initializes the Matrix object.
        
        If specific data is provided, it creates a matrix with that data. 
        Otherwise, it generates a random matrix with values ranging from -10 to 10.

        Args:
            n (int): The number of columns.
            m (int): The number of rows.
            data (list, optional): A predefined 2D list to initialize the matrix. Defaults to None.
        """
        self.row = row
        self.col = col
        
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("Error")

            if len(data) > 0 and isinstance(data[0], list):
                if len(data) != self.row or any(len(r) != self.col for r in data):
                    raise ValueError('error')
                self.matrix = data

            else:
                if (len(data) % self.row != 0) or (self.row * self.col != len(data)):
                                raise ValueError('Error')

                matrix = []
                i = 0
                while i < self.row:
                    split = data[i*self.col : self.col + self.col*i]
                    matrix.append(split)
                    i = i + 1
                    
                self.matrix = matrix

        else:
            self.matrix = [[randint(-10, 10) for i in range(self.col)] for i in range(self.row)]

    def __str__(self):
        """
        Returns a string representation of the matrix for easy printing and readability.
        
        Returns:
            str: The matrix formatted row by row with a separator line at the end.
        """
        matrix = ''
        for row in self.matrix:
            matrix += str(row) + '\n'
        matrix += '-'*10
        return matrix

    def __add__(self, other):
        """
        Performs matrix addition. 
        Both matrices must have the exact same dimensions (order).

        Args:
            other (Matrix): The matrix to be added to the current matrix.

        Returns:
            Matrix or str: A new Matrix object containing the sum, or an error message if dimensions do not match.
        """
        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        sum_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sum_val = self.matrix[i][j] + other.matrix[i][j]
                new_row.append(sum_val)
        
            sum_matrices.append(new_row)

        return Matrix(self.row, self.col, data=sum_matrices)

    def __sub__(self, other):
        """
        Performs matrix subtraction.
        Both matrices must have the exact same dimensions (order).

        Args:
            other (Matrix): The matrix to be subtracted from the current matrix.

        Returns:
            Matrix or str: A new Matrix object containing the difference, or an error message if dimensions do not match.
        """
        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        sub_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sub_val = self.matrix[i][j] - other.matrix[i][j]
                new_row.append(sub_val)
        
            sub_matrices.append(new_row)

        return Matrix(self.row, self.col, data=sub_matrices)

    def __mul__(self, other):

        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        mul_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sum_val = self.matrix[i][j] * other.matrix[i][j]
                new_row.append(sum_val)
        
            mul_matrices.append(new_row)

        return Matrix(self.row, self.col, data=mul_matrices)

    def __truediv__(self, other):

        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        div_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sum_val = self.matrix[i][j] / other.matrix[i][j]
                new_row.append(sum_val)
        
            div_matrices.append(new_row)

        return Matrix(self.row, self.col, data=div_matrices)
    
    def add(self, other):
        """
        Performs matrix addition. 
        Both matrices must have the exact same dimensions (order).

        Args:
            other (Matrix): The matrix to be added to the current matrix.

        Returns:
            Matrix or str: A new Matrix object containing the sum, or an error message if dimensions do not match.
        """
        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        sum_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sum_val = self.matrix[i][j] + other.matrix[i][j]
                new_row.append(sum_val)
        
            sum_matrices.append(new_row)

        return Matrix(self.row, self.col, data=sum_matrices)
    
    def sub(self, other):
        """
        Performs matrix subtraction.
        Both matrices must have the exact same dimensions (order).

        Args:
            other (Matrix): The matrix to be subtracted from the current matrix.

        Returns:
            Matrix or str: A new Matrix object containing the difference, or an error message if dimensions do not match.
        """
        if self.col != other.col or self.row != other.row:
            return "Order must be the same!."

        sub_matrices = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                sub_val = self.matrix[i][j] - other.matrix[i][j]
                new_row.append(sub_val)
        
            sub_matrices.append(new_row)

        return Matrix(self.row, self.col, data=sub_matrices)
    
    def multiply(self, other):
        """
        Performs matrix multiplication (dot product).
        The number of columns in the first matrix must equal the number of rows in the second matrix.

        Args:
            other (Matrix): The matrix to multiply with.

        Returns:
            Matrix or str: A new Matrix object containing the product, or an error message if multiplication is invalid.
        """
        if self.col != other.row:
            return "Multiplication not possible."
        
        result_matrix = []
        for i in range(self.row):
            new_row = []
            for j in range(other.col):
                total_sum = 0
                for k in range(self.col):
                    mul = self.matrix[i][k] * other.matrix[k][j]
                    total_sum += mul

                new_row.append(total_sum)

            result_matrix.append(new_row)

        return Matrix(self.row, other.col, data=result_matrix)
    
    def scalorMultiply(self, integer):
        """
        Multiplies every element in the matrix by a given scalar (integer or float) value.

        Args:
            integer (int or float): The scalar value to multiply the matrix by.

        Returns:
            Matrix: A new Matrix object with the scaled values.
        """
        new_matrix = []
        for i in range(self.row):
            new_row = []
            for j in range(self.col):
                mul = integer*self.matrix[i][j]
                
                new_row.append(mul)

            new_matrix.append(new_row)

        return Matrix(self.row, self.col, data=new_matrix)
    
    def transpose(self):
        """
        Calculates the transpose of the matrix by swapping its rows and columns.

        Returns:
            Matrix: A new Matrix object that is the transpose of the original matrix.
        """
        transposed_matrix = []
        for j in range(self.col):
            new_row = []
            for i in range(self.row):
                new_row.append(self.matrix[i][j])

            transposed_matrix.append(new_row)

        return Matrix(self.col, self.row, data=transposed_matrix)
    
    def isSymmetric(self):
        """
        Checks if the matrix is Symmetric. 
        A matrix is symmetric if it is a square matrix and equals its own transpose.
        """
        if self.col != self.row:
            print("This is not a symmetric matrix. (Not a square matrix)")
            return

        if self.transpose().matrix == self.matrix:
            print("This is a Symmetric Matrix.")

        else:
            print("This is not a Symmetric Matrix.")

    def isSkewSymmetric(self):
        """
        Checks if the matrix is Skew-Symmetric.
        A matrix is skew-symmetric if it is a square matrix and its transpose equals its negative.
        """
        if self.col != self.row:
            print("This is not a Skew-Symmetric Matrix. (Not a square matrix)")
            return

        if  self.scalorMultiply(-1).matrix == self.transpose().matrix:
            print("This is a Skew-Symmetric Matrix.")

        else:
            print("This is not a Skew-Symmetric Matrix.")

if __name__ == "__main__":      
    m1 = Matrix(2, 2)
    m2 = Matrix(2, 2)
    print(m1)
    print(m2)

    print("Addition of matrices -->")
    print(m1.add(m2))

    print("Substraction of matrices -->")
    print(m1.sub(m2))

    print("Multiplication of matrices -->")
    print(m1.multiply(m2))

    print("Scalor multiplication of matrix -->")
    print(m1.scalorMultiply(4))

    print("Transpose of metrix -->")
    print(m1.transpose())

    m1.isSymmetric()

    m3 = Matrix(2, 2)
    m3.isSkewSymmetric()

    print(m1 - m2)
    print(m1 + m2)
    print(m1 * m2)
    print(m1 / m2)