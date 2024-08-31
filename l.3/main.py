import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "Flower collecting"

gameover=False

def over():
    global gameover
    gameover=True

bee = Actor("beebee.png")
flower = Actor("flowert.png")
bee.pos=200,200
def moving():
    k=random.randint(0,500)
    l=random.randint(0,500)
    flower.pos=k,l


def draw():
    screen.blit("grassplain.png", (0,0))
    bee.draw()
    flower.draw()

def update():
    if keyboard.left:
        bee.x=bee.x-10 
    elif keyboard.right:
        bee.x=bee.x+10
    elif keyboard.down:
        bee.y=bee.y+10 
    elif keyboard.up:
        bee.y=bee.y-10
    if bee.colliderect(flower):
        moving()                
    



clock.schedule(over,60)
pgzrun.go()   