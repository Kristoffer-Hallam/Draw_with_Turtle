LENGTH = int(input('Define length of screen with minimum of 750: ')) #1_000
HEIGHT = round(LENGTH/1.040)


# REAL FLAG SIZE
REAL_back = [1_214, 1_167]
# DRAWING SCREEN SIZE
DRAW_back = [LENGTH, HEIGHT]

# RED STRIPES
red_vert_stripe = {'0':['B',(500,71)],
                   '1':['D',(723,71)],
                   '2':['F',(723,1088)],
                   '3':['G',(500,1088)],
                   '4':['B',(500,71)]}
red_horiz_stripe = {'0':['J',(104,467)],
                    '1':['K',(104,690)],
                    '2':['N',(1118,690)],
                    '3':['O',(1118,467)],
                    '4':['J',(104,467)]}
RED_STRIPES = [red_vert_stripe, red_horiz_stripe]

# TRIANGLES
upper_triang = {'0':['A',(500,187)],
                '1':['',(302,71)],
                '2':['',(921,71)],
                '3':['',(723,187)],
                '4':['',(500,187)]}
lower_triang = {'0':['',(500,972)],
                '1':['',(301,1088)],
                '2':['',(921,1088)],
                '3':['',(723,972)],
                '4':['',(500,972)]}
left_triang = {'0':['',(218,467)],
               '1':['',(104,269)],
               '2':['',(104,889)],
               '3':['',(218,690)],
               '4':['',(218,467)]}
right_triang = {'0':['',(1004,690)],
               '1':['',(1118,889)],
               '2':['',(1118,269)],
               '3':['',(1004,467)],
               '4':['',(1004,690)]}
TRIANGLES = [upper_triang, lower_triang, left_triang, right_triang]

# WHITE STRIPES
white_vert_stripe = {'0':['',(569,972)],
                     '1':['',(653,972)],
                     '2':['',(653,187)],
                     '3':['',(569,187)],
                     '4':['',(569,972)]}
white_horiz_stripe = {'0':['',(220,538)],
                      '1':['',(220,620)],
                      '2':['',(1003,620)],
                      '3':['',(1003,538)],
                      '4':['',(220,538)]}
WHITE_STRIPES = [white_vert_stripe, white_horiz_stripe]