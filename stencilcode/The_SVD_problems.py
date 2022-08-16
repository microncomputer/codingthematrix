# version code 0caa61797a35+
# Please fill out this stencil and submit using the provided submission script.

from Tools.mat import Mat
from vec import Vec


## 1: (Problem 11.8.1) Procedure for computing squared Frobenius norm
def squared_Frob(A):
    '''
    Computes the square of the frobenius norm of A.

    Example:
    >>> squared_Frob(Mat(({1, 2}, {1, 2, 3, 4}), {(1, 1): 1, (1, 2): 2, (1, 3): 3, (1, 4): 4, (2, 1): -4, (2, 2): 2, (2, 3): -1}))
    51
    '''
    pass



## 2: (Problem 11.8.2) Frobenius_norm_counterexample
#Give a numerical counterxample.
A = ...
Q = ...



## 3: (Problem 11.8.3) Multiplying a vector by a matrix in terms of the SVD of the matrix
# Use lists instead of Vecs
# Part 1
vT_x_1 = [ ... ]
Sigma_vT_x_1 = [ ... ]
U_Sigma_vT_x_1 = [ ... ]

# Part 2
vT_x_2 = [ ... ]
Sigma_vT_x_2 = [ ... ]
U_Sigma_vT_x_2 = [ ... ]



## 4: (Problem 11.8.4) The SVD of a small simple matrix
# A.D = ({'r1','r2'},{'c1','c2'})
# Row and column labels of SA should be {0,1, ...}
UA = Mat(({...},{...}),{...})
SA = Mat(({...},{...}),{...})
VA = Mat(({...},{...}),{...})

# B.D = ({'r1','r2'},{'c1','c2'})
# Row- and column-labels of SB should be {0,1, ...}
UB = Mat(({...},{...}),{...})
SB = Mat(({...},{...}),{...})
VB = Mat(({...},{...}),{...})

# C.D = ({'r1','r2','r3'},{'c1','c2'})
# Row- and column-labels of SC should be {0,1, ...}
UC = Mat(({...},{...}),{...})
SC = Mat(({...},{...}),{...})
VC = Mat(({...},{...}),{...})



## 5: (Problem 11.8.5) Closest rank-$k$ matrix
# In both parts, your matrices must use 0, 1, 2, ... , n as the indices.

# Part 1
G1 = ...
H1 = ...

# Part 2
G2 = ...
H2 = ...



## 6: (Problem 11.8.7) Writing SVD_solve
def SVD_solve(U, Sigma, V, b):
    '''
    Input:
      - U: orthogonal matrix
      - Sigma: diagonal matrix with non-negative elements
      - V: orthogonal matrix
      - b: vector
    Output:
      - x: a vector such that U*Sigma*V.tranpose()*x = b
      - 'FAIL': if U*Sigma*V.transpose() has no inverse

    Example:
      >>> U = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): -0.44072022797538285, (1, 2): -0.4580160039142736, (0, 0): -0.15323906505773385, (2, 0): -0.8716906349733183, (1, 0): -0.4654817137547351, (2, 2): 0.08909472804179724, (0, 2): 0.8844679019577585, (2, 1): 0.4818895789856551, (1, 1): -0.7573295942443791})
      >>> Sigma = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 0): 39.37043356298421, (1, 1): 2.2839722460456144, (2, 2): 0.867428292102265})
      >>> V = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 0.8797721734901444, (1, 2): -0.7977287698474189, (0, 0): -0.46693900110435005, (2, 0): -0.682398941975231, (1, 0): -0.5624052393414894, (2, 2): 0.5963722979461945, (0, 2): 0.08926865071288784, (2, 1): -0.42269583181462916, (1, 1): -0.21755265229127096})
      >>> b = Vec({0,1,2}, {0:0, 1:1, 2:2})
      >>> x = SVD_solve(U, Sigma, V, b)
      >>> res = b - U*(Sigma*(V.transpose()*x))
      >>> res*res < 1e-20
      True
    '''
    pass

