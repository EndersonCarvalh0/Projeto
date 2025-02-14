import pygame
from pygame.locals import *
import sys
import random
from random import randint
from PIL import Image
import os

dir_princ = os.path.dirname(__file__)
dir_img = os.path.join(dir_princ, "In game")
dir_msc = os.path.join(dir_princ, "Musicas")
dir_pers = os.path.join(dir_princ, "Sprites")
dir_font = os.path.join(dir_princ, "font")

pygame.init()
clock = pygame.time.Clock()
temp_play = pygame.time.get_ticks()
pygame.display.set_caption("Mata os Slimes, Cleitin!")

music = pygame.mixer.music.load(os.path.join(dir_msc, "Otonoke.mp3"))
pygame.mixer.music.play(-1)
death_sound = pygame.mixer.Sound(os.path.join(dir_msc, "Slime.wav"))
gold = pygame.mixer.Sound(os.path.join(dir_msc, "Gold.wav"))
gameOver = pygame.mixer.Sound(os.path.join(dir_msc, "GameOver.wav"))

font_path = (os.path.join(dir_font, "G:/EstudoPython/Game/Game/font/PressStart2P-Regular.ttf"))

larg_tela = 900
alt_tela = 900
tela = pygame.display.set_mode((larg_tela, alt_tela))
grass = pygame.image.load(os.path.join(dir_img, "grass1.png")).convert_alpha()
rock = pygame.image.load(os.path.join(dir_img, "rock_in_water_02.png")).convert_alpha()
floorp = pygame.image.load(os.path.join(dir_img, "srock.png")).convert_alpha()
grasses = pygame.image.load(os.path.join(dir_img, "grassn.png")).convert_alpha()
grasses1 = pygame.image.load(os.path.join(dir_img, "grassn1.png")).convert_alpha()
grasses2 = pygame.image.load(os.path.join(dir_img, "grassn2.png")).convert_alpha()
grasses3 = pygame.image.load(os.path.join(dir_img, "grassn3.png")).convert_alpha()
wood = pygame.image.load(os.path.join(dir_img, "wooden.png")).convert_alpha()
santa = pygame.image.load(os.path.join(dir_img, "Santa.png")).convert_alpha()
cova1 = pygame.image.load(os.path.join(dir_img, "cova1.png")).convert_alpha()
cova2 = pygame.image.load(os.path.join(dir_img, "cova2.png")).convert_alpha()
cova3 = pygame.image.load(os.path.join(dir_img, "cova3.png")).convert_alpha()
arvore = pygame.image.load(os.path.join(dir_img, "arvore.png")).convert_alpha()
arvoreg = pygame.image.load(os.path.join(dir_img, "arvoreg.png")).convert_alpha()
bancoesq = pygame.image.load(os.path.join(dir_img, "bancoesq.png")).convert_alpha()
bancodir = pygame.image.load(os.path.join(dir_img, "bancodir.png")).convert_alpha()
bancof = pygame.image.load(os.path.join(dir_img, "bancof.png")).convert_alpha()
spawn = pygame.image.load(os.path.join(dir_img, "spawn.png")).convert_alpha()
spawng = pygame.image.load(os.path.join(dir_img, "spawng.png")).convert_alpha()
placadir = pygame.image.load(os.path.join(dir_img, "placadir.png")).convert_alpha()
placaesq = pygame.image.load(os.path.join(dir_img, "placaesq.png")).convert_alpha()
objl = pygame.image.load(os.path.join(dir_img, "objl.png")).convert_alpha()
caixaoy = pygame.image.load(os.path.join(dir_img, "caixaoy.png")).convert_alpha()
caixaox = pygame.image.load(os.path.join(dir_img, "caixaox.png")).convert_alpha()
pilarg = pygame.image.load(os.path.join(dir_img, "pilarg.png")).convert_alpha()
pilarm = pygame.image.load(os.path.join(dir_img, "pilarm.png")).convert_alpha()
pilarp = pygame.image.load(os.path.join(dir_img, "pilarp.png")).convert_alpha()
escombros = pygame.image.load(os.path.join(dir_img, "escombros.png")).convert_alpha()
gram1 = pygame.image.load(os.path.join(dir_img, "gram1.png")).convert_alpha()
gram2 = pygame.image.load(os.path.join(dir_img, "gram2.png")).convert_alpha()
gram3 = pygame.image.load(os.path.join(dir_img, "gram3.png")).convert_alpha()
moeda = pygame.image.load(os.path.join(dir_img, "moeda.png")).convert_alpha()
map = Image.open("In game\map1.png")


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


run_up = pygame.image.load(os.path.join(dir_pers, 'andandoc (1).png')).convert_alpha()
run_down = pygame.image.load(os.path.join(dir_pers, 'andandof (1).png')).convert_alpha()
run_left = pygame.image.load(os.path.join(dir_pers, 'andandole (2).png')).convert_alpha()
run_right = pygame.image.load(os.path.join(dir_pers, 'andandol (1).png')).convert_alpha()

sup = pygame.image.load(os.path.join(dir_pers, 'paradoc.png')).convert_alpha()
sdown = pygame.image.load(os.path.join(dir_pers, 'paradof.png')).convert_alpha()
sleft = pygame.image.load(os.path.join(dir_pers, 'paradole.png')).convert_alpha()
sright = pygame.image.load(os.path.join(dir_pers, 'paradol.png')).convert_alpha()

slime_up = pygame.image.load(os.path.join(dir_pers, 'slimec.png')).convert_alpha()
slime_down = pygame.image.load(os.path.join(dir_pers, 'slimef.png')).convert_alpha()
slime_left = pygame.image.load(os.path.join(dir_pers, 'slimele.png')).convert_alpha()
slime_right = pygame.image.load(os.path.join(dir_pers, 'slimel.png')).convert_alpha()

pslime_up = pygame.image.load(os.path.join(dir_pers, 'pslimec.png')).convert_alpha()
pslime_down = pygame.image.load(os.path.join(dir_pers, 'pslimef.png')).convert_alpha()
pslime_left = pygame.image.load(os.path.join(dir_pers, 'pslimele.png')).convert_alpha()
pslime_right = pygame.image.load(os.path.join(dir_pers, 'pslimel.png')).convert_alpha()

death_slime = pygame.image.load(os.path.join(dir_pers, "slimedeath.png")).convert_alpha()

frame_x = 48
frame_y = 58
stand_frames = 4
num_frames = 6
num_rows = 1
stand_frames = 6

frame_x_slime = 33
frame_y_slime = 38
slime_frames = 6
death_slime_frames = 5
stand_slime_frames = 4

moeda_x = 16
moeda_y = 16
moeda_frames = 5
points = 0
spawn_interval = random.randint(10000, 15000)
last_spawn_time = pygame.time.get_ticks()

moeda = cut_sprite(moeda, moeda_x, moeda_y, moeda_frames, num_rows)

player_run_up = cut_sprite(run_up, frame_x, frame_y, num_frames, num_rows)
player_run_down = cut_sprite(run_down, frame_x, frame_y, num_frames, num_rows)
player_run_left = cut_sprite(run_left, frame_x, frame_y, num_frames, num_rows)
player_run_right = cut_sprite(run_right, frame_x, frame_y, num_frames, num_rows)

player_stand_up_frames = cut_sprite(sup, frame_x, frame_y, stand_frames, num_rows)
player_stand_down_frames = cut_sprite(sdown, frame_x, frame_y, stand_frames, num_rows)
player_stand_left_frames = cut_sprite(sleft, frame_x, frame_y, stand_frames, num_rows)
player_stand_right_frames = cut_sprite(sright, frame_x, frame_y, stand_frames, num_rows)

slime_run_up = cut_sprite(slime_up, frame_x_slime,frame_y_slime, slime_frames, num_rows)
slime_run_down = cut_sprite(slime_down, frame_x_slime, frame_y_slime, slime_frames, num_rows)
slime_run_left = cut_sprite(slime_left, frame_x_slime, frame_y_slime, slime_frames, num_rows)
slime_run_right = cut_sprite(slime_right, frame_x_slime, frame_y_slime, slime_frames, num_rows)

slime_stand_up = cut_sprite(pslime_up, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_down = cut_sprite(pslime_down, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_left = cut_sprite(pslime_left, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)
slime_stand_right = cut_sprite(pslime_right, frame_x_slime, frame_y_slime, stand_slime_frames, num_rows)

slime_death = cut_sprite(death_slime, frame_x_slime,frame_y_slime, death_slime_frames, num_rows)

player_larg = 16
player_alt = 16
player_x = 15
player_y = 810
player_speed = 2
current_frame = 0
frame_time = 100
last_frame_time = pygame.time.get_ticks()

last_direction = None

slime_deaths = 0
player_alive = True
slime_alive = True

hitboxes_for_player = []
hitboxes_for_slime = []


def check_collision(rect, hitboxes):
    for hitbox in hitboxes:
        if rect.colliderect(hitbox):
            return True
    return False


class Slime:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        self.steps = 0
        self.max_steps = 150
        self.min_steps = 25
        self.pause_duration = randint(500, 3000)
        self.last_change_time = 0
        self.is_paused = False
        self.is_berserk = False
        self.start_berserk = 0
        self.berserk_duration = 10000
        self.death_animation_playing = False
        self.death_animation_start_time = 0
        self.death_animation_duration = 750
        self.alive = True

    def move(self):
        player_hitbox = get_player_hitbox()
        vision_hitbox = self.get_hitbox()

        global player_x, player_y

        if not self.alive:
            return

        slime_hitbox = self.get_hitbox()
        if check_collision(slime_hitbox, hitboxes_for_slime):
            self.change_direction()

        if vision_hitbox.colliderect(player_hitbox):
            if vision_hitbox.colliderect(player_hitbox):
                if not self.is_berserk:
                    self.is_berserk = True
                    self.berserk_start_time = pygame.time.get_ticks()

        if self.is_berserk:
            if pygame.time.get_ticks() - self.berserk_start_time >= self.berserk_duration:
                self.is_berserk = False
            else:
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
            self.y -= 1.25
        elif self.direction == 'down':
            self.y += 1.25
        elif self.direction == 'left':
            self.x -= 1.25
        elif self.direction == 'right':
            self.x += 1.25

        self.steps += 1

    def change_direction(self):
        self.direction = random.choice(['up', 'down', 'left', 'right'])
        print("mudando")

    def berserk(self):
        global player_x, player_y
        dx = player_x - self.x
        dy = player_y - self.y

        if abs(dx) > abs(dy):
            if dx > 0:
                self.direction = 'right'
            else:
                self.direction = 'left'
        else:
            if dy > 0:
                self.direction = 'down'
            else:
                self.direction = 'up'

        next_x, next_y = self.x, self.y
        speed_slime = 1.85
        if self.direction == 'up':
            next_y -= speed_slime
        elif self.direction == 'down':
            next_y += speed_slime
        elif self.direction == 'left':
            next_x -= speed_slime
        elif self.direction == 'right':
            next_x += speed_slime

        next_hitbox = pygame.Rect(next_x, next_y, self.get_hitbox().width, self.get_hitbox().height)
        if not check_collision(next_hitbox, hitboxes_for_slime):
            self.x, self.y = next_x, next_y
        else:
            self.change_direction()

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
                frame_index = int((elapsed_time / self.death_animation_duration) * len(slime_death))
                if frame_index >= len(slime_death):
                    frame_index = len(slime_death) - 1
                tela.blit(slime_death[frame_index], (self.x, self.y))
            else:
                self.death_animation_playing = False

    def play_death_animation(self):
        death_sound.play()
        self.death_animation_playing = True
        self.death_animation_start_time = pygame.time.get_ticks()

def spawn_coin():
    spawn_point = random.choice(spawn_coin_points)
    coins.append(spawn_point)

def draw_coins():
    for coin in coins:
        tela.blit(moeda[current_frame % len(moeda)], coin)

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
    return pygame.Rect(player_x + 17, player_y + 24, hitbox_width, hitbox_height)

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

def stats():
    global slime_deaths
    font = pygame.font.Font(font_path, 10)
    slime_text = font.render(f'Slime Deaths: {slime_deaths}', True, (0, 175, 0))
    point_text = font.render(f'Points: {points}', True, (0, 175, 0))
    elapsed_time = pygame.time.get_ticks() - temp_play
    seconds = (elapsed_time // 1000) % 60
    minutes = (elapsed_time // 60000) % 60
    time_text = font.render(f'Time: {minutes:02}:{seconds:02}', True, (0, 175, 0))
    slime_rect = slime_text.get_rect(topleft=(5, 5))
    time_rect = time_text.get_rect(topleft=(165, 5))
    point_rect = point_text.get_rect(topleft=(295, 5))
    tela.blit(slime_text, slime_rect)
    tela.blit(time_text, time_rect)
    tela.blit(point_text, point_rect)

def game_over():
    pygame.mixer.music.stop()
    gameOver.play()
    font = pygame.font.Font(font_path, 80)
    font2 = pygame.font.Font(font_path, 20)
    font3 = pygame.font.Font(font_path, 15)
    text = font.render('GAME OVER', True, (255, 0, 0))
    text_rect = text.get_rect(center=(larg_tela // 2, alt_tela // 2))
    text2 = font2.render("Tente novamente pressinando ESPAÇO", True, (255, 0, 0))
    text2_rect = text2.get_rect(center=(larg_tela // 2, alt_tela // 2 + 70))
    mensagens = [("A sorte favorece os audazes..."), ("O homem é a slime do próprio homem..."), ("A força sem sabedoria rui pelo seu próprio peso..."), ("O homem está condenado a ser livre... A slime também..."), ("O conforto é o pior vício..."), ("Ao sem talento, obsessão...")]
    msg = random.choice(mensagens)
    text3 = font3.render(msg, True, (255, 255, 255))
    text3_rect = text3.get_rect(center=(larg_tela // 2, alt_tela // 2 + 400))
    tela.blit(text, text_rect)
    tela.blit(text2, text2_rect)
    tela.blit(text3, text3_rect)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reiniciar_jogo()
                    return

def reiniciar_jogo():
    global temp_play, slime_deaths, player_x, player_y, slimes, coins, points
    pygame.mixer.music.play(-1)
    temp_play = pygame.time.get_ticks()
    slime_deaths = 0
    points = 0
    player_x = 15
    player_y = 810
    slimes = []
    coins = []

last_direction = 'right'
tela.blit(player_stand_right_frames[0], (player_x, player_y))
pygame.display.flip()

clock = pygame.time.Clock()
slimes = []
slimes_death = []
spawn_coin_points = [(47, 45), (836, 50), (837, 375)]
coins = []
spawn_points = [(35, 30), (830, 30), (830, 360)]
last_slime_spawn_time = 0
running = True
while running:
    tela.fill((0, 0, 0))
    hitboxes_for_player.clear()
    hitboxes_for_slime.clear()
    current_time = pygame.time.get_ticks()

    if current_time - last_spawn_time >= spawn_interval:
        spawn_coin()
        last_spawn_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    xy = [0, 0]
    for x in range(30):
        for y in range(30):
            xy = [x, y]
            pixel = map.getpixel(xy)
            if pixel == (0, 0, 0):
                tela.blit(grass, (x*30, y*30))
            if pixel == (255, 255, 255):
                tela.blit(rock, (x*30, y*30))
                hitbox = pygame.Rect(x * 30, y * 30, 30, 30)
                hitboxes_for_player.append(hitbox)
                pygame.draw.rect(tela, (0, 0, 0), hitbox, 2)
            if pixel == (127, 127, 127):
                tela.blit(floorp, (x*30, y*30))
            if pixel == (0, 0, 255):
                tela.blit(wood, (x*30, y*30))
                hitbox = pygame.Rect(x * 30, y * 30, 30, 30)
                hitboxes_for_slime.append(hitbox)
                hitboxes_for_player.append(hitbox)
                pygame.draw.rect(tela, (0, 0, 0), hitbox, 2)

    tela.blit(grasses, (90, 180))
    tela.blit(grasses, (90, 210))
    tela.blit(grasses, (60, 210))
    tela.blit(santa, (375, 0))
    tela.blit(cova1, (330, 75))
    tela.blit(cova2, (380, 75))
    tela.blit(cova3, (420, 85))
    tela.blit(arvore, (255, 675))
    tela.blit(arvore, (437, 465))
    tela.blit(arvoreg, (460, -60))
    tela.blit(grasses2, (305, 500))
    tela.blit(grasses2, (305, 530))
    tela.blit(grasses2, (215, 500))
    tela.blit(grasses2, (215, 530))
    tela.blit(grasses1, (240, 30))
    tela.blit(grasses2, (240, 85))
    tela.blit(grasses2, (240, 120))
    tela.blit(grasses3, (500, 70))
    tela.blit(bancoesq, (450, 120))
    tela.blit(bancodir, (300, 120))
    tela.blit(bancof, (500, 550))
    tela.blit(bancof, (400, 550))
    tela.blit(spawn, (30, 20))
    tela.blit(spawn, (820, 20))
    tela.blit(spawn, (820, 350))
    tela.blit(spawng, (435, 790))
    tela.blit(placadir, (170, 775))
    tela.blit(placadir, (275, 380))
    tela.blit(placaesq, (240, 380))
    tela.blit(objl, (845, 830))
    tela.blit(caixaoy, (750, 810))
    tela.blit(caixaox, (120, 500))
    tela.blit(pilarg, (840, 525))
    tela.blit(pilarm, (840, 100))
    tela.blit(pilarp, (25, 130))
    tela.blit(pilarg, (500, 700))
    tela.blit(pilarm, (450, 700))
    tela.blit(pilarp, (400, 700))
    tela.blit(escombros, (600, 820))
    tela.blit(gram1, (90, 30))
    tela.blit(gram2, (120, 80))
    tela.blit(gram3, (150, 150))
    tela.blit(gram3, (70, 240))
    tela.blit(gram2, (400, 100))
    tela.blit(gram1, (330, 105))
    tela.blit(gram2, (400, 160))
    tela.blit(gram1, (330, 165))
    tela.blit(gram3, (230, 150))
    tela.blit(gram1, (500, 165))
    tela.blit(gram3, (570, 165))
    tela.blit(gram2, (640, 165))
    tela.blit(gram1, (710, 165))
    tela.blit(gram3, (780, 165))
    tela.blit(gram1, (500, 110))
    tela.blit(gram3, (570, 110))
    tela.blit(gram2, (640, 110))
    tela.blit(gram1, (710, 110))
    tela.blit(gram3, (780, 110))
    tela.blit(gram1, (580, 50))
    tela.blit(gram2, (660, 30))
    tela.blit(gram3, (730, 30))
    tela.blit(gram1, (790, 220))
    tela.blit(gram3, (730, 220))
    tela.blit(gram2, (660, 220))
    tela.blit(gram3, (590, 220))
    tela.blit(gram1, (640, 280))
    tela.blit(gram3, (640, 340))
    tela.blit(gram2, (640, 400))
    tela.blit(gram3, (700, 390))
    tela.blit(gram1, (770, 390))
    tela.blit(gram2, (670, 460))
    tela.blit(gram3, (730, 460))
    tela.blit(gram2, (780, 590))
    tela.blit(gram1, (670, 600))
    tela.blit(gram2, (670, 670))
    tela.blit(gram3, (600, 650))
    tela.blit(gram1, (600, 720))
    tela.blit(gram2, (600, 790))
    tela.blit(gram1, (530, 640))
    tela.blit(gram3, (460, 640))
    tela.blit(gram2, (390, 640))
    tela.blit(gram3, (250, 620))
    tela.blit(gram1, (180, 620))
    tela.blit(gram3, (110, 620))
    tela.blit(gram2, (180, 690))
    tela.blit(gram3, (40, 620))
    tela.blit(gram3, (180, 540))
    tela.blit(gram1, (115, 540))
    tela.blit(gram3, (270, 805))
    tela.blit(gram2, (340, 805))
    tela.blit(gram3, (270, 330))
    tela.blit(gram1, (210, 330))
    tela.blit(gram1, (270, 270))
    tela.blit(gram2, (210, 270))
    tela.blit(gram3, (310, 210))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for coin in coins[:]:
        coin_rect = pygame.Rect(coin[0], coin[1], moeda_x, moeda_y)
        if player_hitbox.colliderect(coin_rect):
            gold.play()
            points += 100
            coins.remove(coin)
            spawn_coin()

    if len(coins) == 0:
        for _ in range(1):
            spawn_coin()
    current_time = pygame.time.get_ticks()

    if current_time - last_spawn_time >= spawn_interval:
        spawn_coin()
        last_spawn_time = current_time

    if pygame.time.get_ticks() - last_frame_time > frame_time:
        last_frame_time = pygame.time.get_ticks()
        current_frame = (current_frame + 1) % len(moeda)
    draw_coins()

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
    if check_collision(player_hitbox, hitboxes_for_player):
        if last_direction == 'left':
            player_x += player_speed
        elif last_direction == 'right':
            player_x -= player_speed
        elif last_direction == 'down':
            player_y -= player_speed
        elif last_direction == 'up':
            player_y += player_speed

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
            tela.blit(player_stand_up_frames[current_frame], (player_x, player_y))
        elif last_direction == 'down':
            tela.blit(player_stand_down_frames[current_frame], (player_x, player_y))
        elif last_direction == 'left':
            tela.blit(player_stand_left_frames[current_frame], (player_x, player_y))
        elif last_direction == 'right':
            tela.blit(player_stand_right_frames[current_frame], (player_x, player_y))

    for slime in slimes[:]:
        slime.move()
        slime.draw()

        slime_hitbox = slime.get_body_hitbox()
        if check_collision(slime_hitbox, hitboxes_for_slime):
            if slime.direction == 'up':
                slime.y += 1
            elif slime.direction == 'down':
                slime.y -= 1
            elif slime.direction == 'left':
                slime.x += 1
            elif slime.direction == 'right':
                slime.x -= 1

        if is_player_behind_slime(slime) and slime.get_body_hitbox().colliderect(get_player_hitbox()):
            print("Slime foi morta pelo jogador!")
            slime_deaths += 1
            points += 10
            slime.play_death_animation()
            slime.alive = False
            slimes_death.append(slime)
            slimes.remove(slime)

        if not slime.alive and not slime.death_animation_playing:
            slimes.remove(slime)

    for slime_morta in slimes_death:
        slime_morta.draw()
        if not slime_morta.death_animation_playing:
            slimes_death.remove(slime_morta)

    if pygame.time.get_ticks() - last_slime_spawn_time > 3500:
        spawn_x, spawn_y = random.choice(spawn_points)
        new_slime = Slime(spawn_x, spawn_y)
        slimes.append(new_slime)
        last_slime_spawn_time = pygame.time.get_ticks()
    
    stats()
    draw_hitboxes(slimes)

    pygame.display.flip()
    clock.tick(60)