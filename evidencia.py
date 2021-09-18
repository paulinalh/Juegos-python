"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from random import *
from turtle import *

from freegames import path

stateScore = {'score': 0}
writer = Turtle(visible=False)
finish = Turtle(visible=False)
car = path('car.gif')
letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f' ]
tiles = list(letras) * 2
state = {'mark': None}
hide = [True] * 64
contHide={'contHide':0}


#Funcion que crea los cuadrados del memorama en blanco
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200



def tap(x, y):
    "Update mark and hidden tiles based on tap."
    #Se actualiza el contador de taps 
    writer.undo()
    writer.write(stateScore['score'], font=('Arial', 30, 'normal'))
    stateScore['score'] += 1

    spot = index(x, y)
    mark = state['mark']
    
    #Condicion para esconder la letra del memorama o mostrarla
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        contHide['contHide'] += 1 #se suma 1 al contador de escondidos 
        state['mark'] = None

    #muestra cuando el usuario termino el memorama
    if (contHide['contHide']==32):
        writer.undo()
        writer.write("terminaste", font=('Arial', 10, 'normal'))
        return
    
    



def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y +7)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(600, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
writer.goto(220, 160)
writer.color('black')
writer.write(stateScore['score'], font=('Arial', 30, 'normal'))
listen()
onscreenclick(tap)
draw()
done()