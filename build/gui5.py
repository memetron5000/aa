


import gui2, gui3,gui4, metodos
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, ttk

def titulo(frame1):
    # Limpia el frame
    for item in frame1.winfo_children():
        item.destroy()

def logistica_edit_estado(frame1):
    global button_image_1, button_image_2, button_image_3, button_image_4,button_image_5, entry_image_1, entry_image_2, image_image_1
    
    #limpia el frame
    titulo(frame1)
    
    #verifica el directorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame5"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #lectura del frame
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
        text="Editar estado del envío",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )
    
    canvas.create_text(
        300.0,
        125.0,
        anchor="nw",
        text="ID del envio",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    #cuadro de texto
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        677.0,
        137.5,
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
        x=610.0,
        y=120.0,
        width=134.0,
        height=33.0
    )
    
    #texto
    canvas.create_text(
        300.0,
        177.0,
        anchor="nw",
        text="Ubicacion:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    #cuadro de texto
    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        677.0,
        187.5,
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
        x=610.0,
        y=170.0,
        width=134.0,
        height=33.0
    )

    #texto
    canvas.create_text(
        285.0,
        257.0,
        anchor="nw",
        text="Elja el estado del envio:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    
    #? combobox que crea la lista con los estados de envi
    combo = ttk.Combobox(frame1, state= "readonly",values=["EN_REPARTO_AEREO","VIAJANDO_A_TU_DESTINO","EN_CENTRO_LOGISTICO","EN_CAMINO_HACIA_TI","ENTREGADO","EN_RETRASO"])
    combo.place(x=600.0, y=257.0)
    width=50
    
    #!funcion que actualiza el estado del envio
    def actualizar():
        id_job=entry_1.get()
        if id_job in metodos.sistema.envios:
            pass
        else:
            messagebox.showinfo("Error", f"No se ha encontrado ningún envío con el ID {id_job}")
            return
        ubicacion=entry_2.get()
        if (combo.get()=="" or entry_2.get()==""):
            messagebox.showerror(title=None, message="Rellene todos los espacios", )
        elif metodos.sistema.actualizar_estado_envio(id_job, metodos.EstadoEnvio[combo.get()], ubicacion):
            messagebox.showinfo(title=None, message="Estado actualizado con éxito")
        
    
    #boton cambiar estado
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: actualizar(),
        relief="flat"
    )
    button_1.place(
        x=410.0,
        y=371.0,
        width=153.0,
        height=37.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("ya estas aca"),
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
        frame1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui2.logistica_modificar(frame1),
        relief="flat"
    )
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
        frame1,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui3.logistica_ver(frame1),
        relief="flat"
    )
    button_4.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        frame1,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui4.logistica_asignar_empleado(frame1),
        relief="flat"
    )
    button_5.place(
        x=14.0,
        y=331.0,
        width=158.0,
        height=56.0
    )
