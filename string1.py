'''my_str="Hi\tHello\tWorld!"
#print(my_str.expandtabs(tabsize=8))
print(my_str.expandtabs(tabsize=15))


my_str="bangalore"
print(my_str.find('g'))
print(my_str.find('z'))

name = "Alice"
age = 30
formatted_string = "My name is {} and I am {} years old.".format
(name, age)
print(formatted_string)
formatted_string1 = f"My name is {name} and I am {age} years old."
print(formatted_string1)

my_str="bangalore"
print(my_str.index('g'))
print(my_str.find('g'))'''

'''text1 = "Hello123"
print(text1.isalnum())  

text2 = "Hello 123"
print(text2.isalnum())

text3 = "Hello!"
print(text3.isalnum())  

text4 = ""
print(text4.isalnum())


#my_str="abcde"
my_str="2233"
print(my_str.isalpha())

#my_str="23456"
my_str="aaaaa"
print(my_str.isdecimal())

my_str="23456"
#my_str="aaaaa"
print(my_str.isdigit())

my_str="var123"
print(my_str.isidentifier())

my_str="True"
print(my_str.isidentifier())

strings = ["variable", "var123", "_var", "123var", "var iable", "var@iable", ""]

for s in strings:
    if s.isidentifier():
        print(f"'{s}' is a valid Python identifier.")
    else:
        print(f"'{s}' is NOT a valid Python identifier.")

#my_str="abcdfe"
my_str="AbhTf"
print(my_str.islower())

#my_str="ABDEHV"
my_str="cbvsDT"
print(my_str.isupper())

#my_str="1234"
my_str="12g4"
print(my_str.isnumeric())

string1 = "Hello World!"
print(string1.isprintable())  

string2 = "Hello\nWorld!"
print(string2.isprintable())  

string3 = "Hello\tWorld!"
print(string3.isprintable())  

string4 = ""
print(string4.isprintable())'''

string1 = "   "
print(string1.isspace())  

string2 = "\t"
print(string2.isspace())  

string3 = " \n "
print(string3.isspace())  

string4 = "Hello World"
print(string4.isspace())  

string5 = ""
print(string5.isspace())

my_str="introduction to python"
print(my_str.title())

string1 = "Hello World"
print(string1.istitle())  

string2 = "hello world"
print(string2.istitle())  

string3 = "Hello WoRld"
print(string3.istitle())  

string4 = "Python 101"
print(string4.istitle())  

string5 = "Welcome To The Jungle!"
print(string5.istitle())  

string6 = ""
print(string6.istitle())

characters = "ABCDE"
result = "-".join(characters)
print(result) 

words = "Python is fun"
result = " ".join(words)
print(result)

words = "Python is fun"
result = "".join(words)
print(result)

letters = ['H', 'e', 'l', 'l', 'o']
print(letters)
result = ''.join(letters)
print(result)

text = "Python"
result = text.ljust(50)
#print(result)
print(f"'{result}'")

text = "Python"
result = text.ljust(50, '-')
print(result)

text = "Python"
result = text.rjust(50)
#print(result)
print(f"'{result}'")

text = "Python"
result = text.rjust(50, '-')
print(result)

#text = "HELLO, PYTHON!"
text = "Python Is AWESOME!"
result = text.lower()
print(result)

#text = "HELLO, PYTHON!"
text = "Python Is AWESOME!"
result = text.upper()
print(result)

text = "Hello Students"
text1 = "     Hello Students"
print(text.strip())
print(text1.strip())

text = "   Hello, Python!   "
result = text.lstrip()
print(f"'{result}'")

#text = "000123456"
#text = "000122223456"
text = "2222210567"
result = text.lstrip('0')
print(result)

text = "   Hello, Python!   "
result = text.rstrip()
print(f"'{result}'")

#text = "0123456666"
#text = "0122223456666"
text = "2222210567"
result = text.rstrip('0')
print(result)

text = "Hello, Python is awesome!"
result = text.partition('Python')
print(result)

text = "Hello, world!"
result = text.partition('Python')
print(result)

text = "apple-banana-cherry"
result = text.partition('-')
print(result)

text = "Hello, Python is awesome!"
result = text.rpartition('Python')
print(result)

text = "Hello, world!"
result = text.rpartition('Python')
print(result)

text = "apple-banana-cherry"
result = text.rpartition('-')
print(result)

text = "I love Python. Python is awesome!"
new_text = text.replace('Python', 'programming')
print(new_text)

text = "I love Python. Python is awesome!"
new_text = text.replace('Python', 'programming', 1)
print(new_text)

text = "apple, banana, cherry"
new_text = text.replace(',', ';')
print(new_text)

text = "Python is fun, and Python is powerful."
#index = text.rfind('Python')
index = text.rfind('java')
print(index)

text = "Python is fun, and Python is powerful."
index = text.rfind('fun',0, 15)
print(index)

text = "Python is fun, and Python is powerful."
index = text.rfind('Python')
#index = text.rindex('java')
print(index)

text = "Python is fun, and Python is powerful."
index = text.rindex('fun',0, 15)
print(index)

my_str="hello"
print(my_str.startswith('h'))
print(my_str.startswith('l'))

my_str="Python CLASS"
print(my_str.swapcase())

my_str="123"
print(my_str.zfill(10))

my_str="This is the python class"
print(my_str.split())

my_str="This is the python class"
print(my_str.split(','))

my_str="This is the python class"
print(my_str.split(':'))

my_str="This&is&the&python&class"
print(my_str.split('&',1))

my_str="This&is&the&python&class"
print(my_str.split('&',0))

my_str="This&is&the&python&class"
print(my_str.split('&',4))

my_str="This is the python class"
print(my_str.rsplit())

my_str="This is the python class"
print(my_str.rsplit(','))

my_str="This is the python class"
print(my_str.rsplit(':'))

my_str="This&is&the&python&class"
print(my_str.rsplit('&',1))

my_str="This&is&the&python&class"
print(my_str.rsplit('&',0))

my_str="This&is&the&python&class"
print(my_str.rsplit('&',4))

my_str="This\nis\nthe\npython\nclass"
print(my_str.splitlines())

















