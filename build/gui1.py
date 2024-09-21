

#clases hijas de logistica
import gui2, gui3,gui4,gui5
from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame,BOTH,ttk,Toplevel

#ventana de login de logistica
def logistica():
    
    #verifica el directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame1"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    #creacion de ventana y frame de logistica
    window1 = Toplevel()
    frame1 = Frame(window1)
    window1.title ("YOURWAY TRANSPORT Logistica")
    window1.iconbitmap(relative_to_assets("icon.ico"))
    frame1.pack(fill=BOTH,expand=True)
    window1.geometry("800x600")
    window1.configure(bg = "#FFFFFF")
    
    canvas = Canvas(
        frame1,
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
    
    #boton que cambia de pestaña a ver estado
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame1,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui5.logistica_edit_estado(frame1),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )
    
    #boton que cambia de pestaña a modificar
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame1,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui2.logistica_modificar(frame1),
        relief="flat"
    )
    button_2.place(
        x=14.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #boton que cambia de pestaña a ver
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame1,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui3.logistica_ver(frame1),
        relief="flat"
    )
    button_3.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    
    #boton que cambia de pestaña a asignar empleado
    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        frame1,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui4.logistica_asignar_empleado(frame1),
        relief="flat"
    )
    button_4.place(
        x=14.0,
        y=331.0,
        width=158.0,
        height=56.0
    )
    
    #mantencion de ventana de logistica
    window1.resizable(False, False)
    window1.mainloop()