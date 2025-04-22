from turtle import Turtle, Screen
from random import randint


score=0
game_running=True
speed=0;

tim = Turtle()
tim.penup()
tim.shape("square")
tim.color("white")

tim1 = Turtle()
tim1.penup()
tim1.shape("square")
tim1.color("white")
tim1.setpos(-20, 0)

tim2 = Turtle()
tim2.penup()
tim2.shape("square")
tim2.color("white")
tim2.setpos(-40, 0)


food = Turtle()
food.penup()
food.shape("circle")
food.color("white")
fposx = randint(-280, 280)  
fposy = randint(-280, 280)  
food.setpos(fposx, fposy)


snakelength = [tim, tim1, tim2]
turtlewrite=Turtle()

def do():
   
    global game_running
    global speed
    x=tim.xcor()
    y=tim.ycor()
    if(x>=300 or x<=-300 or y>=300 or y<=-300):
        game_running=False
        speed +=2
        t=Turtle()
        t.penup()
        t.color("white")
        t.hideturtle()
        t.write(f"GAME OVERRR!!!", font=("Arial", 20, "bold"), align="center")

    for i in range(1, len(snakelength)):
        if tim.distance(snakelength[i])<8:
            t=Turtle()
            game_running=False
            t.penup()
            t.color("white")
            t.hideturtle()
            t.write(f"GAME OVERRR!!!", font=("Arial", 20, "bold"), align="center")

    
    global score
    if tim.distance(food) < 15:  
        newT = Turtle()
        score+=1
    
        
        turtlewrite.clear()
        turtlewrite.penup()
        turtlewrite.color("white")
        turtlewrite.hideturtle()
        turtlewrite.goto(0,280)
        #turtlewrite.write("Home = ", align="top")

        turtlewrite.write(f"Score = {score}", font=("Arial", 14, "bold"), align="center")
        newT.penup()
        newT.shape("square")
        newT.color("white")
        snakelength.append(newT)
        
       
        food.clear()
        fposx = randint(-280, 280)
        fposy = randint(-280, 280)
        food.setpos(fposx, fposy)
    
    
    tim.penup()
    pp = tim.pos()
    tim.forward(10)
    

    for i in range(1, len(snakelength)):
        snakelength[i].penup()
        pos = snakelength[i].pos()
        snakelength[i].goto(pp)
        pp = pos

    
    screen.update()


def do1():
    if tim.heading() != 180:  
        tim.setheading(0)  

def do2():
    if tim.heading() != 0:  
        tim.setheading(180)  

def do3():
    if tim.heading() != 270:  
        tim.setheading(90)  

def do4():
    if tim.heading() != 90:  
        tim.setheading(270)  


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()


screen.tracer(0)


screen.onkey(do1, "Right")
screen.onkey(do2, "Left")
screen.onkey(do3, "Up")
screen.onkey(do4, "Down")


def start_game():
    global game_running;
    global speed
    turtlewrite.clear()
    turtlewrite.penup()
    turtlewrite.color("white")
    turtlewrite.hideturtle()
    turtlewrite.goto(0,280)
   

    turtlewrite.write(f"Score = {score}", font=("Arial", 14, "bold"), align="center")

    do() 
    if game_running:
        screen.ontimer(start_game, 100-speed)  


start_game()


screen.mainloop()
