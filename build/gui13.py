

import gui14, gui15, gui16
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame,BOTH,ttk,Toplevel

#se crea la pestaña de Conductor con sus botones respectivos a sus funcionalidades y su propia ventana
def conductor():
    
    #lectura de directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame13"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #crea la ventana
    window4 = Toplevel()
    frame4 = Frame(window4)
    window4.title ("YOURWAY TRANSPORT Transportista")
    window4.iconbitmap(relative_to_assets("icon.ico"))
    frame4.pack(fill=BOTH,expand=True)
    window4.geometry("800x600")
    window4.configure(bg = "#FFFFFF")


    canvas = Canvas(
        frame4,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    #imagen
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

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame4,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui15.conductor_editar_estado(frame4),
        relief="flat"
    )#boton que lleva a la funcionalidad de Conductor editar estado
    button_1.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame4,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui14.conductor_ver(frame4),
        relief="flat"
    )#boton que lleva a la funcionalidad de conductor ver envio
    button_2.place(
        x=13.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame4,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui16.conductor_reportar_accidente(frame4),
        relief="flat"
    )#boton que lleva a la funcionalidad de conductor reportar accidente
    button_3.place(
        x=13.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    
    #mantencion de la ventana
    window4.resizable(False, False)
    window4.mainloop()
