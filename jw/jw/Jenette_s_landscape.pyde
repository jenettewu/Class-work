x=0
x2=640
def setup():
    size(640, 480)
    
def draw():
    global x
    global x2
    if x >= 790:
        x = 0  
    x += 0.5
    
    if -40 >= x2:
        x2 = 640
    x2 -= 2
    
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
    
    fill('#ffff00')
    ellipse(x2, 310, 40, 40)
    fill(0, 0, 0)
    ellipse(x2-10, 306, 4, 4)
    fill('#FFA500')
    triangle(x2-20, 305, x2-20, 315, x2-26, 310)
    triangle(x2+10, 310, x2+16, 317, x2, 307) 
    
    fill('#99CCFF')
    ellipse(x2+70, 340, 40, 40)
    fill(0, 0, 0)
    ellipse(x2+60, 336, 4, 4)
    fill('#FFA500')
    triangle(x2+50, 335, x2+50, 345, x2+45, 340)
    fill('#779ecb')
    triangle(x2+80, 340, x2+86, 347, x2+70, 337) 
    
    fill('#003C00')
    triangle(0, 60, 0, 120, 30, 120)
    quad(0, 120, 0, 280, 80, 280, 5, 120)
    quad(0, 280, 0, 480, 150, 480, 30, 280)
    triangle(580, 100, 600, 150, 560, 150)
    quad(570, 150, 590, 150, 650, 290, 510, 290)
    quad(540, 290, 620, 290, 710, 480, 450, 480)
    
    
    
