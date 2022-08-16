# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one



## 1: (Problem 7.9.2) Recognizing Echelon Form
# Write each matrix as a list of row lists

echelon_form_1 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_2 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_3 = [[   ...   ],
                  [   ...   ],
                  [   ...   ]]

echelon_form_4 = [[   ...   ],
                  [   ...   ],
                  [   ...   ],
                  [   ...   ]]



## 2: (Problem 7.9.3) Is it echelon?
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
        >>> is_echelon([[1,1]])
        True
        >>> is_echelon([[1]])
        True
        >>> is_echelon([[1],[1]])
        False
        >>> is_echelon([[0]])
        True
        >>> is_echelon([[0],[1]])
        False
    '''
    pass



## 3: (Problem 7.9.4) Solving with Echelon Form: No Zero Rows
# Give each answer as a list

echelon_form_vec_a = ...
echelon_form_vec_b = ...
echelon_form_vec_c = ...



## 4: (Problem 7.9.5) Solving with Echelon Form
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None" (without the quotes).

solving_with_echelon_form_a = ...
solving_with_echelon_form_b = ...



## 5: (Problem 7.9.6) Echelon Solver
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})]
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    pass



## 6: (Problem 7.9.7) Solving General Matrices via Echelon
rowlist = [ ... ]    # Provide as a list of Vec instances
label_list = [ ... ] # Provide as a list
b = [ ... ]          # Provide as a list of GF(2) values



## 7: (Problem 7.9.8) Nullspace A
null_space_rows_a = {...} # Put the row numbers of M from the PDF



## 8: (Problem 7.9.9) Nullspace B
null_space_rows_b = {...} # Put the row numbers of M from the PDF

