import turtle 

t = turtle.Turtle()

#radius 
r = 10

for i in range(50): 
    t.circle(r * i) 
    t.up() 
    t.sety((r * i)*(-1)) 
    t.down()
	

