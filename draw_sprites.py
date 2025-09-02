from pyray import *

screen_width = 400
screen_height = 400

init_window(screen_width,screen_height,"Rita Sprites")
'''
    Importera alltid texturer efter att du skapat fönstret.
'''
birds = load_texture("Winter_Birds.png")
while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_texture(birds,0,0,WHITE) #Texture,X,Y,Tint
    end_drawing()


unload_texture(birds) # Kasta bort texturen från GPU-minnet
