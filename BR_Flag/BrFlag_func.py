from turtle import *
from BrFlag_const import *

# SCREEN TITLE
title("A Yellow Diamond on the Green Field below and A White Curved Band on a Starry Sky above")

def green_background():
    bgcolor("#128D2C")
#     penup()
#     goto(-LENGTH/2, HEIGHT/2)
#     pendown()
#     # Green Fill
#     color("#128D2C")
#     begin_fill()
#     forward(LENGTH)
#     right(90)
#     forward(HEIGHT)
#     right(90)
#     forward(LENGTH)
#     end_fill()
    #
    
def yellow_diamond():
    penup()
    goto(0, y-HEIGHT/2)
    pendown()
    color("#FDDB0A")
    begin_fill()
    goto(LENGTH/2 - x,0)
    goto(0, HEIGHT/2 - y)
    goto(x - LENGTH/2,0)
    goto(0, y-HEIGHT/2)
    end_fill()
    #
    
def blue_circle():
    color("#011963")
    penup()
    home()
    goto(r, 0)
    begin_fill()
    left(90)
    circle(r)
    end_fill()
    #
    
def coordinate_calc(coord):
    #x = round(((coord[0]-REC_0[0])*DRAW_back[0])/REAL_back[0]) - DRAW_back[0]/2
    #y = round(((coord[1]-REC_0[1])*DRAW_back[1])/REAL_back[1]) - DRAW_back[1]/2
    x = round((coord[0]*DRAW_back[0])/REAL_back[0] - DRAW_back[0]/2)
    y = -round((coord[1]*DRAW_back[1])/REAL_back[1] - DRAW_back[1]/2) # I put negative in front but it is wrong!!!
    return [x,y]
    #

def white_stripe():
    A = coordinate_calc((1022,594)) # coordinate of lower right stripe vertice
    color('white')
    penup()
    goto(A[0],A[1])
    pendown()
    begin_fill()
    setheading(140)
    circle(rs, 48.5)     # upper arch
    left(50)
    
    WALK1 = round((8*LENGTH) / 1_000)
    ANGLE1 = (5*1_000) / (LENGTH)
    for i in range(WALK1): # 8 left side small arch
        forward(3)
        left(ANGLE1)           # 5
        
    setheading(10)
    circle(-ri, 51.5)      # lower arch
    setheading(65)
    
    WALK2 = WALK1
    ANGLE2 = (3*1_000) / (LENGTH + 300)
    for i in range(WALK2): # 8 right side small arch
        forward(3)
        left(ANGLE2)           # 3
    end_fill()
    penup()
    home()
    
def branca(): # Franklin
    penup()
    x=round((800*1022)/1524)-400
    y=round((560*594)/1080)-280
    goto(x,-y)    
    color("white")
    pendown()
    begin_fill()
    setheading(140)
    rs=(8.5*800)/20
    circle(rs, 48.5)
    left(50)
    circle((1*800)/20, 800*1./20)
    setheading(10)
    rb=(8*800)/20
    circle(-rb, 51.5)
    setheading(65)
    circle((2*800)/20, 800*0.5/20)
    end_fill()

# Draw one star
def star(coord, size):
    STAR_COORD = coordinate_calc(coord)
    penup()
    if STAR_COORD[1] > 0:
        goto(STAR_COORD[0]-7, STAR_COORD[1]-2)
    else:
        goto(STAR_COORD[0]-7, STAR_COORD[1]+3)
    pendown()
    color("white")
    begin_fill()
    if size == 1:
        move = (LENGTH*0.3)/20
    elif size == 2:
        move = (LENGTH*0.25)/20
    elif size == 3:
        move = (LENGTH*0.2)/20
    elif size == 4:
        move = (LENGTH*0.14)/20
    else:
        move = (LENGTH*0.1)/20
    for i in range(5):
        forward(move)
        right(144)
    end_fill()
    #

def input_letters():
    for char, coord in letters.values():
        penup()
        goto(coordinate_calc((coord[0],coord[1]+25)))
        pendown()
        color("#128D2C")
        write(char, False, align="center", font=('Arial', ls, 'normal'))
        right(2)
    #
    
def grid():
    color('white')
    penup()
    goto(0,-HEIGHT/2)
    pendown()
    goto(0,HEIGHT/2)
    penup()
    goto(-LENGTH/2,0)
    pendown()
    goto(LENGTH/2,0)