import sympy as sy
#from sympy import *

from sympy.solvers.solveset import linsolve
from sympy.core.symbol import symbols
from sympy.solvers.solveset import nonlinsolve



m2_1 = sy.Matrix([ [ 1,  0,  0, -1, 0],
                 [-1,  0, -2,  0, 0],
                 [ 0, -1,  0,  0, -3],
                 [ 0,  0,  0, -2, 1],
                 [ 0, -3,  1,  0, 0] ])

print("determinant of M: ", m2_1.det())

a = sy.symbols('a')
m2_2 = sy.Matrix([ [ a,  5,  9],
                 [ a, -1,  4],
                 [ 9, -7,  a] ])

print("det A = ",m2_2.det())
print("a = ", solve(-6*a**2 - 35*a + 261, a))


m2_3 = sy.Matrix([ [-3,  5, -8],
                 [ 8, -5,  1],
                 [ 5,  1,  5] ])
cf = m2_3.cofactor_matrix()
print("cofactor matrix: ",cf)

def minor_matrix(m):
    r , c = m.shape
    new_m = []

    for i in range(r):
        for j in range(c):
            new_m.append(m.minor(i,j))
    return Matrix(r, c, new_m)

print("Minors: ",minor_matrix(m2_3))

m2_4 = sy.Matrix([ [-4,  9, -5],
                   [-9,  7,  5],
                   [ 9,  7, -6] ])

print(m2_4.det())
print(m2_4.inv())

m2_5 = sy.Matrix([ [-5, -5,   4],
                   [ 4,  5,  -5],
                   [ 1,  1,  -1] ])

print(m2_5.inv())

m2_5b = sy.Matrix([ [-2],
                    [ 4],
                    [ 5] ])

print("x is:", m2_5.inv() * m2_5b)

m2_6_A = sy.Matrix([ [ 4, -12, -37],
                     [-2,   7,  20],
                     [ 1,  -3,  -9] ])

m2_6_B = sy.Matrix([ [-4,  12,  25],
                     [ 2,  -7, -15],
                     [ 1,  -3,  -6] ])

m2_6_C = sy.Matrix([ [ 4, -12,  -37,  0,  0,   0],
                     [-2,   7,   20,  0,  0,   0],
                     [ 1,  -3,   -9,  0,  0,   0],
                     [ 0,   0,    0, -4, 12,  25],
                     [ 0,   0,    0,  2, -7, -15],
                     [ 0,   0,    0,  1, -3,  -6] ])

print("m2_6_A inv:", m2_6_A.inv())
print("m2_6_B inv:", m2_6_B.inv())
print("m2_6_C inv:", m2_6_C.inv())

m2_8_A = sy.Matrix([ [ 2, -4,  1],
                     [-1,  1, -1],
                     [ 1, -2,  0] ])

m2_8_B = sy.Matrix([ [3],
                     [0],
                     [3] ])

print("2_8 X is:", m2_8_A.inv() * m2_8_B)


m2_9_A = sy.Matrix([ [ 1, -2, -5],
                     [-4, -2,  4],
                     [ 3,  2, -5] ])

print("A+A.T: ",m2_9_A + m2_9_A.transpose())
print("A-A.T: ",m2_9_A - m2_9_A.transpose())

m2_10_A = sy.Matrix([ [ -4, -5, -8, -9] ])

m2_10_B = sy.Matrix([ [ 5],
                      [-5],
                      [-2],
                      [ 9] ])

print("B*A= ", m2_10_B*m2_10_A)

m2_11_A = sy.Matrix([ [ 6,  4, -3],
                      [-6, -9, -7],
                      [ 2, -6, -4] ])

m2_11_B = sy.Matrix([ [-3, -1, -1],
                      [ 6,  5, -1],
                      [ 4, -3,  0] ])

print("6A = ", 6*m2_11_A)
print("A-7B = ", m2_11_A-(7*m2_11_B))
print("-3A-3B = ", (-3*m2_11_A)-(3*m2_11_B))


m2_12_A = sy.Matrix([ [ 2,  4,  6],
                      [ 2,  4, -2] ])

m2_12_B = sy.Matrix([ [-3,  4,  7],
                      [-4,  1,  3] ])

print(" (-2B - A ) / 3 = ",((-2*m2_12_B)-m2_12_A)/3)

m2_16_A = sy.Matrix([ [-1,  3,  5],
                      [ 1,  8, -6],
                      [-6,  2, -6] ])
print("det(A): ", m2_16_A.det())

m2_18_B = sy.Matrix([ [ 1,  0,  1],
                      [ 2,  2, -1],
                      [ 2, -2, -1] ])
print("det(B^5): ", (m2_18_B**5).det())


a, b, c, d, e, f = sy.symbols('a, b, c, d, e, f')
m2_21_A = sy.Matrix([ [ a,  1,  d],
                      [ b,  1,  e],
                      [ c,  1,  f] ])

m2_21_B = sy.Matrix([ [ a,  1,  d],
                      [ b,  2,  e],
                      [ c,  3,  f] ])
print("det m2_21_A:", m2_21_A.det())
print("det m2_21_B:", m2_21_B.det())


x1, x2, z1, z2 = sy.symbols('x1, x2, z1, z2')
m2_25_A = sy.Matrix([ [ x1, x2],
                      [ z1, z2] ])
m2_25_B = sy.Matrix([ [ 9*x1 + 5*z1, 9*x2 + 5*z2],
                      [ 8*x1 + 4*z1, 8*x2 + 4*z2] ])
print("det(A): ", m2_25_A.det())
print("det(B): ", m2_25_B.det())


m2_27_A = sy.Matrix([ [-3,  7,  0,  1],
                      [ 8, -7,  0,  0],
                      [ 0, -8,  0,  0],
                      [ 3, -8,  6,  4] ])
print("det(A): ", m2_27_A.det())

m2_28_A = sy.Matrix([ [ 0, -4, -7,  0, 0],
                      [ 9,  4, -1,  0, 0],
                      [ 0, -3,  0,  0, 0],
                      [-3, -5, -1, -3, -2],
                      [-5, -7, -1,  0, -2] ])
print("det(A): ", m2_28_A.det())

m2_29_A = sy.Matrix([ [-4, 20,   3],
                      [ 3,  2,  -1],
                      [14,  2, -13] ])
print("det(A): ", m2_29_A.det())









