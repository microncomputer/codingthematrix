# version code d70bb75e3fb2+
# Please fill out this stencil and submit using the provided submission script.

# version code 05f5a0d767f0+
# Please fill out this stencil and submit using the provided submission script.

from vec import Vec
import math

## Task 1
def identity():
    '''
    Return the matrix that, when multiplied by a location vector, yields the same location vector.

    >>> identity() * Vec({'x','y','u'}, {'x':2, 'y':3, 'u':1}) == Vec({'x','y','u'}, {'x':2, 'y':3, 'u':1})
    True
    '''
    pass

## Task 2
def translation(alpha,beta):
    '''
    Input:  a scalar alpha (the increase to the x-coordinate) and a scalar beta (the increase to the y-coordinate)
    Output:  3x3 matrix that, when multiplied by a location vector representing (x,y),
                          yields the location vector of the translated point (x+alpha, y+beta).

    >>> translation(4,-5) * Vec({'x','y','u'}, {'x':2, 'y':3, 'u':1}) == Vec({'x','y','u'}, {'x':6, 'y':-2, 'u':1})
    True
    '''
    pass

## Task 3
def scale(alpha, beta):
    '''
    Input:  a scalar alpha (the multiplier for the x-coordinate) and a scalar beta (the multiplier for the y-coordinate) 
    Output:  3x3 matrix that, when multiplied by a locaiton vector representing (x,y),
                           yields the locaiton vector of the scaled point (alpha*x, beta*y).

    >>> scale(3,4)*Vec({'x','y','u'}, {'x':1,'y':2,'u':1}) == Vec({'x','y','u'}, {'x':3, 'y':8, 'u':1})
    True
    >>> scale(0,0)*Vec({'x','y','u'}, {'x':1,'y':1,'u':1}) == Vec({'x','y','u'}, {'u':1})
    True
    '''
    pass

## Task 4
def rotation(theta):
    '''
    Input:  theta, the angle (in radians) to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.

    >>> def normsq(v): return v*v
    >>> (rotation(math.pi) * Vec({'x','y','u'},{'x':1,'y':2,'u':1}) - Vec({'x','y','u'},{'x': -1, 'y': -2, 'u': 1})).is_almost_zero()
    True
    >>> (rotation(math.pi/2) * Vec({'x','y','u'},{'x':3,'y':1,'u':1}) - Vec({'x','y','u'},{'x': -1, 'y': 3, 'u': 1})).is_almost_zero()
    True
    (rotation(3*math.pi/4) * Vec({'x','y','u'},{'x':4,'y':-3,'u':1}) - Vec({'x','y','u'},{'x':-1/math.sqrt(2), 'y':7/math.sqrt(2), 'u': 1})).is_almost_zero()
    True
    '''
    pass

## Task 5
def rotate_about(theta, x, y):
    '''
    Input:  an angle theta (in radians) by which to rotate, and x- and y- coordinates of a point to rotate about
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
>>> (rotate_about(math.pi/3, 3,4)*Vec({'x','y','u'}, {'x':1, 'y':0, 'u':1}) - Vec({'y', 'x', 'u'},{'y': 0.26794919243112214, 'x': 5.4641016151377535, 'u': 1})).is_almost_zero()
    True
    '''
    pass

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.

    >>> reflect_y()*Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1}) == Vec({'x','y','u'}, {'x':-1, 'y':1, 'u':1})
    True
    >>> reflect_y()* Vec({'x','y','u'}, {'u':1}) == Vec({'x','y','u'},{'u':1})
    True
    '''
    pass

## Task 7
def reflect_x():
    '''
    Input:  None.
    Output:  3x3 X-reflection matrix.

    >>> reflect_x()*Vec({'x','y','u'}, {'x':1, 'y':1, 'u':1}) == Vec({'x','y','u'}, {'x':1, 'y':-1, 'u':1})
    True
    >>> reflect_x()*Vec({'x','y','u'}, {'u':1}) == Vec({'x','y','u'},{'u':1})
    True
    '''
    pass

## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.

    >>> scale_color(1,2,3)*Vec({'r','g','b'},{'r':1,'g':2,'b':3}) == Vec({'r','g','b'},{'r':1,'g':4,'b':9})
    True
    '''
    pass

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    pass

## Task 10
def reflect_about(x1, y1, x2, y2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.

    >>> (reflect_about(0,1,1,1) * Vec({'x','y','u'}, {'u':1}) - Vec({'x', 'u', 'y'},{'x': 0.0, 'u': 1, 'y': 2.0})).is_almost_zero()
    True
    >>> (reflect_about(0,0,1,1) * Vec({'x','y','u'}, {'x':1, 'u':1}) - Vec({'x', 'u', 'y'},{'u': 1, 'y': 1})).is_almost_zero()
    True
    '''
    pass


