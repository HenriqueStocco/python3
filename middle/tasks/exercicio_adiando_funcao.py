def add(x, y):
    return x+y


def multiply(x, y):
    return x*y


def exec(func, x):

    def intern(y):
        return func(x, y)
    
    return intern


sum_with_five = exec(add, 5)
multiply_with_ten = exec(multiply, 10)
print(sum_with_five(10))
print(multiply_with_ten(10))