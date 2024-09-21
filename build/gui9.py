

import gui7, gui8
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# limpia el frame para poder actualizar la ventana
def titulo(frame2):
    # Limpia el frame
    for item in frame2.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa      
def gerente_ver_envio(frame2):
    global button_image_1, button_image_2, button_image_3, button_image_4,entry_image_1,image_image_1
    
    #limpieza de frame
    titulo(frame2)
    
    #verificacion directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame9"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    #lectura de frame
    canvas = Canvas(
        frame2,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        93.0,
        300.0,
        image=image_image_1
    )

    #texto
    canvas.create_text(
        400.0,
        24.0,
        anchor="nw",
        text="BIENVENIDO",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )

    #texto
    canvas.create_text(
        275.0,
        121.0,
        anchor="nw",
        text="Ingrese el ID del envío:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        631.0,
        135.5,
        image=entry_image_1
    )#Cuadro que indica el ID del pedido que se quiere buscar
    entry_1 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=564.0,
        y=118.0,
        width=134.0,
        height=33.0
    )

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame2,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Buscar"),
        relief="flat"
    )#Boton para indicar que ID de pedido buscar
    button_1.place(
        x=729.0,
        y=113.0,
        width=50.0,
        height=45.0
    )

    #texto
    canvas.create_text(
        273.0,
        173.0,
        anchor="nw",
        text="Datos actuales del envío:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        213.0,
        anchor="nw",
        text="Guía aérea",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        213.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        274.0,
        253.0,
        anchor="nw",
        text="Cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        253.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        278.0,
        293.0,
        anchor="nw",
        text="Tipo de medicamento:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        293.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        274.0,
        333.0,
        anchor="nw",
        text="Destino:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        335.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        273.0,
        376.0,
        anchor="nw",
        text="Estado:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        376.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        275.0,
        416.0,
        anchor="nw",
        text="Temperatura:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        417.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        277.0,
        456.0,
        anchor="nw",
        text="Hora de entrega:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        456.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        277.0,
        496.0,
        anchor="nw",
        text="Ubicación actual:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        621.0,
        496.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame2,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui7.gerente_registrar(frame2),
        relief="flat"
    )#Boton que lleva a la funcionalidad de gerente registrar cliente
    button_2.place(
        x=13.0,
        y=58.0,
        width=159.0,
        height=56.0
    )

    #boton
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame2,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui8.gerente_crear_envio(frame2),
        relief="flat"
    )#Boton que lleva a la funcionalidad de gerente crear envio
    button_3.place(
        x=13.0,
        y=149.0,
        width=159.0,
        height=56.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame2,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ya estas aca"),
        relief="flat"
    )#boton de la funcionalidad que se esta presentando en la ventana
    button_4.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    