import tkinter as tk
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk

def Presentacion():
    # Crear una ventana de presentación
    ventana_presentacion = tk.Toplevel()  # Usar Toplevel para abrir una nueva ventana
    ventana_presentacion.title("Presentación del Proyecto")

    # Crear el texto de presentación
    texto_presentacion = (
        "\n{:^70}\n"
        "{:^70}\n"
        "{:^70}\n\n"
        "{:^70}\n\n"
        "{:^70}\n"
        "{:^78}\n"
        "{:^80}\n"
        "{:^76}\n"
        "{:^76}\n\n"
        "{:^70}\n\n"
        "{:^70}\n\n"
    ).format(
        "UNIVERSIDAD TECNOLÓGICA DE PANAMÁ",
        "FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES",
        "DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS",
        "PROYECTO #3",
        "Integrantes: Miguel Arosemana 8-1016-2330",
        "Edward Camaño 8-1010-515",
        "Diego Corrales 8-1001-1890",
        "Edwin Hou 8-1021-1916",
        "Josue Pino 8-1012-688",
        "Profesor: Ing. Samuel Jimenez",
        "SEMESTRE II, 2024"
    )

    label = tk.Label(ventana_presentacion, text=texto_presentacion, justify="center", padx=10, pady=10)
    label.pack()

    exit_button = tk.Button(ventana_presentacion, text="Salir", command=lambda: ventana_presentacion.destroy())
    exit_button.pack(pady=20)
    
def ProvinciasComarcas():
    ventana_provincias = tk.Toplevel()
    ventana_provincias.title("Provincias")
    ventana_provincias.geometry("500x400")
    
    # Crear la barra de menú
    BarraProvincias = tk.Menu(ventana_provincias)
    ventana_provincias.config(menu=BarraProvincias)

    # Crear el menú de provincias
    menu_provincias = tk.Menu(BarraProvincias, tearoff=0)
    menu_provincias.add_command(label="Bocas del Toro", command=Bocasdeltoro)
    menu_provincias.add_command(label="Coclé", command=Cocle)
    menu_provincias.add_command(label="Colón", command=Colon)
    menu_provincias.add_command(label="Chiriquí", command=Chiriqui)
    menu_provincias.add_command(label="Darién", command=Darien)
    menu_provincias.add_command(label="Herrera", command=Herrera)
    menu_provincias.add_command(label="Los Santos", command=LosSantos)
    menu_provincias.add_command(label="Panamá", command=Panama)
    menu_provincias.add_command(label="Veraguas", command=Veraguas)
    menu_provincias.add_command(label="Panamá Oeste", command=PanamaOeste)

    # Añadir el menú de provincias a la barra de menú
    BarraProvincias.add_cascade(label="Provincias ", menu=menu_provincias)

    #menu de comarcas
    menu_comarcas = tk.Menu(BarraProvincias, tearoff=0)
    menu_comarcas.add_command(label="Embera-Wounaan", command= EmberaWounaan)
    menu_comarcas.add_command(label="Guna Yala", command= GunaYala)
    menu_comarcas.add_command(label="Ngabe-Bugle", command= NgabeBugle)
    
    BarraProvincias.add_cascade(label="Comarcas", menu=menu_comarcas)
    
    # Botón para cerrar la ventana
    exit_button = tk.Button(ventana_provincias, text="Cerrar", command=ventana_provincias.destroy)
    exit_button.pack(pady=20)

def Bocasdeltoro():

    ventana_bocas = tk.Toplevel()
    ventana_bocas.title("Bocas del Toro")
    ventana_bocas.geometry("600x400")

    frame = tk.Frame(ventana_bocas)
    frame.pack(pady=20)

    descripcionBocas ="""Bocas del Toro es una provincia de Panamá y su capital es la ciudad homónima de Bocas del Toro.
    Tiene una extensión de 3,037 km², una población de 170 320 habitantes (2018) y sus límites: al norte con el mar Caribe, 
    al sur con la provincia de Chiriquí, al este y sureste con la comarca Ngäbe-Buglé, al oeste con la comarca Naso Tjër Di, 
    al noroeste con la provincia de Limón de Costa Rica y al suroeste con la provincia de Puntarenas de Costa Rica."""
    description_label = tk.Label(frame, text=descripcionBocas, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/bocasdeltoro.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresBocas = tk.Menu(ventana_bocas)
    ventana_bocas.config(menu=lugaresBocas)

    menu_bocas = tk.Menu(lugaresBocas, tearoff=0)
    menu_bocas.add_command(label="Playa Estrella", command= PlayaEstrella )
    menu_bocas.add_command(label="lugar2", )
    menu_bocas.add_command(label="lugar3", )
    menu_bocas.add_command(label="lugar4", )

    lugaresBocas.add_cascade(label="Provincia Chiriqui", menu=menu_bocas)
    
def PlayaEstrella():
    ventana_PlayaEstrella = tk.Toplevel()
    ventana_PlayaEstrella.title("Bahía de los Delfines")
    ventana_PlayaEstrella.geometry("600x500")
    ventana_PlayaEstrella.configure(bg='#009999')  # Fondo color turquesa

    # Título de la actividad
    frame = tk.Label(ventana_PlayaEstrella, text="BAHÍA DE LOS DELFINES", font=("Arial", 18, "bold"), bg='#009999')
    frame.pack(pady=10)

    try:
        image_path = "imagenes/PlayaEstrellaBocas.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción de la bahía
    descripcion_texto = (
        "La Bahía de los Delfines es una laguna en Bocas del Toro que alberga delfines nariz de botella "
        "durante la mayor parte del año. La bahía tiene aguas tranquilas y está rodeada de manglares, "
        "los cuales albergan una gran abundancia de pequeños peces y crustáceos – "
        "entre ellos se encuentra el hábitat perfecto para delfines, especialmente madres y crías."
    )
    descripcion = tk.Label(ventana_PlayaEstrella, text=descripcion_texto, wraplength=250, justify="left", bg='#009999', font=("Arial", 10))
    descripcion.place(x=50, y=250)

    # Incluye detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Fotógrafo Profesional\n"
        "- 30 minutos guiados de interacción con delfines\n"
        "- Kit de fotos con delfines\n"
        "- Almuerzo continental\n"
        "- Transporte\n"
        "Precio: 250.00"
    )
    detalles = tk.Label(ventana_PlayaEstrella, text=detalles_texto, wraplength=200, justify="left", bg='#009999', font=("Arial", 10))
    detalles.place(x=350, y=250)

    # Botones de "RESERVAR" y "VOLVER"
    boton_reservar = tk.Button(ventana_PlayaEstrella, text="RESERVAR", width=15, font=("Arial", 12), bg="white")
    boton_reservar.place(x=200, y=420)

    boton_volver = tk.Button(ventana_PlayaEstrella, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_PlayaEstrella.destroy)
    boton_volver.place(x=350, y=420)


def Cocle():
    messagebox.showinfo(" ")

def Colon():
    messagebox.showinfo(" ")

def Chiriqui():
    messagebox.showinfo(" ")

def Darien():
    messagebox.showinfo(" ")

def Herrera():
    messagebox.showinfo(" ")

def LosSantos():
    messagebox.showinfo(" ")

def Panama():
    messagebox.showinfo(" ")

def Veraguas():
    messagebox.showinfo(" ")

def PanamaOeste():
    messagebox.showinfo(" ")

def EmberaWounaan():
    messagebox.showinfo(" ")
    
def GunaYala():
    messagebox.showinfo(" ")

def NgabeBugle():
    messagebox.showinfo(" ")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Actividades Turísticas en Panamá")
ventana.geometry("400x300")

# Crear la barra de menú
menu_bar = tk.Menu(ventana)

menu_prin = tk.Menu(menu_bar, tearoff=0)
menu_prin.add_command(label="Presentación", command=Presentacion)
menu_prin.add_command(label="Ver Provincias y Comarcas", command=ProvinciasComarcas)
menu_prin.add_separator()  # Añadir un separador
menu_prin.add_command(label="Salir", command=ventana.quit)

# Añadir el menú "Archivo" a la barra de menú
menu_bar.add_cascade(label="Menu", menu=menu_prin)

# Configurar la barra de menú en la ventana principal
ventana.config(menu=menu_bar)

# Ejecutar el bucle principal
ventana.mainloop()