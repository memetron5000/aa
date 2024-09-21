


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame, BOTH, ttk,Toplevel
import gui7, gui8, gui9

#se crea la pestaña de Gerente con sus botones respectivos a sus funcionalidades y su propia ventana
def gerente():
    
    #lectura de directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame6"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
    
    #crea la ventana
    window2 = Toplevel()
    frame2 = Frame(window2)
    window2.title ("YOURWAY TRANSPORT Gerente")
    window2.iconbitmap(relative_to_assets("icon.ico"))
    frame2.pack(fill=BOTH,expand=True)
    window2.geometry("800x600")
    window2.configure(bg = "#FFFFFF")

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
#   boton que lleva a la funcionalidad de gerente registrar cliente
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame2,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui7.gerente_registrar(frame2),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )
#   boton que lleva a la funcionalidad de gerente crear envio
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame2,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui8.gerente_crear_envio(frame2),
        relief="flat"
    )
    button_2.place(
        x=13.0,
        y=149.0,
        width=159.0,
        height=56.0
    )
#   boton que lleva a la funcionalidad de gerente ver envio
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame2,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui9.gerente_ver_envio(frame2),
        relief="flat"
    )
    button_3.place(
        x=13.0,
        y=240.0,
        width=159.0,
        height=56.0
    )
    
    #   mantencion de la ventana
    window2.resizable(False, False)
    window2.mainloop()
