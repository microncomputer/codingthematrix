import numpy as np
from Tools.plotting import plot

'''
sparse representation is used to omit values of zero and make a vector simpler
if a vector is mostly zeroes, it is a sparse vector
when no more than k entries are 0 (entriescount <= k), it's a k-sparse vector
'''

# Task 2.3.2
L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]
plot(L, 4)

'''
Translations
as we saw with complex numbers where z_0 +z is a translation of complex number z_0 by z
vector addition will make translations in geometric planes
'''


def add2(v, w):
    return [v[0] + w[0], v[1] + w[1]]


# plot([add2(v, [1, 2]) for v in L], 4)


# quiz 2.4.4 write procedure addn to compute sum of 2 n-vectors (n-element lists)
def addn(v, w):
    return [v[i] + w[i] for i in range(len(v))]


# quiz 2.5.3 procedure scalar_vector_mult(alpha, v) that multiplies vector v by scalar alpha
def scalar_vector_mult(alpha, v):
    return [alpha * v[i] for i in range(len(v))]


# task 2.5.4 : plot the result of scaling the vectors in L by 0.5, then plot of scaling by -0.5
plot([scalar_vector_mult(.5, v) for v in L], 4)
plot([scalar_vector_mult(-.5, v) for v in L], 4)

# plotting evenly spaced scalars*a vector
v = [2, 3]
plot([scalar_vector_mult(i / 10, v) for i in range(11)], 5)
# and seeing how a bunch of plots in the same scalar*vector looks like a line
plot([scalar_vector_mult(i / 100, v) for i in range(101)], 5)
# we can represent the translation of v and the points that would make up the line segment of v+[0.5,1]
plot([addn(scalar_vector_mult(i / 100, v), [0.5, 1]) for i in range(101)], 5)

# exercise 2.6.1
u = [2, 3]
v = [5, 7]
w = add2(v, scalar_vector_mult(-1, u))


# using the set of convex combinations of two endpoints, we can get the line segment between them
def segment(pt1, pt2):
    # returns a list of 100 evenly spaced points along the line segment whose endpoints are pt1 and pt2
    pts = [addn(scalar_vector_mult(1 - i, pt1), scalar_vector_mult(i, pt2)) for i in np.linspace(0, 1, 100)]
    return pts


# print(segment([0., 0.], [100., 0.]))
plot(segment([3.5, 3], [0.5, 1]))


# now I want to try the same thing with numpy vectors
def npsegment(pt1, pt2):
    return np.linspace(pt1, pt2, 100)

# print(npsegment([0, 0], [100, 0]))
