import pygame
from pygame.locals import *
import sys
import random
from random import randint

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

sup = pygame.image.load('Sprites/paradoc.png')
sdown = pygame.image.load('Sprites/paradof.png')
sleft = pygame.image.load('Sprites/paradole.png')
sright = pygame.image.load('Sprites/paradol.png')

death_player = pygame.image.load("Sprites/death.png")

slime_up = pygame.image.load('Sprites/slimec.png')
slime_down = pygame.image.load('Sprites/slimef.png')
slime_left = pygame.image.load('Sprites/slimele.png')
slime_right = pygame.image.load('Sprites/slimel.png')

pslime_up = pygame.image.load('Sprites/pslimec.png')
pslime_down = pygame.image.load('Sprites/pslimef.png')
pslime_left = pygame.image.load('Sprites/pslimele.png')
pslime_right = pygame.image.load('Sprites/pslimel.png')

death_slime = pygame.image.load("Sprites/slimedeath.png")


frame_x = 48
frame_y = 58
frame_dead_y = 32
stand_frames = 4
num_frames = 6
num_rows = 1
stand_frames = 6
death_player_frames = 3

frame_x_slime = 33
frame_y_slime = 38
slime_frames = 6
death_slime_frames = 5
stand_slime_frames = 4


player_run_up = cut_sprite(run_up, frame_x, frame_y, num_frames, num_rows)
player_run_down = cut_sprite(run_down, frame_x, frame_y, num_frames, num_rows)
player_run_left = cut_sprite(run_left, frame_x, frame_y, num_frames, num_rows)
player_run_right = cut_sprite(
    run_right, frame_x, frame_y, num_frames, num_rows)

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

slime_stand_up = cut_sprite(
    pslime_up, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_down = cut_sprite(
    pslime_down, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_left = cut_sprite(
    pslime_left, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_right = cut_sprite(
    pslime_right, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)

slime_death = cut_sprite(death_slime, frame_x_slime,
                         frame_y_slime, death_slime_frames, num_rows)

player_larg = 16
player_alt = 16
player_x = (larg_tela - player_larg) // 2
player_y = (alt_tela - player_alt) // 2
player_speed = 2
current_frame = 0
frame_time = 100
last_frame_time = pygame.time.get_ticks()

last_direction = None
slime_larg = 16
slime_alt = 16
slime_x = 100
slime_y = 100
slime_speed = 1
slime_speed_berserk = 2

slime_direction = random.choice(['up', 'down', 'left', 'right'])
slime_steps = 0
max_steps = 50
min_steps = 10
pause_duration = randint(500, 3000)
last_change_time = 0
is_paused = False
is_berserk = False
slime_death_animation_playing = False
slime_death_animation_start_time = 0
slime_death_animation_duration = 1000


def reverse_animation(frames):
    return frames[::-1]


def is_player_berserk():
    slime_hitbox = get_slime_hitbox()
    player_hitbox = pygame.Rect(
        player_x + 17, player_y + 22, player_larg, player_alt)
    return slime_hitbox.colliderect(player_hitbox)


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


chase_start_time = 0
chase_duration = 10000


def move_slime():
    global slime_x, slime_y, slime_direction, slime_steps, last_change_time, is_paused, player_x, player_y, is_berserk, chase_start_time, slime_alive

    if not slime_alive:
        return

    if is_player_berserk():
        if not is_berserk:
            chase_start_time = pygame.time.get_ticks()
        is_berserk = True

    if is_berserk:
        if pygame.time.get_ticks() - chase_start_time > chase_duration:
            is_berserk = False
        else:
            berserk()
            return

    if slime_steps >= max_steps:
        is_paused = True
        slime_steps = 0
        last_change_time = pygame.time.get_ticks()

    if is_paused:
        if pygame.time.get_ticks() - last_change_time >= pause_duration:
            slime_direction = random.choice(['up', 'down', 'left', 'right'])
            is_paused = False
        else:
            return

    if slime_direction == 'up':
        slime_y -= slime_speed
    elif slime_direction == 'down':
        slime_y += slime_speed
    elif slime_direction == 'left':
        slime_x -= slime_speed
    elif slime_direction == 'right':
        slime_x += slime_speed

    slime_steps += 1


def get_slime_hitbox():
    if slime_direction == 'up':
        return pygame.Rect(slime_x + 8, slime_y - 28, 16, 40)
    elif slime_direction == 'down':
        return pygame.Rect(slime_x + 8, slime_y + 26, 16, 40)
    elif slime_direction == 'left':
        return pygame.Rect(slime_x - 31, slime_y + 11, 40, 16)
    elif slime_direction == 'right':
        return pygame.Rect(slime_x + 23, slime_y + 11, 40, 16)


def get_slime_body_hitbox():
    hitbox_width = 16
    hitbox_height = 16
    return pygame.Rect(slime_x + (frame_x_slime - hitbox_width) // 2,  slime_y + (frame_y_slime - hitbox_height) // 2, hitbox_width, hitbox_height)


def berserk():
    global slime_x, slime_y, player_x, player_y, slime_direction

    if slime_x < player_x:
        slime_direction = 'right'
    elif slime_x > player_x:
        slime_direction = 'left'

    if slime_y < player_y:
        slime_direction = 'down'
    elif slime_y > player_y:
        slime_direction = 'up'

    if slime_direction == 'up':
        slime_y -= slime_speed
    elif slime_direction == 'down':
        slime_y += slime_speed
    elif slime_direction == 'left':
        slime_x -= slime_speed
    elif slime_direction == 'right':
        slime_x += slime_speed


player_alive = True
slime_alive = True


def is_player_behind_slime():
    global player_x, player_y, slime_x, slime_y, slime_direction

    if slime_direction == 'up':
        return player_y > slime_y
    elif slime_direction == 'down':
        return player_y < slime_y
    elif slime_direction == 'left':
        return player_x > slime_x
    elif slime_direction == 'right':
        return player_x < slime_x


def get_player_hitbox():
    hitbox_width = 16
    hitbox_height = 16
    return pygame.Rect(player_x + 17, player_y + 22, hitbox_width, hitbox_height)


def draw_hitboxes():
    global player_alive, slime_alive
    slime_hitbox = get_slime_hitbox()
    slime_body_hitbox = get_slime_body_hitbox()
    player_hitbox = get_player_hitbox()
    if slime_alive:
        slime_hitbox = get_slime_hitbox()
        slime_body_hitbox = get_slime_body_hitbox()
        pygame.draw.rect(tela, (0, 255, 0), slime_hitbox, 2)
        pygame.draw.rect(tela, (0, 0, 255), slime_body_hitbox, 2)
        
        if slime_body_hitbox.colliderect(player_hitbox):
            if is_player_behind_slime():
                print("Slime foi morta pelo jogador!")
                slime_alive = False
            else:
                print("Jogador foi pego pela slime!")
                game_over()
    pygame.draw.rect(tela, (255, 0, 0), player_hitbox, 2)

def play_slime_death_animation(x, y):
    for frame in slime_death:
        tela.fill(BLACK)
        tela.blit(frame, (x, y))
        pygame.display.flip()
        pygame.time.wait(1000)


def game_over():
    font = pygame.font.SysFont(None, 74)
    text = font.render('GAME OVER', True, (255, 0, 0))
    text_rect = text.get_rect(center=(larg_tela // 2, alt_tela // 2))
    tela.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()


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

    player_hitbox = get_player_hitbox()
    slime_hitbox = pygame.Rect(slime_x, slime_y, slime_larg, slime_alt)

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

    if slime_alive:
        move_slime()

        if slime_direction == 'up':
            draw_slime(slime_x, slime_y, slime_run_up)
        elif slime_direction == 'down':
            draw_slime(slime_x, slime_y, slime_run_down)
        elif slime_direction == 'left':
            draw_slime(slime_x, slime_y, slime_run_left)
        elif slime_direction == 'right':
            draw_slime(slime_x, slime_y, slime_run_right)

    draw_hitboxes()

    if slime_alive and is_player_behind_slime() and get_slime_body_hitbox().colliderect(player_hitbox):
        print("Slime foi morta pelo jogador!")
        slime_death_animation_playing = True
        slime_death_animation_start_time = pygame.time.get_ticks()
        slime_alive = False

    if slime_death_animation_playing:
        elapsed_time = pygame.time.get_ticks() - slime_death_animation_start_time
        if elapsed_time < slime_death_animation_duration:
            frame_index = int((elapsed_time / slime_death_animation_duration) * len(slime_death))
            if frame_index >= len(slime_death):
                frame_index = len(slime_death) - 1
            tela.blit(slime_death[frame_index], (slime_x, slime_y))
        else:
            slime_death_animation_playing = False

    pygame.display.flip()
    clock.tick(60)