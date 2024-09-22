


import gui14,gui15, metodos
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk

# limpia el frame para poder actualizar la ventana
def titulo(frame4):
    # Limpia el frame
    for item in frame4.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa     
def conductor_reportar_accidente(frame4):
    global button_image_1, button_image_2, button_image_3, button_image_4,entry_image_1, entry_image_2, entry_image_3, entry_image_4, image_image_1
    
    #limpia el frame
    titulo(frame4)

    #verifica directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame16"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #lectura de frame
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

    #texto
    canvas.create_text(
        232.0,
        117.0,
        anchor="nw",
        text="ID del envio:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
     #cuadro de texto
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        639.0,
        129.5,
        image=entry_image_4
    )#Cuadro para poner la ubicacion del accidente
    entry_4 = Entry(
        frame4,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=525.0,
        y=112.0,
        width=228.0,
        height=33.0
    )

    #texto
    canvas.create_text(
        261.0,
        174.0,
        anchor="nw",
        text="Ubicacion del accidente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        639.0,
        179.5,
        image=entry_image_1
    )#Cuadro para poner la ubicacion del accidente
    entry_1 = Entry(
        frame4,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=525.0,
        y=162.0,
        width=228.0,
        height=33.0
    )

    
    #texto
    canvas.create_text(
        261.0,
        256.0,
        anchor="nw",
        text="Detalles accidente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        639.0,
        324.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        frame4,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=525.0,
        y=256.0,
        width=228.0,
        height=134.0
    )


    #!funcion que genera accidentes
    def gen_accidente():
        id_job = entry_4.get()
        if id_job in metodos.sistema.envios:
            pass
        else:
            messagebox.showerror(title=None, message=f'No se ha encontrado ningún envío con el id {id_job}')
        ubicacion=entry_1.get()
        detalle=entry_3.get()
        envio = metodos.sistema.envios[id_job]
        envio.accidente=detalle
        metodos.sistema.actualizar_estado_envio(id_job, metodos.EstadoEnvio["EN_RETRASO"], ubicacion)
        messagebox.showinfo(title=None, message="Accidente ingresado con éxito y estado cambiado a: En retraso ")
        
    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame4,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gen_accidente(),
        relief="flat"
    )#Boton que lleva a funcionalidad
    button_1.place(
        x=423.10400390625,
        y=518.0,
        width=168.89610290527344,
        height=37.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame4,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui15.conductor_editar_estado(frame4),
        relief="flat"
    )
    button_2.place(
        x=14.0,
        y=58.0,
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
        command=lambda: gui14.conductor_ver(frame4),
        relief="flat"
    )#Boton que lleva a funcionalidad
    button_3.place(
        x=13.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame4,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ya estas aqui"),
        relief="flat"
    )#Boton que lleva a funcionalidad
    button_4.place(
        x=13.0,
        y=240.0,
        width=158.0,
        height=56.0
    )