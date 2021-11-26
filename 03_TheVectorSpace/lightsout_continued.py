from Tools.vec import Vec
from Tools.GF2 import zero, one
from random import choice

'''
Computational Problem 2.8.4: Solving Lights Out:
Given an initial configuration of lights, find a sequence of button-pushes that turns out all the
lights, or report that none exists.
'''


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
# we only need the subset of button vectors whose sum is s, the original state of the board.. cool


# Computational Problem 2.8.7: Representing a given vector as a sum of a subset of other
# given vectors over GF(2)
# • input: a vector s and a list L of vectors over GF(2)
# • output: A subset of the vectors in L whose sum is s, or a report that there is no such
# subset.
def vector_sum_subset(s, L):
    # NOTE: THIS DOES NOT WORK FOR VEC'S YET. IT WAS WRITTEN FOR LIST VECTORS IN PREVIOUS SECTION
    # the brute force solution is to try all subsets of L, which in this case is 25 different button push vectors
    # that would be 2^|L| computations, 2^25 = 33554432

    # a function used within this function:
    # sum GF2 vector lists and return true if they equal another vector sumVec
    def sumvec(sumVec, vectorlist):
        s = [sum(vectorlist[i][j] for i in range(len(vectorlist))) for j in range(len(vectorlist[0]))]
        if s == sumVec:
            return True
        else:
            return False

    """
    i&1<<k will be true if there's a 1 in the k place in the binary representation of i
    since k will cover each bit in the length of binary needed for all i's EVERy time
    there has to be at least one true i&1<<k for each i > 0

    ok, so i will go from 0 through 2^(len(vectorset))-1
    and at each i, k will go from 0 through len(vectorset)-1
    so 2^len * len operations
    """
    powerset = [[L[k] for k in range(len(L)) if i & 1 << k] for i in range(2 ** (len(L)))]
    powerset.remove([])
    # return powerset
    return [powerset[i] for i in range(len(powerset)) if sumvec(s, powerset[i])]
    # The faster solution will be described in later chapters..


def main():
    domain = {(i, j) for j in range(5) for i in range(5)}
    # print(sorted(domain))
    f = {d: choice([zero, one]) for d in domain}
    s = Vec(domain, f)

    setofallmoves = [buttonPushed(b, s) for b in s.D]

    # uncomment to build the sum_set which will do at least 2^25 operations. v slow
    # sum_to_s = vector_sum_subset(s, setofallmoves)
    # print(sum_to_s)

if __name__ == '__main__':
    main()