def gcd(x, y):
    while(x % y != 0):
        tmp = x
        x = y
        y = tmp % y
    return y

def make_rat(x, y):
    #tmp = [x,y] #x is numerator and y is denominator
    g=gcd(x, y)
    tmp = [int(x / g), int(y / g)]
    return tmp
def add_rat(a, b):
    tmp = make_rat(a[0] * b[1] + b[0] * a[1], a[1] * b[1])
    return tmp
def sub_rat(a, b):
    tmp = make_rat(a[0] * b[1] - b[0] * a[1], a[1] * b[1])
    return tmp
def mul_rat(a, b):
    tmp = make_rat(a[0] * b[0], a[1] * b[1])
    return tmp
def div_rat(a, b):
    tmp = make_rat(a[0] * b[1], a[1] * b[0])
    return tmp
def equal_rat(a, b):
    return a[0] == b[0] and a[1] == b[1]
rat = add_rat(make_rat(1, 3), make_rat(1, 2))
print( str(rat[0]) + "/" + str(rat[1]))
rat = sub_rat(make_rat(1, 3), make_rat(1, 2))
print( str(rat[0]) + "/" + str(rat[1]))
rat = mul_rat(make_rat(1, 3), make_rat(1, 2))
print( str(rat[0]) + "/" + str(rat[1]))
rat = div_rat(make_rat(1, 3), make_rat(1, 2))
print( str(rat[0]) + "/" + str(rat[1]))

