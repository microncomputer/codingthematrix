from Vec import Vec
from GF2 import zero, one
from random import choice

'''
Computational Problem 2.8.4: Solving Lights Out:
Given an initial configuration of lights, find a sequence of button-pushes that turns out all the
lights, or report that none exists.
'''

domain = {(i,j) for j in range(5) for i in range(5)}
# print(sorted(domain))
f = {d:choice([zero, one]) for d in domain}
s = Vec(domain, f)
print(s.f)

def buttonPushed(button, V):
    affectedButtons = {button}
    if(button[0]-1 >= 0):
        affectedButtons.add((button[0]-1, button[1]))
    if(button[0]+1 <= 4):
        affectedButtons.add((button[0]+1, button[1]))
    if(button[1]-1 >= 0):
        affectedButtons.add((button[0], button[1]-1))
    if(button[1]+1 <= 4):
        affectedButtons.add((button[0], button[1]+1))

    f = {affectedButtons[i]:val for i in range(len(affectedButtons)) for (affectedButtons[i],val) in V.f.items()}
    move = Vec(V.D, f)
    return move

