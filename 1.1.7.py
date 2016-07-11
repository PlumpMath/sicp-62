def average(x, y):
    return (x + y) / 2
def square(x):
    return x*x
def good_enough(guess, x):
    return (abs(square(guess) - x) < 0.001);
def improve(guess, x):
    return average(guess, (x / guess))
def sqrt_iter(guess, x):
    if(good_enough(guess, x)):
        return guess
    else:
        return (sqrt_iter (improve(guess, x), x) )

def sqrt(x):
    return (sqrt_iter(1.0, x))

print(sqrt(9))
print(sqrt(100 + 37))
print(sqrt(sqrt(2) + sqrt(3)))


