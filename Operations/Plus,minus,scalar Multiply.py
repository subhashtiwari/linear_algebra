def plus(self, v):
    new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    return Vector(new_coordinates)

def minus(self, v):
    new_coordinates = [x-y for x,y in zip(self.coordinates, v.new_coordinates)]
    return Vector(new_coordinates)

def times_scalar(scalar, c):
    new_coordinates = [c*x for x in self.coordinates]
    return Vector(new_coordinates)


def __str__(self):
    return 'Vector: {}'.format(self.coordinates)


def __eq__(self, v):
    return self.coordinates == v.coordinates