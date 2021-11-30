import turtle, random

n = 10 #nb tortues
tortab = []

def createTurtle():
    for tor in range(10):
        tor= turtle.Turtle()
        tor.color(random.random(),random.random(),random.random())
        tor.shape("circle")
        tor.speed(0)
        tor.penup()
        tor.sety(random.randint(-50,200))
        tor.setx(random.randint(-50,200))
        tortab.append(tor)







createTurtle()

turtle.delay(0)

while True:

    for tor in tortab:
        tor.forward(random.randint(0,30))
        tor.left(45*random.randint(1,5))

input()
