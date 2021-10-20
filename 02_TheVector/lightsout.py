from Vec import Vec
from Tools.GF2 import zero, one
from random import choice

'''
Computational Problem 2.8.4: Solving Lights Out:
Given an initial configuration of lights, find a sequence of button-pushes that turns out all the
lights, or report that none exists.
'''

domain = {(i, j) for j in range(5) for i in range(5)}
# print(sorted(domain))
f = {d: choice([zero, one]) for d in domain}
s = Vec(domain, f)


def buttonPushed(buttonTuple, V):
    '''
    affectedButtons = {buttonTuple}
    if(buttonTuple[0]-1 >= 0):
        affectedButtons.add((buttonTuple[0] - 1, buttonTuple[1]))
    if(buttonTuple[0]+1 <= 4):
        affectedButtons.add((buttonTuple[0] + 1, buttonTuple[1]))
    if(buttonTuple[1]-1 >= 0):
        affectedButtons.add((buttonTuple[0], buttonTuple[1] - 1))
    if(buttonTuple[1]+1 <= 4):
        affectedButtons.add((buttonTuple[0], buttonTuple[1] + 1))
    '''

    affectedButtons = {(i, buttonTuple[0]) for i in range(buttonTuple[0] - 1, buttonTuple[0] + 2)}.union(
        {(buttonTuple[1], j) for j in range(buttonTuple[1] - 1, buttonTuple[1] + 2)})
    f = {button: V[button] + one for button in affectedButtons if button in V.D}

    move = Vec(V.D, f)
    return move


btest = buttonPushed((0, 0), s)
print(btest.f)


# move takes the current state of the board and a button tuple of the form (i, j)
# then adds the board with the result of pushing the button to return the new state of the board
def move(board, button):
    return board + buttonPushed(button, board)


# the problem is: given a vector s representing the
# initial state, select a sequence of button vectors v1,..., vm such that
# (···((s + v1) + v2)···) + vm = the zero vector
# or because of associativity,
# s + v1 + v2 + ... + vm = the zero vector
# now add s to both sides.. (we can add because GF2 works the same with + or - )
# v1 + v2 + ... + vm = s
# now since adding any equal button vectors will cancel them out, we can see that
# we only need the subset of button vectors whose sum is s, the orginal state of the board.. cool

# this leads us to the more general problem of comp problem 2.8.4
# Computational Problem 2.8.7: Representing a given vector as a sum of a subset of other
# given vectors over GF(2)
# • input: a vector s and a list L of vectors over GF(2)
# • output: A subset of the vectors in L whose sum is s, or a report that there is no such
# subset.

# the brute force solution is to try all subsets of L, which in this case is 25 different button push vectors
# that would be 2^|L| computations, 2^25 = 33554432

# The faster solution will be given in later chapters..