import pygame as py
import random 
import sys

# Initialize pygame
py.init()

# Define colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# Set up the game display
sc = py.display.set_mode((600,600))
py.display.set_caption("Snake game")

# Initialize snake starting position and segment length
x = 285
y = 300
seg = 1  # Number of snake segments (starts with head only)
a = 0    # Variable to track key presses

# Initial apple position
apple1 = random.randint(0,520)
apple2 = random.randint(0,520)

# Clock object to control game speed
clock = py.time.Clock()

# List to store positions of snake segments
positions = [] 

# Function to display score
def score():
    global seg
    font = py.font.SysFont("Consolas", 40)  
    score_text = "Score: " + str(seg - 1)
    text = font.render(score_text, True, white)  
    sc.blit(text, (10, 10))

# Function to draw the snake
def snake():
    global x, y, seg, new_h, positions
    positions.insert(0, (x, y))  # Insert new head position

    score()  # Show current score

    # Keep only the latest 'seg' number of positions (snake length)
    if len(positions) > seg:
        positions = positions[:seg] 

    # Draw each segment of the snake
    for pos in positions:
        s_r = py.draw.rect(sc, green, (pos[0], pos[1], 25, 25))

    # Update head rectangle for collision detection
    new_h = py.Rect(x, y, 25, 25)
    py.display.flip()

# Function to update game display (apple and score)
def display():
    global seg, apple1, apple2, x, y, new_h 
    sc.fill(black)  # Clear screen
    score()         # Display current score

    # Draw apple
    apple_rect = py.draw.rect(sc, red, (apple1, apple2, 20, 20))

    # Check if snake head collides with apple
    if new_h.colliderect(apple_rect):
        apple1, apple2 = apple_pos()  # New apple location
        seg += 1  # Increase snake length

# Function to generate new random apple position
def apple_pos():
    x1 = random.randint(0,600)
    y1 = random.randint(0,600)
    return x1, y1

# Function to handle movement and main game loop
def move():
    global a, x, y, seg, s_r
    p = True 
    while p:
        clock.tick(10)  # Control frame rate (10 FPS)

        # Handle events
        for sub in py.event.get():
            if sub.type == py.QUIT:
                sys.exit()
            if sub.type == py.KEYDOWN:
                print("pressed")
                if sub.key == py.K_q:
                    sys.exit()
                if sub.key in [py.K_a, py.K_s, py.K_w, py.K_d]:
                    a = sub.key  # Save direction key

        # Move snake based on direction key
        if a == py.K_a:       # Move left
            x -= 15
        elif a == py.K_s:     # Move down
            y += 15
        elif a == py.K_d:     # Move right
            x += 15
        elif a == py.K_w:     # Move up
            y -= 15

        # Update display and snake after movement
        display()
        snake()

        print(s_r)

        # Check for collision with walls (game over condition)
        if x > 600 or y > 600 or x < 0 or y < 0:
            sc.fill(black)
            py.display.flip()
            font1 = py.font.SysFont("Consolas", 40)
            b = "Congrats your score is " + str(seg - 1)
            text1 = font1.render(b, True, white)
            sc.blit(text1, (30, 30))
            py.display.flip()
            clock.tick(1)
            sys.exit()

# Game starts here
r = True
while r:
    sc.fill(black)
    s_r = py.draw.rect(sc, green, (x, y, 25, 25))  # Initial snake head
    new_h = s_r  # Update head position
    py.display.flip()
    move()
    py.display.flip()

# Quit the game
py.quit()
