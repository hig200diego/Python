from turtle import *

colors = ['red', 'purple', 'blue', 'green', 'orange']
for i in range(200):
	pencolor(colors[i % 5])
	width(5)
	forward(i)
	left(20)
