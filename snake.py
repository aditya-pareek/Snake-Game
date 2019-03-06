import turtle
import time
import random

delay=0.1

#Score
score=0
high_score=0

#Setup the Screen
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#f8e597")
wn.setup(width=600, height=600)
wn.tracer(0)                         #Turns off the screen updates

#Snake Head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#678b5c")
head.penup()                          #doesn't leave a trail
head.goto(0,0)                        #starting position
head.direction="stop"

#Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("#db494a")
food.penup()
food.goto(0,100)

segments=[]

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.shape("square")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  HighScore: 0",align="center",font=("Courier New",24,"normal"))

#Functions
def go_up():
	if head.direction!="down":
		head.direction="up"
def go_down():
	if head.direction!="up":
		head.direction="down"
def go_left():
	if head.direction!="right":
		head.direction="left"
def go_right():
	if head.direction!="left":
		head.direction="right"
def _pause():
	head.direction="stop"

def move():
	x=head.xcor()
	y=head.ycor()
	if head.direction=="up":
		head.sety(y+20)
	if head.direction=="down":
		head.sety(y-20)
	if head.direction=="left":
		head.setx(x-20)
	if head.direction=="right":
		head.setx(x+20)

#Keyboard Bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")
wn.onkeypress(_pause,"space")

#Main Game Loop
while True:
	wn.update()
	
	#check for collision with the border
	if abs(head.xcor())>290 or abs(head.ycor())>290:
		time.sleep(1)
		head.goto(0,0)
		head.direction="stop"
		
		#hide the segments
		for segment in segments:
			segment.goto(1000,1000)
		
		#clear the segments
		segments.clear()
		
		#Change the position and color of food
		food.color("#db494a")
		food.goto(0,100)
		
		#Reset the score and delay
		score=0
		delay=0.1

		#Update the score display
		pen.clear()
		pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("Courier New",24,"normal"))

	#check for collision with food
	if head.distance(food)<20:
		#move the food to a random spot
		x=random.randint(-290,290)
		y=random.randint(-290,290)
		food.goto(x,y)		
	
		#add a segment
		new_segment=turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("circle")
		new_segment.color("#72b573")
		new_segment.penup()
		segments.append(new_segment)

		#Shorten the Delay
		delay-=0.001

		#Increase the Score
		score+=10
		if score>high_score:
			high_score=score

		#Change the color of food 
		if score%50==40:
			food.color("#3f48cc")
		else:
			food.color("#db494a")

		pen.clear()
		pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("Courier New",24,"normal"))

	
	#move the end segments first in reverse order
	for i in range(len(segments)-1,0,-1):
		x=segments[i-1].xcor()
		y=segments[i-1].ycor()
		segments[i].goto(x,y)
	
	#move 0 to where the head is
	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)
	
	move()
	
	#Check for head and body segment collision	
	for segment in segments:
		if segment.distance(head)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
			for segment in segments:
				segment.goto(1000,1000)
			segments.clear()
			
			#Change the position and color of food
			food.color("#db494a")
			food.goto(0,100)
			
			score=0
			delay=0.1
			pen.clear()
			pen.write("Score: {}  HighScore: {}".format(score,high_score),align="center",font=("Courier New",24,"normal"))
	time.sleep(delay)

wn.mainloop()