"""
project: pong game tutorial from freecodecamp

date:  08/25/2021

"""

import turtle


wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #this stops window from updating

# Main game loop 
while True: 
    wn.update()