


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox,ttk
import gui19, gui20, metodos

# limpia el frame para poder actualizar la ventana
def titulo(frame5):
    # Limpia el frame
    for item in frame5.winfo_children():
        item.destroy()

#creacion de todos los elementos de la ventana y acceso a ruta completa      
def cliente_ver_pedido(frame5):
    global button_image_1, button_image_2, button_image_3, button_image_4, button_image_5,entry_image_1,image_image_1
    
    # Limpia el frame
    titulo(frame5)
    
    
    #verifica directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame18"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #lectura de frame
    canvas = Canvas(
        frame5,
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
        text="Ver mis pedidos",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )

    #texto
    canvas.create_text(
        250.0,
        111.0,
        anchor="nw",
        text="Ingrese el ID del cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #! funcion que verifica los pedidos del cliente y los enlista
    def pedidos():
        identificador = entry_1.get()
        if identificador in metodos.sistema.clientes:
            cliente=metodos.sistema.clientes[identificador]
            if cliente.envios:
                cli=[]
                for envio in cliente.envios:
                    cli.append(metodos.sistema.obtener_info_job(envio.id_job))
            else:
                messagebox.showinfo(title=None, message="no tiene pedidos registrados")
        else:
            messagebox.showwarning(title=None, message="cliente no encontrado")
        global combo
        combo = ttk.Combobox(frame5,state="readonly", values=cli)
        combo.place(x=556.0, y=175.0)
    
    #boton que busca los pedidos del cliente
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        frame5,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: pedidos(),
        relief="flat"
    )#Boton para buscar el envio con el ID especificado
    button_5.place(
        x=729.0,
        y=101.0,
        width=50.0,
        height=45.0
    )
    
    
    #texto
    canvas.create_text(
        250.0,
        171.0,
        anchor="nw",
        text="Ingrese el ID del envío a ver:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        631.0,
        125.5,
        image=entry_image_1
    )#Cuadro donde se ingresa ID del envio a ver
    entry_1 = Entry(
        frame5,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=564.0,
        y=108.0,
        width=134.0,
        height=33.0
    )

    #!buscar envio
    def bus_pedido():
        id_job = combo.get()
        if id_job not in metodos.sistema.envios:
            messagebox.showwarning(title=None, message=f"No se ha encontrado ningún envío con el id {id_job}")
        if id_job in metodos.sistema.envios:
            envio = metodos.sistema.envios[id_job]
            canvas.itemconfig(guia_text, text=envio.guia_aerea)
            canvas.itemconfig(cliente_text, text=envio.cliente.nombre)
            canvas.itemconfig(tipo_text, text=envio.tipo_producto)
            canvas.itemconfig(dest_text, text=envio.destino)
            canvas.itemconfig(est_text, text=envio.estado_actual.value)
            canvas.itemconfig(temp_text, text=envio.temperatura)
            canvas.itemconfig(hora_text, text=envio.hora_entrega)
            canvas.itemconfig(ubi_text, text=envio.ubicacion_actual)
    
    #?boton que ve los archivos
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame5,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: bus_pedido(),
        relief="flat"
    )#Boton para buscar el envio con el ID especificado
    button_1.place(
        x=729.0,
        y=163.0,
        width=50.0,
        height=45.0
    )

    #texto
    #Informacion solicitada
    canvas.create_text(
        273.0,
        223.0,
        anchor="nw",
        text="Datos actuales del envío:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        263.0,
        anchor="nw",
        text="Guía aérea",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto guia aerea
    guia_text=canvas.create_text(
        621.0,
        263.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        303.0,
        anchor="nw",
        text="Cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto cliente
    cliente_text=canvas.create_text(
        621.0,
        303.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        343.0,
        anchor="nw",
        text="Tipo de medicamento:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto tipo producto
    tipo_text=canvas.create_text(
        621.0,
        343.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        274.0,
        384.0,
        anchor="nw",
        text="Destino:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto des
    dest_text = canvas.create_text(
        621.0,
        385.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        426.0,
        anchor="nw",
        text="Estado:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto estado del envio
    est_text =canvas.create_text(
        621.0,
        426.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        466.0,
        anchor="nw",
        text="Temperatura:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto temperatura
    temp_text = canvas.create_text(
        621.0,
        467.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        503.0,
        anchor="nw",
        text="Hora de entrega:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto Hora entrega
    hora_text = canvas.create_text(
        621.0,
        506.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #texto
    canvas.create_text(
        272.0,
        546.0,
        anchor="nw",
        text="Ubicación actual:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto para ver la ubicacion actual
    ubi_text = canvas.create_text(
        621.0,
        546.0,
        anchor="nw",
        text="+++",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame5,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Ya estas aca"),
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
        frame5,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui19.cliente_ver_estado(frame5),
        relief="flat"
    )#Boton funcionaliad
    button_3.place(
        x=14.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame5,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui20.cliente_ver_historial(frame5),
        relief="flat"
    )#Boton funcionaliadad
    button_4.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    
