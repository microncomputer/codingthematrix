"""
using this file to work through things in the chapter, including quizzes and
examples that I want to mess around with
"""

'''
Quiz 3.1.7: Define a procedure lin_comb(vlist, clist) with the following spec:
• input: a list vlist of vectors, a list clist of the same length consisting of scalars
• output: the vector that is the linear combination of the vectors in vlist with corresponding
coefficients clist

NOTE: answer in book is wrong. this is a correct solution
'''


def lin_comb(vlist, clist):
    assert len(vlist) == len(clist)
    return [sum(clist[i] * vlist[i][j] for i in range(len(clist))) for j in range(len(vlist[0]))]


a = [2, 3, 4, 5]
v = [[1, 2, 3, 4], [2, 4, 6, 8], [0, 1, 2, 3], [5, 4, 3, 2]]
b = lin_comb(v, a)
print(b)

'''
Computational Problem 3.1.8: Expressing a given vector as a linear combination of other
given vectors
• input: a vector b and a list [v1,..., vn] of n vectors
• output: a list [α1,..., αn] of coefficients such that
b = α1 v1 + ··· + αn vn
or a report that none exists.
'''


def solve_lin_comb_coefs(b, vlist):
    """
    b is a vector, a is a vector, v is a vector of vectors
    len(b) == len(v) == len(a) == n
    b[0] = a[0]v[0][0] + a[1]v[1][0] + ... + a[n-1]v[n-1][0]
    b[i] = a[0]v[0][i] + a[1]v[1][i] + ... + a[n-1]v[n-1][i]
    a[0] = (a[1]v[1][i] + ... + a[n-1]v[n-1][i] - b[i]) / -v[0][i]
    """
    return []


lc = solve_lin_comb_coefs(b, v)

'''
3.2 Span
    -the set of all linear combinations of vectors v1,...,vn is called the span of these vectors
    -written Span{v1,...,vn}
    -over an infinite field, the span is usually an infinite set. for vectors over GF2, a finite
    field, the span is finite
'''

# Quiz 3.2.2: How many vectors are in Span {[1, 1], [0, 1]} over the field GF(2)?
v1 = [1, 1]
v2 = [0, 1]


def scalar_vector_mult(a, v):
    return [a * v[i] for i in range(len(v))]


spanvec1 = scalar_vector_mult(0, v1) + scalar_vector_mult(0, v2)
spanvec2 = scalar_vector_mult(0, v1) + scalar_vector_mult(1, v2)
spanvec3 = scalar_vector_mult(1, v1) + scalar_vector_mult(0, v2)
spanvec4 = scalar_vector_mult(1, v1) + scalar_vector_mult(1, v2)

# four vectors in the span

# Quiz 3.2.3: How many vectors are in Span {[1, 1]} over the field GF(2)?
# two vectors, 0*v and 1*v

# Quiz 3.2.4: How many vectors are in the span of an empty set of 2-vectors?
# one, [0,0]

# Quiz 3.2.5: How many vectors are in the span of the 2-vector [2, 3] over R?
# infinite. {alpha[2,3] : alpha E reals}  (using E as the set notation symbol for "of the set")

# Quiz 3.2.6: For which 2-vector v over R does Span {v} consists of a finite number of vectors?
# [0,0] the zero vector
