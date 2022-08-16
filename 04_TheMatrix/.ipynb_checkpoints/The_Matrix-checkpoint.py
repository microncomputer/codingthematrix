from Tools.vec import Vec

"""
Work from chapter 4: The Matrix
"""

# Quiz 4.1.1: Write a nested comprehension whose value is a list-of-row-list representation of a
# 3x4 matrix all of whose elements are zero.
list_of_row_list = [[0 for n in range(4)] for m in range(3)]
print(list_of_row_list)

# Quiz 4.1.2: Write a nested comprehension whose value is list-of-column-lists representation of
# a 3 × 4 matrix whose i, j element is i − j
list_of_column_list = [[i - j for i in range(3)] for j in range(4)]
print(list_of_column_list)

# Quiz 4.1.4: Give a Python expression using Vec for column '?' (see p. 151 for more info)
colvec = Vec({'a', 'b'}, {'a': 3, 'b': 30})

# Quiz 4.1.5: Give a Python expression whose value is the coldict representation of the matrix
# of Example 4.1.3 (Page 187).
coldict = {'@': Vec({'a', 'b'}, {'a': 1, 'b': 10}), '#': Vec({'a', 'b'}, {'a': 2, 'b': 20}),
           '?': Vec({'a', 'b'}, {'a': 3, 'b': 30})}
print(coldict)


class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function


# Quiz 4.1.7: Write an expression for the {'a','b','c'}×{'a','b','c'} identity matrix represented as an instance of Mat
idmat = Mat(({'a', 'b', 'c'}, {'a', 'b', 'c'}), {('a', 'a'): 1, ('b', 'b'): 1, ('c', 'c'): 1})


# Quiz 4.1.8: Write a one-line procedure identity(D) that, given a finite set D, returns the
# D × D identity matrix represented as an instance of Mat.
def identity(D):
    return Mat((D, D), {(d, d): 1 for d in D})


# Quiz 4.1.9: Write a one-line procedure mat2rowdict(A) that, given an instance of Mat, returns the
# rowdict representation of the same matrix. Use dictionary comprehensions.
def mat2rowdict(A):
    return {r: Vec(A.D[1], {c: A[r, c] for c in A.D[1]}) for r in A.D[0]}


# Quiz 4.1.10: Write a one-line procedure mat2coldict(A) that, given an instance of Mat,
# returns the coldict representation of the same matrix. Use dictionary comprehensions.
def mat2coldict(A):
    return {c: Vec(A.D[0], {r: A[r, c] for r in A.D[0]}) for c in A.D[1]}


# Quiz 4.3.1: Write the procedure mat2vec(M) that, given an instance of Mat, returns the corresponding instance of Vec
def mat2vec(M):
    return Vec({(r, c) for r in M.D[0] for c in M.D[1]}, M.f)


# Quiz 4.4.2: Write the procedure transpose(M) that, given an instance of Mat representing a
# matrix, returns the representation of the transpose of that matrix.
def transpose(M):
    # this first try didn't work because Mat objects aren't subscriptable yet as defined very simply above
    # return Mat((M.D[1], M.D[0]), {(j, i): M[i, j] for (i, j) in M.f.keys()})
    return Mat((M.D[1], M.D[0]), {(j, i):v for (i,j),v in M.f.items()})


# Example 4.6.4 downsampling
# recall that the average of the entries of an n-vector can be expressed as a dot product
# by doing dot product of the vector with a vector where all entries are 1/n.
"""
general review of dot product applications and intricacies:
- consider a cost vector with price per unit amounts for a set of foods,ingredients
and a quantity vector with amount of each type of food
the dot product between them is the total cost 
 or caloric_content vector dot quantity vector = total calories in the whole amount

- sensor node with various hardware pieces. the domain are the elements: radio, sensor, memory, CPU
rate vector is power consumption in Watts of each element. duration vector is how long each component is on during a 
test period
total energy consumed in Joules is rate dot duration
-- if rate was not known and we did a number of test runs,
[durationvec1                  [totalJoules1
 durationvec2     * rate =      totalJoules2
 durationvec3]                  totalJoules3]                 
let D = the durations matrix, j = joules vector
[D|j]=rate


"""
