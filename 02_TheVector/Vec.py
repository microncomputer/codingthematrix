class Vec:
    def __init__(self, domain, function):
        self.D = domain
        self.f = function

    # Quiz 2.7.1: write a procedure that takes a set D and returns a Vec representing a D-vector all of whose entries
    # have value zero
    def zero_vec(D):
        # return Vec(D, {d: 0 for d in D})
        # it could be computationally simpler by using the sparse-representation convention and saying
        return Vec(D, {})

    def __setitem__(self, key, value):
        self.f[key] = value

    # Quiz 2.7.2 write a procedure which takes an instance v of Vec, an element d of the set v.D
    # returns value of entry d of v
    def __getitem__(self, d):
        return self.f[d] if d in self.f else 0

    # Quiz 2.7.3 write procedure that takes an instance of Vec, v and scalar alpha
    # returns a new Vec that is the scalar multiple of alpha*v
    # *try to make it as sparse as the original
    def scalar_mul(self, alpha):
        # this way does not preserve sparsity(will include everything in the domain in the new function despite 0's):
        # return Vec(self.D, {d:alpha * self.__getitem__(d) for d in self.D})
        # this way preserves sparsity:
        return Vec(self.D, {d: alpha * value for d, value in self.f.items()})

    def __mul__(self, other):
        # scalar multiplication
        if isinstance(other, int) or isinstance(other, float):
            return self.scalar_mul(other)

        # dot product
        if isinstance(other, Vec):
            assert self.D == other.D
            return sum([self[d]*other[d] for d in self.D])


    # Quiz 2.7.4 write procedure to add two Vec's and return the vector sum of the two
    def __add__(self, v):
        if self.D != v.D:
            raise ValueError("can't add vectors of different dimensions/domains")
        else:
            return Vec(self.D, {d: self.__getitem__(d) + v.__getitem__(d) for d in self.D})

    # Quiz 2.7.5: write procedure to return the negative of a Vec vector
    def __neg__(self):
        return Vec(self.D, {d: -v for d, v in self.f.items()})

    '''
    ended up being provided in vecutil.py so I am commenting it out here
    
    # Quiz 2.10.1: list2vec for turning list vectors into Vec vectors
    def list2vec(L):
        return Vec(set(range(len(L))), {i:L[i] for i in range(len(L))})
    '''

    '''
    backward substitution method for solving upper triangular systems:
    '''

def triangular_solve_n(rowlist, b):
    """
    input: for some integer n, a triangular system consisting of a list rowlist of n-vectors, and
        a length-n list b of numbers

    output: a vector x such that, for i = 0, 1,...,n − 1, the dot-product of rowlist[i] with xˆ
        equals b[i]
    """
    D = rowlist[0].D
    n = len(D)
    assert D == set(range(n))
    x = rowlist.zero_vec(D)
    for i in reversed(range(n)):
        x[i] = (b[i] - rowlist[i] * x)/rowlist[i][i]
    return x


# example usage:
v = Vec({'A', 'B', 'C'}, {'A': 1, 'B': -4})
u = Vec({'B', 'A', 'C'}, {'C': 3})
j = v+u

n = -v
t = v*u
#print(n.f)


