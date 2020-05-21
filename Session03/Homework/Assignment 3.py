# example = ["hello", 2.0, 5]
# print(example)


#Turtle exercises
# from turtle import *
# speed(-1)
# colors = ['red', 'blue', 'brown', 'yellow', 'grey']

# for i in range (3, 8):
#     color(colors[i-3])
#     for j in range (i):
#         forward(150)
#         left(360/i)
# mainloop()


# Serious exercises (2.1 - 2.3)
# sizes = [5, 7, 300, 90, 24, 50, 75]
# print('Hello, my name is Hiep and these are my sheep sizes\n',sizes,'\n')   #\n xuống dòng
# print('Now my biggest sheep has size', max(sizes), "let's shear it",'\n')
# index_max = sizes.index(max(sizes))
# sizes[index_max] = 8
# print('After shearing, here is my flock\n',sizes,'\n')


# Serious exercises (2.4)
# sizes = [5, 7, 300, 90, 24, 50, 75]
# print('Hello, my name is Hiep and here is my flock\n',sizes,'\n')
# print('Now my biggest sheep has size', max(sizes), "let's shear it",'\n')
# index_max = sizes.index(max(sizes))
# sizes[index_max] = 8
# print('After shearing, here is my flock\n',sizes,'\n')
# for i in range(len(sizes)):
#     sizes[i]+=50
# print('One month has passed, now here is my flock\n',sizes,'\n')
   
   
# Serious exercises (2.5)
# sizes = [5, 7, 300, 90, 24, 50, 75]
# print('Hello, my name is Hiep and here is my flock\n',sizes,'\n')
# for j in range(1,4):
#     print('MONTH', j, ':')
#     for i in range(len(sizes)):
#         sizes[i]+=50
#     print('One month has passed, now here is my flock\n',sizes)
#     print('Now my biggest sheep has size', max(sizes), "let's shear it")
#     index_max = sizes.index(max(sizes))
#     sizes[index_max] = 8
#     print('After shearing, here is my flock\n',sizes,'\n')


# Serious exercises (2.6)
# sizes = [5, 7, 300, 90, 24, 50, 75]
# print('Hello, my name is Hiep and here is my flock\n',sizes,'\n')
# print('Now my biggest sheep has size', max(sizes), "let's shear it")
# index_max = sizes.index(max(sizes))
# sizes[index_max] = 8
# print('After shearing, here is my flock\n',sizes,'\n')
# for j in range(1,3):
#     print('MONTH', j, ':')
#     for i in range(len(sizes)):
#         sizes[i]+=50
#     print('One month has passed, now here is my flock\n',sizes)
#     print('Now my biggest sheep has size', max(sizes), "let's shear it")
#     index_max = sizes.index(max(sizes))
#     sizes[index_max] = 8
#     print('After shearing, here is my flock\n',sizes,'\n')
# print('MONTH', 3, ':')
# for i in range(len(sizes)):
#     sizes[i]+=50
# print('One month has passed, now here is my flock\n',sizes,'\n')
# total = 0
# for i in range(len(sizes)):
#     total+=sizes[i]
# print('My flock has size in total:', total)
# print('I would get', total, '* 2$ =', total*2,'$')


#Jumble game
#3a
# from random import shuffle
# from getpass import getpass

# quiz = getpass('Enter your quiz: ').lower()

# list_quiz = list(quiz)
# shuffle(list_quiz)
# for i in range(len(list_quiz)):
#     print(list_quiz[i].lower(), end=' ')
# print('\n',end = '')
# ans = input('Your answer: ')
# if ans == quiz:
#     print('Hura')
# else:
#     print(':(')

#3b
from random import choice
from random import shuffle
from getpass import getpass

word_list = ['meticulous','champion','hexagon']
getpass('Your quiz: ').lower()
for i in word_list:
    quiz = choice(word_list)
    list_quiz = list(quiz)
    shuffle(list_quiz)
    for j in range(len(list_quiz)):
        print(list_quiz[j].lower(), end=' ')
    print('\n',end = '')
    ans = input('Your answer: ')
    if ans == quiz:
        print('Hura')
    else:
        print(':(')
