#1
# from turtle import *
# n = int(input('So hinh vuong: '))
# speed(-1)
# color('blue')
# for i in range(n):
#     for j in range(4):
#         forward(100)
#         left(90)
#     left(360/n)
# mainloop()


#2
from turtle import *
speed(-1)
color('blue')
Do_dai_canh = 5
for i in range(42):
    for j in range(4):
        forward(Do_dai_canh)
        left(90)
    left(360/30)
    Do_dai_canh += 3
mainloop()