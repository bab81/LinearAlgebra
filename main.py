import sympy as sy
from sympy import *

"""
2x+8y=−40
4x+16y=−79
"""

x, y, z = sy.symbols('x, y, z')
eq1 = sy.Eq(-7*x - 3*y + 3*z, 5)
eq2 = sy.Eq(-2*x + 5*y - 4*z, 5)
eq3 = sy.Eq(-27*x - 35*y + 31*z, 5)

eq4 = sy.Eq(10*x + 4*y - 6*z, -8)
eq5 = sy.Eq(20*x + 8*y - 12*z, -16)
eq6 = sy.Eq(35*x + 14*y + 21*z, -28)

eq7 = sy.Eq(5*x + 10*y + 19*z, 6)
eq8 = sy.Eq(-2*x - 3*y - 7*z, 1)
eq9 = sy.Eq(3*x + 6*y + 12*z, 9)

eq10 = sy.Eq(-7*x - 3*y + 3*z, 5)
eq11 = sy.Eq(-2*x + 5*y - 4*z, 5)
eq12 = sy.Eq(-27*x - 35*y + 31*z, 4)

ans1 = sy.solve((eq1, eq2, eq3), (x, y, z))
print(ans1)
ans2 = sy.solve((eq4, eq5, eq6), (x, y, z))
print(ans2)
ans3 = sy.solve((eq7, eq8, eq9), (x, y, z))
print("ans3:",ans3)
ans4 = sy.solve((eq10, eq11, eq12), (x, y, z))
print("ans4:",ans4)

eq13 = sy.Eq(x - 4*y - 4*z, -3)
eq14 = sy.Eq(x - 6*y - 8*z, 1)
eq15 = sy.Eq(-2*x + 11*y + 14*z, 0)
ans5 = sy.solve((eq13, eq14, eq15), (x, y, z))
print("ans5:",ans5)


M = Matrix([[1, -4, -4, -3], [1, -6, -8, 1], [-2, 11, 14, 0]])

# Use sympy.rref() method
M_rref = M.rref(pivots=True)

print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))


h , k = sy.symbols('h, k')
eq16 = sy.Eq(-7*x + 7*y + 7*z, -6)
eq17 = sy.Eq(-2*x - 9*y - 5*z, 3)
eq18 = sy.Eq(11*x + 11*y + h*z, k)
ans6 = sy.solve((eq16, eq17, eq18), (x, y, z))
print("ans6:",ans6)

