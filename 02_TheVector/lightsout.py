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

    affectedButtons = {(i, buttonTuple[0]) for i in range(buttonTuple[0] - 1, buttonTuple[0] + 2)}.union({(buttonTuple[1], j) for j in range(buttonTuple[1] - 1, buttonTuple[1] + 2)})
    f = {button:V[button]+one for button in affectedButtons if button in V.D}

    move = Vec(V.D, f)
    return move


btest = buttonPushed((0, 0), s)
print(btest.f)
