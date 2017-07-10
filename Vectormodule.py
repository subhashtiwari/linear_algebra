class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                self.coordinates = tuple(coordinates)
                self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates


my_vector = Vector([1,2,3])        
print my_vector

my_vector2 = Vectro([1,2,3])
my_vector3 = Vector([-1,2,3])

print my_vector == my_vector2
print my_vector == my_vector3