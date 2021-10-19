from Tools.plotting import plot
from math import e, pi
from Tools.image import file2image as f2i
from Tools.image import color2gray as cg

##task 1.4.1
S = {2+2j, 3+2j, 1.75+1j, 2+1j, 2.25+1j, 2.5+1j, 2.75+1j, 3+1j, 3.25+1j}
plot(S, 4)

## Task 1.4.3
plot({1+2j+z for z in S}, 4)

## Bonus
plot({z.conjugate() for z in S})

## Task 1.4.7
plot({.5*z for z in S}, 4)


## Task 1.4.8
plot({.5*z*1j for z in S})

## Task 1.4.9
plot({.5*z*1j-1j+2 for z in S})

## task 1.4.10
data = cg(f2i("../Tools/img01.png"))
pts = [x +y*1j for y in range(len(data)) for x in range(len(data[0])) if data[y][x] < 120]

## task 1.4.11
'''
Input: complex number z
Output: when applied to each z in S the set of resulting numbers is centered around the origin

this question seems strange because it seems like it would depend on the other elements in S
yet it is framed as f(z) and that can be done on all the elements separately, but aren't they
relative to one another when it comes to centering?

to center all the points, find the length of the x part of the vector and y part then subtract 
half that for each pt.
'''

#centeredpts = 
def centeredpts(pts):
    xlen = abs(pts[len(pts)-1].real)
    ylen = abs(pts[len(pts)-1].imag)
    return [(x.real-xlen + x.imag*1j-ylen) for x in pts]
    
##  task 1.4.17
n = 20
w = e**(2*pi*1j/n)
wlist = [w**i for i in range(n)]
plot(wlist, 3)

## SECTION 1.4.10 rotate a complex number z by tau radians 
def f(z, tau): return z * e**(tau * 1j)

## task 1.4.18 : set whose values are the elements of S rotated by pi/4
S_pi4 = {f(x, pi/4) for x in S}
plot(S_pi4)

## task 1.4.19: rotating pts by pi/4
pts_pi4 = {f(x, pi/4) for x in pts}
plot(pts_pi4, 256)


## task 1.4.20: translate pts to be centered, then rotate by pi/4, then scale by half
#this is wrong but I want to move on..
plot(centeredpts(pts), 400)



'''
1.6 Review Questions
-Name three fields
    GF2, Reals, Complex numbers
-What is the conjugate of a complex number?
    for complex number (x + y*i), the conjugate is (x - y*i)
    wrt the absolute value of a complex number z, |z|^2 = z*z~ , where z~ is the conjugate of z
-how does complex number addition work?
    add the real parts together and the imaginary parts together
-how does complex number multiplication work?
    FOIL the complex numbers as you would with binomials
-how can translation be defined in terms of complex numbers?
    you can use addition to translate with complex  numbers where f(z), a translation, = z+z0 where z,z0 are 2 complex numbers
-how can scaling be defined in terms of complex numbers?
    using multiplication by a real number
-how can rotation by 180 degrees be defined in terms of complex numbers?
    to rotate complex number z by any degrees d, you turn it to radians by doing d*pi/180 = tau radians
    then f(z) = z*e^(tau*i) to rotate by tau
-how does addition of GF(2) values work?
    1+1=0, 1+0=1, 0+0=0
-how does multiplication of GF(2) values work?
    1*1=1, 1*0=0, 0*0=0
'''


##  1.7 PYTHON COMPREHENSION PROBLEMS
#1.7.1 
def my_filter(L, num):
    '''
    input: list of numbers and a positive int
    output: list of numbers not containing a multiple of num
    '''
    return [x for x in L if x%num !=0]

#1.7.2
def my_lists(L):
    '''
    input: list L of non negative ints
    output: a list of lists: for every x in L, a list > [1,2,...,x]
    '''
    return [[a for a in range(1, x+1)] for x in L] 

#1.7.3
def my_function_composition(f,g):
    '''
    input: two functions f and g represented as dictionaries, such that g(f(x)) exists
    output: dictionary that represents the function g(f(x))
    '''
    return {x: g[f[x]] for x in f.keys()}

#1.7.4










