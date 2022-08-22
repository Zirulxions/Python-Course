
from ast import excepthandler


l = [1,2,3,4,5,6,7,8,9]

# def functionX(list):
#     try:
#         print(l.index(10))
#         return list
#     except ValueError:
#         return False

try:
    l.index(8)
    print("Esta")
except:
    print("No esta")
finally:
    print("o wao")

# for value in range(len(l)):
#     l[value] = 10

# print(functionX(l))
