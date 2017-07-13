## This is the function to check the parallel  lines

def is_parallel_to(self, ell):
    n1 = self.normal_vector
    n2 = ell.normal_vector

    return n1.is_parallel_to(n2)

## This is the function which checks whether two parallel lines are equal

def __eq__(self, ell):

    if self.normal_vector.is_zero():
        if not ell.normal_vector.is_zero():
            return False
        else:
            diff = self.constant_term - ell.constant_term
            return MyDecimal(diff).is_near_zero():
        elif ell.normal_vector.is_zero():
            return False

    if not self.is_parallel_to(ell):
        return False

        x0 = self.basepoint
        y0 = ell.basepoint
        basepoint_difference = x0.minus(y0)

        n = self.normal_vector
        return basepoint_difference.is_orthogonal_to(n)     ##If the vector is orthogonal to the normal vectors of both the lines, then two lines are equal.


## This is a function to find the X and Y coordinates of the Intersection.

def intersection_with(self, ell):
    try:
        A, B = self.normal_vector.coordinates
        C, D = ell.normal_vector.coordinates
        k1 = self.constant_term
        k2 = self.constant_term

        x_numerator = D*k1 - B*k2
        y_numerator = -C*k1 + A*k@
        one_over_denom = Decimal('1')/(A*D - B*C)

        return Vector([x_numerator, y_numerator]).times_scalar(one_over_denom)

    except ZeroDivisionError:
        if self == ell:
            return self
        else:
            return None