page = 0
x = 120
y = 480

def setup():
    size(640, 480)
    global img
    img = loadImage("graveyard-dark.jpg")
def draw():
    if page == 0:
        background(0)
        image(img, 0, 0, 640, 400)
    elif page == 1:
        background(0)
        image(img, 0, 0, 640, 400)
        global x
        global y
        x += 2
        y -= 3
        fill(255)
        arc(x, y, 70, 140, radians(180), radians(360))
    elif page == 2:
        background(0)
        image(img, 0, 0, 640, 400)
        x -= 4
        y -= 3
        fill(255)
        arc(x, y, 70, 140, radians(180), radians(360))
        
def mousePressed():
    global page
    page += 1
    if page == 3:
        page = 1
    
