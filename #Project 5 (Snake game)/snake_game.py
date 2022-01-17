#sorry this game dont work properly
import turtle
import time
import random

delay = 0.1

score = 0
high_Score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor('yellow')
wn.setup(width=600, height=600)
wn.tracer(0)

#Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Snake food
# foodShape = random.Random("square", "rectangle")
# foodColour = random.Random("Red", "Green")
food  = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#scorebar
sc = turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("black")
sc.penup()
sc.hideturtle()
sc.goto(0, 260)
sc.write("score: 0  High Score :0", align="center", font=("ds-digital", 24, "normal"))

#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"  
def go_right():
    if head.direction != "left":
        head.direction = "right"  

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

#MainLoop
while True:
    wn.update()

    #check collision with border area 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #Hide the segment of the body
        for segment in segments:
            segments.goto(1000, 1000) #out of range 
        #Clear the segment 
        segments.clear()

        #reset the score
        score = 0 

        #reset delay 
        delay = 0.1

        sc.clear()
        sc.write(f"Score: {score} High Score: {high_Score}", align="center", font=("ds-digital", 24, "normal"))

    #check collision with food
    if head.distance(food) <20:
        # move the food to random place 
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        # Add a new segment to the head 
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)


        delay -= 0.001

        score += 10

        if score > high_Score:
            high_Score = score
        sc.clear()
        sc.write(f"Score: {score}, High score: {high_Score}", align="center", font=("ds-digital", 24, "normal"))
    
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments)>0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    for segments in segments:
        if segments.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            score = 0
            delay = 0.1

            sc.clear()
            sc.write(f"Score: {score}, High score: {high_Score}", align="center", font=("ds-digital", 24, "normal"))
    time.sleep(delay)
wn.mainloop()
