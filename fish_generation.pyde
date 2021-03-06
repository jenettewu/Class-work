rand_fish_x = -50
rand_fish_y = 100
    
def setup():
    size(640, 480)
playing_pass = False
leaderboard_pass = False
def draw():
    global page
    background(255)
    draw_button("PLAY", 170, 190, 300, 80, (239, 201, 239))
    draw_button("LEADERBOARD", 170, 300, 300, 80, (239, 201, 239))
    play()
    leaderboard()

def draw_button(button_text, button_x, button_y, button_width, button_height, (r, g, b)):
    global page,playing_pass, leaderboard_pass
    noStroke()
    
    rect(button_x, button_y, button_width, button_height)
    if mouseX in range(button_x, button_x + button_width) and mouseY in range(button_y, button_y + button_height):
        fill(r - 50, g - 50, b - 50)
        if mousePressed:
            if button_text == "PLAY":
                playing_pass = True
            elif button_text == "LEADERBOARD":
                leaderboard_pass = True 
    else:
        fill(r, g, b)

    rect(button_x, button_y, button_width, button_height)
    
    fill(255)
    textSize(30)
    textAlign(CENTER, CENTER)
    pushMatrix()
    translate(button_x, button_y)
    text(button_text, button_width / 2, button_height / 2)
    popMatrix()
    
fish_x = 320
fish_y = 240
def fish_movement():
    global fish_x
    global fish_y
    fill(0)
    ellipse(fish_x, fish_y, 50, 50)
    if fish_x < 0 - 25:
        fish_x = 640 + 25
    elif fish_x > 640 + 25:
        fish_x = 0 - 25
    
def keyPressed():
    global fish_x
    global fish_y
    if key == CODED:
        if keyCode == UP:
            fish_y -= 10
        elif keyCode == DOWN:
            fish_y += 10
        elif keyCode == RIGHT:
            fish_x += 10
        elif keyCode == LEFT:
            fish_x -= 10

def play():
    global fish_x, fish_y, fish_movement
    if playing_pass == True:
        background("#6EC5E9")    
        fish_movement()
        fish_generation()
        
def leaderboard():
    if leaderboard_pass == True:
        background(0, 255, 255)
        
def fish_generation():
    global rand_fish_x, rand_fish_y
    if rand_fish_x >= 690:
        rand_fish_x = -50
        rand_fish_y = random(50, 430)
    rand_fish_x += 5
    fill("#ffa500")
    ellipse(rand_fish_x, rand_fish_y, 50, 50)

        
        
            
