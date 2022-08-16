# version code c2eb1c41017f+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
from Tools.mat import Mat

## Task 1

# see documentation of eigenfaces.load_images
face_images = { ... } # dict of Vecs

## Task 2

centroid = Vec(..., ...)
centered_face_images = { ... }

## Task 3

A = Mat(..., ...) # centered image vectors

orthonormal_basis = Mat(..., ...) # 10 rows

## Task 4

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projected_representation(M, x):
    '''
    Input:
        - M: a matrix with orthonormal rows with M.D[1] == x.D
        - x: a vector
    Output:
        - the projection of x onto the row-space of M
    Examples:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1, 1: 2})
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projected_representation(M, x)
        Vec({0, 1},{0: 1.6, 1: 2.333333333333333})
    '''
    pass

## Task 5

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def projection_length_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the norm of the projection of x into the
          row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> projection_length_squared(M, x)
        5
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> projection_length_squared(M, x)
        5.644424691358024
    '''
    pass

## Task 6

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def distance_squared(M, x):
    '''
    Input:
        - M: matrix with orthonormal rows with M.D[1] == x.D
        - x: vector
    Output:
        - the square of the distance from x to the row-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0, 0], [0, 1, 0]])
        >>> distance_squared(M, x)
        9
        >>> M = listlist2mat([[3/5, 1/5, 1/5], [0, 2/3, 1/3]])
        >>> distance_squared(M, x)
        8.355575308641976
    '''
    pass

## Task 7

distances_to_subspace = list(...)

## Task 8

classified_as_faces = set(...) # of dictionary keys

## Task 9

threshold_value = ...

## Task 10

#This is the "transpose" of what was specified in the text.
#Follow the spec given here.
def project(M, x):
    '''
    Input:
        - M: an orthogonal matrix with row-space equal to x's domain
        - x: a Vec
    Output:
        - the projection of x into the column-space of M
    Example:
        >>> from vecutil import list2vec
        >>> from matutil import listlist2mat
        >>> x = list2vec([1, 2, 3])
        >>> M = listlist2mat([[1, 0], [0, 1], [0, 0]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 1, 1: 2, 2: 0})
        >>> M = listlist2mat([[3/5, 0], [1/5, 2/3], [1/5, 1/3]])
        >>> project(M, x)
        Vec({0, 1, 2},{0: 0.96, 1: 1.8755555555555554, 2: 1.0977777777777777})
    '''
    pass

## Task 11

# see documentation for image.image2display

## Task 12

