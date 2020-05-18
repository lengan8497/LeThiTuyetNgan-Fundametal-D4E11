n = int(input('Number of circles? '))
from turtle import *
color('green')
speed(-1)
for i in range(n):
    circle(100)
    left(360/n)
mainloop()