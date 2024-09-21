


from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import gui11

# limpia el frame para poder actualizar la ventana
def titulo(frame3):
    # Limpia el frame
    for item in frame3.winfo_children():
        item.destroy()
    

def quimico_edit_estado(frame3):
    global button_image_1, button_image_2, button_image_3, image_image_1
    
    #limpia el frame
    titulo(frame3)
    
    #verifica el direcorio de las imagenes
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame12"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)   

    #lectura de frame
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

    #texto
    canvas.create_text(
        283.0,
        117.0,
        anchor="nw",
        text="Elija el estado del envío:",
        fill="#000000",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #boton
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        frame3,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("Actualizar"),
        relief="flat"
    )
    button_1.place(
        x=422.0,
        y=178.0,
        width=153.0,
        height=37.0
    )

    #boton
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        frame3,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:  print("Ya estas aca"),
        relief="flat"
    )
    button_2.place(
        x=13.0,
        y=58.0,
        width=158.0,
        height=56.0
    )

    #boton
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        frame3,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: gui11.quimico_ver_envio(frame3) ,
        relief="flat"
    )
    button_3.place(
        x=13.0,
        y=149.0,
        width=159.0,
        height=56.0
    )
    
