# from random import shuffle

# quiz = input('Enter your quiz: ').lower()

# list_quiz = list(quiz)
# shuffle(list_quiz)
# for i in range(len(list_quiz)):
#     print(list_quiz[i].upper(), end=' ')

# ans = input('Your guess? ')
# if ans == quiz:
#     print('Bingo!!')
# else:
#     print(':(')



from random import shuffle
from getpass import getpass

quiz = getpass('Enter your quiz: ').lower()

list_quiz = list(quiz)
shuffle(list_quiz)
for i in range(len(list_quiz)):
    print(list_quiz[i].upper(), end=' ')

ans = input('Your guess? ')
if ans == quiz:
    print('Bingo!!')
else:
    print(':(')
