page = 0
x = 120
y = 480
witch_x = 0
witch_y = 240

def setup():
    size(640, 480)
    global scene
    global ghost
    global pumpkin
    global witch
    scene = loadImage("graveyard-dark.jpg")
    ghost = loadImage("ghost.png")
    pumpkin = loadImage("pumpkin.png")
    witch = loadImage("witch.png")
    
def draw():
    if page == 0:
        background(0)
        image(scene, 0, 0, 640, 400)
        image(pumpkin, 480, 320, 140, 140)
        
    elif page == 1:
        background(0)
        image(scene, 0, 0, 640, 400)
        image(pumpkin, 480, 320, 140, 140)
        
        global witch_x
        global witch_y
        if witch_x >= 640:
            witch_x = 0
            witch_y = 240
        witch_x += 8
        witch_y -= 2
        image(witch, witch_x, witch_y, 120, 70)
        
        global x
        global y
        if x >= 640:
            x = -150
        x += 4
        if y <= -150:
            y = 480
        y -= 3
        image(ghost, x, y, 150, 150)
        
    elif page == 2:
        background(0)
        image(scene, 0, 0, 640, 400)
        image(pumpkin, 480, 320, 140, 140)
        
        global witch_x
        global witch_y
        if witch_x >= 640:
            witch_x = 0
            witch_y = 240
        witch_x += 8
        witch_y -= 2
        image(witch, witch_x, witch_y, 120, 70)
        
        if x <= -150:
            x = 640
        x -= 4
        if y <= -150:
            y = 480
        y -= 3
        image(ghost, x, y, 150, 150)
        
def mousePressed():
    global page
    page += 1
    if page == 3:
        page = 1
    
