x=0
y=640
def setup():
    size(640, 480)
    
def draw():
    global x
    global y
    if x >= 640:
        x = 0  
    x += 1
    if y >= 0:
        y = 640
    y = y-1
    
    background(135, 206, 235)
    noStroke()
    fill('#ffffff')
    ellipse(x, 80, 72, 95)
    ellipse(x, 90, 100, 68)
    ellipse(x+40, 115, 72, 45)
    ellipse(x-35, 86, 79, 68)
    ellipse(x-45, 107, 100, 53)
    
    ellipse(x-100, 130, 72, 95)
    ellipse(x-100, 140, 100, 68)
    ellipse(x-60, 165, 72, 45)
    ellipse(x-135, 136, 79, 68)
    ellipse(x-145, 157, 100, 53)
    
    fill('#9678b6')
    ellipse(220, 480, 220, 520)
    ellipse(470, 480, 280, 600)
            
    fill('#4e2e53')
    ellipse(0, 480, 480, 680)  
    ellipse(320, 480, 320, 390)
    ellipse(640, 480, 350, 740)
    
    fill('#003C00')
    triangle(0, 60, 0, 120, 30, 120)
    quad(0, 120, 0, 280, 80, 280, 5, 120)
    quad(0, 280, 0, 480, 150, 480, 30, 280)
    
    fill('#ffff00')
    ellipse(y, 300, 40, 40)
    
