# version code b7f7ff63f9f3+
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from Tools.plotting import plot
from Tools.GF2 import one
import numpy as np

## 1: (Problem 2.14.1) Vector Addition Practice 1
# Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [p1_v[i] + p1_u[i] for i in range(len(p1_v))]
p1_v_minus_u = [p1_v[i] - p1_u[i] for i in range(len(p1_v))]
p1_three_v_minus_two_u = [3 * p1_v[i] - 2 * p1_u[i] for i in range(len(p1_v))]

## 2: (Problem 2.14.2) Vector Addition Practice 2
p2_u = [-1, 1, 1]
p2_v = [2, -1, 5]
p2_v_plus_u = [p2_v[i] + p2_u[i] for i in range(len(p2_v))]
p2_v_minus_u = [p2_v[i] - p2_u[i] for i in range(len(p2_v))]
p2_two_v_minus_u = [2 * p2_v[i] - p2_u[i] for i in range(len(p2_v))]
p2_v_plus_two_u = [2 * p2_u[i] + p2_v[i] for i in range(len(p2_v))]

## 3: (Problem 2.14.3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [0 + one, one + one, one + one]
p3_vector_sum_2 = [0 + one + one, one + one + one, one + one + one]

## 4: (Problem 2.14.4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.

'''
find subset of a-f that sums to u1 and that sums to u2
u1 = 0010010
u2 = 0100010
'''
a = [one, one, 0, 0, 0, 0, 0]
d = [0, 0, 0, one, one, 0, 0]
b = [0, one, one, 0, 0, 0, 0]
e = [0, 0, 0, 0, one, one, 0]
c = [0, 0, one, one, 0, 0, 0]
f = [0, 0, 0, 0, 0, one, one]

u1 = [0, 0, one, 0, 0, one, 0]
u2 = [0, one, 0, 0, 0, one, 0]


def vector_sum_subset(sumVector, vectorSet):
    # a function used within this function:
    # sum GF2 vector lists and return true if they equal another vector list
    def sumGF2vec(sumVec, vectorlist):
        s = [sum(vectorlist[i][j] for i in range(len(vectorlist))) for j in range(len(vectorlist[0]))]
        if s == sumVec:
            return True
        else:
            return False

    """
    there will be 2^n subsets of a set, where n is the number of elements in the set (or lists in this case)
    I will always admit when I did not do my own work and this is a moment where I
    must admit I found the next algorithm for making a powerset on stack exchange
    in a moment of low energy and escapism. hey, we all do it.
    the part I did not understand was the "if i&1<<k" which I assumed was some kind of bit shifting
    so I will try to explain it for my own understanding here.
    order of precedence favors << so that will happen first..
    1<<k means 1 * 2^k since 00000001 will be shifted to the left k places. each place is 2^(place)
    so i&1<<k means i&(2^k)
    i&1<<k will be true if there's a 1 in the k place in the binary representation of i

    so the subsets comprehension does:
    for each new entry that will be added to subsets, it can be up to len(vectorset) elements(lists) in the new entry.
    it adds the empty set only once because i&1<<k will only be false for all k's in the range when i is 0. otherwise,
    at least one true will happen. this is bc when i >0, there's going to be a 1 in at least one of the bits making up
    the binary representation of i. since k will cover each bit in the length of binary needed for all i's EVERy time
    then there has to be at least one true i&1<<k for each i > 0

    ok, so i will go from 0 through 2^(len(vectorset))-1
    and at each i, k will go from 0 through len(vectorset)-1
    so 2^len * len operations
    """

    powerset = [[vectorSet[k] for k in range(len(vectorSet)) if i & 1 << k] for i in range(2 ** (len(vectorSet)))]
    powerset.remove([])
    # return powerset
    return [powerset[i] for i in range(len(powerset)) if sumGF2vec(sumVector, powerset[i])]


u_0010010 = vector_sum_subset(u1, [a, b, c, d, e, f])
u_0100010 = vector_sum_subset(u2, [a, b, c, d, e, f])

## 5: (Problem 2.14.5) GF2 Vector Addition B
# Use the same format as the previous problem
a = [one, one, 0, 0, 0, 0, 0]
b = [0, one, one, 0, 0, 0, 0]
c = [0, 0, one, one, 0, 0, 0]
d = [0, 0, 0, one, one, 0, 0]
e = [0, 0, 0, 0, one, one, 0]
f = [0, 0, 0, 0, 0, one, one]

v_0010010 = vector_sum_subset([0, 0, one, 0, 0, one, 0], [a, b, c, d, e, f])
v_0100010 = vector_sum_subset([0, one, 0, 0, 0, one, 0], [a, b, c, d, e, f])

## 6: (Problem 2.14.6) Solving Linear Equations over GF(2)
# You should be able to solve this without using a computer.
x_gf2 = [one, 0, 0, 0]

## 7: (Problem 2.14.7) Formulating Equations using Dot-Product
# Please provide each answer as a list of numbers
v1 = [2, 3, -4, 1]
v2 = [1, -5, 2, 0]
v3 = [4, 1, -1, -1]

## (Problem 2.14.8) plotting lines
# use the plot module to plot substantial portion of line through [-1.5, 2] and [3,0]
# and the line segment between [2,1] and [-2,2]
p1 = [-1.5, 2]
p2 = [3, 0]
p3 = [2,1]
p4 = [-2,2]


def scalar_multiple(s, v):
    # assuming v is a list..
    return [s * v[i] for i in range(len(v))]


def add_vecs(vecs):
    return [sum([vecs[i][j] for i in range(len(vecs))]) for j in range(len(vecs[0]))]


line_through_points = [add_vecs([scalar_multiple(alpha, p2), scalar_multiple(1 - alpha, p1)]) for alpha in
               np.linspace(-100, 100, 400)]
# uncomment to plot
# plot(line_through_points, 20)

line_segment = [add_vecs([scalar_multiple(alpha, p3), scalar_multiple(1-alpha, p4)]) for alpha in np.linspace(0,1, 10)]
# uncomment to plot
# plot(line_segment, 5)


## 8: (Problem 2.14.9) Practice with Dot-Product
uv_a = [1*5 + 0*4321]
uv_b = [0*12345 + 1*6]
uv_c = [-1*5 + 3*7]
uv_d = [(-2**.5/2)*(2**.5/2) + (2**.5/2)*(-2**.5/2)]
