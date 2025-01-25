import pygame
from pygame.locals import *
import sys

pygame.init()
pygame.display.set_caption("Kill Those Slimes, Cleitin!")

larg_tela = 800
alt_tela = 600
tela = pygame.display.set_mode((larg_tela, alt_tela)) #Observar para adaptar melhor o tamanho da tela

WHITE = (255, 255, 255) #Lembrar de tirar depois, pra colocar o fundo do game mesmo

def cut_sprite(sprite, frame_x, frame_y, num_frames, linha_frame):
    animation = []
    larg_sheet, alt_sheet = sprite.get_size()
    for l in range(linha_frame):
        for c in range(num_frames):
            x = c * frame_x
            y = l * frame_y
            cut_frame = pygame.Rect(x, y, frame_x, frame_y)
            frame = sprite.subsurface(cut_frame)
            animation.append(frame)
    return animation

#Esperando os cortes para colocar as sprites
sprite_sup = pygame.image.load("")
sprite_sdown = pygame.image.load("")
sprite_sleft = pygame.image.load("")
sprite_sright = pygame.image.load("")

sprite_up = pygame.image.load("")
sprite_down = pygame.image.load("")
sprite_left = pygame.image.load("")
sprite_right = pygame.image.load("")

sprite_atk_up = pygame.image.load("")
sprite_atk_down = pygame.image.load("")
sprite_atk_left = pygame.image.load("")
sprite_atk_right = pygame.image.load("")

sprite_dead = pygame.image.load("")

#Sprite Slime
sprite_up_slime = pygame.image.load("")
sprite_down_slime = pygame.image.load("")
sprite_left_slime = pygame.image.load("")
sprite_right_slime = pygame.image.load("")

sprite_dead_slime = pygame.image.load("")

#parametros da animação, obs* lembrar de colocar os outros
frame_x = 48
frame_y = 48
num_frames = 6
linha_frame = 1
atk_frames = 4
dead_frames = 3

stop_up = cut_sprite(sprite_sup, frame_x, frame_y, num_frames, linha_frame)
stop_down = cut_sprite(sprite_sdown, frame_x, frame_y, num_frames, linha_frame)
stop_left = cut_sprite(sprite_sleft, frame_x, frame_y, num_frames, linha_frame)
stop_right = cut_sprite(sprite_sright, frame_x, frame_y, num_frames, linha_frame)

run_up = cut_sprite(sprite_up, frame_x, frame_y, num_frames, linha_frame)
run_down = cut_sprite(sprite_down, frame_x, frame_y, num_frames, linha_frame)
run_left = cut_sprite(sprite_left, frame_x, frame_y, num_frames, linha_frame)
run_right = cut_sprite(sprite_right, frame_x, frame_y, num_frames, linha_frame)

atk_up = cut_sprite(sprite_atk_up, frame_x, frame_y, num_frames, linha_frame)
atk_down = cut_sprite(sprite_atk_down, frame_x, frame_y, num_frames, linha_frame)
atk_left = cut_sprite(sprite_atk_left, frame_x, frame_y, num_frames, linha_frame)
atk_right = cut_sprite(sprite_atk_right, frame_x, frame_y, num_frames, linha_frame)

death = cut_sprite(sprite_dead, frame_x, frame_y, num_frames, linha_frame)

#faltam alguns parâmetros, atualizar conforme faz
pframe = 0
frame_time = 100
last_frame_time = pygame.time.get_ticks()

last_direction = None
is_atk = False
atk_frame_time = 100
last_atk_time = pygame.time.get_ticks()

player_alt = 50
player_larg = 50
player_speed = 2

player_x = (alt_tela - larg_tela) // 2
player_y = (alt_tela - larg_tela) // 2

#desenhar a sprite
def play_animation(x, y, anime):
    if pframe < len(anime):
        tela.blit(anime[pframe], (x, y))
    else:
        tela.blit(anime[0], (x, y))

#loop principal, atualizar sempre
clock = pygame.time.Clock()
running =  True
while running:
    tela.fill(WHITE)
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


    pygame.display.flip()
    

pygame.quit()
sys.exit()