
import gui1,  gui6,    gui10,     gui13,       gui17     ,gui22      ,metodos
    #(Logis)(Gerente)(Quimico)(Transportista)(Cliente)(destinatario)

from pathlib import Path


from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Frame,BOTH,ttk
import datetime
from enum import Enum

#clases del prototipo





#funcion que se llama de main
def login():
    
    #busqueda de directorio de las imagenes
    global user
    try:
        ruta_escritorio = Path.home() / "Desktop"
        ruta_completa = ruta_escritorio / "proyecto" / "build" / "assets"/"frame0"
        
    except Exception as e:
        print(f"Error al obtener la ruta del escritorio: {e}")
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(ruta_completa)


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    #creacion de ventana
    window = Tk()
    frame = Frame(window)
    window.title ("YOURWAY TRANSPORT")
    window.iconbitmap(relative_to_assets("icon.ico"))
    frame.pack(fill=BOTH,expand=True)
    window.geometry("800x600")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        frame,
        bg = "#FFFFFF",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    
    #carga de imagenes de logo
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        400.0,
        173.0,
        image=image_image_1
    )
    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        423.0,
        75.0,
        image=image_image_2
    )
    #texto
    canvas.create_text(
        52.0,
        356.0,
        anchor="nw",
        text="Tipo de usuario",
        fill="#727272",
        font=("MicrosoftSansSerif", 20 * -1)
    )
    
    #combobox de opciones de usuarios
    combo = ttk.Combobox(state= "readonly",values=[metodos.Rol.PERSONAL_LOGISTICA.value , metodos.Rol.GERENTE_COMERCIAL.value, metodos.Rol.QUIMICO.value, metodos.Rol.CONDUCTOR.value, metodos.Rol.CLIENTE.value, metodos.Rol.DESTINATARIO.value])
    combo.place(x=52.0, y=390.0)
    width=50
    # Crear el texto "disponibles" vacio y lo guarda en la memoria
    available_text = canvas.create_text(
        454.0,
        356.0,
        anchor="nw",
        text="",
        fill="#727272",
        font=("MicrosoftSansSerif", 20 * -1)
    )

    #verifica la seleccion de opciones en ese instante del combobox para ocultar o mostrar el texto de disponibles mas el rol
    def update_available_text(event):
        global user
        selected_role = combo.get()
        #si rol==destinatario oculta el cuadro de dispobibles y el cuadro de texto de identificador de cliente
        if selected_role in (metodos.Rol.DESTINATARIO.value,):
            canvas.itemconfig(available_text, state='hidden')
            canvas.itemconfig(entry_bg_1, state='hidden')
            entry_1.place_forget()
        #si rol==cliente muestra el cuadro de dispobibles y el cuadro de texto de identificador de cliente
        elif(selected_role in ( metodos.Rol.CLIENTE.value)):
            canvas.itemconfig(available_text, state='normal', text="Ingrese ID")
            entry_1.place(
                x=564.0,
                y=403.0,
                width=134.0,
                height=33.0
            )
            canvas.itemconfig(entry_bg_1, state='normal')
        else:
            #si no selecciona nada se queda en esa pestaña al hacer login
            canvas.itemconfig(entry_bg_1, state='hidden')
            entry_1.place_forget()
            user=selected_role+" disponible"
            canvas.itemconfig(available_text, state='normal',text=user)
            
    #crea combobox con valores de usuarios
    combo = ttk.Combobox(state="readonly", values=[rol.value for rol in metodos.Rol])
    combo.place(x=52.0, y=390.0)
    combo.bind("<<ComboboxSelected>>", update_available_text)

    #obtiene valor de usuario de combobox 
    def seleccion():
        print (combo.get())
        if (combo.get()==metodos.Rol.PERSONAL_LOGISTICA.value):
            gui1.logistica()
        elif(combo.get()==metodos.Rol.GERENTE_COMERCIAL.value):
            gui6.gerente()
        elif(combo.get()==metodos.Rol.QUIMICO.value):
            gui10.quimico()
        elif(combo.get()==metodos.Rol.CONDUCTOR.value):
            gui13.conductor()
        elif(combo.get()==metodos.Rol.CLIENTE.value):
            gui17.cliente()
        elif(combo.get()==metodos.Rol.DESTINATARIO.value):
            gui22.destinatario()
        else:
            pass            
    
    #entrada de texto de cliente
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        631.0,
        420.0,
        state="hidden",
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=564.0,
        y=403.0,
        width=134.0,
        height=33.0
    )
    entry_1.place_forget()
    
    
    #boton de login
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: seleccion(),
        
        relief="flat"
    )
    button_1.place(
        
        x=323.0,
        y=502.0,
        width=153.0,
        height=37.0
    )
    
    #creacion de ventana
    window.resizable(False, False)
    window.mainloop()