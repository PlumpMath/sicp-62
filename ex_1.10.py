def Ackemann(x, y):
    if(y == 0):
        return 0
    if(x == 0):
        return 2 * y
    if(y == 1):
        return 2
    return Ackemann(x - 1, Ackemann(x, y - 1))

print(Ackemann(1, 10))
print(Ackemann(2, 4))
print(Ackemann(3, 3))

