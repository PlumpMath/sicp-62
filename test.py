def gcd(x, y):
    while(x % y != 0):
        print(x)
        print(y)
        x = y
        y = (x % y)
    return y
print(gcd(4,5))
