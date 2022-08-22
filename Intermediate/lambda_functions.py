def palindrome_2(string):
    return string == string[::-1]

print(palindrome_2('arepera'))



palindrome = lambda string: string == string[::-1]

print(palindrome('arepera'))