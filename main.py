import pygame
from sys import exit
import random

# initialise pygame (always needed)
pygame.init()
clock = pygame.time.Clock()

# create the window 600/width x 400/height
screen = pygame.display.set_mode((600, 400))
# window title
pygame.display.set_caption("Dice Roll Simulator")

# load the background image and font (used later)
background_image = pygame.image.load('graphics/background2.png')
font = pygame.font.Font('font/SunnyspellsRegular.otf', 50)
roll_message = font.render('Press SPACEBAR to roll the dice', True, (255, 235, 193))

# declare arrays to hold the dice and rolling animation images
dice_images = []
dice_rolling_images = []

# 6 dice images -> can use a for loop to load all
for i in range(1, 7):
    dice_image = pygame.image.load('graphics/dice/' + str(i) + '.png')
    dice_images.append(dice_image)

# 8 rolling dice images -> can use a for loop to load all 
for i in range(1, 9):
    dice_rolling_image = pygame.image.load('graphics/animation/roll' + str(i) + '.png')
    dice_rolling_images.append(dice_rolling_image)

# audio
rolling_sound = pygame.mixer.Sound('audio/roll_aud.mp3')
rolling_stop_sound = pygame.mixer.Sound('audio/roll_stop_aud.mp3')

# default values for rolling animation
is_rolling = False
rolling_images_counter = 0
dice_num_image = dice_images[0]  # default dice image (1)

while True:
    # event loop (close window -> exit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_image, (0, 0))
    screen.blit(roll_message, (50, 300))

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not is_rolling:
        #start rolling
        is_rolling = True
        rolling_sound.play()
        rand_num = random.randint(0, 5)
        dice_num_image = dice_images[rand_num]
        screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
        rolling_images_counter += 1
               
    else:
        if is_rolling:
            #showing rolling animation images
            screen.blit(dice_rolling_images[rolling_images_counter], (250, 150))
            rolling_images_counter += 1
            if rolling_images_counter >= 8:
                is_rolling = False
                rolling_images_counter = 0
                rolling_stop_sound.play()
            
        else:
            #show the dice with the rolled number
            screen.blit(dice_num_image, (250, 150))
            
    pygame.display.update()
    clock.tick(13)  # limit the frame rate to 13 FPS