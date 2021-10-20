# quiz 2.9.4: Write a procedure list_dot(u, v) with the following spec:
# • input: equal-length lists u and v of field elements
# • output: the dot-product of u and v interpreted as vectors
# Use the sum(·) procedure together with a list comprehension.


def list_dot(u, v):
    assert len(u) == len(v)
    return sum([u[i]*v[i] for i in range(len(u))])


print(list_dot([1, 2, 3], [2, 2, 2]))