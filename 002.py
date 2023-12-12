import pygame
import sys
import random
pygame.init()

WHITE = (255, 255, 255)

WIDTH, HEIGHT = 800, 300

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

background_img = pygame.image.load("01.jpg")
dino_img = pygame.image.load("02.png")
cactus_img = pygame.image.load("03.png")

dino_x = 50
dino_y = HEIGHT - dino_img.get_height() - 30
dino_speed = 5

cactus_x = WIDTH
cactus_y = HEIGHT - cactus_img.get_height() - 30
cactus_speed = 5

jumping = False
jump_count = 15  

score = 0  

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

def jump():
    global dino_y, jumping, jump_count
    if not jumping:
        jumping = True
        jump_count = 10  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jump()

    if jumping:
        if jump_count >= -10:  
            neg = 1
            if jump_count < 0:
                neg = -1
            dino_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jumping = False

    
    cactus_x -= cactus_speed
    if cactus_x < 0:
        cactus_x = WIDTH
        cactus_y = HEIGHT - cactus_img.get_height() - 30
        score += 1

    
    if dino_x < cactus_x + cactus_img.get_width() and \
            dino_x + dino_img.get_width() > cactus_x and \
            dino_y < cactus_y + cactus_img.get_height() and \
            dino_y + dino_img.get_height() > cactus_y:
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()
    
    screen.blit(background_img, (0, 0))
    screen.blit(dino_img, (dino_x, dino_y))
    screen.blit(cactus_img, (cactus_x, cactus_y))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(30)
