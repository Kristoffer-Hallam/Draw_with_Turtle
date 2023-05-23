# SCREEN SIZE
LENGTH = int(input('Define length of screen with minimum of 750: ')) #1_000
HEIGHT = round(LENGTH/1.411)


# REAL FLAG SIZE
REAL_back = [1_524, 1_080]
# DRAWING SCREEN SIZE
DRAW_back = [LENGTH, HEIGHT]

# LETTER SIZE
ls = round((20*LENGTH)/1_000)

# State stars coordinates
State_stars = {'AM': (547,495,1),
               'MT': (570,606,1),
               'AP': (539,630,2),
               'RO': (592,591,4),
               'RR': (622,633,2),
               'TO': (617,663,3),
               'PA': (843,464,1),
               'PI': (952,637,1),
               'MA': (990,640,3),
               'CE': (961,662,2),
               'AL': (898,722,2),
               'SE': (898,750,3),
               'PB': (925,695,3),
               'RN': (949,685,2),
               'PE': (897,695,3),
               'MS': (663,552,2),
               'AC': (830,524,3),
               'SP': (763,666,1),
               'RJ': (790,608,2),
               'BA': (767,585,2),
               'MG': (733,611,3),
               'ES': (750,629,4),
               'RS': (842,727,2),
               'SC': (866,701,3),
               'PR': (820,695,3),
               'GO': (657,690,1),
               'DF': (761,755,5)}

# Letters coordinates
letters = {0: ['O',(545,452)],
           1: ['R',(574,451)],
           2: ['D',(603,450)],
           3: ['E',(631,450)],
           4: ['M',(659,452)],
           5: ['E',(714,459)],
           6: ['P',(765,470)],
           7: ['R',(798,480)],
           8: ['O',(832,491)],
           9: ['G',(865,505)],
           10: ['R',(897,520)],
           11: ['E',(927,537)],
           12: ['S',(956,554)],
           13: ['S',(982,572)],
           14: ['O',(1010,593)]}

# BACKGROUND (20, 14) in units of distance
# 20 - LENGTH
# 1.7 - x -> x is the horizontal distance from the edge in our drawing
x = (LENGTH*1.7)/20
# 14 - HEIGHT
# 1.7 - y  -> y is the vertical distance from the edge in our drawing
y = (HEIGHT*1.7)/14

# Circle radius
# r = 3.5
# 20 - LENGTH
# R - r
r = (3.5*LENGTH)/20

# Superior arch radius
# rs = 8.5
# 20 - LENGTH
# 8.5 - rs
rs = (8.5*LENGTH)/20

# Inferior arch radius
# ri = 8
# 20 - LENGTH
# 8 - ri
ri = (8*LENGTH)/20

# Arch width
# arch_width = 0.5
# 20 - LENGTH
# 0.5 - ri
arch_width = (0.5*LENGTH)/20