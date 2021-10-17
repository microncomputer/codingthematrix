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

    # Quiz 2.7.4 write procedure to add two Vec's and return the vector sum of the two
    def add(self, v):
        if self.D != v.D:
            raise ValueError("can't add vectors of different dimensions/domains")
        else:
            return Vec(self.D, {d: self.__getitem__(d) + v.__getitem__(d) for d in self.D})

    # Quiz 2.7.5: write procedure to return the negative of a Vec vector
    def __neg__(self):
        return Vec(self.D, {d: -v for d, v in self.f.items()})


# example usage:
v = Vec({'A', 'B', 'C'}, {'A': 1, 'B': -4})
u = Vec({'B', 'A', 'C'}, {'C': 3})
j = v.add(u)

n = -v
#print(n.f)
