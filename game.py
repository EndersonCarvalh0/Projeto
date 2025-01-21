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
