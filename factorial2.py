def fact(num):
    factorial = 1
    if str(num).isdigit():
        if num < 0:
               print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
               print("The factorial of 0 is 1")
        else:
               for i in range(1,num + 1):
                   factorial = factorial*i
        print("The factorial of",num,"is",factorial)
    else:
        print("its not a number")
   
num = int(input("Enter a number: "))
fact(num)