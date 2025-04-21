from turtle import Turtle, Screen
from random import randint


score=0
game_running=True
speed=0;
# Create snake segments
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

# Create food (random position within screen bounds)
food = Turtle()
food.penup()
food.shape("circle")
food.color("white")
fposx = randint(-280, 280)  # Random x position within screen bounds
fposy = randint(-280, 280)  # Random y position within screen bounds
food.setpos(fposx, fposy)

# Snake movement
snakelength = [tim, tim1, tim2]
turtlewrite=Turtle()

def do():
    # Check if the snake's head is near foo
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
    if tim.distance(food) < 15:  # Check if the snake eats the food (distance < 15)
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
        
        # Move the food to a new random position
        food.clear()
        fposx = randint(-280, 280)
        fposy = randint(-280, 280)
        food.setpos(fposx, fposy)
    
    # Move the snake
    tim.penup()
    pp = tim.pos()
    tim.forward(10)
    
    # Move the rest of the snake
    for i in range(1, len(snakelength)):
        snakelength[i].penup()
        pos = snakelength[i].pos()
        snakelength[i].goto(pp)
        pp = pos

    # Update the screen (only if necessary, for smoother animations)
    screen.update()

# Direction control functions
def do1():
    if tim.heading() != 180:  # Check if the snake is not already going left
        tim.setheading(0)  # Right

def do2():
    if tim.heading() != 0:  # Check if the snake is not already going right
        tim.setheading(180)  # Left

def do3():
    if tim.heading() != 270:  # Check if the snake is not already going down
        tim.setheading(90)  # Up

def do4():
    if tim.heading() != 90:  # Check if the snake is not already going up
        tim.setheading(270)  # Down

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.listen()

# Disable automatic screen updates for better performance (manual update instead)
screen.tracer(0)

# Key press events
screen.onkey(do1, "Right")
screen.onkey(do2, "Left")
screen.onkey(do3, "Up")
screen.onkey(do4, "Down")

# Start the snake's automatic movement
def start_game():
    global game_running;
    global speed
    turtlewrite.clear()
    turtlewrite.penup()
    turtlewrite.color("white")
    turtlewrite.hideturtle()
    turtlewrite.goto(0,280)
    #turtlewrite.write("Home = ", align="top")

    turtlewrite.write(f"Score = {score}", font=("Arial", 14, "bold"), align="center")

    do()  # Start moving the snake
    if game_running:
        screen.ontimer(start_game, 100-speed)  # Call start_game again after 100 ms (10 times per second)

# Start the game
start_game()

# Keep the window open
screen.mainloop()
