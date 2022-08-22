# def saludo(function):
#     function()

# def hello_n():
#     print('Sup Nigga !')

# def bye_n():
#     print('Banzai !')

# saludo(hello_n)
# saludo(bye_n)

# FILTER

from functools import reduce

my_list = [1,2,3,4,5]
squares = list(map(lambda x:x**2, my_list))
print(squares)

del my_list, squares

my_list = [1,4,5,8,4,2,51,65,2,47,3,47,5,27]
odd = list(filter(lambda x:x%2 != 0, my_list))
print(odd)

del my_list, odd

my_list = [2,2,2,2,2]
all_multiplied = reduce(lambda a, b: a + b, my_list)
print(all_multiplied)