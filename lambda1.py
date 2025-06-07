'''double=lambda x: x * 2
print(double(5))

def add(x, y):
    return x + y
    
add = lambda x, y: x + y

print(add(3, 5))

square = lambda x: x * x
print(square(4))''' 

string='let us learn more about lambda'
print(lambda string : print(string))

x="let us learn more about lambda"
(lambda x : print(x))(x)

res=(lambda x : x + x)(2)
print(res)

#filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)

words = ["apple", "bat", "cat", "dog", "elephant", "fox"]
long_words = list(filter(lambda word: len(word) > 3, words))
print(long_words)

numbers = [-10, -5, 0, 5, 10, 15]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

words = ["level", "world", "madam", "python", "racecar", "java"]
palindromes = list(filter(lambda word: word == word[::-1], words))
print(palindromes)

# map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)

words = ['apple', 'banana', 'cherry']
uppercased_words = list(map(lambda word: word.upper(), words))
print(uppercased_words)

numbers = [1, 2, 3, 4, 5]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_of_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_of_lists) 

words = ['apple', 'banana', 'cherry']
word_lengths = list(map(lambda word: len(word), words))
print(word_lengths) 

#reduce()
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

from functools import reduce
numbers = [1, 5, 3, 9, 2]
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)

from functools import reduce
words = ['Python', 'is', 'awesome']
sentence = reduce(lambda x, y: x + ' ' + y, words)
print(sentence)

from functools import reduce
lists = [[1, 2], [3, 4], [5, 6]]
flattened_list = reduce(lambda x, y: x + y, lists)
print(flattened_list)''' 











