from cross_const import *
from turtle import *

def coordinate_calc(coord):
    x = round((coord[0]*DRAW_back[0])/REAL_back[0] - DRAW_back[0]/2)
    y = -round((coord[1]*DRAW_back[1])/REAL_back[1] - DRAW_back[1]/2) # I put negative in front but it is wrong!!!
    return [x,y]
    #
    
def red_stripes():
    color('#CB000F')
    begin_fill()
    for i, coord in enumerate(RED_STRIPES[0].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()
    
    penup()
    begin_fill()
    for i, coord in enumerate(RED_STRIPES[1].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()

def triangles():
    color('#CB000F')
    begin_fill()
    for i, coord in enumerate(TRIANGLES[0].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()
    
    penup()
    begin_fill()
    for i, coord in enumerate(TRIANGLES[1].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()

    penup()
    begin_fill()
    for i, coord in enumerate(TRIANGLES[2].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()
    
    penup()
    begin_fill()
    for i, coord in enumerate(TRIANGLES[3].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()
    
def white_stripes():
    color('white')
    begin_fill()
    penup()
    for i, coord in enumerate(WHITE_STRIPES[0].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()
    
    penup()
    begin_fill()
    for i, coord in enumerate(WHITE_STRIPES[1].values()):
        x, y = coordinate_calc((coord[1][0], coord[1][1]))
        if i == 0:
            penup()
        else:
            pendown()
        goto(x,-y)
    end_fill()