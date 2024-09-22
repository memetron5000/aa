
#clases hijas de logistica
import gui3,gui4,gui5, metodos
from pathlib import Path
import datetime

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox

#limpieza de frame de logistica
def titulo(frame1):
    # Limpia el frame
    for item in frame1.winfo_children():
        item.destroy()

#pantalla de modificar de logistica
def logistica_modificar(frame1):
    #hace llamado global a las imagenes que se usan en logistica modificar para incluirlas en el frame !!importante
    global button_image_1,button_image_2,button_image_3,button_image_4,button_5,button_image_1,button_image_2,button_image_3,button_image_4,button_image_5,button_image_6,image_image_1,entry_image_1,entry_image_2,entry_image_3,entry_image_4,entry_image_5,entry_image_6,entry_image_7,entry_image_8,entry_image_9,image_image_1
    
    #limpia el frame
    titulo(frame1)
    
    #verifica el directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame2"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #lectura de frame
    canvas = Canvas(
        frame1,
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
        213.0,
        112.0,
        anchor="nw",
        text="Ingrese el ID del envío a modificar:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        626.0,
        119.5,
        image=entry_image_1
        
    )
    entry_1 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=559.0,
        y=102.0,
        width=134.0,
        height=33.0
    )

    #boton de buscar
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: bus_pedido(),
        relief="flat"
    )
    button_1.place(
        x=714.0,
        y=97.0,
        width=50.0,
        height=45.0
    )
    
    #!buscar envio
    def bus_pedido():
        id_job = entry_1.get()
        if id_job not in metodos.sistema.envios:
            messagebox.showwarning(title=None, message=f"No se ha encontrado ningún envío con el {id_job}")
        if id_job in metodos.sistema.envios:
            envio = metodos.sistema.envios[id_job]
            print("Datos actuales del envío:")
            entry_2.insert(0, envio.guia_aerea)
            canvas.itemconfig(cli, text=envio.cliente.nombre)
            entry_4.insert(0, envio.tipo_producto)
            entry_5.insert(0, envio.destino)
            canvas.itemconfig(estado, text=envio.estado_actual.value)
            entry_7.insert(0, envio.temperatura)
            entry_8.insert(0, envio.hora_entrega)
            entry_9.insert(0, envio.ubicacion_actual)

    #texto
    canvas.create_text(
        305.0,
        175.0,
        anchor="nw",
        text="Datos actuales del envío:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    canvas.create_text(
        250.0,
        215.0,
        anchor="nw",
        text="Guía aérea",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        627.5,
        227.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=510.0,
        y=215.0,
        width=235.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        250.0,
        255.0,
        anchor="nw",
        text="Cliente:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #?texto cliente
    cli=canvas.create_text(
        629.0,
        263.5,
        anchor="nw",
        text="",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )
    

    #texto
    canvas.create_text(
        250.0,
        295.0,
        anchor="nw",
        text="Tipo de medicamento:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        628.0,
        304.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_4.place(
        x=512.0,
        y=292.0,
        width=232.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        252.0,
        335.0,
        anchor="nw",
        text="Destino:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        629.0,
        345.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_5.place(
        x=513.0,
        y=333.0,
        width=232.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        250.0,
        378.0,
        anchor="nw",
        text="Estado:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    estado=canvas.create_text(
        628.0,
        387.5,
        anchor="center",
        text="",
        fill="#000000",
        font=("MicrosoftSansSerif", 13 * -1)
    )

    

    #texto
    canvas.create_text(
        250.0,
        418.0,
        anchor="nw",
        text="Temperatura:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        628.0,
        427.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_7.place(
        x=512.0,
        y=415.0,
        width=232.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        250.0,
        458.0,
        anchor="nw",
        text="Hora de entrega:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        626.0,
        467.5,
        image=entry_image_8
    )
    entry_8 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_8.place(
        x=510.0,
        y=455.0,
        width=232.0,
        height=23.0
    )

    #texto
    canvas.create_text(
        250.0,
        498.0,
        anchor="nw",
        text="Ubicación actual:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #cuadro de texto rellenable
    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        626.0,
        507.5,
        image=entry_image_9
    )
    entry_9 = Entry(
        frame1,
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_9.place(
        x=510.0,
        y=495.0,
        width=232.0,
        height=23.0
    )

    #! subir al sistema los nuevos cambios en los detalles del pedido
    def sub_cambios():
        id_job=entry_1.get()
        if id_job not in metodos.sistema.envios:
            messagebox.showwarning(title=None, message=f'No se ha encontrado ningún envío con el {id_job}')
        if id_job in metodos.sistema.envios:
            envio = metodos.sistema.envios[id_job]
            
            tipo_producto = entry_4.get()
            if tipo_producto:
                envio.tipo_producto = tipo_producto
            
            destino = entry_5.get()
            if destino:
                envio.destino = destino
            
            temperatura = entry_7.get()
            if temperatura:
                envio.temperatura = temperatura
            
            hora_entrega = entry_8.get()
            if hora_entrega:
                envio.hora_entrega = datetime.datetime.strptime(hora_entrega, "%Y-%m-%d %H:%M")
                
            messagebox.showinfo(title=None, message="Datos de envio actualizados")
        else:
            messagebox.showwarning(title=None, message="Envio no encontrado")

    #boton de subir cambios
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: sub_cambios(),
        relief="flat"
    )
    button_2.place(
        x=380.0,
        y=543.0,
        width=153.0,
        height=37.0
    )
    

    #boton que cambia a pestaña de logistica editar estado
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui5.logistica_edit_estado(frame1),
        relief="flat"
    )
    button_3.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton que avisa que ya estas en esa pestaña
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame1,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ya estas en esta pestaña"),
        relief="flat"
    )
    button_4.place(
        x=14.0,
        y=149.0,
        width=159.0,
        height=56.0
    )

    #boton que cambia la pestaña a logistica ver
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        frame1,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui3.logistica_ver(frame1),
        relief="flat"
    )
    button_5.place(
        x=13.0,
        y=240.0,
        width=159.0,
        height=56.0
    )

    #boton que cambia a logistica asignar
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_6 = Button(
        frame1,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui4.logistica_asignar_empleado(frame1),
        relief="flat"
    )
    button_6.place(
        x=14.0,
        y=331.0,
        width=158.0,
        height=56.0
    )
