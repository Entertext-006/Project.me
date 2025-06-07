str1 = "chamarajanagara"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)
print('length:', len(str1))