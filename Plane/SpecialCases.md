There are some special cases that are discussed below.

1.  The set of equation does not always have a unique solution. It occurs when in a equation we get a nonzero number on left hand side and a zero on right hand side but the equality is contradictory. e.g. 0 = 1.
Then the system is called inconsistent.

For following set of equation the system is Inconsistent.

x + 2y + 3z = 1
3x + 2y + z = 0
7x + 6y + 5z = 2

2. But when a eequation vanishes completely after some elimation steps then we get multiple solutions.
To obtain those solutions we use reduced row-echelon form, in this each pivot variable has coefficient 1 and is in own column.

The example below will explain the above Case.

x + 2y + 3z = 1
3x + 2y + z = 0
7x + 6y + 5z = 1

Operation Steps

1. Add -3Eq.1 to Eq.2       So, Eq.2 : -4y - 8z = -3

2. Add -7Eq.1 to Eq.3       So, Eq.3 : -8y - 16z = -6

3. Add -2Eq.2 to Eq.3       So, Eq.3 : 0 = 0 #In this step the Eq.3 vanishes completely.

"Now we deal with
Pivot Variable : It is variable thet is in a leading term when the system is in triangular form.

Free Variable : A variable in a system which is not a pivot variable. It becomes the parameters of a parametrization of a solution set."

4. Make coefficient of pivot variable equal to 1. So, Multiply Eq.2 by (-1/4)     So, Eq.2 : y + 2z = 3/4

5. Clear above pivot variable. So, Add -2Eq.2 to Eq.1       So, x - z = (-1/2)

6. Now Each pivot variable has coefficient 1 and is in own column as shown below.

x     -  z = (-1/2)
    y + 2z = 3/4
         0 = 0

The solution is shown in a image named SpecialCase.