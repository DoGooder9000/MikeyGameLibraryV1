from MikeyGames import *

window(600, 800, "Test")
 
running = True

while running:
    for event in Get_Event():
        if event == QUIT:
            running = False

close()