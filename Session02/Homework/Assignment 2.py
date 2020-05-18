# Example 1:
# x = 159 
# y = (123+36)
# print(x==y)

# x = 159 
# y = (15*9)
# print(x==y)

# x = 'Momo '
# test = x + 'Tarou' != 'Momo Tarou'
# print(test)


# Example 3:
# x = int(input('Enter evaluation score? '))
# if x > 5:
#     if x >= 8:
#         print('Pass;', 'Good')
#     else:
#         print('Pass;', 'Need to improve more')
# else:
#     print('Not pass')


# Turtle exercises
#1
# from turtle import *
# color('red')
# for j in range(4):
#     for i in range(4):
#         if i == 0:
#             left(120)
#         elif i == 2:
#             right(120)
#         else:
#             right(60)
#         forward(100)
#     left(30)
# mainloop()


#2
# from turtle import *
# color('red')
# for edge in range (3, 7):
#     for i in range (edge):
#         forward(100)
#         left(360/edge)
#         if edge == 3 or edge == 5:
#             color('blue')
#         else:
#             color('red')
# mainloop()


#Serious exercises
#1
# weight = float(input("Please enter your weight (kg): "))
# height = float(input("Please enter your height (cm): "))
# height_m = height / 100
# BMI = weight / height_m**2

# if BMI < 16:
#     print("Severely Underweight")
# elif 16 <= BMI < 18.5:
#     print("Underweight")
# elif 18.5 <= BMI < 25:
#     print("Normal")
# elif 25 <= BMI <= 30:
#     print("Overweight")
# else:
#     print("Obese")


#2
# n = int(input('Enter the number n: '))
# f = 1
# for i in range(1,n+1):
#     f = f*i
# print('n! =', f)


#3
# a)
# i.
# print(*range(20))


# ii.
# n = int(input('Enter a number: '))
# print(*range(n))


# b)
# i.
# while True:
#     print(1, 0, end = ' ')


# ii.
# n = int(input('Enter the total number of 1 and 0: '))
# for i in range(n):
# 	if i % 2 == 0:
# 		print(1, end = ' ')
# 	else:
# 		print(0, end = ' ')


# c)
# i.
# for i in range(1,10):
# 	for j in range(1,10):
# 		print(i*j, end = ' ')
# 	print()


# ii.
# n = int(input('Enter a number: '))
# for i in range(1,n+1):
# 	for j in range(1,n+1):
# 		print(i*j, end = ' ')
# 	print()


# d)
# i.
# for i in range(10):
#     for j in range(10):
#         if (i % 2) == (j % 2):
#             print(1, end = ' ')
#         else: 
#             print(0, end = ' ')
#     print()


# ii.
# n = int(input('Enter a number: '))
# column = n
# row = n
# for i in range(column):
#     for j in range(row):
#         if (i % 2) == (j % 2):
#             print(1, end = ' ')
#         else: 
#             print(0, end = ' ')
#     print()