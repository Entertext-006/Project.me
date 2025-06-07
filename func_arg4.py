'''def greet(*names):
    for name in names:
        print("hello",name)
greet("kate","monica","steve","john")


def add(*n):
    res=0
    for i in n:
        res= res + i
        i=i+1
    print(res)
add(2,3,4,5,10)

def add1(a,b):
    c=a+b
    print(c)
add1(2,3)'''


def sqr(*n):
    res=0
    for i in n:
        res= i * i * i
        print(res)
sqr(2,3,4,5,10)
