from MikeyGames import *

window = Window(600, 600, "Test")

Drawer = Draw()
 
running = True

while running:
    for event in Get_Event():
        if event.type == QUIT:
            running = False
    
    Drawer.Color = Color(black)
    Drawer.Window_Fill(window)
    Drawer.Color = Color(white)
    Drawer.Line(window, (0, 0), (100, 100))
    Update()

close()