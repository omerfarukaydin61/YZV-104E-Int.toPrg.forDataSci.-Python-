# name: Omer Faruk AYDIN
# id: 150210726

class Matrix:
    def __init__(self, m, n, values=None):  # Take values parameter as None as default
        self.m = m
        self.n = n
        self.values = values
        if self.values == None:  # If values parameter is None
            temp = []
            for i in range(0, self.m):
                try:
                    r = input().split(" ")  # Take inputs row by row for self.values
                    if self.n != len(r):  # If self.n is not equal to length of input, it gives the error message
                        print(f"You must enter n={self.n} number(s) in each row")
                        exit()
                    else:
                        k = [float(z) for z in r]  # Convert to float each element in input
                        temp.append(k)  # and add them to temp
                    self.values = temp
                except (EOFError, ValueError, TypeError,IndexError):  # If user input wrong item, it exits
                    exit()

    def __add__(self, other):  # Function for "+" operator

        if self.m == other.m and self.n == other.n:  # Check the size of matrices
            result = []
            for i in range(0, self.m):
                a = self.values[i]
                b = other.values[i]
                zi_L = zip(a, b)  # Take each element of the matrices to hand
                sum = [x + y for (x, y) in zi_L]  # Sum the elements that in our hand
                result.append(sum)
            m_result = Matrix(self.m, self.n, result)
            return m_result  # Return to matrix object

        else:  # If the size of matrices not equal, return the error message
            return f"Both matrices must have the same dimension." \
                   f"\nFirst: {self.m}x{self.n} Second: {other.m}x{other.n}"

    def __sub__(self, other):  # Function for "-" operator

        if self.m == other.m and self.n == other.n:  # Check the size of matrices
            result = []
            for i in range(0, self.m):
                a = self.values[i]
                b = other.values[i]
                zi_L = zip(a, b)  # Take each element of the matrices to hand
                sum = [x - y for (x, y) in zi_L]  # Subtract the elements that in our hand
                result.append(sum)
            m_result = Matrix(self.m, other.n, result)
            return m_result  # Return to matrix object

        else:  # If the size of matrices not equal, return the error message
            return f"Both matrices must have the same dimension." \
                   f"\nFirst: {self.m}x{self.n} Second: {other.m}x{other.n}"

    def __mul__(self, other):  # Function for "*" operator

        if isinstance(other, float) or isinstance(other, int):  # If the type of other is float or integer
            result = [[i * other for i in lst] for lst in
                      self.values]  # Multiply each element of self.values with other
            m_result = Matrix(self.m, self.n, result)
            return m_result  # Return to matrix object

        elif isinstance(other, Matrix):  # If the type of other is Matrix
            if self.n == other.m:
                result = [[sum(a * b for a, b in zip(row, col))
                           for col in zip(*other.values)] for row in
                          self.values]  # Multiply each element in rows in self.values with
                # each element in rows in other.values
                m_result = Matrix(self.m, other.n, result)
                return m_result  # Return to matrix object
            else:  # If the type of other is not float or integer, return the error message
                return f"Number of columns in first must be equal " \
                       f"to number of rows in second.\nFirst: {self.m}x{self.n} Second: {other.m}x{other.n}"
        else:  # If the type of other is not Matrix, return the error message
            return f"Unsupported operand type(s) " \
                   f"for: '{type(self)}' and '{type(other)}'"

    def transpose(self):
        # Change row and column indexes with each other for each element in self.values
        result = [[self.values[j][i] for j in range(self.m)] for i in range(self.n)]
        m_result = Matrix(self.n, self.m, result)
        return m_result  # Return to matrix object

    def submatrix(self, dm, dn):
        self.dm = dm  # dm is the index of row which will be deleted
        self.dn = dn  # dn is the index of column which will be deleted

        if 0 <= self.dm < self.m and 0 <= self.dn < self.n:  # Row or column numbers should be a non-negative value
            del self.values[self.dm]  # Delete the indexed row
            result = []
            for i in self.values:
                del i[self.dn]  # Delete the elements in indexed columns
                result.append(i)
            m_result = Matrix(self.m - 1, self.n - 1, result)
            return m_result  # Return to matrix object
        else:  # If row or column numbers are not a non-negative value, return the error message
            return f"row and column numbers must be " \
                   f"positive and smaller than dimension: {self.m}x{self.n}"

    def determinant(self):
        if self.m == self.n:  # The Matrix should be square matrix
            det = 0
            if len(self.values) == 2:  # If the matrix is 2 by 2 matrix, apply the simple determinant formula
                det = self.values[0][0] * self.values[1][1] - self.values[0][1] * self.values[1][0]
            else:
                for i in range(len(self.values)):  # If the matrix is not 2 by 2 matrix, go to recursive loop
                    result = self.cof(self.values, 0, i)
                    m_result = Matrix(self.m, self.n, result)
                    det += self.values[0][i] * m_result.determinant() * (-1) ** i
            return det  # Return the value of determinant
        else:
            return f"Matrix must be square for determinant calculation. " \
                   f"Dimensions: {self.m}x{self.n}"

    def cof(self, c_values, cm, cn):  # Cofactor function for recursive loop
        self.c_values = c_values
        self.cm = cm
        self.cn = cn
        result = []

        for i in range(len(self.c_values)):
            if not i == self.cm:
                result.append([])
                for j in range(len(self.c_values)):
                    if not j == self.cn:
                        result[-1].append(self.c_values[i][j])  # Create sub-matrices for cofactors
        return result  # Return the list of matrices for cofactors

    def __repr__(self):  # Function for printing string format

        if self.m <= 0 or self.n <= 0:  # Check the values of dimensions(Are they negative or not)
            return f"Matrix must have a positive dimension: mxn={self.m}x{self.n}"

        if self.values != None:
            if isinstance(self.values, list) or isinstance(self.values, tuple):  # Check the type of self.values
                for i in self.values:
                    if not isinstance(i, list) or isinstance(i, tuple):  # Check the type of each row in self.values
                        return "values parameter must be list of list"
                if self.m == len(self.values):  # Check that is the number of rows in self.values and self.m equal ?
                    for i in self.values:
                        if self.n != len(i):  # If the number of columns in self.values and self.n is not equal, it returns the error message
                            return f"Number of columns in values must be equal to n={self.n} in each row"
                    for i in self.values:
                        if not isinstance(i, list) or isinstance(i, tuple): # Check the type of rows in self.values
                            return "values parameter must be list of list"

                        else:   # If there is no problem for our object, then it returns our matrix in string format
                            z = '\n'.join(
                                [''.join(['{:10.3f}'.format(item) for item in row]) for row in self.values])
                            a = f"Matrix with {self.m}x{self.n} dimension \n{z}"
                            if isinstance(a, str):
                                return a
                            else:
                                break
                else:   # If the number of rows in self.values and self.m is not equal, it returns the error message
                    return f"Number of rows in values must be equal to m={self.m}"
            else:   # If the type of self.values is not list or tuple, it returns the error message
                return "values parameter must be list of list"

    pass

# DO NOT CHANGE BELOW
if __name__ == "__main__":
    try:
        print("Matrix(0, -1)")
        print(Matrix(0, -1))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, -1)")
        print(Matrix(2, 3, -1))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[3, 2])")
        print(Matrix(2, 3, values=[3, 2]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], 3.5])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], 3.5]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], [3.5, -1, 2], [3, 6.5, 8]])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], [3.5, -1, 2], [3, 6.5, 8]]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2]])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2]]))
    except Exception as error:
        print(error)

    m1 = Matrix(4, 2, values=[[1, 2.0], [3, 2], [12, 6], [1, 0]])
    print("m1:", m1)
    m2 = Matrix(2, 4, values=[[1, 25, 4.5, 24.3368], [13.5, 82.2, 76, 13]])
    print("m2:", m2)
    m3 = Matrix(4, 4, values=[[1, 2.0, 3, 7], [3, 4, 5, 2], [9, 12, 15, 18], [1, 0, 1, 0]])
    print("m3:", m3)
    m4 = Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2, 6]])
    print("m4:", m4)
    m5 = Matrix(2, 3, values=[[1, 12.66, 4.7985], [1, 0, 1]])
    print("m5:", m5)

    try:
        print("m1 + m2")
        print(m1 + m2)
    except Exception as error:
        print(error)
    try:
        print("m1 - m2")
        print(m1 - m2)
    except Exception as error:
        print(error)
    try:
        print("m1 * m2")
        print(m1 * m2)
    except Exception as error:
        print(error)
    try:
        print("m1 * 2.5")
        print(m1 * 2.5)
    except Exception as error:
        print(error)
    try:
        print("m1 * \"2.5\"")
        print(m1 * "2.5")
    except Exception as error:
        print(error)
    try:
        print("m1 * m2 + m3")
        print(m1 * m2 + m3)
    except Exception as error:
        print(error)
    try:
        print("m4 + m5")
        print(m4 + m5)
    except Exception as error:
        print(error)
    try:
        print("m4 - m5")
        print(m4 - m5)
    except Exception as error:
        print(error)
    try:
        print("m4 * m5")
        print(m4 * m5)
    except Exception as error:
        print(error)

    print("m1.transpose()")
    print(m1.transpose())

    try:
        print("m1.submatrix(4, 1)")
        print(m1.submatrix(4, 1))
    except Exception as error:
        print(error)
    try:
        print("m1.submatrix(3, 1)")
        print(m1.submatrix(3, 1))
    except Exception as error:
        print(error)
    try:
        print("m2.determinant()")
        print(m2.determinant())
    except Exception as error:
        print(error)
    try:
        print("m3.determinant()")
        print(m3.determinant())
    except Exception as error:
        print(error)

    try:
        m6 = Matrix(4, 2)
        print("m6:", m6)
        m7 = Matrix(2, 4)
        print("m7:", m7)
        m8 = Matrix(4, 4)
        print("m8:", m8)
        m9 = Matrix(2, 3)
        print("m9:", m9)
        m10 = Matrix(2, 3)
        print("m10:", m10)

        try:
            print("m6 + m7")
            print(m6 + m7)
        except Exception as error:
            print(error)
        try:
            print("m6 - m7")
            print(m6 - m7)
        except Exception as error:
            print(error)
        try:
            print("m6 * m7")
            print(m6 * m7)
        except Exception as error:
            print(error)
        try:
            print("m6 * 2.5")
            print(m6 * 2.5)
        except Exception as error:
            print(error)
        try:
            print("m6 * \"2.5\"")
            print(m6 * "2.5")
        except Exception as error:
            print(error)
        try:
            print("m6 * m7 + m8")
            print(m6 * m7 + m8)
        except Exception as error:
            print(error)
        try:
            print("m9 + m10")
            print(m9 + m10)
        except Exception as error:
            print(error)
        try:
            print("m9 - m10")
            print(m9 - m10)
        except Exception as error:
            print(error)
        try:
            print("m9 * m10")
            print(m9 * m10)
        except Exception as error:
            print(error)

        print("m6.transpose()")
        print(m6.transpose())

        try:
            print("m6.submatrix(4, 1)")
            print(m6.submatrix(4, 1))
        except Exception as error:
            print(error)
        try:
            print("m6.submatrix(3, 1)")
            print(m6.submatrix(3, 1))
        except Exception as error:
            print(error)
        try:
            print("m7.determinant()")
            print(m7.determinant())
        except Exception as error:
            print(error)
        try:
            print("m8.determinant()")
            print(m8.determinant())
        except Exception as error:
            print(error)
    except Exception as error:
        print(error)
