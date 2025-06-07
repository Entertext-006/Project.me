def func(n):
    if n == 0:
        return n
    else:
        return func(n-1)
        print(n)
x = func(100)
print(x)