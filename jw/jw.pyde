x = 0
def setup():
    size(640, 480)
    
def draw():
    global x
    if x >= 640:
        x = 0  
    x += 1
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
    

    triangle(0, 0, 0, 50, 20, 50)
    triangle(0, 50, 0, 120, 40, 120)
    triangle(0, 120, 0, 280, 80, 280)
