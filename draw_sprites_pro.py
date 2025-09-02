from pyray import *

screen_width = 400
screen_height = 400

init_window(screen_width,screen_height,"Rita Sprites")
'''
    Importera alltid texturer efter att du skapat fönstret.
'''
birds = load_texture("Winter_Birds.png")
pic_width = 48 #Används ej 
pic_height = 48 #Används ej 
source_rec = Rectangle(0,0,16,16) # Området på bilden
dest_rec = Rectangle (100,100,32,32) # Området på skärmen 
rotation = 0 #Om man vill rotera bilden
position = (0,0) # Bildens position på skärmen (x,y)-koordinater
while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_texture_pro(birds,source_rec,dest_rec,position,rotation,WHITE) #Texture,X,Y,Tint
    end_drawing()


unload_texture(birds) # Kasta bort texturen från GPU-minnet
