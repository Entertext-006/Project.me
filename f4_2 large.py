def max_of_two(x, y):
    if (x.isdigit() and y.isdigit()):
        if x > y:
            return x
        return y
    else:
        print("not a proper input")

print(max_of_two('a', 6)) 
