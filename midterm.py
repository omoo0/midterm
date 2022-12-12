#Name: Elizabeth Mata-Cerqueira 
#Date: October 25, 2022
#Student Number: 041072562
#This program takes user input and draws a square or a triangle 

import turtle
import tkinter

#The value of number and choice are given by user input
shape = turtle.Turtle()
number = turtle.numinput("Midterm","Enter length of sides:")
choice = turtle.numinput("Midterm", "Enter 1 for Sqare, 2 for Triangle")

#This function draw a square with user input
def square (number):
                shape.forward(number) #moves foward
                shape.left(90) #rotates

                shape.forward(number) #moves forward
                shape.left(90) #rotates

                shape.forward(number) #moves forward
                shape.left(90) #rotates

                shape.forward(number) #moves forward
                shape.left(90) #rotates

                turtle.done() #completes shape

#This function draw a triangle with user input
# Second shape example 
def triangle(number):
                shape.forward(number) #moves foward
                shape.left(120) #rotates

                shape.forward(number) #moves forward
                shape.left(120) #rotates

                shape.forward(number) #moves forward
                shape.left(120) #rotates 

                turtle.done() #completes shape

#These if statements detetermine the shape the user wants to draw
#While loop ensures that user inputs a valid number
while choice != 1 and choice != 2:
         choice = turtle.numinput("Midterm", "Error! Enter 1 for Sqare, 2 for Triangle")
if choice == 1:
                square(number)
if choice == 2:
                triangle(number)
