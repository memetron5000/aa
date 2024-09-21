

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame,BOTH,ttk,Toplevel
import gui24, gui25

#se crea la pestaña de Gerente con sus botones respectivos a sus funcionalidades y su propia ventana
def destinatario():
    
    #lectura de directorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame22"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #crea la ventana
    window6 = Toplevel()
    frame6 = Frame(window6)
    window6.title ("YOURWAY TRANSPORT Destinatario")
    window6.iconbitmap(relative_to_assets("icon.ico"))
    frame6.pack(fill=BOTH,expand=True)
    window6.geometry("800x600")
    window6.configure(bg = "#FFFFFF")


    canvas = Canvas(
        frame6,
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
        file=relative_to_assets("button_2.png"))
    button_1 = Button(
        frame6,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui24.destinatario_ver_estado(frame6),
        relief="flat"
    )#Boton funcionalidad que lleva a destinatario ver estado del envio
    button_1.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_2 = Button(
        frame6,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui25.destinatario_ver_historial(frame6),
        relief="flat"
    )#Boton funcionalidad que lleva a destinatario ver historial del envio
    button_2.place(
        x=14.0,
        y=149.0,
        width=158.0,
        height=56.0
    )

    #mantencion de la ventana
    window6.resizable(False, False)
    window6.mainloop()