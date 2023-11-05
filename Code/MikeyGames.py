import pygame
import pygame.gfxdraw
import time


#Event Types#

QUIT = pygame.QUIT
KEYDOWN = pygame.KEYDOWN

#Basic Color Tuples
black = (0, 0, 0)
white = (255, 255, 255)

#Colors
class Color:
    def __init__(self, rgb: (int, int, int)):
        self.rgb = rgb
        self.r = rgb[0]
        self.g = rgb[1]
        self.b = rgb[2]

#Basic Drawing Functions#
class Draw:
    def __init__(self):
        self.Color = Color(white)

    def Window_Fill(self, window):
        window.fill(self.Color.rgb)
        
    
    def Point(self, window, x: int, y: int):
        pygame.gfxdraw.pixel(window, x, y, self.Color.rgb)

    def Line(self, window, p1: (int, int), p2: (int, int)):
        pygame.gfxdraw.line(window, p1[0], p1[1], p2[0], p2[1], self.Color.rgb)


def init():
    pygame.init()

def close():
    pygame.quit()

def wait(sec: float):
    time.sleep(sec)

def Window(width: int, height: int, name: str = None):
    window = pygame.display.set_mode((width, height))
    if name: pygame.display.set_caption(name)
    return window

def Get_Event():
    return pygame.event.get()

def Update():
    pygame.display.update()