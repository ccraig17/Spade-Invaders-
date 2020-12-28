#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 08:33:33 2020

@author: ccraig
"""

# Space Invaders
# Sound (MacOs Only)

#Set Up Screen
#Building using the Turtle Module

import turtle  # the module used to create the objects in the game..is called from this Module
import os
import math
import random


#Setup Screen
wn = turtle.Screen()   #the Screen is from the "turtle module."
wn.bgcolor("black")
wn.title("Space Invaders by Craig")

#Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)     #the speed of pen. "0" is the fastest
border_pen.color("white")
border_pen.penup() #penup() allows the pen to draw without leaving trailing lines
border_pen.setposition(-300,-300) # remember the default starting coordinate are (0,0)
border_pen.pendown()  #pendown allows for the lines to be drawn after "setposition" is created
border_pen.pensize(3) # the size is 3 pixel wide

for side in range(4):  # the For Loop creates the Border as Square
    border_pen.fd(600)
    border_pen.lt(90)  # Left(lt (90)) indicates the angle for the Turtle Pen to turn to create the border
border_pen.hideturtle() # hides the Turtle Pen after drawing the border

#Create a Player Turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90) #sets the turtle player to face up, turning the player 90 degrees

#Move Players Left and Right
playerspeed = 15



# Choosing the number of enemies
number_of_enemies = 5
# Create a list of enemies

enemies = [] 

# add enemies to list
for i in range(number_of_enemies):
    # create tthe enemies here
    enemies.append(turtle.Turtle())
    
for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 2


# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90) # this gives the direction of the bullet, pointing up
bullet.shapesize(0.5, 0.5) 
bullet.hideturtle()  # hides the bullet when the game starts

bulletspeed = 20

#Define bullet 2 states
# ready- ready to fire
# fire - bullet is fired
bulletstate = "ready" # when the game has started


def move_left():
    x = player.xcor() #this is the starting X-coordinate/location
    x -= playerspeed  # this is the playspeed interval btn movements left
    if x < -280:  # this is limitation set on the boundary left-side of limit -280
        x = -280  # this tells the player to NOT pass -280 on the left-side
    player.setx(x) # this returns the Player to the new set position
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)
    
def fire_bullet():
    #decalre bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
       bulletstate = "fire"
    
    #Move the bullet to just above the player
       x = player.xcor()
       y = player.ycor() +10
       bullet.setposition(x, y)
       bullet.showturtle()
       
#collison of bullet with enemy/invader
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2+math.pow(t1.ycor()-t2.ycor(),2)))
    if distance < 15:
        return True
    else:
        return False
    
    
#Create Keyboard Bindings
turtle.listen()
turtle.onkeypress(move_left, "Left") # this binds the left-movement to the Left Arrow Key
turtle.onkeypress(move_right, "Right") # this binds the right-movement to the Right Arrow Key
turtle.onkeypress(fire_bullet, "space")

# Create Main Game Loop this is where the actual game takes place.
while True:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()  #the current location of the enemy
        x += enemyspeed   # the speed of the enemy at new location
        enemy.setx(x)     # sets the enemy's new position after the new speed (x) is aded.
    
        # Move the enemy back and down
        if enemy.xcor() > 280:  # reads, if the coordinate of the enemy's X-coordinate is greater than 280 (touching the border)
            y = enemy.ycor()  # this set the y-position of the invader
            y -= 40            # this decreases the invader's position by 40 pixels down moving closer to the Player after hitting the boarder
            enemy.sety(y)      # this set the enemy's new position after the new "y" or 40 pixel is added
            enemyspeed *= -1  # this mean when the enemy reaches the right border at 280, reverse direction
        
        
        if enemy.xcor() < -280:
            y = enemy.ycor()  # starting "y- coordinate"
            y -= 40            # the enemy drops down (- 40 pixel) after hitting the left boarder
            enemy.sety(y)      # this sets the new "y-coordinate" position for the enemy
            enemyspeed *= -1  # this mean when the enemy reaches the left border at 280, reverse direction
        
        #Check for collision btn the bullet and the enemy
        if isCollision(bullet, enemy):
                #Reset the bullent
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = randon.randint(100, 250)
            enemy.setposition(x, y)# reset the enemy's position to the starting position
              
            #Check when the enemy collide with the player
        if isCollision (enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
        break

        #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
    
        # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"   
    
    



delay = input("press enter to finish")  # Keeps the Screen/Window open