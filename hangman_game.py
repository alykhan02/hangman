import pygame
import random
import math


# Constants
WHITE = (255,255,255)
BLACK = (0,0,0)
RADIUS = 20
GAP = 15
FPS = 60
WIDTH, HEIGHT = 800, 800
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 700
A = 65
is_visible = True

# fonts

for i in range(26):
    x = startx + GAP *2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x,y, chr(A+i), True])

#load images
images = []
for i in range(6):
    image = pygame.image.load("assets/hangman" + str(i)+".png")
    images.append(image)
print(images)    

# game variables
hangman_status = 5
words = ["HELLO", "ALYKHAN", "TESTING", "CODING"]
word = random.choice(words)
guessed = []


# setup display

pygame.init()
LETTER_FONT = pygame.font.SysFont('courier', 40)
WORD_FONT = pygame.font.SysFont('courier', 50)
TITLE_FONT = pygame.font.SysFont('courier', 60)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

clock = pygame.time.Clock()
run = True


def display_message(message):
    pygame.time.delay(1500)
    win.fill((WHITE))
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw():
    win.fill((WHITE))

    # draw title
    text = WORD_FONT.render("ALYKHAN'S HANGMAN", 1, BLACK)
    win.blit(text, (270, 50))
    text_lives = WORD_FONT.render("LIVES: "+str(hangman_status) , 1, BLACK)
    win.blit(text_lives, (270, 150))
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (300,400))

    # draw buttons
    for letter in letters:
        x, y, ltr, is_visible = letter
        if is_visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2,y - text.get_height()/2))
        
    win.blit(images[hangman_status], (10, 10))
    pygame.display.update()

# setup game loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, is_visible = letter
                dis = math.sqrt((x - m_x)**2 + (y-m_y)**2)
                if dis < RADIUS:
                    letter[3] = False
                    guessed.append(ltr)
                    if ltr not in word and hangman_status > 0:
                        hangman_status -= 1

    draw()
    
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON!")
        break
    if hangman_status == 0:
        display_message("You LOST!")
        break

pygame.quit()



