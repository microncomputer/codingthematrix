# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 0.8.3) Tuple Sum
def tuple_sum(A, B):
    return [(A[i][0] + B[i][0], A[i][1] + B[i][1]) for i in range(len(A))]
    '''
    Input:
      -A: a list of tuples
      -B: a list of tuples
    Output:
      -list of pairs (x,y) in which the first element of the
      ith pair is the sum of the first element of the ith pair in
      A and the first element of the ith pair in B
    Examples:
    >>> tuple_sum([(1,2), (10,20)],[(3,4), (30,40)])
    [(4, 6), (40, 60)]
    >>> tuple_sum([(0,1),(-1,0),(2,2)], [(3,4),(5,6),(7,8)])
    [(3, 5), (4, 6), (9, 10)]
    '''
    pass



## 2: (Problem 0.8.4) Inverse Dictionary
def inv_dict(d):
    return {y:x for(x,y) in d.items()}
    '''
    Input:
      -d: dictionary representing an invertible function f
    Output:
      -dictionary representing the inverse of f, the returned dictionary's
       keys are the values of d and its values are the keys of d
    Example:
    >>> inv_dict({'goodbye':  'au revoir', 'thank you': 'merci'}) == {'merci':'thank you', 'au revoir':'goodbye'}
    '''
    pass



## 3: (Problem 0.8.5) Nested Comprehension
def row(p, n):
    return [p+i for i in range(n)]
    '''
    Input:
      -p: a number
      -n: a number
    Output:
      - n-element list such that element i is p+i
    Examples:
    >>> row(10,4)
    [10, 11, 12, 13]
    '''
    pass

comprehension_with_row = [row(i, 20) for i in range(15)]

comprehension_without_row = [[p+i for i in range(20)] for p in range(15)]



## 4: (Problem 0.8.10) Probability Exercise 1
Pr_f_is_even = .7
Pr_f_is_odd  = .3



## 5: (Problem 0.8.11) Probability Exercise 2
Pr_g_is_1    = .4
Pr_g_is_0or2 = .3

