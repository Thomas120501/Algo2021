import turtle, random


tor= turtle.Turtle()
tor1= turtle.Turtle()
tor2= turtle.Turtle()

tor.pencolor("red")
tor1.pencolor("blue")
tor2.pencolor("green")

tor.speed(0)
turtle.delay(0)

for i in range(0,10000):
    tor.forward(random.randint(0,30))
    tor.left(45*random.randint(1,5))
    tor1.forward(random.randint(0,50))
    tor1.left(45*random.randint(1,5))
    tor2.forward(random.randint(0,30))
    tor2.left(45*random.randint(1,5))

input()
