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


def reverse_animation(frames):
    return frames[::-1]


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


player_alive = True
slime_alive = True


class Slime:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.steps = 0
        self.max_steps = 100
        self.min_steps = 25
        self.pause_duration = randint(500, 3000)
        self.last_change_time = 0
        self.is_paused = False
        self.is_berserk = False
        self.death_animation_playing = False
        self.death_animation_start_time = 0
        self.death_animation_duration = 750
        self.alive = True

    def move(self):
        global player_x, player_y

        if not self.alive:
            return

        player_hitbox = get_player_hitbox()
        vision_hitbox = self.get_hitbox()
        if vision_hitbox.colliderect(player_hitbox):
            self.is_berserk = True

        if self.is_berserk:
            self.berserk()
            return

        if self.steps >= self.max_steps:
            self.is_paused = True
            self.steps = 0
            self.last_change_time = pygame.time.get_ticks()

        if self.is_paused:
            if pygame.time.get_ticks() - self.last_change_time >= self.pause_duration:
                self.direction = random.choice(['up', 'down', 'left', 'right'])
                self.is_paused = False
            else:
                return

        if self.direction == 'up':
            self.y -= 1
        elif self.direction == 'down':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1

        self.steps += 1

    def berserk(self):
        global player_x, player_y

        if self.x < player_x:
            self.direction = 'right'
        elif self.x > player_x:
            self.direction = 'left'

        if self.y < player_y:
            self.direction = 'down'
        elif self.y > player_y:
            self.direction = 'up'

        if self.direction == 'up':
            self.y -= 2
        elif self.direction == 'down':
            self.y += 2
        elif self.direction == 'left':
            self.x -= 2
        elif self.direction == 'right':
            self.x += 2

    def get_hitbox(self):
        if self.direction == 'up':
            return pygame.Rect(self.x + 8, self.y - 28, 16, 40)
        elif self.direction == 'down':
            return pygame.Rect(self.x + 8, self.y + 26, 16, 40)
        elif self.direction == 'left':
            return pygame.Rect(self.x - 31, self.y + 11, 40, 16)
        elif self.direction == 'right':
            return pygame.Rect(self.x + 23, self.y + 11, 40, 16)

    def get_body_hitbox(self):
        hitbox_width = 16
        hitbox_height = 16
        return pygame.Rect(self.x + (frame_x_slime - hitbox_width) // 2, self.y + (frame_y_slime - hitbox_height) // 2, hitbox_width, hitbox_height)

    def draw(self):
        if self.alive:
            if self.direction == 'up':
                draw_slime(self.x, self.y, slime_run_up)
            elif self.direction == 'down':
                draw_slime(self.x, self.y, slime_run_down)
            elif self.direction == 'left':
                draw_slime(self.x, self.y, slime_run_left)
            elif self.direction == 'right':
                draw_slime(self.x, self.y, slime_run_right)
        elif self.death_animation_playing:
            elapsed_time = pygame.time.get_ticks() - self.death_animation_start_time
            if elapsed_time < self.death_animation_duration:
                frame_index = int(
                    (elapsed_time / self.death_animation_duration) * len(slime_death))
                if frame_index >= len(slime_death):
                    frame_index = len(slime_death) - 1
                tela.blit(slime_death[frame_index], (self.x, self.y))
            else:
                self.death_animation_playing = False

    def play_death_animation(self):
        self.death_animation_playing = True
        self.death_animation_start_time = pygame.time.get_ticks()


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


def get_player_hitbox():
    hitbox_width = 16
    hitbox_height = 16
    return pygame.Rect(player_x + 17, player_y + 22, hitbox_width, hitbox_height)


def draw_hitboxes(slimes):
    global player_alive, slime_alive
    player_hitbox = get_player_hitbox()

    pygame.draw.rect(tela, (255, 0, 0), player_hitbox, 2)

    for slime in slimes:
        if slime.alive:
            vision_hitbox = slime.get_hitbox()
            slime_body_hitbox = slime.get_body_hitbox()

            pygame.draw.rect(tela, (0, 255, 0), vision_hitbox, 2)
            pygame.draw.rect(tela, (0, 0, 255), slime_body_hitbox, 2)
            if slime_body_hitbox.colliderect(player_hitbox):
                print("Jogador foi pego pela slime!")
                game_over()


def is_player_behind_slime(slime):
    global player_x, player_y

    if slime.direction == 'up':
        return player_y > slime.y
    elif slime.direction == 'down':
        return player_y < slime.y
    elif slime.direction == 'left':
        return player_x > slime.x
    elif slime.direction == 'right':
        return player_x < slime.x


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
slimes = [Slime(100, 100)]
last_slime_spawn_time = pygame.time.get_ticks()
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
    if keys[pygame.K_d]:
        player_x += player_speed
        last_direction = 'right'
        moving = True
    if keys[pygame.K_s]:
        player_y += player_speed
        last_direction = 'down'
        moving = True
    if keys[pygame.K_w]:
        player_y -= player_speed
        last_direction = 'up'
        moving = True

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

    for slime in slimes[:]:
        slime.move()
        slime.draw()

        if is_player_behind_slime(slime) and slime.get_body_hitbox().colliderect(get_player_hitbox()):
            print("Slime foi morta pelo jogador!")
            slime.play_death_animation()
            slime.alive = False

        if not slime.alive and not slime.death_animation_playing:
            slimes.remove(slime)

    draw_hitboxes(slimes)

    if pygame.time.get_ticks() - last_slime_spawn_time > 10000:
        new_slime = Slime(randint(100, 700), randint(100, 500))
        slimes.append(new_slime)
        last_slime_spawn_time = pygame.time.get_ticks()

    pygame.display.flip()
    clock.tick(60)
