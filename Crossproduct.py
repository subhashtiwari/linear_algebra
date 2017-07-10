##This is the function of the cross product.
def cross(self, v):
    try:
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = v.coordinates
        new_coordinates = [y_1*z_2 - y_2*z_1 ,
                          -(x_1*z_2 - x_2*z_1),
                          x_1*y_2 - x_2*y_1   ]
        return Vector(new_coordinates)

    except ValueError as e:
        msg = str(e)
        if msg == 'need more than 2 values to unpack':
            self_embedded_in_R3 = Vector(self.coordinates + ('0',))
            v_embedded_in_R3 = Vector(V.coordinates + ('0',))
            return self_embedded_in_R3.cross(v.v_embedded_in_R3)
        elif (msg == 'too many values to unpack' or
              msg == 'need more than 1 value to unpack')
            raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
        else:
            raise e


##This is the function for area of triangle and area of the parallelogram.
def area_of_triangle_with(self, v):
    return self.area_of_parallelogram_with(v) / Deciaml('2.0')


def area_of_parallelogram_with(self, v)
    cross_product = self.cross(v)
    return cross_product.magnitude()


def cross(self, v):
    try:
        x_1, y_1, z_1 = self.coordinates
        x_2, y_2, z_2 = v.coordinates
        new_coordinates = [   y_1*z_2 - y_2*z_1 ,
                            -(x_1*z_2 - x_2*z_1),
                              x_1*y_2 - x_2*y_1   ]
        return Vector(new_coordinates)


def __str__(self):
    coordinates_as_floats = map(float, self.coordinates)
    return 'Vector: {}'.format(coordinates_as_floats)

def __eq__(self, v):
    return self.coordinates == v.coordinates

##In here we have printed the output of the problem.

v = Vector(['8.462', '7.893', '-8.187'])
w = Vector(['6.984', '-5.975', '4.778'])
print '#1:', v.cross(w)

v = Vector(['-8.987','-9.838','5.031'])
w = Vector(['-4.268','-1.861','-8.866'])
print '#2:', v.area_of_parallelogram_with(w)

v = Vector(['1.5', '9.547', '3.691'])
w = Vector(['-6.007', '0,124', '5.772'])
print '#3:', v.area_of_triangle_with(w)