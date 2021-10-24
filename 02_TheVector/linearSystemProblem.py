"""
Computational Problem 2.9.12: Solving a linear system
• input: a list of vectors a1,..., am, and corresponding scalars β1,..., βm (the right-hand
sides)
• output: a vector xˆ satisfying the linear system 2.3 or a report that none exists.
"""

def linearSystem(vectors, scalars):
    assert len(vectors) == len(scalars)
    x = []
    for a in range(len(vectors)):
        for i in range(len(a)):
            x += {("x"+str(i),a[i])}
    return [x for ]


def solveForVars(vec, rhs):
    x = []
    for i in range(vec):
        x[i] = "  n"