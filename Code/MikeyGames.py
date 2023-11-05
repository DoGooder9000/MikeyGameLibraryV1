import pygame
import time


#Event Types#

QUIT = pygame.QUIT
KEYDOWN = pygame.KEYDOWN


def init():
    pygame.init()

def close():
    pygame.quit()

def wait(sec: float):
    time.sleep(sec)

def window(width: int, height: int, name: str = None):
    window = pygame.display.set_mode((width, height))
    if name: pygame.display.set_caption(name)
    return window

def Get_Event():
    return pygame.event.get()