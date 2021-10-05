from math import pi, e

import numpy as np

from image import color2gray as c
# from importlib import reload as rl
from image import file2image as f
from plotting import plot

# chapter 1: The Field
# a field is a set of values with plus and times operations
#   eg: real numbers, complex numbers, GF2(galois field which is just set the set containing 1 and 0

# a complex number z can be thought of as a point in the complex plane where z.real is the x val and z.imag is the y val

# Task 1.4.1
s = {2 + 2j, 3 + 2j, 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
plot(s)
a = {1 + 3j}
print("\n\n\n\ns, a set of complex numbers: ")
print(s)

# the absolute value of a complex number z, abs(z), is actually the distance from the origin to (z.real, z.imag) in
# the complex plane. pythagorean theorem says -> abs(z)**2 == z.real**2 + z.imag**2 or less pythonically -> |z|^2 =
# z.real^2 + z.imag^2

# the conjugate of a complex number z is z̄ , z.real-z.imag, where the normal way is z.real+z.imag
# conjugate of z is written z with a bar on top..

# a complex number z is a number that has a real part and a so called imaginary part. i, the imaginary number,
# was an addition to math to symbolize sqrt(-1), thereby expanding the possibilities to be explored in math. z can
# now represent the number sqrt(-9) or the number (3+sqrt(-x)) and so on for numbers where when written as a
# logarithm, the base is negative, as in -> log(base = -b, z) = 2. (3+ sqrt(-9)) = (3+3j(python, remember?))
Z = 3 + 3j


#   math.log(z,


# so now that complex numbers exist, we can do cool shit with the properties of polynomials that come with that
# territory of (c+x) algebrao

#  z_0, a complex number added to z represents a translation.
# the following function will add z_0 = 1+2j to each element in the data set
# translation of all points in data set 1+2j away from location at input
def fun142add(dataset, z_0):
    return {z_0 + x for x in dataset}


print("\nadding 1+2j to each element in s with fun142add: ")
print(fun142add(s, 1 + 2j))

"""
toOrigin = 0j
while toOrigin != -2 - 2j:
    if toOrigin != 0j:
        print("\n\nno, try again:")

    toOrigin = complex(input( "\n\nthe left eye of the face that is made when s is plotted on a graph is at 2+2j. 
    \nfor what value of z_0 would fun142add move the left eye to the origin? \n\n")) print("good job. yeah its 
    -2-2j..") """


# problem 1.4.5
# show that, for any two distinct points z_1 and z_2, there is a translation that maps z_1 to z_2:
# proof:
# let z_1 = 1+2j and z_2 = 2+5j
# if a translation exists, there must be some complex number z_3 such that z_2 = z_1 + z_3
# then 2+5j = 1+2j + z_3
#     1+3j = z_3

# show that, for any two distinct points z_1 and z_2, there is a translation that maps z_2 to z_1:
# proof:
# let z_1 and z_2 be as defined 7 lines above
# then if a translation exists, there must be some complex number z_3 such that z_1 = z_2 + z_3
# so 1+2j = 2+5j + z_3
#  -1-3j = z_3

# show that, for any two distinct points z_1 and z_2, there is no translation that both maps z_2 to z_1 and z_1 to z_2:
# proof:
# suppose there is a translation where a complex number z_3 which maps both z_2 to z_1 and z_1 to z_2.
# then z_2 + z_3 = z_1 and z_1 + z_3 = z_2
#  so z_3 = z_1 - z_2 and z_3 = z_2 - z_1
#  so z_3 = z_1 = z_2 = 0+0j is the only solution.


# translations are also complex numbers..
# add complex number vectors to create a new translation vector from the sum.
def translationComplexNums(numslist):
    return sum(numslist)


# task 1.4.7
scaledpoints = {.5 * x for x in s}
# plot(scaledpoints)

# when you multiply a complex number by i, you rotate by pi/2 this is easy to intuit when you see that z*-1 will
# rotate everything by 180, since (+z.real +z.imag)* -1 = -z.real-z.imag


# task 1.4.8 scale by 1/2 and rotate pi/2
sr = {x * 1j for x in scaledpoints}
# plot(sr)

# task 1.4.9 scale by 1/2, rotate pi/2, then translate down 1 and right 2
# srt = {.5+1j * x + 2-1j for x in s}
# above doesn't work because you can't add .5 and 1j..
srt = {.5 * z * 1j + 2 - 1j for z in s}
# plot(srt)

# task 1.4.10
data = c(f("img01.png"))
# plotting only pixels in img01 that have intensity < 120
# In this task, you should assign to pts the list of complex numbers
# x + iy such that the image intensity of pixel (x, y) is less than 120.
# apparently matrix dimensions are rows by columns so x vals will be
pts = {x + y * 1j for x in range(np.shape(data)[1]) for y in range(np.shape(data)[0]) if data[y][x] < 120}


# plot(pts, 200)


# currently this plots the image upside down..

# task 1.4.11 translation function for moving each complex number z so that for a set of complex numbers
# they will be centered at the origin
def toOrigin(points):
    lx = max(x.real for x in points) / 2
    ly = max(y.imag for y in points) / 2
    return {z - lx - ly * 1j for z in points}


# plot(toOrigin(pts), 200)


# task 1.4.17 for n = 20 and w = e^(2pi*i/n), make list from w^0 through w^(n-1) and plot
def task147(n):
    return [e ** ((2 * pi * 1j) / n) ** x for x in range(n)]


k = task147(20)
print(k)


# plot(task147(20), 1)


# given complex num z, zprime returns the complex number point where z touches unit circle. |zprime| is 1
def zprime(z):
    return 1 / abs(z) * z


# polarcoordinate takes complex number z and returns the polar coordinate in a list as [r, theta],
# where r is the absolute value of z and theta is the angle in radians
# note: z = x+iy = |z|e^(i*theta)
# def polarcoordinate(z):
#    return [abs(z), math.tan(z.imag, z.real)]


# z = re^(theta*i)

# rotate z by tau radians, re^((theta+tau)i) = re^(theta*i)e^(tau*i) = ze^(tau*i)
def rotateZby(z, tau):
    return z * e ** (tau * 1j)


# task 1.4.18 rotate s by pi/4
S_rotatepi4 = {rotateZby(z, pi / 4) for z in s}
# plot(S_rotatepi4, 4)

# task 1.4.19 rotate pts by pi/4
pts_rotate_pi4 = {rotateZby(z, pi / 4) for z in pts}
# plot(pts_rotate_pi4, 200)

# task 1.4.20 translate to center, rotate pi/4, scale by half and plot
pts_combotransform = {.5 * rotateZby(z, pi / 4) for z in toOrigin(pts)}


# plot(pts_combotransform, 200)


# 1.6 review questions: conjugate of a complex number z is z.real-z.imag. what does this have to do with the abs(z)?
# abs(z) = z*z.conjugate() how does complex number addition work? real parts are added, imaginary parts are added.
# also represents translation how does complex number multiplication work? just like with polynomials. if it's just
# by a scaler, each part is multiplied by that translation in complex numbers can be defined as adding complex
# numbers and a translation is a complex number itself so z + translation = newlocation scaling can be defined as
# multiplying a complex number by a scalar rotation by 180 is multiplying by -1 rotation by 90 is multiplying by i

# 1.7 problems

# problem 1.7.1
def my_filter(L, num):
    """
    input: list of numbers and a positive int
    output: list of numbers not containing a multiple of num
    """
    return [x for x in L if x % num]


# problem 1.7.2
def my_lists(L):
    """
    input: list L of non neg ints
    output: list of lists: for every element x in L create a list containing 1 through x
    """
    return [[x for x in range(1, n + 1)] for n in L]


# problem 1.7.3
def my_function_composition(func, g):
    """
    input: 2 functions f and g represented as dictionaries such that g(f()) exists
    output: dictionary that represents function g(f())
    """
    return {x: g[func[x]] for x in func.keys()}


# problem 1.7.4
def my_sum(L):
    """
    input: list of numbers
    output: sum of numbers in list
    """
    current = 0
    for x in L:
        current += x
    return current


# problem 1.7.5
def my_product(L):
    current = 1
    for x in L:
        current *= x
    return current


# problem 1.7.6
def my_min(L):
    current = 0
    for x in L:
        if x < current:
            current = x
    return current


# problem 1.7.7
def my_concat(L):
    """
    input: list of strings
    output: concatenation of all the strings in L
    """
    current = ""
    for x in L:
        current += x
    return current


# problem 1.7.8
def my_union(L):
    """
    input: list of sets
    output: union of all sets
    """
    current = set()
    for x in L:
        current = current | x
    return current


# problem 1.7.12
def transform(c1, c2, L):
    """
    input: complex numbers a and b, and list L of complex numbers
    output: list of complex numbers az+b for each z in L
    a. translate z 1 up and 1 right, rotate -pi/2, scale by 2
        = (z + 1+1j) * -1 * 2
        = -2z -2-2j
        = -2z +(-2-2j)
        a=-2, b=-2-2j
    b. scale real part by 2, imag part by 3, rotate pi/4, then translate down 2 and left 3
    """
    return [c1 * z + c2 for z in L]
