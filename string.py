#my_string = 'Hello'
#print(my_string)

#my_string = "Hello"
#print(my_string)

#my_string = '''Hello'''
#print(my_string)

#str = 'programming'
#print('str=',str)

#print('str[0] = ', str[0])

#print('str[-1] = ', str[-1])

#print('str[1:5] = ',str[1:5])

#print('str[5:-2] = ',str[5:-2])

#print('str[-5:-2] = ',str[-5:-2])
#print('str[-2:-5] = ',str[-2:-5])

#print('str[:2] = ',str[:2])

#print('str[::2] = ',str[::2])

'''str1="Apple"
str1="Mango"
print(str1)

del str1

print(str1)


my_string = "12345"
#my_string = "123a5"
result = all(char.isdigit() for char in my_string)
print(result)  

my_string = "hello"
#my_string = "bcd"
result = any(char in 'aeiou' for char in my_string)
print(result)

my_string = "hello"
for index, char in enumerate(my_string):
    print(f"Index: {index}, Character: '{char}'")


my_string = "hello, world!"
length = len(my_string)
print(length)


my_string = "xyzabc"
max_char = max(my_string)
print(max_char)

my_string = "xyzabc"
min_char = min(my_string)
print(min_char)

my_string = "hello"
sorted_chars = sorted(my_string)
sorted_chars1 = ''.join(sorted_chars)
print(sorted_chars1)


my_string = "abc"
ascii_sum = sum(ord(char) for char in my_string)
print(ascii_sum)

my_string = "hello"
print(type(my_string))
print(id(my_string))

number = 15
print(number.bit_length())

float_number = float("2.5")
print(float_number)
print(float_number.as_integer_ratio())

my_string = "hello"
s = slice(1, 4)
print(my_string[s])

ascii_value = 99
print(chr(ascii_value))
print(ord("A"))

my_str1="PES"
my_str2=" University "
new_str=my_str1+my_str2
print(new_str)

my_str1=new_str
print(my_str1*5)'''


#python programs to find vowels in a given string
my_str=input("Enter the string\n")
vowels="aeiouAEIOU"
new_str=sum(1 for char in my_str if char in vowels)
print("number of vowels:",new_str)

#python programs to print the strings in reverse order
my_str=input("Enter the string\n")
reverse_string=my_str[::-1]
print(reverse_string)

#python program to validate the given string is palindrome or not
my_str=input("Enter the string\n")
if(my_str == my_str[::-1]):
    print("Both are equal")
else:
    print("Both are different")

#python program to find the length of a string
my_str=input("Enter the string\n")
new_str=len(my_str)
print(new_str)'''

my_str="hello"
print(my_str.capitalize())

my_str="HELLO"
print(my_str.casefold())

my_str="HELLO"
print(my_str.center(50))

my_str="HELLO"
print(my_str.count('L'))

my_str="hello"
print(my_str.encode())

my_str="hello"
print(my_str.endswith('o'))
print(my_str.endswith('l'))

my_str="hello"
print(my_str.expandtabs(10000))'''