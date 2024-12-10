# L=[1,4,6,7,4,3,6,7]
# list_iterator=iter(L)
# # print(list_iterator)
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))
# print(next(list_iterator))


# my_list=[1,2,3]
# my_list_iter=iter(my_list)
#
#
# while True:
#     try:
#         print(next(my_list_iter))
#     except StopIteration:
#         break


# f=open(file="World_cyclones.csv")
# print(next(f))
# print(next(f))



# def try_generator(y):
#     n=y
#     n+=1
#     print("Performed addition")
#     yield n
#
#     n*=2
#     print("Performed multiplication")
#     yield n
#
# result=try_generator(5)
# print(next(result))
# print(next(result))


# def  return_squared(min , max):
#     for i in range(min,max):
#         yield i**2
#
#     result=return_squared(1,5)
#
#     for item in result:
#         print(item)


# my_list_com=[num for num in range(5)]
# print(my_list_com)
#
# my_generator=(num for num in range(5))
# print(my_generator)
# for i in my_generator:
#     print(i)





# def prime_generator():
#     def is_prime(number):
#         if number < 2:
#             return False
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 return False
#         return True
#
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
#
# primes = prime_generator()
# for _ in range(6):
#     print(next(primes))


# import itertools
# def password_generator(input_string):
#     for pwd in itertools.permutations(input_string):
#         yield ''.join(pwd)
#
# input_string="abs"
# passwords=password_generator(input_string)
# for _ in range(6):
#     print(next(passwords))


# def fibonacci_generator():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# fibonacci=fibonacci_generator()
# for _ in range(10):
#     print(next(fibonacci))



# import itertools
#
# def group_generator(lst,n):
#     for group in itertools.combinations(lst,n):
#         yield group
# my_list=[1,2,3,4]
# n=2
# groups=group_generator(my_list,n)
# for group in groups:
#     print(group)


# x=[1,2,3,4,5]
#
# for i in x:
#     print(i)
# for i in iter(x):
#     print(i)


# def basic_gen():
#     yield 1
#     yield 2
# print(basic_gen())
#
# for i in basic_gen():
#     print(i)
#
# basic_gen=basic_gen()
# print(next(basic_gen))


# import matplotlib.pyplot as plt
#
# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]
#
# plt.figure(figsize=(8, 5))
# plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = 2x')
# plt.title('Chiziqli grafik')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.legend()
# plt.show()


# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.linspace(0,2 * np.pi, 100)
# y_sin = np.sin(x)
# y_cos = np.cos(x)
# plt.figure(figsize=(8, 5))
# plt.plot(x, y_sin, label='sin(x)', color='r')
# plt.plot(x, y_cos, label='cos(x)', color='b')
# plt.title('Funksiyalarni taqqoslash sin(x) и cos(x)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid(True)
# plt.legend()
# plt.show()
