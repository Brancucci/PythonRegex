import re # used for regular expressions
from fractions import Fraction # used for fractions

# the regular expression used to extract two fractions and an operator
patt = re.compile(r'(?P<num>-?\d+)/(?P<den>-?\d+)\s*(?P<op>[+\-*/])\s*(?P<num2>-?\d+)/(?P<den2>-?\d+)')

# loop forever until the user entered a blank string or has an error
while True:
    user_string = input("Enter: <fraction> <operater> <fracion> >> ") # get the user string
    if user_string: # if the user entered something ...
        data = re.findall(patt, user_string) # gives us a 5 tuple
        num = int(data[0][0])
        den = int(data[0][1])
        X = Fraction(num, den) # create a fraction object with the lhs of the equation
        num1 = int(data[0][3])
        den1 = int(data[0][4])
        Y = Fraction(num1, den1) # creates a fraction object with the rhs of the equation
        op = data[0][2] # extracts the operator from the user
        # switch statement to apply appropriate operator to calculation
        if op == '+':
            R = X + Y
        elif op == '-':
            R = X - Y
        elif op == '*':
            R = X * Y
        elif op == '/':
            R = X / Y
        else:
            break
            # print the results to user
        print('{} = {}'.format(user_string, R))

    else:
        break




