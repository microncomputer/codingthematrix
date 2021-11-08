"""
This file is where I will store various interesting methods I have written along the way
for coding-the-matrix that I didn't want to lose track of among the various other files
so they will go here for now
"""

# written for lists, sumVector is a vector that you want to find a subset of vectorSet
# for which the sum of the subset is sumVector
def vector_sum_subset(sumVector, vectorSet):
    # a function used within this function:
    # sum GF2 vector lists and return true if they equal another vector sumvec
    def sumvec(sumVec, vectorlist):
        s = [sum(vectorlist[i][j] for i in range(len(vectorlist))) for j in range(len(vectorlist[0]))]
        if s == sumVec:
            return True
        else:
            return False

    """
    there will be 2^n subsets of a set, where n is the number of elements in the set (or lists in this case)
    I will always admit when I did not do my own work and this is a moment where I
    must admit I found the next algorithm for making a powerset on stack exchange
    in a moment of low energy and escapism. hey, we all do it.
    the part I did not understand was the "if i&1<<k" which I assumed was some kind of bit shifting
    so I will try to explain it for my own understanding here.
    order of precedence favors << so that will happen first..
    1<<k means 1 * 2^k since 00000001 will be shifted to the left k places. each place is 2^(place)
    so i&1<<k means i&(2^k)
    i&1<<k will be true if there's a 1 in the k place in the binary representation of i

    so the subsets comprehension does:
    for each new entry that will be added to subsets, it can be up to len(vectorset) elements(lists) in the new entry.
    it adds the empty set only once because i&1<<k will only be false for all k's in the range when i is 0. otherwise,
    at least one true will happen. this is bc when i >0, there's going to be a 1 in at least one of the bits making up
    the binary representation of i. since k will cover each bit in the length of binary needed for all i's EVERy time
    then there has to be at least one true i&1<<k for each i > 0

    ok, so i will go from 0 through 2^(len(vectorset))-1
    and at each i, k will go from 0 through len(vectorset)-1
    so 2^len * len operations
    """

    powerset = [[vectorSet[k] for k in range(len(vectorSet)) if i & 1 << k] for i in range(2 ** (len(vectorSet)))]
    powerset.remove([])
    # return powerset
    return [powerset[i] for i in range(len(powerset)) if sumvec(sumVector, powerset[i])]

