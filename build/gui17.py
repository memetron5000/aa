


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame,BOTH,ttk,Toplevel
import gui18, gui19, gui20

#se crea la pestaña de Gerente con sus botones respectivos a sus funcionalidades y su propia ventana
def cliente():
    
    #verifica el diectorio de imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame17"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)



    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    #creacion de ventana y frames de c
    window5 = Toplevel()
    frame5 = Frame(window5)
    window5.title ("YOURWAY TRANSPORT Cliente")
    window5.iconbitmap(relative_to_assets("icon.ico"))
    frame5.pack(fill=BOTH,expand=True)
    window5.geometry("800x600")
    window5.configure(bg = "#FFFFFF")


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
        text="BIENVENIDO",
        fill="#000000",
        font=("MicrosoftSansSerif", 32 * -1)
    )

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame5,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui18.cliente_ver_pedido(frame5),
        relief="flat"
    )
    button_1.place(
        x=14.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame5,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui19.cliente_ver_estado(frame5),
        relief="flat"
    )
    button_2.place(
        x=14.0,
        y=149.0,
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
        command=lambda: gui20.cliente_ver_historial(frame5),
        relief="flat"
    )
    button_3.place(
        x=14.0,
        y=240.0,
        width=158.0,
        height=56.0
    )
    
    #mantencion de la ventana
    window5.resizable(False, False)
    window5.mainloop()
    
