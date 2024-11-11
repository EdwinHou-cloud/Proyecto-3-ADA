#InicioAlgoritmo
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

#Inicio Funciones provincias
def Bocasdeltoro():
    ventana_bocas = tk.Toplevel()
    ventana_bocas.title("Bocas del Toro")
    ventana_bocas.geometry("600x400")

    # Título de la provincia
    title_label = tk.Label(ventana_bocas, text="Provincia: Bocas del Toro", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_bocas)
    frame.pack(pady=10)

    # Descripción de la provincia
    descripcionBocas = (
        "Bocas del Toro es una provincia de Panamá y su capital es la ciudad homónima de Bocas del Toro. "
        "Tiene una extensión de 3,037 km², una población de 170 320 habitantes (2018) y sus límites: al norte con el mar Caribe, "
        "al sur con la provincia de Chiriquí, al este y sureste con la comarca Ngäbe-Buglé, al oeste con la comarca Naso Tjër Di, "
        "al noroeste con la provincia de Limón de Costa Rica y al suroeste con la provincia de Puntarenas de Costa Rica."
    )
    description_label = tk.Label(frame, text=descripcionBocas, wraplength=500, justify="left")
    description_label.pack()

    # Imagen de la provincia
    try:
        image_path = "imagenes/Bocasdeltoro/bocasdeltoro.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    # Menú desplegable para lugares turísticos con título dentro
    lugaresBocas = tk.Menu(ventana_bocas)
    ventana_bocas.config(menu=lugaresBocas)

    menu_bocas = tk.Menu(lugaresBocas, tearoff=0)
    menu_bocas.add_command(label="Playa Estrella", command=PlayaEstrellaBocas)
    menu_bocas.add_command(label="Green Acres", command=GreenAcresBocas)
    menu_bocas.add_command(label="Bahía de los Delfines", command=BahiaDelfinesBocas)
    menu_bocas.add_command(label="Aldea de Botellas Plásticas", command=AldeaBotellasBocas)

    lugaresBocas.add_cascade(label="Lugares Turistico de Bocas del Toro que deberias visitar", menu=menu_bocas)

    # Botón de regresar
    boton_regresar = tk.Button(ventana_bocas, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_bocas.destroy)
    boton_regresar.place(x=450, y=335)

#Inicio Lugares Turisticos de Bocas del Toro
def PlayaEstrellaBocas():
    ventana_PlayaEstrella = tk.Toplevel()
    ventana_PlayaEstrella.title("Playa Estrella")
    ventana_PlayaEstrella.geometry("700x600")
    ventana_PlayaEstrella.configure(bg='#009999')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_PlayaEstrella, bg='#009999')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Playa Estrella", font=("Arial", 20, "bold"), bg='#009999')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/BocasdelToro/PlayaEstrellaBocas.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#009999')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción de la bahía
    descripcion_texto = (
        "Playa Estrella es una playa caribeña situada en la isla Colón, famosa por sus aguas cristalinas y "
        "la abundancia de estrellas de mar en sus costas. Los visitantes pueden nadar en aguas poco profundas, "
        "hacer snorkel y disfrutar del ambiente tropical rodeado de palmeras. Además, el lugar cuenta con áreas para "
        "descansar y disfrutar de comida local frente al mar, permitiendo a los turistas sumergirse en un ambiente "
        "natural y relajante con vistas panorámicas."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Fotógrafo Profesional\n"
        "- 30 minutos guiados de interacción con delfines\n"
        "- Kit de fotos con delfines\n"
        "- Almuerzo continental\n"
        "- Transporte\n"
        "\nPrecio: 250.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_PlayaEstrella, bg='#009999')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=Reserva)
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_PlayaEstrella.destroy)
    boton_volver.pack(side="left", padx=10)

def GreenAcresBocas():
    ventana_GreenAcres = tk.Toplevel()
    ventana_GreenAcres.title("Green Acres")
    ventana_GreenAcres.geometry("600x500")
    ventana_GreenAcres.configure(bg='#008000')  # Fondo color verde

    frame = tk.Label(ventana_GreenAcres, text="GREEN ACRES", font=("Arial", 18, "bold"), bg='#008000')
    frame.pack(pady=10)

    try:
        image_path = "imagenes/Bocasdeltoro/GreenAcresBocas.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Green Acres es una reserva de cacao orgánico en la isla Bastimentos. "
        "Los visitantes pueden conocer el proceso del cacao, caminar por senderos naturales "
        "y observar fauna como ranas venenosas y aves tropicales. Se promueve el cultivo sustentable "
        "y se ofrecen degustaciones de cacao artesanal."
    )
    descripcion = tk.Label(ventana_GreenAcres, text=descripcion_texto, wraplength=250, justify="left", bg='#008000', font=("Arial", 10))
    descripcion.place(x=50, y=250)

    detalles_texto = (
        "Incluye:\n"
        "- Recorrido guiado por el cultivo de cacao\n"
        "- Degustación de cacao orgánico\n"
        "- Paseo ecológico por la reserva\n"
        "Precio: 120.00"
    )
    detalles = tk.Label(ventana_GreenAcres, text=detalles_texto, wraplength=200, justify="left", bg='#008000', font=("Arial", 10))
    detalles.place(x=350, y=250)

    boton_reservar = tk.Button(ventana_GreenAcres, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=Reserva)
    boton_reservar.place(x=300, y=435)

    boton_volver = tk.Button(ventana_GreenAcres, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_GreenAcres.destroy)
    boton_volver.place(x=450, y=435)
   
def BahiaDelfinesBocas():
    ventana_BahiaDelfines = tk.Toplevel()
    ventana_BahiaDelfines.title("Bahía de los Delfines")
    ventana_BahiaDelfines.geometry("600x500")
    ventana_BahiaDelfines.configure(bg='#3399FF')

    frame = tk.Label(ventana_BahiaDelfines, text="BAHÍA DE LOS DELFINES", font=("Arial", 18, "bold"), bg='#3399FF')
    frame.pack(pady=10)

    try:
        image_path = "imagenes/Bocasdeltoro/BahiaDelfinesBocas.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Bahía de los Delfines es un área protegida conocida por ser hábitat de delfines en su entorno natural. "
        "Los visitantes pueden realizar paseos en lancha para observar delfines, disfrutar de paisajes y hacer snorkel."
    )
    descripcion = tk.Label(ventana_BahiaDelfines, text=descripcion_texto, wraplength=250, justify="left", bg='#3399FF', font=("Arial", 10))
    descripcion.place(x=50, y=250)

    detalles_texto = (
        "Incluye:\n"
        "- Fotógrafo Profesional\n"
        "- 30 minutos guiados de interacción con delfines\n"
        "- Kit de fotos con delfines\n"
        "- Almuerzo continental\n"
        "- Transporte\n"
        "Precio: 250.00"
    )
    detalles = tk.Label(ventana_BahiaDelfines, text=detalles_texto, wraplength=200, justify="left", bg='#3399FF', font=("Arial", 10))
    detalles.place(x=350, y=250)

    boton_reservar = tk.Button(ventana_BahiaDelfines, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=Reserva)
    boton_reservar.place(x=300, y=435)

    boton_volver = tk.Button(ventana_BahiaDelfines, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_BahiaDelfines.destroy)
    boton_volver.place(x=450, y=435)

def AldeaBotellasBocas():
    ventana_AldeaBotellas = tk.Toplevel()
    ventana_AldeaBotellas.title("Aldea de Botellas Plásticas")
    ventana_AldeaBotellas.geometry("600x500")
    ventana_AldeaBotellas.configure(bg='#6699FF')

    frame = tk.Label(ventana_AldeaBotellas, text="ALDEA DE BOTELLAS PLÁSTICAS", font=("Arial", 18, "bold"), bg='#6699FF')
    frame.pack(pady=10)

    try:
        image_path = "imagenes/Bocasdeltoro/AldeaBotellasBocas.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "La Aldea de Botellas Plásticas es una ecoaldea construida con materiales reciclados. "
        "Los visitantes pueden participar en talleres de reciclaje y conciencia ambiental."
    )
    descripcion = tk.Label(ventana_AldeaBotellas, text=descripcion_texto, wraplength=250, justify="left", bg='#6699FF', font=("Arial", 10))
    descripcion.place(x=50, y=250)

    detalles_texto = (
        "Incluye:\n"
        "- Tour guiado\n"
        "- Taller de reciclaje\n"
        "- Souvenir ecológico\n"
        "Precio: 50.00"
    )
    detalles = tk.Label(ventana_AldeaBotellas, text=detalles_texto, wraplength=200, justify="left", bg='#6699FF', font=("Arial", 10))
    detalles.place(x=350, y=250)

    boton_reservar = tk.Button(ventana_AldeaBotellas, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=Reserva)
    boton_reservar.place(x=300, y=435)

    boton_volver = tk.Button(ventana_AldeaBotellas, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_AldeaBotellas.destroy)
    boton_volver.place(x=450, y=435)  
#Fin Lugares turisticos de Bocas del Toro

def Cocle():
    ventana_cocle = tk.Toplevel()
    ventana_cocle.title("Cocle")
    ventana_cocle.geometry("600x400")
    # Título de la provincia
    title_label = tk.Label(ventana_cocle, text="Provincia: Cocle", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_cocle)
    frame.pack(pady=10)

    descripcionCocle ="""Coclé es una provincia del centro de Panamá. Su superficie es de 4,927km² y 
    cuenta con 268,264 habitantes (2023).Su capital es Penonomé. Limita al norte con la provincia de Colón, 
    al este con la provincia de Panamá Oeste, al sur con la de Herrera y el golfo de Parita y al oeste con la de Veraguas. 
    El centro y norte de la provincia esta accidentados por la cordillera central; al sur pertenece las llanuras centrales, 
    tierras bajas muy fértiles que se extienden hasta el litoral. También es una provincia de gran riqueza natural y material. 
    Es además el epicentro de la cultura precolombina más avanzada del istmo."""
    description_label = tk.Label(frame, text=descripcionCocle, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Cocle/Cocle.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresCocle = tk.Menu(ventana_cocle)
    ventana_cocle.config(menu=lugaresCocle)

    menu_cocle = tk.Menu(lugaresCocle, tearoff=0)
    menu_cocle.add_command(label="lugar1",)
    menu_cocle.add_command(label="lugar2", )
    menu_cocle.add_command(label="lugar3", )
    menu_cocle.add_command(label="lugar4", )

    lugaresCocle.add_cascade(label="Provincia Cocle", menu=menu_cocle)
    
    boton_regresar = tk.Button(ventana_cocle, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_cocle.destroy)
    boton_regresar.place(x=450, y=335)

def Colon():
    ventana_colon= tk.Toplevel()
    ventana_colon.title("Colon")
    ventana_colon.geometry("600x400")

    title_label = tk.Label(ventana_colon, text="Provincia: Colon", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_colon)
    frame.pack(pady=10)

    descripcionColon ="""Colón es la capital de la provincia panameña de Colón, ubicada en la costa caribeña de Panamá. 
    La población estimada para 2016 es de unas 84,229 personas en su conurbación. 
    Está comunicada con la capital por medio de la Carretera Transístmica (autopista Panamá-Colón), 
    que la une en 78,9 km con la costa del océano Pacífico. Es la segunda ciudad más poblada del Caribe de Centroamérica. 
    Su casco urbano tiene unos 79 000 habitantes. Posee uno de los puertos más grandes de América Latina"""
    description_label = tk.Label(frame, text=descripcionColon, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Colon/Colon.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresColon = tk.Menu(ventana_colon)
    ventana_colon.config(menu=lugaresColon)

    menu_colon = tk.Menu(lugaresColon, tearoff=0)
    menu_colon.add_command(label="lugar1",)
    menu_colon.add_command(label="lugar2", )
    menu_colon.add_command(label="lugar3", )
    menu_colon.add_command(label="lugar4", )
    
    lugaresColon.add_cascade(label="Provincia Colon", menu=menu_colon)
    
    boton_regresar = tk.Button(ventana_colon, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_colon.destroy)
    boton_regresar.place(x=450, y=335)

def Chiriqui():
    ventana_chiriqui= tk.Toplevel()
    ventana_chiriqui.title("Chiriqui")
    ventana_chiriqui.geometry("600x400")

    title_label = tk.Label(ventana_chiriqui, text="Provincia: Chiriqui", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_chiriqui)
    frame.pack(pady=10)

    descripcionchiriqui ="""Chiriquí es una provincia de Panamá ubicada en la región occidental del país, 
    teniendo como límites al norte la provincia de Bocas del Toro y la comarca Ngäbe-Buglé, 
    al oeste la República de Costa Rica (Provincia de Puntarenas), al este la provincia de Veraguas 
    y al sur el océano Pacífico."""
    description_label = tk.Label(frame, text=descripcionchiriqui, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Chiriqui/Chiriqui.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresChiriqui = tk.Menu(ventana_chiriqui)
    ventana_chiriqui.config(menu=lugaresChiriqui)

    menu_chiriqui = tk.Menu(lugaresChiriqui, tearoff=0)
    menu_chiriqui.add_command(label="lugar1",)
    menu_chiriqui.add_command(label="lugar2", )
    menu_chiriqui.add_command(label="lugar3", )
    menu_chiriqui.add_command(label="lugar4", )
    
    lugaresChiriqui.add_cascade(label="Provincia Chiriqui", menu=menu_chiriqui)
    
    boton_regresar = tk.Button(ventana_chiriqui, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_chiriqui.destroy)
    boton_regresar.place(x=450, y=335)

def Darien():
    ventana_darien= tk.Toplevel()
    ventana_darien.title("Darien")
    ventana_darien.geometry("600x400")

    title_label = tk.Label(ventana_darien, text="Provincia: Darien", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_darien)
    frame.pack(pady=10)

    descripciondarien ="""Darién es una de las diez provincias de Panamá. Su capital es la ciudad de La Palma. 
    Tiene una extensión de 11 896,5 km², siendo por lo tanto la más extensa del país. Está ubicada en el extremo 
    oriental del país y limita al norte con la provincia de Panamá y la comarca Guna Yala. Al sur limita con el 
    océano Pacífico y la República de Colombia. Al este limita con el departamento de Chocó en la República de 
    Colombia y al oeste limita con el océano Pacífico y la provincia de Panamá."""
    description_label = tk.Label(frame, text=descripciondarien, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Darien/Darien.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresDarien = tk.Menu(ventana_darien)
    ventana_darien.config(menu=lugaresDarien)

    menu_darien = tk.Menu(lugaresDarien, tearoff=0)
    menu_darien.add_command(label="lugar1",)
    menu_darien.add_command(label="lugar2", )
    menu_darien.add_command(label="lugar3", )
    menu_darien.add_command(label="lugar4", )
    
    lugaresDarien.add_cascade(label="Provincia Darien", menu=menu_darien)
    
    boton_regresar = tk.Button(ventana_darien, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_darien.destroy)
    boton_regresar.place(x=450, y=335)

def Herrera():
    ventana_herrera= tk.Toplevel()
    ventana_herrera.title("Herrera")
    ventana_herrera.geometry("600x400")

    title_label = tk.Label(ventana_herrera, text="Provincia: Herrera", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_herrera)
    frame.pack(pady=10)

    descripcionherrera ="""Herrera es una provincia panameña situada en el norte de la península de Azuero y 
    su cabecera es la ciudad de Chitré. Limita al norte con las provincias de Veraguas y Coclé, al sur con 
    la provincia de Los Santos, al este con el golfo de Parita y la provincia de Los Santos y al oeste con 
    la provincia de Veraguas concretamente con el distrito de Mariato. Tiene una extensión de 2340.7 km² y 
    en 2008 contaba con una población de 111 647 habitantes, población que se estimó en 107 911 habitantes en 2010."""
    description_label = tk.Label(frame, text=descripcionherrera, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Herrera/Herrera.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresHerrera = tk.Menu(ventana_herrera)
    ventana_herrera.config(menu=lugaresHerrera)

    menu_herrera = tk.Menu(lugaresHerrera, tearoff=0)
    menu_herrera.add_command(label="lugar1",)
    menu_herrera.add_command(label="lugar2", )
    menu_herrera.add_command(label="lugar3", )
    menu_herrera.add_command(label="lugar4", )
    
    lugaresHerrera.add_cascade(label="Provincia Herrera", menu=menu_herrera)
    
    boton_regresar = tk.Button(ventana_herrera, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_herrera.destroy)
    boton_regresar.place(x=450, y=335)

def LosSantos():
    ventana_lossantos= tk.Toplevel()
    ventana_lossantos.title("Los Santos")
    ventana_lossantos.geometry("600x400")

    title_label = tk.Label(ventana_lossantos, text="Provincia: Los Santos", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_lossantos)
    frame.pack(pady=10)

    descripcionlossantos ="""Los Santos es una provincia panameña, situada al sureste de la península de Azuero. 
    Las Tablas es su capital y localidad más poblada. Está compuesta por los distritos de Los Santos, Guararé, 
    Las Tablas, Macaracas, Pedasí, Pocrí y Tonosí. Con una superficie de 3 809,4 km² y una población de 95 540 habitantes, 
    limita al sur y al este con el océano Pacífico, al norte con el océano Pacífico y la provincia de Herrera, y al oeste 
    con la provincia de Veraguas, concretamente con el distrito de Mariato."""
    description_label = tk.Label(frame, text=descripcionlossantos, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/LosSantos/LosSantos.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresLossantos = tk.Menu(ventana_lossantos)
    ventana_lossantos.config(menu=lugaresLossantos)

    menu_losantos= tk.Menu(lugaresLossantos, tearoff=0)
    menu_losantos.add_command(label="lugar1",)
    menu_losantos.add_command(label="lugar2", )
    menu_losantos.add_command(label="lugar3", )
    menu_losantos.add_command(label="lugar4", )
    
    lugaresLossantos.add_cascade(label="Provincia Los Santos", menu=menu_losantos)
    
    boton_regresar = tk.Button(ventana_lossantos, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_lossantos.destroy)
    boton_regresar.place(x=450, y=335)

def Panama():
    ventana_panama= tk.Toplevel()
    ventana_panama.title("Panama")
    ventana_panama.geometry("600x400")

    title_label = tk.Label(ventana_panama, text="Provincia: Panama", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_panama)
    frame.pack(pady=10)

    descripcionpanama ="""Panamá es una provincia y la capital del país, ubicada en la región central. 
    Tiene una extensión de 11,289 km² y una población de aproximadamente 1.8 millones de habitantes (2018). 
    Limita al norte con Colón, al sur con el océano Pacífico, al este con Darién y al oeste con Panamá Oeste."""
    description_label = tk.Label(frame, text=descripcionpanama, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Panama/Panama.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresPanama = tk.Menu(ventana_panama)
    ventana_panama.config(menu=lugaresPanama)

    menu_panama= tk.Menu(lugaresPanama, tearoff=0)
    menu_panama.add_command(label="lugar1",)
    menu_panama.add_command(label="lugar2", )
    menu_panama.add_command(label="lugar3", )
    menu_panama.add_command(label="lugar4", )
    
    lugaresPanama.add_cascade(label="Provincia Panama", menu=menu_panama)
    
    boton_regresar = tk.Button(ventana_panama, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_panama.destroy)
    boton_regresar.place(x=450, y=335)

def Veraguas():
    ventana_veraguas= tk.Toplevel()
    ventana_veraguas.title("Veraguas")
    ventana_veraguas.geometry("600x400")

    title_label = tk.Label(ventana_veraguas, text="Provincia: Veraguas", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_veraguas)
    frame.pack(pady=10)

    descripcionveraguas ="""Veraguas es una de las diez provincias de Panamá. Su capital es la ciudad de Santiago de Veraguas. 
    Tiene una superficie de 10 629 km², y un área de 10.587,6 km² y en el año 2022 tenía una población estimada de 248,000.3. 
    Limita al norte con el mar Caribe, al sur con el océano Pacífico, al este con las provincias de Colón, Coclé, Herrera, 
    Los Santos y al oeste con la provincia de Chiriquí y la Comarca Ngäbe-Buglé. Es la única provincia de Panamá que tiene 
    costas en los océanos Atlántico y Pacífico, condición que a nivel de subdivisión nacional solo comparte con el departamento 
    del Chocó en Colombia en todo el continente americano."""
    description_label = tk.Label(frame, text=descripcionveraguas, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/Veraguas/Veraguas.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresVeraguas = tk.Menu(ventana_veraguas)
    ventana_veraguas.config(menu=lugaresVeraguas)

    menu_veraguas= tk.Menu(lugaresVeraguas, tearoff=0)
    menu_veraguas.add_command(label="lugar1",)
    menu_veraguas.add_command(label="lugar2", )
    menu_veraguas.add_command(label="lugar3", )
    menu_veraguas.add_command(label="lugar4", )
    
    lugaresVeraguas.add_cascade(label="Provincia Veraguas", menu=menu_veraguas)
    
    boton_regresar = tk.Button(ventana_veraguas, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_veraguas.destroy)
    boton_regresar.place(x=450, y=335)

def PanamaOeste():
    ventana_panoeste= tk.Toplevel()
    ventana_panoeste.title("Panama Oeste")
    ventana_panoeste.geometry("600x400")

    title_label = tk.Label(ventana_panoeste, text="Provincia: Panama Oeste", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_panoeste)
    frame.pack(pady=10)

    descripcionpanoeste ="""Panamá Oeste es una de las diez provincias de Panamá, creada el 1.º de enero de 2014 
    a partir de territorios segregados de la provincia de Panamá ubicados al oeste del canal de Panamá. 
    Está conformado por 5 distritos: Arraiján, Capira, Chame, La Chorrera y San Carlos. Su capital es La Chorrera."""
    description_label = tk.Label(frame, text=descripcionpanoeste, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/PanamaOeste/PanamaOeste.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugarespanoeste = tk.Menu(ventana_panoeste)
    ventana_panoeste.config(menu=lugarespanoeste)

    menu_panoeste= tk.Menu(lugarespanoeste, tearoff=0)
    menu_panoeste.add_command(label="lugar1",)
    menu_panoeste.add_command(label="lugar2", )
    menu_panoeste.add_command(label="lugar3", )
    menu_panoeste.add_command(label="lugar4", )
    
    lugarespanoeste.add_cascade(label="Provincia Panama Oeste", menu=menu_panoeste)
    
    boton_regresar = tk.Button(ventana_panoeste, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_panoeste.destroy)
    boton_regresar.place(x=450, y=335)
#Fin Funciones provincias

#Inicio Funciones comarcas
def EmberaWounaan():
    ventana_embera= tk.Toplevel()
    ventana_embera.title("Embera Wounaan")
    ventana_embera.geometry("600x400")

    title_label = tk.Label(ventana_embera, text="Comarca: Embera Wounaan", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_embera)
    frame.pack(pady=10)

    descripcionembera ="""Emberá-Wounaan es una comarca indígena de Panamá. Fue creada en 1983 a partir de dos 
    enclaves ubicados en la provincia de Darién, específicamente de los distritos de Chepigana y Pinogana. 
    Su capital es Unión Chocó. Su extensión abarca 4383,5 km² y posee una población de 9544 habitantes (2010),
    la mayoría de estos pertenecen a las etnias emberá y wounaan, distribuidas en 40 comunidades."""
    description_label = tk.Label(frame, text=descripcionembera, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/EmberaWounaan/EmberaWounaan.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresEmbera = tk.Menu(ventana_embera)
    ventana_embera.config(menu=lugaresEmbera)

    menu_embera= tk.Menu(lugaresEmbera, tearoff=0)
    menu_embera.add_command(label="lugar1",)
    menu_embera.add_command(label="lugar2", )
    menu_embera.add_command(label="lugar3", )
    menu_embera.add_command(label="lugar4", )
    
    lugaresEmbera.add_cascade(label="Comarca Embera Wounaan", menu=menu_embera)
    
    boton_regresar = tk.Button(ventana_embera, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_embera.destroy)
    boton_regresar.place(x=450, y=335)
    
def GunaYala():
    ventana_guna= tk.Toplevel()
    ventana_guna.title("Guna Yala")
    ventana_guna.geometry("600x400")

    title_label = tk.Label(ventana_guna, text="Comarca: Guna Yala", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_guna)
    frame.pack(pady=10)

    descripcionguna ="""Guna Yala es una comarca indígena en Panamá, habitada por la etnia guna. 
    Antiguamente la comarca se llamó San Blas, hasta 1998 y Kuna Yala, hasta 2010. Los locales 
    la conocen con varios nombres como: "Dulenega", "Yarsuid", "Duleyala". Su capital es Gairgirgordub. 
    Limita al norte con el mar Caribe, al sur con la provincia de Darién y la comarca Emberá Wounnan, 
    al este con Colombia y al oeste con la provincia de Colón."""
    description_label = tk.Label(frame, text=descripcionguna, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/GunaYala/GunaYala.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresGuna = tk.Menu(ventana_guna)
    ventana_guna.config(menu=lugaresGuna)

    menu_guna= tk.Menu(lugaresGuna, tearoff=0)
    menu_guna.add_command(label="lugar1",)
    menu_guna.add_command(label="lugar2", )
    menu_guna.add_command(label="lugar3", )
    menu_guna.add_command(label="lugar4", )
    
    lugaresGuna.add_cascade(label="Comarca Guna Yala", menu=menu_guna)
    
    boton_regresar = tk.Button(ventana_guna, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_guna.destroy)
    boton_regresar.place(x=450, y=335)

def NgabeBugle():
    ventana_ngabe= tk.Toplevel()
    ventana_ngabe.title("Ngabe-Bugle")
    ventana_ngabe.geometry("600x400")

    title_label = tk.Label(ventana_ngabe, text="Comarca: Ngabe-Bugle", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_ngabe)
    frame.pack(pady=10)

    descripcionngabe ="""Esta comarca fue creada en 1997 a partir del territorio de Bocas del Toro, 
    Chiriquí y Veraguas. Su capital es Llano Tugrí (o Buabïti). La comarca está habitada por las 
    etnias indígenas ngäbe y buglé, así como campesinos, y habitan en ella 154.355 personas (según el censo del 2010), 
    y su área es de 6968 km²."""
    description_label = tk.Label(frame, text=descripcionngabe, wraplength=500, justify="left")
    description_label.pack()

    try:
        image_path = "imagenes/NgabeBugle/NgabeBugle.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    lugaresNgabe = tk.Menu(ventana_ngabe)
    ventana_ngabe.config(menu=lugaresNgabe)

    menu_ngabe= tk.Menu(lugaresNgabe, tearoff=0)
    menu_ngabe.add_command(label="lugar1",)
    menu_ngabe.add_command(label="lugar2", )
    menu_ngabe.add_command(label="lugar3", )
    menu_ngabe.add_command(label="lugar4", )
    
    lugaresNgabe.add_cascade(label="Comarca Ngabe-Bugle", menu=menu_ngabe)
    
    boton_regresar = tk.Button(ventana_ngabe, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_ngabe.destroy)
    boton_regresar.place(x=450, y=335)
#Fin Funciones comarcas
def Reserva():
    ventana_reserva = tk.Toplevel()
    ventana_reserva.title("Reservar Actividad Turística")
    ventana_reserva.geometry("600x500")

    # Variables para almacenar los datos del cliente
    nombre_var = StringVar()
    nacionalidad_var = StringVar()
    sexo_var = StringVar()
    identificacion_var = StringVar()
    telefono_var = StringVar()
    cantidad_personas_var = StringVar()

    # Preguntar la cantidad de personas
    tk.Label(ventana_reserva, text="Cantidad de personas:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=cantidad_personas_var).pack(pady=5)

    # Preguntar el nombre del usuario
    tk.Label(ventana_reserva, text="Nombre:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=nombre_var).pack(pady=5)

    # Preguntar la nacionalidad
    tk.Label(ventana_reserva, text="Nacionalidad:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=nacionalidad_var).pack(pady=5)

    # Preguntar el sexo
    tk.Label(ventana_reserva, text="Sexo:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=sexo_var).pack(pady=5)

    # Preguntar la identificación personal
    tk.Label(ventana_reserva, text="Identificación Personal:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=identificacion_var).pack(pady=5)

    # Preguntar el teléfono
    tk.Label(ventana_reserva, text="Teléfono:").pack(pady=5)
    tk.Entry(ventana_reserva, textvariable=telefono_var).pack(pady=5)

    # Función para manejar el pago
    def pagar():
        messagebox.showinfo("pagar", "Funcionalidad de pagar no implementada.")

    # Función para manejar el abono
    def abono():
        messagebox.showinfo("Abono", "Funcionalidad de abono no implementada.")

    # Botones de Pagar y Abono
    tk.Button(ventana_reserva, text="Pagar", command=pagar).pack(pady=10)
    tk.Button(ventana_reserva, text="Abono", command=abono).pack(pady=10)

    # Botón para regresar al menú anterior
    tk.Button(ventana_reserva, text="Regresar", command=ventana_reserva.destroy).pack(pady=10)
    
    
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

menu_bar.add_cascade(label="Menu", menu=menu_prin)

# Configurar la barra de menú en la ventana principal
ventana.config(menu=menu_bar)

# Ejecutar el bucle principal
ventana.mainloop()
#FinAlgoritmo