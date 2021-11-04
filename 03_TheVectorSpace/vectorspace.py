"""
using this file to work through things in the chapter, including quizzes and
examples that I want to mess around with
"""


'''
Quiz 3.1.7: Define a procedure lin_comb(vlist, clist) with the following spec:
• input: a list vlist of vectors, a list clist of the same length consisting of scalars
• output: the vector that is the linear combination of the vectors in vlist with corresponding
coefficients clist

NOTE: answer in book is wrong. this is a correct solution
'''
def lin_comb(vlist, clist):
    assert len(vlist) == len(clist)
    return [sum(clist[i] * vlist[i][j] for i in range(len(clist))) for j in range(len(vlist[0]))]


a = [2,3,4,5]
v = [[1,2,3,4],[2,4,6,8],[0,1,2,3],[5,4,3,2]]
l = lin_comb(v, a)
print(l)