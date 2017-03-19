import re

class Fraction():
    num = 0
    den = 0


# >>> s = "-23/45 + 14/9"
# >>> re.findall(patt,s)
# [( "-23","45","+","14","49")


patt = re.compile(r'(?P<num>-?\d+)/(?P<den>-?\d+)\s*(?P<op>[+\-*/])\s*(?P<num2>-?\d+)/(?P<den2>-?\d+)')
X = Fraction()
Y = Fraction()

while True:
    user_string = input("Enter: <fraction> <operater> <fracion> >> ")
    if user_string:
        data = re.findall(patt, user_string)

    else:
        break




