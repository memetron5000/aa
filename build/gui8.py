
import datetime
import gui7, gui9, metodos
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

# limpia el frame para poder actualizar la ventana
def titulo(frame2):
    # Limpia el frame
    for item in frame2.winfo_children():
        item.destroy()
        
#creacion de todos los elementos de la ventana y acceso a ruta completa
def gerente_crear_envio(frame2):
    global button_image_1, button_image_2, button_image_3, button_image_4,entry_image_1,entry_image_2,entry_image_3,entry_image_4, entry_image_5, entry_image_6, entry_image_7,  entry_image_8, image_image_1
    
    # Limpia el frame
    titulo(frame2)
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame8"
        
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
        244.0,
        222.0,
        anchor="nw",
        text="Ingrese el identificador del cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
        
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        669.0,
        231.5,
        image=entry_image_1
    )#Cuadro que ingresa el ID del cliente
    entry_1 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=600.0,
        y=219.0,
        width=138.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        239.0,
        262.0,
        anchor="nw",
        text="Ingrese el número de guia aerea:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        670.0,
        272.5,
        image=entry_image_2
    )#Cuadro que ingresa el numero de guia aerea
    entry_2 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=600.0,
        y=260.0,
        width=140.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        241.0,
        301.0,
        anchor="nw",
        text="Ingrese el tipo de producto:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    ) 
    
    #cuadro de texto
    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        670.5,
        313.5,
        image=entry_image_3
    )#Cuadro que ingresa el tipo de producto
    entry_3 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=600.0,
        y=301.0,
        width=141.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        238.0,
        344.0,
        anchor="nw",
        text="Ingrese el destino:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        670.0,
        353.5,
        image=entry_image_4
    )#Cuadro que ingresa el destino
    entry_4 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=600.0,
        y=341.0,
        width=140.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        242.0,
        382.0,
        anchor="nw",
        text="Ingrese la temperatura requerida:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        670.0,
        395.5,
        image=entry_image_5
    )#Cuadro que ingresa la temperatura requerida
    entry_5 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    
    #cuadro de texto
    entry_5.place(
        x=600.0,
        y=383.0,
        width=140.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        239.0,
        421.0,
        anchor="nw",
        text="Ingrese la fecha y hora de entrega:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto
    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        669.0,
        435.5,
        image=entry_image_6
    )#Cuadro que ingresa la hora de entrega
    entry_6 = Entry(
        frame2,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_6.place(
        x=600.0,
        y=423.0,
        width=138.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        226.0,
        499.0,
        anchor="nw",
        text="Nuevo envío creado con ID:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        670.0,
        511.5,
        image=entry_image_7
    )#Cuadro que ingresa el ID del envio nuevo

    #!funcion que registra pedido
    def r_pedido():
        identificador_cliente = entry_1.get()
        if identificador_cliente in metodos.sistema.clientes:
            cliente = metodos.sistema.clientes[identificador_cliente]
            guia_aerea = entry_2.get()
            tipo_producto = entry_3.get()
            destino = entry_4.get()
            temperatura = entry_5.get()
            #hora_entrega = input("Ingrese la hora de entrega (YYYY-MM-DD HH:MM): ")
            while True:
                hora_entrega = entry_6.get()
                try:
                    hora_entrega = datetime.datetime.strptime(hora_entrega, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    messagebox.showerror(title=None, message="El formato de la fecha esta incorrecto\n debe ser (YYYY-MM-DD HH:MM)\n ejemplo 2004-11-27 12:21",)
            
            id_job = metodos.sistema.crear_envio(guia_aerea, cliente, tipo_producto, destino, temperatura, hora_entrega)
            canvas.create_text(
                670.0,
                512.0,
                anchor="center",
                text=id_job,
                fill="#000000",
                font=("MicrosoftSansSerif", 20 * -1)
                )
            messagebox.showinfo(title=None, message="Pedido creado con exito")
        else:
            messagebox.showwarning(title=None, message="cliente no encontrado")
    
    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame2,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: r_pedido(),
        relief="flat"
    )#Boton para crear el pedido
    button_1.place(
        x=387.0,
        y=547.0,
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
        command=lambda: gui7.gerente_registrar(frame2),
        relief="flat"
    )#Boton que lleva a la funcionalidad de gerente registrar cliente
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
        command=lambda: print("ya estas aqui"),
        relief="flat"
    )#boton de la funcionalidad que se esta presentando en la ventana
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
        command=lambda: gui9.gerente_ver_envio(frame2),
        relief="flat"
    )#Boton que lleva a la funcionalidad gerente ver envio
    button_4.place(
        x=13.0,
        y=240.0,
        width=159.0,
        height=56.0
    )
    
