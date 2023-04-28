import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h == 1:
            det = self.g[0]
        elif self.h == 2:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[1][0]
            d = self.g[1][1]
            
            det = a*d-b*c
        elif self.h == 3:
            a = self.g[0][0]
            b = self.g[0][1]
            c = self.g[0][2]
            d = self.g[1][0]
            e = self.g[1][1]
            f = self.g[1][2]
            g = self.g[2][0]
            h = self.g[2][1]
            i = self.g[2][2]
            
            det = a*(e*i-f*h)-b*(d*i-f*g)+c(d*h-e*g)
            
        return det

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace = 0
        
        for i in range(self.h):
            for j in range(self.w):
                if i == j:
                    trace += self.g[i][j]
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        
   
        inverse = []
    
        if len(self) == 1:
            inverse.append([1 / self.g[0][0]])
        elif len(self) == 2:
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]
            
                factor = 1 / (a * d - b * c)
            
                inverse = [[d, -b],[-c, a]]
            
                for i in range(len(inverse)):
                    for j in range(len(inverse[0])):
                        inverse[i][j] = factor * inverse[i][j]
    
        return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        # Loop through columns on outside loop
        for c in range(self.w):
            new_row = []
            # Loop through columns on inner loop
            for r in range(self.h):
                # Column values will be filled by what were each row before
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return matrix_transpose

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
                           
        matrixSum = []
    
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self[i][j] + other[i][j])
            matrixSum.append(row)
    
        return matrixSum

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
                           
        negated = []
                           
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(-1*self.g[i][j])
            negated.append(row)
                           
        return negated
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
                           
        matrixDiff = []
    
        for i in range(self.h):
            row = []
            for j in range(self.w):
                row.append(self.g[i][j] - other.g[i][j])
            matrixDiff.append(row)
    
        return matrixDiff

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
                        
        def dot_product(vector_one, vector_two):
            dot = 0
            for i in range(len(vector_one)):
                dot += vector_one[i]*vector_two[i]
            return dot

        def get_column(matrix, column_number):
            column = []
            for i in range(len(matrix)):
                column.append(matrix[i][column_number])
            return column
    
        def get_row(matrix, row):
            return matrix[row]
                               
        m_rows = len(matrixA)
        p_columns = len(matrixB[0])
        
        result = []
    
        for i in range(m_rows):
            row_result = []
            row_vector = get_row(matrixA, i)
            for j in range(p_columns):
                column_vector = get_column(matrixB, j)
                row_result.append(dot_product(row_vector, column_vector))
            result.append(row_result)
            
        return result
                           
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):        
            reg = []
            for i in range(self.h):
                for j in range(self.w):
                    reg[i][j] = self.g[i][j]*other
            return reg