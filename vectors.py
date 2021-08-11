from sympy import ImmutableMatrix as Matrix
from sympy.vector import CoordSys3D, matrix_to_vector

import numpy as np
import sympy as sy


m3_1_x = Matrix([-5, 5, -2])
m3_1_y = Matrix([ 2, 2, -5])

C = CoordSys3D('C')
x_3_1 = matrix_to_vector(m3_1_x, C)
y_3_1 = matrix_to_vector(m3_1_y, C)

print("x+y = ", x_3_1 + y_3_1)
print("2x = ", 2*x_3_1)
print("x-y = ", x_3_1 - y_3_1)
print("2x+10y = ", 2*x_3_1 + 10*y_3_1)


x_3_2 = np.array([[-2, 2, 1],
                 [-1, 0, 1],
                 [1, -1, 0]])
y_3_2 = ([18, 9, -7])
print("coefficients of linear combo are: ", np.linalg.solve(x_3_2, y_3_2) )

m_3_2 = sy.Matrix([[-2, 2, 1,18],
                  [-1, 0, 1, 9],
                  [1, -1, 0, -7]])

print(m_3_2.rref(pivots=True))

m_3_3 = sy.Matrix([[-1,  1, -1,  13],
                   [ 1,  0,  1,  -8],
                   [ 1, -1,  2, -16]])

print(m_3_3.rref(pivots=True))

m_3_4 = sy.Matrix([[ 5,  5,  0,  -2],
                   [ 1, -1, -2,   3],
                   [-1, -1,  3,  -1]])

print(m_3_4.rref(pivots=True))

m_3_5 = sy.Matrix([[ 3,  1, -5,   26],
                   [ 2,  4,  1,    9]])

print(m_3_5.rref(pivots=True))


m_3_6 = sy.Matrix([[ 0,   0,  1,   -5], #note each column is a vector
                   [ -1,  2, -3,   12],
                   [ -1,  1, -2,   11]])

print(m_3_6.rref(pivots=True))

m_3_7 = sy.Matrix([[ -5,  5, -10,  -30],
                   [ -4,  2,  -6,  -16],
                   [  1,  0,   2,    3]])

print(m_3_7.rref(pivots=True))

m3_8_u = Matrix([ 6, -2,  9]) # this is one vector as a 1 x 3 matrix
m3_8_v = Matrix([ 6,  3,  1])
m3_8_w = Matrix([ 1, -3,  1])

C = CoordSys3D('C')
x_8_u = matrix_to_vector(m3_8_u, C)
x_8_v = matrix_to_vector(m3_8_v, C)
x_8_w = matrix_to_vector(m3_8_w, C)

print("2u+3v-9w = ", 2*x_8_u + 3*x_8_v - 9*x_8_w)


m_3_9 = sy.Matrix([[  -2,   2, -6,  0],
                    [ -1,  -5,  9,  0]])

print(m_3_9.rref(pivots=True))


m_3_10 = sy.Matrix([[  9,  -6,  0,  0],
                    [  9, -10,  2,  0],
                    [ -6,  -8,  6,  0]])

print(m_3_10.rref(pivots=True))

m_3_13_1 = sy.Matrix([[  4,  -2,  8, -10, -5, 0],
                      [ -9,   5, -9,  -4,  5, 0],
                      [ -5,  -1,  7,  -4,  9, 0],
                      [ 10,   9, -8,   1, -7, 0]])

print(m_3_13_1.rref(pivots=True))

m_3_13_2 = sy.Matrix([[  4,   8, 0],
                      [  4,   8, 0],
                      [  2,   4, 0],
                      [  5,   10, 0]])

print(m_3_13_2.rref(pivots=True))

k = sy.symbols('k')
m_3_14 = sy.Matrix([ [ -1,    1,      3, 0],
                     [ -2,   -2,     -5, 0],
                     [ -5,  -15 + k, -7, 0]])

print(m_3_14.rref(pivots=True))


m_4_2 = sy.Matrix([[-2,  2,  3, -9],
                   [-1,  0,  0, -1],
                   [ 1, -1, -1,  5]])

print(m_4_2.rref(pivots=True)) #coefficients of linear combo are in last column


m_4_3 = sy.Matrix([[-1,  5,  1, -5],
                   [-4, -1, -2, -5],
                   [ 1, -4,  2,  2]])

print(m_4_3.rref(pivots=True)) #coefficients of linear combo are in last column

m_4_4 = sy.Matrix([[ 2,  2,  8],
                   [-1, -2, -9],
                   [ 1,  1,  4]])

print(m_4_4.rref(pivots=True)) #coefficients of linear combo are in last column

m_4_5 = sy.Matrix([[-2, -2,  3, -6],
                   [ 1,  0,  0, -5],
                   [ 1,  1, -1,  2]])

print(m_4_5.rref(pivots=True)) #coefficients of linear combo are in last column

m_4_6 = sy.Matrix([[ 1,  1, -3, 0],
                   [ 2, -1, -3, 3],
                   [-4, -5, 13, 18]])

print(m_4_6.rref(pivots=True)) #coefficients of linear combo are in last column


m4_7_x = Matrix([4, -2, 0])
m4_7_y = Matrix([-5, 1, 5])

C = CoordSys3D('C')
x4_7 = matrix_to_vector(m4_7_x, C)
y4_7 = matrix_to_vector(m4_7_y, C)

print("3x = ", 3*x4_7 )
print("x+y = ", x4_7+y4_7)
print("3x+y = ", 3*x4_7 + y4_7)

m_4_8 = sy.Matrix([[ -1, -1, -2],
                   [ -2,  1, -1],
                   [  3,  5,  8]])

print(m_4_8.rref(pivots=True)) #coefficients of linear combo are in last column

m_4_10 = sy.Matrix([[ -16,  16, -5,  -2],
                    [ -9,  -19, -10, -18],
                    [  4,   12, -16,  12],
                    [-11,   -7, -15,  -4]])

print(m_4_10.rref(pivots=True)) #check pivots

m_4_10_w = sy.Matrix([[ -16,  16, -5, -11],
                      [ -9,  -19, -10, -27],
                      [  4,   12, -16,  36],
                      [-11,   -7, -15, -14]])

print(m_4_10_w.rref(pivots=True)) #check pivots

m_4_11 = sy.Matrix([[ -15,  0, 15, 0], #added 0s to check independence
                    [ -10, -8,  2, 0],
                    [  14, 31, 17, 0]])

print(m_4_11.rref(pivots=True)) #coefficients of linear combo are in last column


m_4_12 = sy.Matrix([[   4, -4,  8, 0], #added 0s to check independence
                    [  12,  3, 15, 0],
                    [   9,  6,  9, 0]])

print(m_4_12.rref(pivots=True)) #coefficients of linear combo are in last column


m_4_13 = sy.Matrix([[  1,    k,  0], #added 0s to check independence
                    [  k, 6*k+7, 0]])

print(m_4_13.rref(pivots=True)) #coefficients of linear combo are in last column

m_4_14 = sy.Matrix([  [  4,  -3,  1, -5, 0],
                      [  5,  -1, -3,  2, 0],
                      [ -3,  -4,  5, -3, 0],
                      [ -5,  -2,  2,  1, 0]])

print(m_4_14.rref(pivots=True)) #check pivots

m_4_15 = sy.Matrix([[  -1,  2,    -1, 0], #added 0s to check independence
                    [  -5, -12+k, -3, 0],
                    [  -3, -2,    -1, 0]])

print(m_4_15.rref(pivots=True)) #coefficients of linear combo are in last column


