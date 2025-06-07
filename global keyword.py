'''c=1
def add():
    print(c)
add()








c=1
def add():
    c=c+2
    print(c)
add()'''

c=1
print(c)
def add():
    global c
    c=c+2
    print("inside add():",c)
add()
print("in main program:",c)
