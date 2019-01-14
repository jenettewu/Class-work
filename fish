def setup():
    size(640, 480)
playing_pass = False
leaderboard_pass = False
pause_pass = False
menu_screen = True
death = False
looping = True
reset = False
generate = False

def draw():
    menu()
    
def menu():
    background("#6EC5E9")
    draw_button("PLAY", 170, 190, 300, 80, (239, 201, 239))
    fill(255)
    triangle(410, 210, 410, 250, 450, 230)
    draw_button("LEADERBOARD", 170, 300, 300, 80, (239, 201, 239))
    leaderboard()
    play()

def draw_button(button_text, button_x, button_y, button_width, button_height, (r, g, b)):
    global playing_pass, leaderboard_pass, reset
    noStroke()
    
    rect(button_x, button_y, button_width, button_height)
    if mouseX in range(button_x, button_x + button_width) and mouseY in range(button_y, button_y + button_height):
        fill(r - 50, g - 50, b - 50)
        if mousePressed:
            if button_text == "PLAY" or button_text == "RESTART":
                reset()
            elif button_text == "LEADERBOARD":
                leaderboard_pass = True 
            elif button_text == "BACK":
                leaderboard_pass = False
            elif button_text == "EXIT":
                death = False
                menu_screen = True
                playing_pass = False

    else:
        fill(r, g, b)

    rect(button_x, button_y, button_width, button_height)
    
    fill(255)
    textSize(30)
    textAlign(CENTER, CENTER)
    pushMatrix()
    translate(button_x, button_y)
    text(button_text, button_width/2, button_height/2)
    popMatrix()
    
fish_x = 0
fish_y = 0
fish_size_width = 50
fish_size_height = 50

def reset():
    global playing_pass, menu_screen, score, death, fish_x, fish_y
    death = False
    playing_pass = True
    menu_screen = False
    score = 0
    o_fish_x = 0
    o_fish_y = 0
    fish_size_width = 50
    fish_size_height = 50
    play()
    
    
def fish_movement():
    global fish_x, fish_y, fish_size_width, fish_size_height
    fill(0)
    ellipse(fish_x, fish_y, fish_size_width, fish_size_height)
    fish_x = mouseX
    fish_y = mouseY
    
def keyPressed():
    if key == ' ':
        global looping
        if looping == True:
            looping = False
            noLoop()
        elif looping == False:
            looping = True
            loop()

def play():
    global fish_x, fish_y, fish_movement
    if playing_pass == True:
        background(110, 197, 233)
        fill(245, 225, 125)
        rect(0, 400, 648, 80)    
        fill(110, 197, 233, 100)
        rect(0, 0, 640, 480)
        fish_movement()
        other_fish()
        death_screen()
        
#leaderboard() and pause() must be defined like below
number_of_games = 1
word_height = 140
game_scores = [10,15,9]
rank = 0
def leaderboard():
    global number_of_games, word_height, score
    if leaderboard_pass == True:
        background(0, 255, 255)
        rect(120,40,400,400)
        textSize(32)
        fill(0, 102, 153)
        text("LEADERBOARD", 315, 70)
        draw_button("BACK", 525, 350, 100, 70, (255, 0, 0))
        textSize(24)
        fill(0, 102, 153)
        text("Game " + str(number_of_games)+ "            score " + str(game_scores[rank]), 280, word_height)
    elif death == True:
        number_of_games + 1 
        word_height + 20
        rank + 1
        game_scores.append(score)
        for scores in game_scores:
            game_scores.sort()
        
o_fish_x = 641
o_fish_width = random(5, 20)
o_fish_height = random(5, 20)
o_fish_y = random(o_fish_width + 10, 480 - o_fish_width)
points = 0
update_points = 0
score = 0
def other_fish():
    global generate
    if generate = True:
        global o_fish_x, o_fish_y, o_fish_width, o_fish_height, points, update_points, fish_size_width, fish_size_height, death_pass, score,death
        ellipse(o_fish_x, o_fish_y, o_fish_width, o_fish_height)
        o_fish_x += 2
        if o_fish_x > 640:
            o_fish_x = 0
            o_fish_y = 240
            o_fish_height = random(5, 100)
            o_fish_width = o_fish_height + random(1, 20)
        
        if fish_size_height > o_fish_height:
            if o_fish_x in range(int(fish_x - fish_size_width/2 + o_fish_width/2), int(fish_x + fish_size_width/2 - o_fish_width/2)) and o_fish_y in range(int(fish_y - fish_size_height/2 + o_fish_height/2), int(fish_y + fish_size_height/2 - o_fish_height/2)):
                points += 1
        elif fish_size_height + 5 < o_fish_height:
            if fish_x in range(int(o_fish_x - o_fish_x/2 + fish_size_width/2.5), int(o_fish_x + o_fish_width/2 - fish_size_width/2.5)) and fish_y in range(int(o_fish_y - o_fish_y/2 + fish_size_height/2.5), int(o_fish_y + o_fish_y/2 - fish_size_height/2.5)):
                death = True
    
        if points != update_points:
            score += int(o_fish_width + o_fish_height)/10
            fish_size_width += (o_fish_width + o_fish_height)/10
            fish_size_height += (o_fish_width + o_fish_height)/10
            o_fish_x = 1000
            update_points = points
        show_score()
    
def death_screen():
    if death == True:
        playing_pass = False
        background("#6EC5E9")
        global score
    
        textSize(60)
        fill(0)
        textAlign(CENTER, CENTER)
        text("YOU DIED!", 320, 100)
        textSize(30)
        text("YOUR SCORE: " + str(score), 320, 200)
        
        draw_button("EXIT", 30, 300, 140, 140, (239, 201, 239))
        draw_button("RESTART", 460, 300, 140, 140, (239, 201, 239))
    
def show_score():
    global score
    textSize(25)
    text("Score: " + str(score), 80, 50)