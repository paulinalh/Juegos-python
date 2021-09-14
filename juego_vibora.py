"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
foodPos= vector(-15,15)
color =['black', 'yellow', 'green', 'blue', 'purple']
colorBody=random.choice(color)
colorFood=random.choice(color)
while(colorFood==colorBody):
    colorFood=random.choice(color)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def changeFood(x, y):
    "Change food position."
    arrPaso=[-10,10,0]
    if(x==151 or x==-151 or y==151 or y==-151):
            x = 0
            y = 0
    else:
        x = x+random.choice(arrPaso)
        y = y+random.choice(arrPaso)

    square(x, y, 9, colorFood
    )



def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    #direccion=1

    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, colorBody
)

    
    arrPaso=[-1,1,0]
    arrDir=[1,2,3,4]
    direccion=random.choice(arrDir)
    if(head != food):
        changeFood(food.x,food.y)


    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()