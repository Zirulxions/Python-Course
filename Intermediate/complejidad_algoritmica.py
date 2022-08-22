# import time
# import sys


# def factorial(n):
#     respuesta = 1
#     while n > 1:
#         respuesta *= n
#         n -= 1
#     return respuesta

# def factorial_r(n):
#     if n == 1:
#         return 1
#     return n * factorial_r(n - 1)


# def my_func(x):
#     respuesta = 0
#     for i in range(2000):
#         respuesta += 1
#     return respuesta

# if __name__ == '__main__':
#     n = 2500
#     sys.setrecursionlimit(n + 10)

#     comienzo = time.time()
#     factorial(n)
#     final = time.time()
#     print(final - comienzo)

#     # del comienzo, final

#     comienzo2 = time.time()
#     # print(factorial_r(n))
#     factorial_r(n)

#     final2 = time.time()
#     print(final2 - comienzo2)

respuesta = 0
for i in range(2000):
    respuesta += 1
print(respuesta)