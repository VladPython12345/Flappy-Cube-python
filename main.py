import pygame
import pygame.freetype
import random
import time

width = 500
height = 600
pygame.init()
timer = 0
bird = pygame.sprite
pipe = pygame.sprite
font = pygame.font.SysFont('arial', 64, 2)
display = pygame.display.set_mode((width, height))
pygame.display.update()
pygame.display.set_caption("Flappy cube!!")
pygame_icon = pygame.image.load('logo.png')
pygame.display.set_icon(pygame_icon)
points = 0
bird_pos = {
    "x": 50,
    "y": height / 2 - 5,
    "change x": 0
}
pipe_pos = {
    "x": 490,
    "y": random.randrange(250, 525),
    "change x": -10
}
pipe2_pos = {
    "x": 490,
    "y": pipe_pos["y"] - 625,
    "change x": -10
}

colors = {
    "pipe": (0, 185, 100),  # red(255, 0, 0) light brown(255, 185, 100) green(0, 185, 100)
    "bird": (255, 255, 0),  # orange(255, 175, 0) yellow(255, 255, 0)
    "ground": (115, 66, 34)
}
bird_size = (50, 50)
pipe_size = (50, 350)
pipe2_size = (50, 500)
ground_size = (500, 30)
game_end = False

pipe_spd = 5
while not game_end:
    bird_pos["change x"] = 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_end = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bird_pos["change x"] = -30
            if event.key == pygame.K_DOWN:
                bird_pos["change x"] = 30

    display.fill((0, 230, 255))
    points = str(points)
    text = font.render(points, 1, (0, 0, 0), (0, 230, 255))
    bird_pos["y"] += bird_pos["change x"]
    pipe_pos["x"] += pipe_pos["change x"]
    pipe2_pos["x"] += pipe2_pos["change x"]
    pygame.draw.rect(display, colors["bird"], [
        bird_pos["x"],
        bird_pos["y"],
        bird_size[0],
        bird_size[1]])
    pygame.draw.rect(display, colors["pipe"], [
        pipe_pos["x"],
        pipe_pos["y"],
        pipe_size[0],
        pipe_size[1]])
    pygame.draw.rect(display, colors["ground"], [
        0,
        580,
        ground_size[0],
        ground_size[1]])
    pygame.draw.rect(display, colors["pipe"], [
        pipe2_pos["x"],
        pipe2_pos["y"],
        pipe2_size[0],
        pipe2_size[1]])
    display.blit(text, (10, 0))
    if pipe_pos["x"] < 20:
        pipe_pos["x"] = 490
        pipe_pos["y"] = random.randrange(250, 525)
    if pipe2_pos["x"] < 20:
        pipe2_pos["x"] = 490
        pipe2_pos["y"] = pipe_pos["y"] - 625
        points = int(points)
        points += 1
        points = str(points)

    if bird_pos["y"] > 555:
        quit()

    if bird_pos["y"] < -18:
        quit()

    if pipe_pos["x"] - 40 <= bird_pos["x"] and pipe_pos["y"] < bird_pos["y"] > pipe2_pos["y"]:
        quit()
    if pipe2_pos["x"] - 40 <= bird_pos["x"] and bird_pos["y"] < pipe_pos["y"] - 125:
        quit()
    pygame.display.update()
    time.sleep(0.1)
