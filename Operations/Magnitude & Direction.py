from math import sqrt

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError:
            self.coordinate = tuple(coordinates)
            self.dimansion = len(coordinates)
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def magnitude()self:
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))


    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')


    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __equ__(self, v):
        returnself.coordinates == v.coordinates


v = Vector([-0.221, 7.437])
print v.magnitude()

v = Vector([8.813, -1.331, -6.247])
print v.normalized()

v = Vector([5.581, -2.136])
print v.normalized()

v = Vector([1.996, 3.108, -4.554])
print v.normalized()