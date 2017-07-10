def is_orthogonal_to(self, v, tolerance=1e-10):
    return abs(self.dot(v)) < tolerance

def is_parallel_to(self, v):
    return ( self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi )

def is_zero(self, tolerance=1e-10):
    return self.magnitude() < tolerance 

print 'first pair...'
v = Vector(['-7.579', '-7.88'])
w = Vector(['22.737', '23.64'])
prit 'is parallel : ', v.is_parallel_to(w)
print 'is orthogonal : ', v.is_orthogonal_to(w)

print 'second pair...'
v = Vector(['-2.029', '9.97', '4.172'])
w = Vector(['-9.231', '-6.639', '-7.245'])
print 'is parallel : ', v.is_parallel_to(w)
print 'is parallel : ', v.is_orthogonal_to(w)

print 'third pair...'
v = Vector(['-2.328', '-7.284', '-1.214'])
w = Vector(['-1.821', '1.072', '-2.94'])
print 'is parallel : ', v.is_parallel_to(w)
print 'is parallel : ', v.is_orthogonal_to(w)

print 'fourth pair...'
v = Vector(['2.118', '4.827'])
w = Vector(['0', '0'])
prit 'is parallel : ', v.is_parallel_to(w)
print 'is orthogonal : ', v.is_orthogonal_to(w)