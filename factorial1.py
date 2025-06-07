def fact(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
   
num = int(input("Enter a number: "))
fact(num)
