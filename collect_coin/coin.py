from random import randint
import time
Width=400
Height=400
score=0
game_over=False
time_left=10
restart=False

fox=Actor("fox")
fox.pos=100,100

coin=Actor("coin")
coin.pos=200,200



def draw():
    global time_left
    global restart
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("score : "+str(score),
    color="black",topleft=(10,10))
    screen.draw.text(str(time_left),color="black",topleft=(700,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score : "+str(score),
        topleft=(10,10),fontsize=60)    
        if keyboard.up:
            restart=True
            if restart:
             screen.clear()
             screen.fill("green")
             time_left=10
             fox.draw()
             coin.draw()
             screen.draw.text("score : "+str(score),
             color="black",topleft=(10,10))
             screen.draw.text(str(time_left),color="black",topleft=(700,10))

def time_up():
    global game_over
    game_over=True

def timer():
    global time_left
    time_left = time_left - 1
    if time_left==0:
        time_up
   
def place_coin():
    coin.x=randint(20,Width-20)
    coin.y=randint(20,Height-20)

def update():
    global score
    global least_time

    coin_collected=fox.colliderect(coin)

    if coin_collected:
        score=score+10
        place_coin()

    if keyboard.left:
        fox.x=fox.x-5
    elif keyboard.right:
        fox.x=fox.x+5
    elif keyboard.up:
        fox.y=fox.y-5
    elif keyboard.down:
        fox.y=fox.y+5
    
    clock.schedule(time_up,10.0)
    clock.schedule_interval(timer, 1.0)

    
