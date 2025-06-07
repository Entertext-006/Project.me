def factorial(x):
    """This is a recursive function to find the
    find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x*factorial(x-1))
x=factorial(4)
print("The factorial is", x)
