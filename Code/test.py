from MikeyGames import *

window(600, 600, "Test")
 
running = True

while running:
    for event in Get_Event():
        if event.type == QUIT:
            running = False

close()