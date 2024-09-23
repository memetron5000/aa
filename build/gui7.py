

import gui8, gui9, metodos
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

# limpia el frame para poder actualizar la ventana
def titulo(frame2):
    # Limpia el frame
    for item in frame2.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa     
def gerente_registrar(frame2):
    global button_image_1, button_image_2, button_image_3, button_image_4,entry_image_1,entry_image_2,image_image_1
    
    #limpia el frame
    titulo(frame2)
    
    #verifica directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame7"
        
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
        216.0,
        132.0,
        anchor="nw",
        text="Ingrese el nombre del cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        637.0,
        139.5,
        image=entry_image_1
    )# aca se ingresa el nombre del cliente
    entry_1 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=570.0,
        y=124.0,
        width=134.0,
        height=29.0
    )

    #cuadro de texto
    canvas.create_text(
        216.0,
        180.0,
        anchor="nw",
        text="Ingrese el identificador del cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        637.0,
        190.5,
        image=entry_image_2
    )## aca se ingresa el ID del cliente
    entry_2 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=570.0,
        y=175.0,
        width=134.0,
        height=29.0
    )

    #!registrar cliente
    def re_cli():
        try:
            id=int(entry_2.get())
            if entry_1.get() == "" or id == None:
                messagebox.showwarning(title=None, message="rellene todos los campos correctamente \n nombre= solo letras \n id= solo numeros")
            else:
                nombre=entry_1.get()
                identificador=entry_2.get()
                if identificador not in metodos.sistema.clientes:
                    nuevo_cliente = metodos.Cliente(nombre, identificador)
                    metodos.sistema.agregar_usuario(nuevo_cliente)
                    messagebox.showinfo(title=None, message=(f"Nuevo cliente agregado con nombre: {nombre} e identificador JOB: {identificador}"))
                else: 
                    messagebox.showinfo(title=None, message="El cliente ya se encuentra registrado")
        except ValueError:
            messagebox.showerror(title=None, message="El id debe ser un valor entero")
            
        
    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame2,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: re_cli(),
        relief="flat"
    )#boton de crear nuevo cliente
    button_1.place(
        x=422.0,
        y=251.0,
        width=153.0,
        height=37.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame2,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ya estas aqui"),
        relief="flat"
    )#boton de la funcionalidad que se esta presentando en la ventana
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
        frame2,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui8.gerente_crear_envio(frame2),
        relief="flat"
    )#boton que lleva a la funcionalidad de gerente crear envio
    button_3.place(
        x=13.0,
        y=149.0,
        width=159.0,
        height=57.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame2,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui9.gerente_ver_envio(frame2),
        relief="flat"
    )#boton que lleva a la funcionalidad de gerente ver envio
    button_4.place(
        x=13.0,
        y=240.0,
        width=159.0,
        height=56.0
    )
