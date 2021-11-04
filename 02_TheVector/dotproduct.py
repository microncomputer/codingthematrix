# quiz 2.9.4: Write a procedure list_dot(u, v) with the following spec:
# • input: equal-length lists u and v of field elements
# • output: the dot-product of u and v interpreted as vectors
# Use the sum(·) procedure together with a list comprehension.


def list_dot(u, v):
    assert len(u) == len(v)
    return sum([u[i] * v[i] for i in range(len(u))])


print(list_dot([1, 2, 3], [2, 2, 2]))

"""
comparing two audio clips by dot product would give us an idea of how similar they are. The more
positive the result, the more alike. 
We could also search for a "needle" in a "haystack", or a short audio segment in a longer clip
by moving element by element and computing the dot product of the needle with the segment of the larger clip starting 
at the current element.
if started at the first element of the larger clip, the number of possible starting positions
is l-s+1, where l is len(haystack) and s is len(needle)

Quiz 2.9.13: Suppose the haystack is [1, −1, 1, 1, 1, −1, 1, 1, 1] and the needle is [1, −1, 1, 1, −1, 1].
Compute the dot-products and indicate which position achieves the best match.
"""

# NOTE: I redid a more concise version of this function as prompted later for quiz2.9.15 below as dot_product_list()
# returns list of possible positions in H that N starts
def needleInHaystack(H, N):  # answer to quiz 2.9.13
    h = len(H)
    n = len(N)
    dots = []
    for i in range(h - n + 1):
        dots.append(list_dot(H[i:i + n], N))
    return [i for i, val in enumerate(dots) if val == max(dots)]


bestmatches = needleInHaystack([1, -1, 1, 1, 1, -1, 1, 1, 1], [1, -1, 1, 1, -1, 1])
print(bestmatches)

'''
Quiz 2.9.14: This method of searching is not universally applicable. Say we wanted to locate
the short clip [1, 2, 3] in the longer segment [1, 2, 3, 4, 5, 6]. What would the dot-product method
select as the best match?
'''
q14 = needleInHaystack([1,2,3,4,5,6], [1,2,3])
print(q14)
# returns index 3 as the answer which is not right.. interesting.

'''
Quiz 2.9.15: Write a procedure dot_product_list(needle,haystack) with the following
spec:
• input: a short list needle and a long list haystack, both containing numbers
• output: a list of length len(haystack)-len(needle) such that entry i of the output list
equals the dot-product of the needle with the equal-length sublist of haystack starting at
position i
Your procedure should use a comprehension and use the procedure list_dot(u,v) from Quiz 2.9.4.
Hint: you can use slices as described in Section 0.5.5.
'''
def dot_product_list(needle, haystack):
    return [list_dot(needle, haystack[i:i+len(needle)]) for i in range(len(haystack)-len(needle)+1)]

q15 = dot_product_list([1,2,3], [1,2,3,4,5,6])
print(q15)

# what I am getting out of this is that the needle in the haystack search using dot product
# only (basically) works for the audio clips and politician voting records comparisons
# because the numbers are oscillating and not ever increasing/decreasing numbers.

