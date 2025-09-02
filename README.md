# Rita Sprites

För att rita sprites(bilder på skärmen), behöver du göra följande:

1. Ladda in bilden: 

    ```python
    min_textur = load_texture("filnamn.png")
    ```

Du **måste** öppna fönstret med init_window innan du laddar in bilden.

2. Rita bilden
    
    ```python
    x = 0
    y = 0
    tint = WHITE
    draw_texture(min_textur,x,y,tint)
    ```

Rita bilden gör du efter begin_drawing() men före end_drawing()

3. Ta bort bilden ur arbetsminnet

    ```python
    unload_texture(min_textur)
    ```

Ta bort bilden gör du sist i ditt program, utanför eventloopen.
