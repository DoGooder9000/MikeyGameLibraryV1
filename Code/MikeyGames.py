import pygame
import time


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