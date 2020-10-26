import random
import time
import turtle
from datetime import date


delay = 0.12
dif = 0.15
menu = False

GameScreen = turtle.Screen()
GameScreen.setup(width=1300, height=900)
GameScreen.tracer(0)
GameScreen.bgcolor("Green")
#Snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"


food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("Yellow")
food.penup()
food.goto(0, 0)

#Score
pen = turtle.Turtle()
pen.shape("square")
pen.color("black")
pen.hideturtle()
pen.goto(0,350)

#tail
tail = []
score = 0
r = open("personalbest.txt", "r")
content=r.read()
personal_best=0
personal_best = int(content[:2])



def menu_screen():
    global menu
    if menu == True:
        menu = False
        GameScreen.update()
        GameScreen.mainloop()
    if menu == False:
        menu = True
        GameScreen.update()
        GameScreen.mainloop()

#difficulties
def easy():
    global dif, delay
    dif = 0.2
    delay = 0.2
    pen.clear()
    pen.write("Score?: {}  Personal Best: {} Dif:{}, press 'm' to open up a menu".format(score, personal_best, delay),
              align="center",
              font=("Calibri", 20, "bold"))


def normal():
    global dif, delay
    dif = 0.1
    delay = 0.1
    pen.clear()
    pen.write("Score?: {}  Personal Best: {} Dif:{}, press 'm' to open up a menu".format(score, personal_best, delay),
              align="center",
              font=("Calibri", 20, "bold"))


def hard():
    global dif, delay
    dif = 0.05
    delay = 0.05
    pen.clear()
    pen.write("Score?: {}  Personal Best: {} Dif:{}, press 'm' to open up a menu".format(score, personal_best, delay),
              align="center",
              font=("Calibri", 20, "bold"))


#Directions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


#binds
GameScreen.listen()
GameScreen.onkeypress(menu_screen, "m")
GameScreen.onkeypress(go_up, "Up")
GameScreen.onkeypress(go_down, "Down")
GameScreen.onkeypress(go_left, "Left")
GameScreen.onkeypress(go_right, "Right")
GameScreen.onkeypress(easy, "1")
GameScreen.onkeypress(normal, "2")
GameScreen.onkeypress(hard, "3")


def directions():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


def die():
    global delay, score
    time.sleep(0)
    head.goto(0, 0)
    head.direction = "stop"
    for part in tail:
        part.goto(50000, 50000)
    tail.clear()
    score = 0
    delay = 0.1

    message()


def message():
    pen.clear()
    pen.write("Score?: {}  Personal Best: {} Dif:{}, press 'm' to open up a menu".format(score, personal_best, delay),
              align="center",
              font=("Calibri", 20, "bold"))


def Arena():
    turtle.clear()
    turtle.penup()
    turtle.speed(0)
    turtle.pensize(15)
    turtle.shape("circle")
    turtle.color("black")
    turtle.goto(-304,304)
    turtle.pendown()
    turtle.goto(304,304)
    turtle.goto(304,-304)
    turtle.goto(-304,-304)
    turtle.goto(-304,304)
    turtle.penup()
    turtle.goto(0,0)
    turtle.color("green")
    turtle.hideturtle()
    turtle.goto(0,0)

while (menu == False):
    GameScreen.update()
    Arena()
    #
    if (head.xcor() >= 302 or head.xcor() <= -302 or head.ycor() <= -302 or head.ycor() >= 302):
        die()
        message()

    if (head.distance(food) < 21):
        food.goto(random.randint(-290,290),random.randint(-290,290))
        #add_tail
        add_tail=turtle.Turtle()
        add_tail.speed(0)
        add_tail.penup()
        add_tail.shape("circle")
        add_tail.color("grey")
        tail.append(add_tail)
        #speed
        score=score+1
        if (delay>=0.03):
            delay = delay - 0.012
        #add score
        if (score>personal_best):
            personal_best=score
            f = open("personalbest.txt", "w")
            f.write(str(personal_best) + " date: " + str(date.today()))
            f.close()
        message()
    #add tail backwards
    for i in range((len(tail) - 1), 0, -1):
        tail[i].goto(tail[i - 1].xcor(),tail[i - 1].ycor())
    #attach to the back
    if (len(tail) > 0):
        tail[0].goto(head.xcor(),head.ycor())
    #moving to selected direction
    directions()
    #body collision
    for tails_part in tail:
        if tails_part.distance(head) < 19:
            die()
    time.sleep(delay)

GameScreen.mainloop()
