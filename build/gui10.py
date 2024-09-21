



from pathlib import Path    


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame, BOTH, ttk,Toplevel
import gui11, gui12

#se crea la pestaña de Gerente con sus botones respectivos a sus funcionalidades y su propia ventana
def quimico():
    
    #verificacion directorio de archivos
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame10"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

#Creacion de la ventana
    window3 = Toplevel()
    frame3 = Frame(window3)
    window3.title ("YOURWAY TRANSPORT Quimico")
    window3.iconbitmap(relative_to_assets("icon.ico"))
    frame3.pack(fill=BOTH,expand=True)
    window3.geometry("800x600")
    window3.configure(bg = "#FFFFFF")


    canvas = Canvas(
        frame3,
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

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame3,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui12.quimico_edit_estado(frame3),
        relief="flat"
    )#Boton que lleva a la funcionalidad de quimico editar estado del envio
    button_1.place(
        x=13.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame3,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui11.quimico_ver_envio(frame3),
        relief="flat"
    )#Boton que lleva a la funcionalidad de quimico ver envio
    button_2.place(
        x=13.0,
        y=149.0,
        width=159.0,
        height=56.0
    )
    
    #mantencion de la ventana
    window3.resizable(False, False)
    window3.mainloop()
