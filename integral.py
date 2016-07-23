def u_sum(ter, a, nex, b):
    if a > b:
        return 0
    return (ter(a) + u_sum(ter, nex(a), nex, b))
def integral(f, a, b, dx):
    return(u_sum(f, (a+dx/2.0), lambda x: x+dx, b))
def cube(x):
    return x*x*x;
print(integral(cube, 0, 1, 1))
