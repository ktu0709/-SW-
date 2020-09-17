#py zero game
from random import randint

point=0
apple =Actor("apple")
orange =Actor("orange")
pineapple =Actor("pineapple")

def draw():
    screen.clear()
    screen.draw.text("point :"+str(point),topleft=(10,20))
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x=randint(10,800)
    apple.y=randint(10,600)

def place_orange():
    orange.x=randint(30,800)
    orange.y=randint(60,600)    

def place_pineapple():
    pineapple.x=randint(20,800)
    pineapple.y=randint(80,600)

def on_mouse_down(pos):
    global point  #전역변수를 사용할때는 함수내에서 전역변수라는 것을 명시
    if apple.collidepoint(pos) or orange.collidepoint(pos) or pineapple.collidepoint(pos):
        print("Good Shot!")
        point=point+1
        place_apple()
        place_orange()
        place_pineapple()
    
    else:
        print("game over")
        quit()
    
        
        

