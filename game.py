import pygame
from pygame.locals import *
import sys
import math

pygame.init()
pygame.display.set_caption("Mata os Slimes, Cleitin!")

larg_tela = 800
alt_tela = 600
tela = pygame.display.set_mode((larg_tela, alt_tela))
BLACK = (0, 0, 0)


def cut_sprite(sprite, frame_x, frame_y, num_frames, num_rows):
    animation = []
    for l in range(num_rows):
        for c in range(num_frames):
            x = c * frame_x
            y = l * frame_y
            frame_rect = pygame.Rect(x, y, frame_x, frame_y)
            frame = sprite.subsurface(frame_rect)
            animation.append(frame)
    return animation


run_up = pygame.image.load('Sprites/andandoc (1).png')
run_down = pygame.image.load('Sprites/andandof (1).png')
run_left = pygame.image.load('Sprites/andandole (2).png')
run_right = pygame.image.load('Sprites/andandol (1).png')

atk_up = pygame.image.load('Sprites/attackc.png')
atk_down = pygame.image.load('Sprites/attackf.png')
atk_left = pygame.image.load('Sprites/attackle.png')
atk_right = pygame.image.load('Sprites/attackl.png')

sup = pygame.image.load('Sprites/paradoc.png')
sdown = pygame.image.load('Sprites/paradof.png')
sleft = pygame.image.load('Sprites/paradole.png')
sright = pygame.image.load('Sprites/paradol.png')

death_player = pygame.image.load("Sprites/death.png")

frame_x = 48
frame_y = 58
frame_dead_y = 32

num_frames = 6
num_rows = 1
atk_frames = 4
stand_frames = 6
death_player_frames = 3


slime_up = pygame.image.load('Sprites/slimef.png')
slime_down = pygame.image.load('Sprites/slimec.png')
slime_left = pygame.image.load('Sprites/slimele.png')
slime_right = pygame.image.load('Sprites/slimel.png')

death_slime = pygame.image.load("Sprites/slimedeath.png")

slime_frames = 6
death_slime_frames = 5
frame_x_slime = 33
frame_y_slime = 38

player_run_up = cut_sprite(run_up, frame_x, frame_y, num_frames, num_rows)
player_run_down = cut_sprite(run_down, frame_x, frame_y, num_frames, num_rows)
player_run_left = cut_sprite(run_left, frame_x, frame_y, num_frames, num_rows)
player_run_right = cut_sprite(
    run_right, frame_x, frame_y, num_frames, num_rows)

player_atk_up = cut_sprite(atk_up, frame_x, frame_y, atk_frames, num_rows)
player_atk_down = cut_sprite(atk_down, frame_x, frame_y, atk_frames, num_rows)
player_atk_left = cut_sprite(atk_left, frame_x, frame_y, atk_frames, num_rows)
player_atk_right = cut_sprite(
    atk_right, frame_x, frame_y, atk_frames, num_rows)

player_stand_up_frames = cut_sprite(
    sup, frame_x, frame_y, stand_frames, num_rows)
player_stand_down_frames = cut_sprite(
    sdown, frame_x, frame_y, stand_frames, num_rows)
player_stand_left_frames = cut_sprite(
    sleft, frame_x, frame_y, stand_frames, num_rows)
player_stand_right_frames = cut_sprite(
    sright, frame_x, frame_y, stand_frames, num_rows)

player_death = cut_sprite(death_player, frame_x,
                          frame_dead_y, death_player_frames, num_rows)

slime_run_up = cut_sprite(slime_up, frame_x_slime,
                          frame_y_slime, slime_frames, num_rows)
slime_run_down = cut_sprite(
    slime_down, frame_x_slime, frame_y_slime, slime_frames, num_rows)
slime_run_left = cut_sprite(
    slime_left, frame_x_slime, frame_y_slime, slime_frames, num_rows)
slime_run_right = cut_sprite(
    slime_right, frame_x_slime, frame_y_slime, slime_frames, num_rows)


slime_death = cut_sprite(death_slime, frame_x_slime,
                         frame_y_slime, death_slime_frames, num_rows)

if not (player_run_up and player_run_left and player_run_down and player_run_right):
    print("Erro: Nenhum quadro foi cortado das sprite sheets.")
    pygame.quit()
    sys.exit()

player_larg = 13
player_alt = 19
player_x = (larg_tela - player_larg) // 2
player_y = (alt_tela - player_alt) // 2
player_speed = 2
current_frame = 0
frame_time = 100
last_frame_time = pygame.time.get_ticks()

last_direction = None
is_attacking = False
atk_frame_time = 100
last_attack_time = pygame.time.get_ticks()

slime_larg = 16
slime_alt = 11
slime_x = 100
slime_y = 100
slime_speed = 1


def reverse_animation(frames):
    return frames[::-1]


def draw_player(x, y, animation_frames):
    if current_frame < len(animation_frames):
        tela.blit(animation_frames[current_frame], (x, y))
    else:
        tela.blit(animation_frames[0], (x, y))


def draw_slime(x, y, animation_frames):
    if current_frame < len(animation_frames):
        tela.blit(animation_frames[current_frame], (x, y))
    else:
        tela.blit(animation_frames[0], (x, y))


def move_slime_towards_player():
    global slime_x, slime_y

    dx = player_x - slime_x
    dy = player_y - slime_y
    distance = math.sqrt(dx**2 + dy**2)

    if distance != 0:
        dx /= distance
        dy /= distance

    if abs(dx) > abs(dy):
        slime_x += dx * slime_speed
    else:
        slime_y += dy * slime_speed


clock = pygame.time.Clock()
running = True
while running:
    tela.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    moving = False
    if keys[pygame.K_a]:
        player_x -= player_speed
        last_direction = 'left'
        moving = True
    elif keys[pygame.K_d]:
        player_x += player_speed
        last_direction = 'right'
        moving = True
    elif keys[pygame.K_s]:
        player_y += player_speed
        last_direction = 'down'
        moving = True
    elif keys[pygame.K_w]:
        player_y -= player_speed
        last_direction = 'up'
        moving = True

    if keys[pygame.K_SPACE] and not is_attacking:
        is_attacking = True
        current_frame = 0
        last_attack_time = pygame.time.get_ticks()

    if moving:
        if last_direction == 'left':
            if pygame.time.get_ticks() - last_frame_time > frame_time:
                last_frame_time = pygame.time.get_ticks()
                current_frame = (current_frame + 1) % len(player_run_left)
            draw_player(player_x, player_y, reverse_animation(player_run_left))

        elif last_direction == 'right':
            if pygame.time.get_ticks() - last_frame_time > frame_time:
                last_frame_time = pygame.time.get_ticks()
                current_frame = (current_frame + 1) % len(player_run_right)
            draw_player(player_x, player_y, player_run_right)

        elif last_direction == 'down':
            if pygame.time.get_ticks() - last_frame_time > frame_time:
                last_frame_time = pygame.time.get_ticks()
                current_frame = (current_frame + 1) % len(player_run_down)
            draw_player(player_x, player_y, player_run_down)

        elif last_direction == 'up':
            if pygame.time.get_ticks() - last_frame_time > frame_time:
                last_frame_time = pygame.time.get_ticks()
                current_frame = (current_frame + 1) % len(player_run_up)
            draw_player(player_x, player_y, player_run_up)

    elif is_attacking:
        if pygame.time.get_ticks() - last_attack_time > atk_frame_time:
            last_attack_time = pygame.time.get_ticks()
            current_frame = (current_frame + 1) % len(player_atk_up)

            if current_frame == 0:
                is_attacking = False

        if last_direction == 'up':
            draw_player(player_x, player_y, (player_atk_up))
        elif last_direction == 'down':
            draw_player(player_x, player_y, (player_atk_down))
        elif last_direction == 'left':
            draw_player(player_x, player_y, reverse_animation(player_atk_left))
        elif last_direction == 'right':
            draw_player(player_x, player_y, (player_atk_right))
    else:
        if pygame.time.get_ticks() - last_frame_time > frame_time:
            last_frame_time = pygame.time.get_ticks()
            current_frame = (current_frame + 1) % len(player_stand_up_frames)

        if last_direction == 'up':
            tela.blit(
                player_stand_up_frames[current_frame], (player_x, player_y))
        elif last_direction == 'down':
            tela.blit(
                player_stand_down_frames[current_frame], (player_x, player_y))
        elif last_direction == 'left':
            tela.blit(
                player_stand_left_frames[current_frame], (player_x, player_y))
        elif last_direction == 'right':
            tela.blit(
                player_stand_right_frames[current_frame], (player_x, player_y))

    move_slime_towards_player()
    if abs(player_x - slime_x) > abs(player_y - slime_y):
        if slime_x < player_x:
            draw_slime(slime_x, slime_y, slime_run_right)
        elif slime_x > player_x:
            draw_slime(slime_x, slime_y, reverse_animation(slime_run_left))
    else:
        if slime_y < player_y:
            draw_slime(slime_x, slime_y, slime_run_up)
        elif slime_y > player_y:
            draw_slime(slime_x, slime_y, slime_run_down)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()