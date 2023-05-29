import turtle as trtl
import turtle
from turtle import Screen
import random
import time
import random
import simpleaudio as sa

#Setting up the screen
screen = trtl.Screen()
screen.bgpic('equationsBoard.png')
screen.bgcolor('#edd9b8')

#Creating writing/drawing turtle
painter = trtl.Turtle()
painter.hideturtle()
painter.speed(-1)
painter.color('#69BF80')
painter.pensize(3)
painter.penup()
painter.goto(-360, 292)
painter.pendown()

#Drawing Timer Box
painter.goto(-510, 292)
painter.goto(-510, 230)
painter.goto(-360, 230)
painter.goto(-360, 292)

#Creating Countdown Writing Turtle
countdownWriter = trtl.Turtle()
countdownWriter.hideturtle()
countdownWriter.speed(-1)
countdownWriter.penup()
countdownWriter.goto(-473, 243)

#Creating Dice Roll Turtle
roller = trtl.Turtle()
roller.hideturtle()
roller.penup()
roller.goto(473, 0)
roller.shape('square')
roller.color('cornflower blue')
roller.turtlesize(4)
roller.showturtle()

#Writing Roll
painter.penup()
painter.goto(473,40)
painter.pencolor("navy")
painter.write("ROLL", align = "center", font=("Helvetica", 30, "bold"))

#Creating Sound Cancelling Turtle
canceller = trtl.Turtle()
canceller.hideturtle()
canceller.penup()
canceller.shape('square')
canceller.goto(-500, -300)
canceller.turtlesize(2)
canceller.color('red')
canceller.showturtle()

#Creating Cat Turtle
cat = trtl.Turtle()
cat.hideturtle()
cat.penup()
screen.addshape("cat.gif")
cat.shape("cat.gif")
cat.goto(520, -250)
cat.turtlesize(2)
cat.showturtle()

#Creating Cat Meow Wave Object
meow_wave_obj = sa.WaveObject.from_wave_file("meow.wav")

#Meow Playing Function
def play_meow(x,y):
    global meow_wave_obj
    # sa.stop_all()
    play_obj = meow_wave_obj.play()

# define the countdown func. 
def countdown(t, timer):
    
    countdownWriter.clear()

    #Set Number of Seconds to 60 (One Minute)
    t = 60
    
    #Until Time Runs Out
    while t > 0: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        countdownWriter.write(timer, font=("Helvetica", 30, "bold"))
        time.sleep(1) 
        t -= 1
        countdownWriter.clear()
    countdownWriter.goto(-498, 245)
    countdownWriter.write("Time's Up!", font=("Helvetica", 25, "bold"))

#Cancel Sound Function
def cancel_sound(x, y):
    sa.stop_all()

#Roll Function
def roll(x,y): 

    #Get Dice Images
    blue1 = ("blue1.gif")
    blue2 = ("blue2.gif")
    blue3 = ("blue3.gif")
    blue4 = ("blue4.gif")
    blue5 = ("blue5.gif")
    blue6 = ("blue6.gif")

    #Add Dice Images as Shapes
    screen.addshape(blue1)
    screen.addshape(blue2)
    screen.addshape(blue3)
    screen.addshape(blue4)
    screen.addshape(blue5)
    screen.addshape(blue6)

    blueChoices = [blue1, blue2, blue3, blue4, blue5, blue6]
    blueCubes = []

    #Get Dice Images
    red1 = ("red1.gif")
    red2 = ("red2.gif")
    red3 = ("red3.gif")
    red4 = ("red4.gif")
    red5 = ("red5.gif")
    red6 = ("red6.gif")

    #Add Dice Images as Shapes
    screen.addshape(red1)
    screen.addshape(red2)
    screen.addshape(red3)
    screen.addshape(red4)
    screen.addshape(red5)
    screen.addshape(red6)

    redChoices = [red1, red2, red3, red4, red5, red6]
    redCubes = []

    #Get Dice Images
    black1 = ("black1.gif")
    black2 = ("black2.gif")
    black3 = ("black3.gif")
    black4 = ("black4.gif")
    black5 = ("black5.gif")
    black6 = ("black6.gif")

    #Add Dice Images as Shapes
    screen.addshape(black1)
    screen.addshape(black2)
    screen.addshape(black3)
    screen.addshape(black4)
    screen.addshape(black5)
    screen.addshape(black6)

    blackChoices = [black1, black2, black3, black4, black5, black6]
    blackCubes = []
    
    #Get Dice Images
    green1 = ("green1.gif")
    green2 = ("green2.gif")
    green3 = ("green3.gif")
    green4 = ("green4.gif")
    green5 = ("green5.gif")
    green6 = ("green6.gif")

    #Add Dice Images as Shapes
    screen.addshape(green1)
    screen.addshape(green2)
    screen.addshape(green3)
    screen.addshape(green4)
    screen.addshape(green5)
    screen.addshape(green6)

    greenChoices = [green1, green2, green3, green4, green5, green6]
    greenCubes = []

    def cubeCreator(cube):

        newCube = trtl.Turtle()

        choices = None

        if cube == "blue":
            choices = blueChoices
        elif cube == "red":
            choices = redChoices
        elif cube == "green":
            choices = greenChoices
        else:
            choices = blackChoices

        #Assign newCube a shape depending
        newCube.shape(random.choice(choices))

        #Set newCube speed
        newCube.speed(-1)

        #Penup
        newCube.penup()

        #Return newCube
        return newCube

    #Set Starting Positions
    cubeY = -250
    cubeX = -329

    #Create 6 Blue Cubes
    for i in range(6):
        newBlue = cubeCreator("blue")
        blueCubes.append(newBlue)
        newBlue.goto(cubeX, cubeY)

        cubeX += 60

    #Blue Draggable
    def b1(x,y):
        blueCubes[0].goto(x,y)

    def b2(x,y):
        blueCubes[1].goto(x,y)

    def b3(x,y):
        blueCubes[2].goto(x,y)

    def b4(x,y):
        blueCubes[3].goto(x,y)

    def b5(x,y):
        blueCubes[4].goto(x,y)

    def b6(x,y):
        blueCubes[5].goto(x,y)

    blueCubes[5].ondrag(b6)
    blueCubes[4].ondrag(b5)
    blueCubes[3].ondrag(b4)
    blueCubes[2].ondrag(b3)
    blueCubes[1].ondrag(b2)
    blueCubes[0].ondrag(b1)

    #Create 6 Red Cubes
    for i in range(6):
        newRed= cubeCreator("red")
        redCubes.append(newRed)
        newRed.goto(cubeX, cubeY)

        cubeX += 60

    #Red Draggable
    def r1(x,y):
        redCubes[0].goto(x,y)

    def r2(x,y):
        redCubes[1].goto(x,y)

    def r3(x,y):
        redCubes[2].goto(x,y)

    def r4(x,y):
        redCubes[3].goto(x,y)

    def r5(x,y):
        redCubes[4].goto(x,y)

    def r6(x,y):
        redCubes[5].goto(x,y)

    redCubes[5].ondrag(r6)
    redCubes[4].ondrag(r5)
    redCubes[3].ondrag(r4)
    redCubes[2].ondrag(r3)
    redCubes[1].ondrag(r2)
    redCubes[0].ondrag(r1)

    #Set New Starting Y
    cubeY = -310

    #Reset Starting X
    cubeX = -329

    #Create 6 Black Cubes
    for i in range(6):
        newBlack= cubeCreator("black")
        blackCubes.append(newBlack)
        newBlack.goto(cubeX, cubeY)

        cubeX += 60
        
    #Black Draggable
    def bk1(x,y):
        blackCubes[0].goto(x,y)

    def bk2(x,y):
        blackCubes[1].goto(x,y)

    def bk3(x,y):
        blackCubes[2].goto(x,y)

    def bk4(x,y):
        blackCubes[3].goto(x,y)

    def bk5(x,y):
        blackCubes[4].goto(x,y)

    def bk6(x,y):
        blackCubes[5].goto(x,y)

    blackCubes[5].ondrag(bk6)
    blackCubes[4].ondrag(bk5)
    blackCubes[3].ondrag(bk4)
    blackCubes[2].ondrag(bk3)
    blackCubes[1].ondrag(bk2)
    blackCubes[0].ondrag(bk1)

    #Create 6 Green Cubes
    for i in range(6):
        newGreen = cubeCreator("green")
        greenCubes.append(newGreen)
        newGreen.goto(cubeX, cubeY)

        cubeX += 60
        
    #Green Draggable
    def g1(x,y):
        greenCubes[0].goto(x,y)

    def g2(x,y):
        greenCubes[1].goto(x,y)

    def g3(x,y):
        greenCubes[2].goto(x,y)

    def g4(x,y):
        greenCubes[3].goto(x,y)

    def g5(x,y):
        greenCubes[4].goto(x,y)

    def g6(x,y):
        greenCubes[5].goto(x,y)

    greenCubes[5].ondrag(g6)
    greenCubes[4].ondrag(g5)
    greenCubes[3].ondrag(g4)
    greenCubes[2].ondrag(g3)
    greenCubes[1].ondrag(g2)
    greenCubes[0].ondrag(g1)

#Countdown Turtle
hourglass = trtl.Turtle()
hourglassImage = ("hourglass.gif")
screen.addshape(hourglassImage)
hourglass.penup()
hourglass.goto(-410, -292)
hourglass.shape(hourglassImage)

#Start Countdown on CLick
hourglass.onclick(countdown)

#Roll on Click
roller.onclick(roll)

#Cancel Sound on Click
canceller.onclick(cancel_sound)

#Play Meow on Click
cat.onclick(play_meow)

#Keep the Program in a Loop
screen.mainloop()