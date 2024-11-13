#InicioAlgoritmo
import tkinter as tk
from tkinter import ttk
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

    exit_button = tk.Button(ventana_presentacion, text="REGRESAR", command=lambda: ventana_presentacion.destroy())
    exit_button.pack(pady=20)
    
def ProvinciasComarcas():
    ventana_provincias = tk.Toplevel()
    ventana_provincias.title("Provincias")
    ventana_provincias.geometry("600x450")
    frame = tk.Frame(ventana_provincias)
    frame.pack(pady=10)
        
    try:
        image_path = "imagenes/empresas_hou.jpg"
        image = Image.open(image_path)
        image = image.resize((500, 400), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

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
    exit_button = tk.Button(ventana_provincias, text="REGRESAR", command=ventana_provincias.destroy)
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
    ventana_PlayaEstrella.configure(bg='#009999')  

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

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Playa Estrella"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_PlayaEstrella.destroy)
    boton_volver.pack(side="left", padx=10)
def GreenAcresBocas():
    ventana_GreenAcres = tk.Toplevel()
    ventana_GreenAcres.title("Green Acres")
    ventana_GreenAcres.geometry("700x600")
    ventana_GreenAcres.configure(bg='#009999')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_GreenAcres, bg='#009999')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="GREEN ACRES", font=("Arial", 20, "bold"), bg='#009999')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/BocasdelToro/GreenAcresBocas.jpg"  # Ruta a la imagen
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
        "Green Acres es una reserva de cacao orgánico en la isla Bastimentos. "
        "Los visitantes pueden conocer el proceso del cacao, caminar por senderos naturales "
        "y observar fauna como ranas venenosas y aves tropicales. Se promueve el cultivo sustentable "
        "y se ofrecen degustaciones de cacao artesanal."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido guiado por el cultivo de cacao\n"
        "- Degustación de cacao orgánico\n"
        "- Paseo ecológico por la reserva\n"
        "Precio: 120.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_GreenAcres, bg='#009999')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="GREEN ACRES"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_GreenAcres.destroy)
    boton_volver.pack(side="left", padx=10)     
def BahiaDelfinesBocas():
    ventana_BahiaDelfines = tk.Toplevel()
    ventana_BahiaDelfines.title("Bahía de los Delfines")
    ventana_BahiaDelfines.geometry("700x600")
    ventana_BahiaDelfines.configure(bg='#009999')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_BahiaDelfines, bg='#009999')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="BAHÍA DE LOS DELFINES", font=("Arial", 20, "bold"), bg='#009999')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/BocasdelToro/BahiaDelfinesBocas.jpg"  # Ruta a la imagen
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
        "Bahía de los Delfines es un área protegida conocida por ser hábitat de delfines en su entorno natural. "
        "Los visitantes pueden realizar paseos en lancha para observar delfines, disfrutar de paisajes y hacer snorkel."
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
        "Precio: 250.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_BahiaDelfines, bg='#009999')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Bahía de los Delfines"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_BahiaDelfines.destroy)
    boton_volver.pack(side="left", padx=10)  
def AldeaBotellasBocas():
    ventana_AldeaBotellas = tk.Toplevel()
    ventana_AldeaBotellas.title("Aldea de Botellas Plásticas")
    ventana_AldeaBotellas.geometry("700x600")
    ventana_AldeaBotellas.configure(bg='#009999')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_AldeaBotellas, bg='#009999')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="ALDEA DE BOTELLAS PLÁSTICAS", font=("Arial", 20, "bold"), bg='#009999')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/BocasdelToro/AldeaBotellasBocas.jpg"  # Ruta a la imagen
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
        "La Aldea de Botellas Plásticas es una ecoaldea construida con materiales reciclados. "
        "Los visitantes pueden participar en talleres de reciclaje y conciencia ambiental."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Tour guiado\n"
        "- Taller de reciclaje\n"
        "- Souvenir ecológico\n"
        "Precio: 50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_AldeaBotellas, bg='#009999')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Aldea de Botellas Plásticas"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_AldeaBotellas.destroy)
    boton_volver.pack(side="left", padx=10)
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

    descripcionCocle =(
        "Coclé es una provincia del centro de Panamá. Su superficie es de 4,927km² y cuenta con" 
        "268,264 habitantes (2023).Su capital es Penonomé. Limita al norte con la provincia de Colón,"
        "al este con la provincia de Panamá Oeste, al sur con la de Herrera y el golfo de Parita y al" 
        "oeste con la de Veraguas. El centro y norte de la provincia esta accidentados por la cordillera" 
        "central; al sur pertenece las llanuras centrales, tierras bajas muy fértiles que se extienden hasta" 
        "el litoral. También es una provincia de gran riqueza natural y material. Es además el epicentro de la" 
        "cultura precolombina más avanzada del istmo.")
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
    menu_cocle.add_command(label="Zoológico El Níspero", command= ZoologicoElNispero)
    menu_cocle.add_command(label="Mariposario del Valle", command= MariposarioDelValle)
    menu_cocle.add_command(label="Sendero de La India Dormida", command= SenderoIndiaDormidaCocle)
    menu_cocle.add_command(label="Serpentario Maravillas Tropicales", command= SerpentarioMaravillasCocle)

    lugaresCocle.add_cascade(label="Lugares Turistico de Cocle que deberias visitar", menu=menu_cocle)
    
    boton_regresar = tk.Button(ventana_cocle, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_cocle.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Cocle
def ZoologicoElNispero():
    ventana_ZoologicoElNispero = tk.Toplevel()
    ventana_ZoologicoElNispero.title("Zoológico El Níspero")
    ventana_ZoologicoElNispero.geometry("700x600")
    ventana_ZoologicoElNispero.configure(bg='#D3D3D3')

    main_frame = tk.Frame(ventana_ZoologicoElNispero, bg='#D3D3D3')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Zoológico El Níspero", font=("Arial", 20, "bold"), bg='#D3D3D3')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Cocle/ZoologicoElNispero.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#D3D3D3')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "Ubicado en el Valle de Antón, El Níspero es un zoológico y jardín botánico con una variedad de "
        "animales nativos y exóticos. Los visitantes pueden ver monos, tucanes, ranas doradas y disfrutar "
        "de un ambiente natural ideal para la educación y la conservación."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido guiado por el zoológico y jardín botánico\n"
        "- Observación de animales como monos, tucanes y ranas doradas\n"
        "- Actividades de conservación\n"
        "- Área educativa sobre especies endémicas\n"
        "Precio: 10.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_ZoologicoElNispero, bg='#D3D3D3')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Zoológico El Níspero"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_ZoologicoElNispero.destroy)
    boton_volver.pack(side="left", padx=10)     
def MariposarioDelValle():
    ventana_MariposarioDelValle = tk.Toplevel()
    ventana_MariposarioDelValle.title("Mariposario del Valle")
    ventana_MariposarioDelValle.geometry("700x600")
    ventana_MariposarioDelValle.configure(bg='#D3D3D3')

    main_frame = tk.Frame(ventana_MariposarioDelValle, bg='#D3D3D3')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Mariposario del Valle", font=("Arial", 20, "bold"), bg='#D3D3D3')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Cocle/MariposarioDelValle.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#D3D3D3')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")
        
    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "El Mariposario del Valle es un centro dedicado a la conservación de diversas especies de mariposas, "
        "donde los visitantes pueden observar todas las etapas de desarrollo de estos insectos."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Recorrido guiado sobre el ciclo de vida de las mariposas\n"
        "- Observación de diversas especies de mariposas\n"
        "- Talleres de conservación\n"
        "- Interacción con guías especializados\n"
        "Precio: 8.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_MariposarioDelValle, bg='#D3D3D3')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Mariposario del Valle"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_MariposarioDelValle.destroy)
    boton_volver.pack(side="left", padx=10)   
def SenderoIndiaDormidaCocle():
    ventana_IndiaDormida = tk.Toplevel()
    ventana_IndiaDormida.title("Sendero de La India Dormida")
    ventana_IndiaDormida.geometry("700x600")
    ventana_IndiaDormida.configure(bg='#D3D3D3')
    
    main_frame = tk.Frame(ventana_IndiaDormida, bg='#D3D3D3')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Sendero de La India Dormida", font=("Arial", 20, "bold"), bg='#D3D3D3')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Cocle/SenderoIndiaDormida.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#D3D3D3')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "El Sendero de La India Dormida es una popular ruta de senderismo en el Valle de Antón que lleva a la cima de una montaña con forma de mujer acostada. "
        "Es ideal para quienes disfrutan de la naturaleza, ya que ofrece vistas panorámicas, además de observar flora y fauna autóctona."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Senderismo por ruta escénica con cascadas y ríos\n"
        "- Vista panorámica desde la cima\n"
        "- Observación de flora y fauna autóctona\n"
        "- Acceso a zonas de descanso y fotografía\n"
        "\nPrecio: 50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_IndiaDormida, bg='#D3D3D3')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Sendero de la India Dormida"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_IndiaDormida.destroy)
    boton_volver.pack(side="left", padx=10)       
def SerpentarioMaravillasCocle():
    ventana_Serpentario = tk.Toplevel()
    ventana_Serpentario.title("Serpentario Maravillas Tropicales")
    ventana_Serpentario.geometry("700x600")
    ventana_Serpentario.configure(bg='#D3D3D3')
    
    main_frame = tk.Frame(ventana_Serpentario, bg='#D3D3D3')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Serpentario Maravillas Tropicales", font=("Arial", 20, "bold"), bg='#D3D3D3')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Cocle/Serpentario.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#D3D3D3')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "Este serpentario en el Valle de Antón alberga una variedad de reptiles y ofrece una experiencia educativa "
        "sobre la importancia de la conservación."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Observación de serpientes nativas y exóticas\n"
        "- Explicaciones sobre biología y conservación\n"
        "- Exhibición de reptiles en ambiente seguro\n"
        "- Interacción con expertos en herpetología\n"
        "\nPrecio: 50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_Serpentario, bg='#D3D3D3')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Serpentario Maravillas Tropicales"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_Serpentario.destroy)
    boton_volver.pack(side="left", padx=10)    
#Fin Lugares Turisticos de Cocle

def Colon():
    ventana_colon= tk.Toplevel()
    ventana_colon.title("Colon")
    ventana_colon.geometry("600x400")

    title_label = tk.Label(ventana_colon, text="Provincia: Colon", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_colon)
    frame.pack(pady=10)

    descripcionColon =(
        "Colón es la capital de la provincia panameña de Colón, ubicada en la costa caribeña de Panamá." 
        "La población estimada para 2016 es de unas 84,229 personas en su conurbación. Está comunicada" 
        "con la capital por medio de la Carretera Transístmica (autopista Panamá-Colón), que la une en" 
        "78,9 km con la costa del océano Pacífico. Es la segunda ciudad más poblada del Caribe de Centroamérica."
        "Su casco urbano tiene unos 79 000 habitantes. Posee uno de los puertos más grandes de América Latina")
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
    menu_colon.add_command(label="El Castillo de San Lorenzo El Real de Chagres", command= CastilloSanLorenzo)
    menu_colon.add_command(label="Esclusas de Gatún", command= EsclusasGatun )
    menu_colon.add_command(label="Esclusas de agua clara", command= EsclusasAguaClaraColon )
    menu_colon.add_command(label="Parque Nacional Chagres", command= ParqueNacionalChagres )
    
    lugaresColon.add_cascade(label="Provincia Colon", menu=menu_colon)
    
    boton_regresar = tk.Button(ventana_colon, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_colon.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Colon   
def CastilloSanLorenzo():
    ventana_CastilloSanLorenzo = tk.Toplevel()
    ventana_CastilloSanLorenzo.title("Castillo de San Lorenzo")
    ventana_CastilloSanLorenzo.geometry("700x600")
    ventana_CastilloSanLorenzo.configure(bg='#2F4F4F')
    
    main_frame = tk.Frame(ventana_CastilloSanLorenzo, bg='#2F4F4F')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)
    
    titulo = tk.Label(main_frame, text="Castillo de San Lorenzo", font=("Arial", 20, "bold"), bg='#2F4F4F')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Colon/CastilloSanLorenzo.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#2F4F4F')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")
    
    descripcion_texto = (
        "El Castillo de San Lorenzo es una fortaleza histórica situada en la entrada del río Chagres. "
        "Construido en el siglo XVII, su objetivo era proteger el comercio en el Canal de Panamá. "
        "Los turistas pueden explorar las ruinas, aprender sobre su historia militar y disfrutar de vistas "
        "panorámicas del río y la selva circundante."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()
    
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido por las ruinas de la fortaleza histórica\n"
        "- Vista panorámica del río y la selva\n"
        "- Explicación de la historia militar y comercial\n"
        "- Espacios para fotografía y exploración\n"
        "\nPrecio: 2.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_CastilloSanLorenzo, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Castillo de San Lorenzo"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_CastilloSanLorenzo, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_CastilloSanLorenzo.destroy)
    boton_volver.pack(side="left", padx=10)
def EsclusasGatun():
    ventana_EsclusasGatun = tk.Toplevel()
    ventana_EsclusasGatun.title("Esclusas de Gatún")
    ventana_EsclusasGatun.geometry("700x600")
    ventana_EsclusasGatun.configure(bg='#2F4F4F')

    main_frame = tk.Frame(ventana_EsclusasGatun, bg='#2F4F4F')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Esclusas de Gatún", font=("Arial", 20, "bold"), bg='#2F4F4F')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Colon/EsclusasGatun.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#2F4F4F')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Las Esclusas de Gatún, ubicadas en el Canal de Panamá, permiten observar el funcionamiento de las esclusas, "
        "donde los barcos son elevados o descendidos. Es un lugar para conocer sobre el impacto del canal en la economía."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Observación del funcionamiento de las esclusas\n"
        "- Información educativa sobre el Canal de Panamá\n"
        "- Vista de barcos en tránsito\n"
        "- Experiencia en el centro de visitantes\n"
        "\nPrecio: 15.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_EsclusasGatun, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Esclusas de Gatún"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_EsclusasGatun, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_EsclusasGatun.destroy)
    boton_volver.pack(side="left", padx=10)
def EsclusasAguaClaraColon():
    ventana_AguaClara = tk.Toplevel()
    ventana_AguaClara.title("Esclusas de Agua Clara")
    ventana_AguaClara.geometry("700x600")
    ventana_AguaClara.configure(bg='#2F4F4F')
    
    main_frame = tk.Frame(ventana_AguaClara, bg='#2F4F4F')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Esclusas de Agua Clara", font=("Arial", 20, "bold"), bg='#2F4F4F')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Colon/EsclusasAguaClara.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#2F4F4F')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "Las Esclusas de Agua Clara permiten observar el proceso de tránsito de barcos por el Canal de Panamá, "
        "con un centro de visitantes que ofrece una experiencia educativa sobre el impacto del canal en el comercio global."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Vista de las operaciones de tránsito de barcos\n"
        "- Explicación sobre la construcción del canal\n"
        "- Exhibiciones sobre el comercio mundial\n"
        "- Observación de ingeniería en acción\n"
        "\nPrecio: 15.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_AguaClara, bg='#2F4F4F')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Esclusas de Agua Clara"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_AguaClara.destroy)
    boton_volver.pack(side="left", padx=10) 
def ParqueNacionalChagres():
    ventana = tk.Toplevel()
    ventana.title("Parque Nacional Chagres")
    ventana.geometry("700x600")
    ventana.configure(bg='#2F4F4F')

    main_frame = tk.Frame(ventana, bg='#2F4F4F')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Parque Nacional Chagres", font=("Arial", 20, "bold"), bg='#2F4F4F')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Colon/ParqueNacionalChagres.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#2F4F4F')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "El Parque Nacional Chagres es un extenso parque natural que alberga el río Chagres. "
        "Ofrece oportunidades para realizar deportes acuáticos y explorar la naturaleza en su estado puro."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Caminatas por senderos en el bosque tropical\n"
        "- Observación de cascadas y ríos\n"
        "- Información sobre el Camino Real histórico\n"
        "- Actividades de ecoturismo y conservación\n"
        "\nPrecio: $45.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#2F4F4F')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parque Nacional Chagres"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos de Colon

def Chiriqui():
    ventana_chiriqui= tk.Toplevel()
    ventana_chiriqui.title("Chiriqui")
    ventana_chiriqui.geometry("600x400")

    title_label = tk.Label(ventana_chiriqui, text="Provincia: Chiriqui", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_chiriqui)
    frame.pack(pady=10)

    descripcionchiriqui =(
        "Chiriquí es una provincia de Panamá ubicada en la región occidental del país, teniendo como límites" 
        "al norte la provincia de Bocas del Toro y la comarca Ngäbe-Buglé, al oeste la República de Costa Rica" 
        "(Provincia de Puntarenas), al este la provincia de Veraguas y al sur el océano Pacífico.")
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
    menu_chiriqui.add_command(label="Parque Nacional Volcán Barú", command= ParqueVolcanBaru)
    menu_chiriqui.add_command(label="Las Cascadas Perdidas", command= CascadasPerdidas)
    menu_chiriqui.add_command(label="Refugio de Vida Silvestre Jungla de Panamá", command= RefugioJunglaChiriqui)
    menu_chiriqui.add_command(label="Abejas y Mariposas de Boquete", command=AbejasMariposasBoquete)
    
    lugaresChiriqui.add_cascade(label="Provincia Chiriqui", menu=menu_chiriqui)
    
    boton_regresar = tk.Button(ventana_chiriqui, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_chiriqui.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos Chiriqui
def ParqueVolcanBaru():
    ventana_ParqueVolcanBaru = tk.Toplevel()
    ventana_ParqueVolcanBaru.title("Parque Nacional Volcán Barú")
    ventana_ParqueVolcanBaru.geometry("700x600")
    ventana_ParqueVolcanBaru.configure(bg='#6A5ACD')

    main_frame = tk.Frame(ventana_ParqueVolcanBaru, bg='#6A5ACD')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Parque Nacional Volcán Barú", font=("Arial", 20, "bold"), bg='#6A5ACD')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Chiriqui/ParqueVolcanBaru.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#6A5ACD')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "El Parque Nacional Volcán Barú alberga el volcán más alto de Panamá. Los visitantes pueden hacer "
        "senderismo hasta la cima para disfrutar de vistas espectaculares, desde donde se pueden ver tanto el "
        "océano Pacífico como el mar Caribe en días despejados. Ideal para los amantes del montañismo y la naturaleza."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Senderismo hasta la cima del volcán\n"
        "- Observación de flora y fauna en ambiente volcánico\n"
        "- Puntos de descanso y miradores\n"
        "- Caminatas guiadas por expertos\n"
        "Precio: 50.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_ParqueVolcanBaru, bg='#6A5ACD')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parque Nacional Volcán Barú"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_ParqueVolcanBaru.destroy)
    boton_volver.pack(side="left", padx=10)  
def CascadasPerdidas():
    ventana_CascadasPerdidas = tk.Toplevel()
    ventana_CascadasPerdidas.title("Las Cascadas Perdidas")
    ventana_CascadasPerdidas.geometry("700x600")
    ventana_CascadasPerdidas.configure(bg='#6A5ACD')

    main_frame = tk.Frame(ventana_CascadasPerdidas, bg='#6A5ACD')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Las Cascadas Perdidas", font=("Arial", 20, "bold"), bg='#6A5ACD')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Chiriqui/CascadasPerdidas.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#6A5ACD')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Ubicadas en Boquete, Las Cascadas Perdidas son un conjunto de cascadas accesibles a través de un sendero "
        "de selva tropical. Los excursionistas pueden disfrutar de vistas y áreas de descanso junto a las cascadas."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Senderismo por la selva tropical\n"
        "- Descanso junto a las cascadas\n"
        "- Observación de biodiversidad local\n"
        "- Áreas de picnic y fotografía\n"
        "\nPrecio: 10.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_CascadasPerdidas, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Las Cascadas Perdidas"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_CascadasPerdidas, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_CascadasPerdidas.destroy)
    boton_volver.pack(side="left", padx=10)
def RefugioJunglaChiriqui():
    ventana_Jungla = tk.Toplevel()
    ventana_Jungla.title("Refugio de Vida Silvestre Jungla de Panamá")
    ventana_Jungla.geometry("700x600")
    ventana_Jungla.configure(bg='#6A5ACD')
    
    main_frame = tk.Frame(ventana_Jungla, bg='#6A5ACD')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Refugio de Vida Silvestre Jungla de Panamá", font=("Arial", 20, "bold"), bg='#6A5ACD')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Chiriqui/RefugioJungla.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#6A5ACD')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "Este refugio en Boquete alberga animales rescatados y ofrece un ambiente de conservación. "
        "Los visitantes pueden ver de cerca especies locales y aprender sobre la rehabilitación de animales."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Observación de animales rescatados\n"
        "- Información sobre programas de rescate y rehabilitación\n"
        "- Recorridos guiados por el refugio\n"
        "- Interacción con cuidadores de animales\n"
        "\nPrecio: 70.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_Jungla, bg='#6A5ACD')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Refugio de Vida Silvestre Jungla de Panamá"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_Jungla.destroy)
    boton_volver.pack(side="left", padx=10)
def AbejasMariposasBoquete():
    ventana = tk.Toplevel()
    ventana.title("Abejas y Mariposas de Boquete")
    ventana.geometry("700x600")
    ventana.configure(bg='#6A5ACD')

    main_frame = tk.Frame(ventana, bg='#6A5ACD')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Abejas y Mariposas de Boquete", font=("Arial", 20, "bold"), bg='#6A5ACD')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Chiriqui/AbejasMariposasBoquete.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#6A5ACD')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "Centro ecológico especializado en la cría de mariposas y abejas. "
        "Ofrece una experiencia educativa sobre la importancia de los polinizadores, "
        "con recorrido y demostración de miel orgánica."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido por el centro ecológico\n"
        "- Observación de mariposas y producción de miel orgánica\n"
        "- Jardines diseñados para polinizadores\n"
        "- Charlas educativas sobre la importancia de las abejas\n"
        "\nPrecio: $30.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#6A5ACD')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Abejas y Mariposas de Boquete"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos Chiriqui

def Darien():
    ventana_darien= tk.Toplevel()
    ventana_darien.title("Darien")
    ventana_darien.geometry("600x400")

    title_label = tk.Label(ventana_darien, text="Provincia: Darien", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_darien)
    frame.pack(pady=10)

    descripciondarien =(
        "Darién es una de las diez provincias de Panamá. Su capital es la ciudad de La Palma. Tiene una extensión" 
        "de 11 896,5 km², siendo por lo tanto la más extensa del país. Está ubicada en el extremo oriental del país" 
        "y limita al norte con la provincia de Panamá y la comarca Guna Yala. Al sur limita con el océano Pacífico y" 
        "la República de Colombia. Al este limita con el departamento de Chocó en la República de Colombia y al oeste"
        "limita con el océano Pacífico y la provincia de Panamá.")
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
    menu_darien.add_command(label="Parque Nacional Darién", command=ParqueNacionalDarien)
    menu_darien.add_command(label="La Palma", command= LaPalma)
    menu_darien.add_command(label="Yaviza y el fin de la carretera Panamericana", command= YavizaFinPanamericana)
    menu_darien.add_command(label="Río Chucunaque", command=RioChucunaqueDarien)
    
    lugaresDarien.add_cascade(label="Provincia Darien", menu=menu_darien)
    
    boton_regresar = tk.Button(ventana_darien, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_darien.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos Darien
def ParqueNacionalDarien():
    ventana_ParqueNacionalDarien = tk.Toplevel()
    ventana_ParqueNacionalDarien.title("Parque Nacional Darién")
    ventana_ParqueNacionalDarien.geometry("700x600")
    ventana_ParqueNacionalDarien.configure(bg='#87CEEB')

    main_frame = tk.Frame(ventana_ParqueNacionalDarien, bg='#87CEEB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Parque Nacional Darién", font=("Arial", 20, "bold"), bg='#87CEEB')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Darien/ParqueNacionalDarien.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#87CEEB')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "El Parque Nacional Darién es un área protegida famosa por su biodiversidad y paisajes inexplorados. "
        "Ofrece senderos para explorar la selva tropical, observación de aves y aventuras en la naturaleza. "
        "Es un destino ideal para el ecoturismo y la conservación."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Senderos para explorar la selva tropical\n"
        "- Observación de aves y vida silvestre\n"
        "- Información sobre la flora y fauna de la región\n"
        "- Actividades de ecoturismo y conservación\n"
        "Precio: 100.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_ParqueNacionalDarien, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parque Nacional Darién"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_ParqueNacionalDarien, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_ParqueNacionalDarien.destroy)
    boton_volver.pack(side="left", padx=10)    
def YavizaFinPanamericana():
    ventana_YavizaFinPanamericana = tk.Toplevel()
    ventana_YavizaFinPanamericana.title("Yaviza y el Fin de la Carretera Panamericana")
    ventana_YavizaFinPanamericana.geometry("700x600")
    ventana_YavizaFinPanamericana.configure(bg='#87CEEB')

    main_frame = tk.Frame(ventana_YavizaFinPanamericana, bg='#87CEEB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Yaviza y el Fin de la Carretera Panamericana", font=("Arial", 20, "bold"), bg='#87CEEB')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Darien/YavizaFinPanamericana.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#87CEEB')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Yaviza es un pequeño pueblo en Darién, conocido por ser el punto final de la Carretera Panamericana, "
        "que conecta América del Norte con América del Sur. Un destino remoto rodeado de selva tropical."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Vista del punto final de la Carretera Panamericana\n"
        "- Excursiones hacia la selva tropical\n"
        "- Interacción con guías locales sobre la historia de Yaviza\n"
        "- Fotografía de paisajes y flora de la región\n"
        "Precio: 20.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_YavizaFinPanamericana, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Yaviza y el Fin de la Carretera Panamericana"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_YavizaFinPanamericana, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_YavizaFinPanamericana.destroy)
    boton_volver.pack(side="left", padx=10)  
def RioChucunaqueDarien():
    ventana_Chucunaque = tk.Toplevel()
    ventana_Chucunaque.title("Río Chucunaque")
    ventana_Chucunaque.geometry("700x600")
    ventana_Chucunaque.configure(bg='#87CEEB')
    
    main_frame = tk.Frame(ventana_Chucunaque, bg='#87CEEB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Río Chucunaque", font=("Arial", 20, "bold"), bg='#87CEEB')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Darien/RioChucunaque.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#87CEEB')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "El Río Chucunaque es un destino ideal para la aventura en Darién, donde se pueden realizar paseos en bote y pesca, rodeado por exuberante vegetación y biodiversidad local."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Paseos en bote por el río\n"
        "- Oportunidad de pesca en aguas naturales\n"
        "- Observación de vegetación y fauna\n"
        "- Experiencia inmersiva en la naturaleza\n"
        "\nPrecio: 120.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_Chucunaque, bg='#87CEEB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Rio Chucunaque"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_Chucunaque.destroy)
    boton_volver.pack(side="left", padx=10)
def LaPalma():
    ventana = tk.Toplevel()
    ventana.title("La Palma")
    ventana.geometry("700x600")
    ventana.configure(bg='#87CEEB')

    main_frame = tk.Frame(ventana, bg='#87CEEB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="La Palma", font=("Arial", 20, "bold"), bg='#87CEEB')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Darien/LaPalma.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#87CEEB')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "La Palma es un destino cultural en Darién, con opciones para explorar la naturaleza y conocer la "
        "cultura indígena local, además de ser la entrada al Parque Nacional Darién."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido por la capital de Darién\n"
        "- Interacción con comunidades indígenas\n"
        "- Exploración de paisajes naturales\n"
        "- Oportunidad de conocer la cultura local\n"
        "\nPrecio: $60.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#87CEEB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="La Palma"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos Darien

def Herrera():
    ventana_herrera= tk.Toplevel()
    ventana_herrera.title("Herrera")
    ventana_herrera.geometry("600x400")

    title_label = tk.Label(ventana_herrera, text="Provincia: Herrera", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_herrera)
    frame.pack(pady=10)

    descripcionherrera =(
        "Herrera es una provincia panameña situada en el norte de la península de Azuero y su cabecera es la" 
        "ciudad de Chitré. Limita al norte con las provincias de Veraguas y Coclé, al sur con la provincia de" 
        "Los Santos, al este con el golfo de Parita y la provincia de Los Santos y al oeste con la provincia de" 
        "Veraguas concretamente con el distrito de Mariato. Tiene una extensión de 2340.7 km² y en 2008 contaba" 
        "con una población de 111 647 habitantes, población que se estimó en 107 911 habitantes en 2010.")
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
    menu_herrera.add_command(label="Pesé y sus destilerías de ron", command= PeseDestileriasRon)
    menu_herrera.add_command(label="Parita y su arquitectura colonial", command= ParitaHerrera)
    menu_herrera.add_command(label="Museo de Herrera en Chitré", command= MuseoHerreraChitre)
    menu_herrera.add_command(label="Las Tablas de Sarigua", command=LasTablasDeSarigua)
    
    lugaresHerrera.add_cascade(label="Provincia Herrera", menu=menu_herrera)
    
    boton_regresar = tk.Button(ventana_herrera, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_herrera.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos Herrera
def PeseDestileriasRon():
    ventana_PeseDestileriasRon = tk.Toplevel()
    ventana_PeseDestileriasRon.title("Pesé y sus Destilerías de Ron")
    ventana_PeseDestileriasRon.geometry("700x600")
    ventana_PeseDestileriasRon.configure(bg='#3CB371')

    main_frame = tk.Frame(ventana_PeseDestileriasRon, bg='#3CB371')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Pesé y sus Destilerías de Ron", font=("Arial", 20, "bold"), bg='#3CB371')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Herrera/PeseDestileriasRon.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#3CB371')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Pesé es famoso por su producción de ron. Los visitantes pueden recorrer las destilerías locales, "
        "conocer el proceso de fabricación del ron y degustar algunas de las mejores marcas nacionales. "
        "Es una experiencia cultural y sensorial para los interesados en las tradiciones panameñas."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Recorrido guiado por las destilerías locales\n"
        "- Explicación del proceso de fabricación del ron\n"
        "- Degustación de diferentes variedades de ron\n"
        "- Historia de la destilación en Panamá\n"
        "Precio: 30.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_PeseDestileriasRon, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Pesé y sus Destilerías de Ron"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_PeseDestileriasRon, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_PeseDestileriasRon.destroy)
    boton_volver.pack(side="left", padx=10) 
def MuseoHerreraChitre():
    ventana_MuseoHerreraChitre = tk.Toplevel()
    ventana_MuseoHerreraChitre.title("Museo de Herrera en Chitré")
    ventana_MuseoHerreraChitre.geometry("700x600")
    ventana_MuseoHerreraChitre.configure(bg='#3CB371')

    main_frame = tk.Frame(ventana_MuseoHerreraChitre, bg='#3CB371')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Museo de Herrera en Chitré", font=("Arial", 20, "bold"), bg='#3CB371')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Herrera/MuseoHerreraChitre.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#3CB371')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "El Museo de Herrera en Chitré alberga exposiciones sobre la historia y cultura de la región, "
        "incluyendo la historia de la colonización y las tradiciones indígenas. Es ideal para quienes desean "
        "profundizar en la historia de la península de Azuero."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
        "- Exposiciones sobre la historia de la región\n"
        "- Muestras de tradiciones indígenas y coloniales\n"
        "- Información sobre la colonización y eventos históricos\n"
        "- Recorridos guiados por las exhibiciones\n"
        "Precio: 5.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_MuseoHerreraChitre, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Museo de Herrera en Chitré"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_MuseoHerreraChitre, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_MuseoHerreraChitre.destroy)
    boton_volver.pack(side="left", padx=10)
def ParitaHerrera():
    ventana_Parita = tk.Toplevel()
    ventana_Parita.title("Parita y su arquitectura colonial")
    ventana_Parita.geometry("700x600")
    ventana_Parita.configure(bg='#3CB371')
    
    main_frame = tk.Frame(ventana_Parita, bg='#3CB371')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Parita y su arquitectura colonial", font=("Arial", 20, "bold"), bg='#3CB371')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/Herrera/Parita.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#3CB371')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "Parita, en Herrera, es famosa por su arquitectura colonial bien conservada. Los visitantes pueden pasear y disfrutar de un ambiente histórico relajado."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Paseo por calles con arquitectura colonial\n"
        "- Observación de casas antiguas bien conservadas\n"
        "- Explicación de la historia y cultura local\n"
        "- Interacción con guías locales\n"
        "\nPrecio: 60.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_Parita, bg='#3CB371')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parita y su arquitectura colonial"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_Parita.destroy)
    boton_volver.pack(side="left", padx=10)
def LasTablasDeSarigua():
    ventana = tk.Toplevel()
    ventana.title("Las Tablas de Sarigua")
    ventana.geometry("700x600")
    ventana.configure(bg='#3CB371')

    main_frame = tk.Frame(ventana, bg='#3CB371')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Las Tablas de Sarigua", font=("Arial", 20, "bold"), bg='#3CB371')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Herrera/LasTablasDeSarigua.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#3CB371')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "Las Tablas de Sarigua es una reserva arqueológica y natural en Herrera, "
        "con restos de antiguos asentamientos indígenas y oportunidades para el ecoturismo."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Exploración de restos de antiguos asentamientos indígenas\n"
        "- Observación de flora y fauna autóctona\n"
        "- Senderos en el parque arqueológico\n"
        "- Charlas sobre la importancia histórica del área\n"
        "\nPrecio: $35.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#3CB371')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Las Tablas de Sarigua"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos Herrera

def LosSantos():
    ventana_lossantos= tk.Toplevel()
    ventana_lossantos.title("Los Santos")
    ventana_lossantos.geometry("600x400")

    title_label = tk.Label(ventana_lossantos, text="Provincia: Los Santos", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_lossantos)
    frame.pack(pady=10)

    descripcionlossantos =(
        "Los Santos es una provincia panameña, situada al sureste de la península de Azuero. Las Tablas es su capital y" 
        "localidad más poblada. Está compuesta por los distritos de Los Santos, Guararé, Las Tablas, Macaracas, Pedasí," 
        "Pocrí y Tonosí. Con una superficie de 3 809,4 km² y una población de 95 540 habitantes, limita al sur y al este" 
        "con el océano Pacífico, al norte con el océano Pacífico y la provincia de Herrera, y al oeste con la provincia" 
        "de Veraguas, concretamente con el distrito de Mariato.")
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
    menu_losantos.add_command(label="Isla Iguana", command=IslaIguana)
    menu_losantos.add_command(label="Pedasí", command= Pedasi)
    menu_losantos.add_command(label="Playa Venao", command= PlayaVenao)
    menu_losantos.add_command(label="Museo de la Nacionalidad en Villa de Los Santos", command= MuseoNacionalidadLosSantos)
    
    lugaresLossantos.add_cascade(label="Provincia Los Santos", menu=menu_losantos)
    
    boton_regresar = tk.Button(ventana_lossantos, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_lossantos.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio lugares Turisticos de Los Santos
def IslaIguana():
    ventana_IslaIguana = tk.Toplevel()
    ventana_IslaIguana.title("Isla Iguana")
    ventana_IslaIguana.geometry("700x600")
    ventana_IslaIguana.configure(bg='#1E90FF')

    main_frame = tk.Frame(ventana_IslaIguana, bg='#1E90FF')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Isla Iguana", font=("Arial", 20, "bold"), bg='#1E90FF')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/LosSantos/IslaIguana.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#1E90FF')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_texto = (
        "Isla Iguana es una pequeña isla frente a la costa de Pedasí, famosa por su biodiversidad, especialmente "
        "por la gran población de iguanas. Es ideal para snorkel, observación de fauna marina, y disfrutar de playas "
        "de arena blanca y aguas cristalinas."
    )
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_texto = (
        "Incluye:\n"
    "- Snorkel y observación de vida marina\n"
    "- Paseo por playas de arena blanca\n"
    "- Observación de iguanas y otras especies\n"
    "- Senderos naturales en la isla\n"
        "\nPrecio: 40.00"
    )
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    boton_reservar = tk.Button(ventana_IslaIguana, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Isla Iguana"))
    boton_reservar.pack(side="left", padx=10, pady=20)
    
    boton_volver = tk.Button(ventana_IslaIguana, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_IslaIguana.destroy)
    boton_volver.pack(side="left", padx=10)  
def MuseoNacionalidadLosSantos():
    ventana_Museo = tk.Toplevel()
    ventana_Museo.title("Museo de la Nacionalidad en Villa de Los Santos")
    ventana_Museo.geometry("700x600")
    ventana_Museo.configure(bg='#1E90FF')
    
    main_frame = tk.Frame(ventana_Museo, bg='#1E90FF')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Museo de la Nacionalidad en Villa de Los Santos", font=("Arial", 20, "bold"), bg='#1E90FF')
    titulo.pack(pady=10)

    try:
        image_path = "imagenes/LosSantos/MuseoNacionalidad.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#1E90FF')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    descripcion_texto = (
        "El Museo de la Nacionalidad en Villa de Los Santos ofrece una visión de la historia y cultura de Panamá, ideal para quienes desean explorar el patrimonio del país."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    detalles_texto = (
        "Incluye:\n"
        "- Exposiciones sobre la independencia y cultura panameña\n"
        "- Exhibición de artefactos históricos\n"
        "- Información sobre la historia de la región de Azuero\n"
        "- Visitas guiadas por el museo\n"
        "\nPrecio: 80.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    botones_frame = tk.Frame(ventana_Museo, bg='#1E90FF')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Museo de la Nacionalidad en Villa"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_Museo.destroy)
    boton_volver.pack(side="left", padx=10)
def PlayaVenao():
    ventana = tk.Toplevel()
    ventana.title("Playa Venao")
    ventana.geometry("700x600")
    ventana.configure(bg='#1E90FF')

    main_frame = tk.Frame(ventana, bg='#1E90FF')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Playa Venao", font=("Arial", 20, "bold"), bg='#1E90FF')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/LosSantos/PlayaVenao.jpg"
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#1E90FF')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "Playa ideal para el surf y disfrutar de atardeceres. Cuenta con áreas para camping "
        "y restaurantes, ofreciendo un ambiente relajado y natural."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Olas ideales para surf y deportes acuáticos\n"
        "- Áreas de camping y restaurantes\n"
        "- Ambiente relajado y natural\n"
        "- Espacios para disfrutar de atardeceres\n"
        "\nPrecio: $50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#1E90FF')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Playa Venao"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
def Pedasi():
    ventana = tk.Toplevel()
    ventana.title("Pedasí")
    ventana.geometry("700x600")
    ventana.configure(bg='#1E90FF')

    main_frame = tk.Frame(ventana, bg='#1E90FF')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    titulo = tk.Label(main_frame, text="Pedasí", font=("Arial", 20, "bold"), bg='#1E90FF')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/LosSantos/Pedasi.jpg"  # Ruta a la imagen de Pedasí
        image = Image.open(image_path)
        image = image.resize((250, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#1E90FF')
        image_label.image = photo
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")
    descripcion_texto = (
        "Pedasí es un pintoresco pueblo costero en la península de Azuero, conocido por su arquitectura "
        "colonial y la tranquilidad de sus playas. Los turistas pueden disfrutar de la vida local, "
        "participar en festividades tradicionales y explorar los alrededores, con playas ideales "
        "para deportes acuáticos y contacto directo con la naturaleza."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Detalles de actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido por arquitectura colonial\n"
        "- Participación en festividades tradicionales\n"
        "- Exploración de playas cercanas\n"
        "- Actividades de cultura local\n"
        "\nPrecio: $55.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana, bg='#1E90FF')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Pedasí"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin lugares Turisticos de Los Santos

def Panama():
    ventana_panama= tk.Toplevel()
    ventana_panama.title("Panama")
    ventana_panama.geometry("600x400")

    title_label = tk.Label(ventana_panama, text="Provincia: Panama", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_panama)
    frame.pack(pady=10)

    descripcionpanama =(
        "Panamá es una provincia y la capital del país, ubicada en la región central. Tiene una extensión de 11,289 km²" 
        "y una población de aproximadamente 1.8 millones de habitantes (2018). Limita al norte con Colón, al sur con el" 
        "océano Pacífico, al este con Darién y al oeste con Panamá Oeste.")
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
    menu_panama.add_command(label="Canal de Panamá", command= CanalPanama)
    menu_panama.add_command(label="Casco Viejo", command= CascoPanama)
    menu_panama.add_command(label="Cerro Ancón", command= AnconPanama )
    menu_panama.add_command(label="Parque Natural Metropolitano", command= MetropolitanoPanama)
    
    lugaresPanama.add_cascade(label="Lugares Turistico de Panama que deberias visitar", menu=menu_panama)
    
    boton_regresar = tk.Button(ventana_panama, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_panama.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio lugaes Turisticos de Panama   
def CanalPanama():
    ventana_canal = tk.Toplevel()
    ventana_canal.title("Canal de Panamá")
    ventana_canal.geometry("700x600")
    ventana_canal.configure(bg='#FF7F50')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_canal, bg='#FF7F50')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Canal de Panamá", font=("Arial", 20, "bold"), bg='#FF7F50')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Panama/Canal.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FF7F50')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "El Canal de Panamá es una de las maravillas de la ingeniería moderna y conecta el océano Atlántico" 
        "con el Pacífico. Los visitantes pueden recorrer los centros de observación y conocer la historia y" 
        "el funcionamiento de las esclusas. Además, ofrece la oportunidad de ver los barcos atravesando el canal," 
        "una experiencia educativa y cultural única."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Entrada al centro de observación\n"
        "- Tour guiado sobre la historia y el funcionamiento del canal\n"
        "- Observación de barcos en las esclusas\n\n"
        "Precio: $50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_canal, bg='#FF7F50')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Canal de Panamá"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_canal.destroy)
    boton_volver.pack(side="left", padx=10)
def CascoPanama():
    ventana_casco = tk.Toplevel()
    ventana_casco.title("Casco Viejo")
    ventana_casco.geometry("700x600")
    ventana_casco.configure(bg='#FF7F50')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_casco, bg='#FF7F50')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Casco Viejo", font=("Arial", 20, "bold"), bg='#FF7F50')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Panama/Casco.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FF7F50')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Casco Viejo es el centro histórico de la Ciudad de Panamá, conocido por su arquitectura colonial" 
        "y sus plazas históricas. Los turistas pueden pasear por las calles empedradas, visitar museos y" 
        "disfrutar de la gastronomía local. Este área es Patrimonio de la Humanidad de la UNESCO y refleja" 
        "la historia y cultura de Panamá."

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido por las calles históricas\n"
        "- Visita a museos locales\n"
        "- Degustación de platillos típicos\n\n"
        "Precio: $40.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_casco, bg='#FF7F50')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Casco Viejo"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_casco.destroy)
    boton_volver.pack(side="left", padx=10)
def AnconPanama():
    ventana_ancon = tk.Toplevel()
    ventana_ancon.title("Cerro Ancón")
    ventana_ancon.geometry("700x600")
    ventana_ancon.configure(bg='#FF7F50')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_ancon, bg='#FF7F50')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cerro Ancón", font=("Arial", 20, "bold"), bg='#FF7F50')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Panama/Ancon.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FF7F50')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "El cerro Ancón es una elevación de 199 m situada en la ciudad de Panamá y forma parte del corregimiento" 
        "de Ancón. Su nombre proviene del «Sitio del Ancón»,nombre dado en referencia al ancón que se formaba en" 
        "la costa del océano Pacífico. Este cerro estuvo bajo la jurisdicción de los Estados Unidos, como parte de" 
        "la Zona del Canal de Panamá, durante gran parte del siglo XX. A pesar de que se encuentra dentro de la Ciudad" 
        "de Panamá, no es una zona urbanizada."

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Caminata guiada al cerro\n"
        "- Observación de la fauna y flora\n"
        "- Vistas panorámicas\n\n"
        "Precio: $30.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_ancon, bg='#FF7F50')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cerro Ancón"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_ancon.destroy)
    boton_volver.pack(side="left", padx=10)
def MetropolitanoPanama():
    ventana_metropolitano = tk.Toplevel()
    ventana_metropolitano.title("Parque Natural Metropolitano")
    ventana_metropolitano.geometry("700x600")
    ventana_metropolitano.configure(bg='#FF7F50')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_metropolitano, bg='#FF7F50')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Parque Natural Metropolitano", font=("Arial", 20, "bold"), bg='#FF7F50')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Panama/Metropolitano.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FF7F50')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Este parque es una reserva natural ubicada en la Ciudad de Panamá que ofrece senderos para caminatas" 
        "y áreas para la observación de aves y fauna local. Es un espacio verde ideal para quienes deseen desconectar" 
        "de la ciudad y disfrutar de la naturaleza."

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Entrada al parque\n"
        "- Caminata guiada por los senderos principales\n"
        "- Observación de fauna y flora (posibilidad de ver monos, perezosos y aves exóticas)\n"
        "- Acceso a áreas de descanso y miradores\n\n"
        "Precio: $25.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_metropolitano, bg='#FF7F50')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parque Natural Metropolitano"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_metropolitano.destroy)
    boton_volver.pack(side="left", padx=10)    
#Fin Lugares Turisticos de Panama

def Veraguas():
    ventana_veraguas= tk.Toplevel()
    ventana_veraguas.title("Veraguas")
    ventana_veraguas.geometry("600x400")

    title_label = tk.Label(ventana_veraguas, text="Provincia: Veraguas", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_veraguas)
    frame.pack(pady=10)

    descripcionveraguas =(
        "Veraguas es una de las diez provincias de Panamá. Su capital es la ciudad de Santiago de Veraguas. Tiene una" 
        "superficie de 10 629 km², y un área de 10.587,6 km² y en el año 2022 tenía una población estimada de 248,000" 
        "Limita al norte con el mar Caribe, al sur con el océano Pacífico, al este con las provincias de Colón, Coclé," 
        "Herrera, Los Santos y al oeste con la provincia de Chiriquí y la Comarca Ngäbe-Buglé. Es la única provincia de" 
        "Panamá que tiene costas en los océanos Atlántico y Pacífico, condición que a nivel de subdivisión nacional solo" 
        "comparte con el departamento del Chocó en Colombia en todo el continente americano.")
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
    menu_veraguas.add_command(label="Isla Coiba", command= CoibaVeraguas)
    menu_veraguas.add_command(label="Santa Catalina", command= CatalinaVeraguas )
    menu_veraguas.add_command(label="Reserva Forestal La Yeguada", command= LaYeguadaVeraguas )
    menu_veraguas.add_command(label="Parque Nacional Cerro Hoya", command= HoyaVeraguas)
    
    lugaresVeraguas.add_cascade(label="Lugares Turistico de Veraguas que deberias visitar", menu=menu_veraguas)
    
    boton_regresar = tk.Button(ventana_veraguas, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_veraguas.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Veraguas
def CoibaVeraguas():
    ventana_coiba = tk.Toplevel()
    ventana_coiba.title("Isla Coiba")
    ventana_coiba.geometry("700x600")
    ventana_coiba.configure(bg='#FAFAD2')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_coiba, bg='#FAFAD2')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Isla Coiba", font=("Arial", 20, "bold"), bg='#FAFAD2')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Veraguas/Coiba.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FAFAD2')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Isla Coiba es un parque nacional ubicado en el océano Pacífico, conocido por su biodiversidad" 
        "y paisajes naturales. Declarada Patrimonio de la Humanidad por la UNESCO, esta isla es un paraíso" 
        "para los ecoturistas, que pueden disfrutar de actividades como el snorkel, el buceo y la observación" 
        "de fauna marina, incluyendo tiburones, tortugas y peces tropicales."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Transporte en bote a la isla\n"
        "- Equipo de snorkel y guía especializado\n"
        "- Almuerzo y refrigerios\n"
        "- Entrada al parque nacional\n"
        "- Posibilidad de avistamiento de fauna marina (tiburones, tortugas, peces tropicales)\n\n"
        "Precio: $150.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_coiba, bg='#FAFAD2')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Isla Coiba"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_coiba.destroy)
    boton_volver.pack(side="left", padx=10)
def CatalinaVeraguas():
    ventana_catalina = tk.Toplevel()
    ventana_catalina.title("Santa Catalina")
    ventana_catalina.geometry("700x600")
    ventana_catalina.configure(bg='#FAFAD2')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_catalina, bg='#FAFAD2')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Santa Catalina", font=("Arial", 20, "bold"), bg='#FAFAD2')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Veraguas/Catalina.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FAFAD2')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Santa Catalina es un pequeño pueblo costero famoso entre los surfers y turistas que buscan escapar" 
        "de las multitudes. Sus playas ofrecen olas de calidad para la práctica del surf, además de ser un" 
        "excelente punto de partida para visitar la Isla Coiba. El ambiente tranquilo, combinado con la oferta"
        "de actividades acuáticas y senderismo, hace de Santa Catalina un destino ideal para los amantes de la" 
        "naturaleza y los deportes acuáticos."

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Clases de surf (opcional)\n"
        "- Equipo de surf disponible para alquilar\n"
        "- Excursiones de snorkel y buceo\n"
        "- Transporte a la Isla Coiba (opcional)\n"
        "- Guía especializado en actividades acuáticas\n\n"
        "Precio: $120.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_catalina, bg='#FAFAD2')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Santa Catalina"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_catalina.destroy)
    boton_volver.pack(side="left", padx=10)
def LaYeguadaVeraguas():
    ventana_yeguada = tk.Toplevel()
    ventana_yeguada.title("Reserva Forestal La Yeguada")
    ventana_yeguada.geometry("700x600")
    ventana_yeguada.configure(bg='#FAFAD2')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_yeguada, bg='#FAFAD2')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Reserva Forestal La Yeguada", font=("Arial", 20, "bold"), bg='#FAFAD2')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Veraguas/LaYeguada.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FAFAD2')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "La Reserva Forestal La Yeguada es una área natural protegida en Veraguas, ideal para los excursionistas" 
        "y los amantes de la naturaleza. En este parque, los visitantes pueden disfrutar de caminatas entre bosques"
        "tropicales, explorar senderos y observar la vida silvestre, como aves, monos y mamíferos. La reserva es también" 
        "un lugar excelente para el camping y la fotografía de paisajes."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Caminatas guiadas por la reserva\n"
        "- Observación de vida silvestre\n"
        "- Oportunidades para fotografía de naturaleza\n"
        "- Espacios designados para camping\n"
        "- Guías locales especializados\n\n"
        "Precio: $50.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_yeguada, bg='#FAFAD2')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Reserva Forestal La Yeguada"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_yeguada.destroy)
    boton_volver.pack(side="left", padx=10)
def HoyaVeraguas():
    ventana_hoya = tk.Toplevel()
    ventana_hoya.title("Parque Nacional Cerro Hoya")
    ventana_hoya.geometry("700x600")
    ventana_hoya.configure(bg='#FAFAD2')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_hoya, bg='#FAFAD2')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Parque Nacional Cerro Hoya", font=("Arial", 20, "bold"), bg='#FAFAD2')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/Veraguas/CerroHoya.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#FAFAD2')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "El Parque Nacional Cerro Hoya es un vasto parque de montañas y bosques tropicales que alberga una" 
        "rica biodiversidad. Los visitantes pueden disfrutar de excursiones para observar fauna nativa, como" 
        "jaguares y aves endémicas, así como explorar sus senderos y disfrutar de vistas panorámicas desde los" 
        "puntos más altos del parque. Es un excelente destino para los amantes del ecoturismo y el senderismo."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Excursiones guiadas\n"
        "- Observación de fauna y flora nativas\n"
        "- Senderismo por rutas escénicas\n"
        "- Guía local con conocimiento ecológico\n\n"
        "Precio: $70.00 "
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_hoya, bg='#FAFAD2')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Parque Nacional Cerro Hoya"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_hoya.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos de Veraguas

def PanamaOeste():
    ventana_panoeste= tk.Toplevel()
    ventana_panoeste.title("Panama Oeste")
    ventana_panoeste.geometry("600x400")

    title_label = tk.Label(ventana_panoeste, text="Provincia: Panama Oeste", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_panoeste)
    frame.pack(pady=10)

    descripcionpanoeste =(
        "Panamá Oeste es una de las diez provincias de Panamá, creada el 1.º de enero de 2014 a partir de territorios" 
        "segregados de la provincia de Panamá ubicados al oeste del canal de Panamá. Está conformado por 5 distritos:" 
        "Arraiján, Capira, Chame, La Chorrera y San Carlos. Su capital es La Chorrera.")
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
    menu_panoeste.add_command(label="Centro de Visitantes de Miraflores", command= MirafloresPanoeste)
    menu_panoeste.add_command(label="Playa Punta Chame", command= PuntaChamePanoeste)
    menu_panoeste.add_command(label="Cascada El Chorro", command= ElChorroPanoeste)
    menu_panoeste.add_command(label="Playa Malibú", command= MalibuPanoeste )
    
    lugarespanoeste.add_cascade(label="Lugares Turistico de Panama Oeste que deberias visitar", menu=menu_panoeste)
    
    boton_regresar = tk.Button(ventana_panoeste, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_panoeste.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Panama Oeste
def MirafloresPanoeste():
    ventana_miraflores = tk.Toplevel()
    ventana_miraflores.title("Centro de Visitantes de Miraflores")
    ventana_miraflores.geometry("700x600")
    ventana_miraflores.configure(bg='#98FB98')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_miraflores, bg='#98FB98')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Centro de Visitantes de Miraflores", font=("Arial", 20, "bold"), bg='#98FB98')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/PanamaOeste/Miraflores.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#98FB98')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "El Centro de Visitantes de Miraflores es un atractivo turístico único en la Ciudad de Panamá," 
        "ideal para quienes desean conocer el funcionamiento del famoso Canal de Panamá. Desde sus" 
        "plataformas de observación, los visitantes pueden ver de cerca las enormes embarcaciones" 
        "atravesando las esclusas de Miraflores.Además, el centro cuenta con un museo interactivo" 
        "que muestra la historia, ingeniería y biodiversidad de la región" 
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Acceso a las plataformas de observación\n"
        "- Entrada al museo interactivo\n"
        "- Guía turístico\n\n"
        "Precio: $150.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_miraflores, bg='#98FB98')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Centro de Visitantes de Miraflores"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_miraflores.destroy)
    boton_volver.pack(side="left", padx=10)
def PuntaChamePanoeste():
    ventana_puntachame = tk.Toplevel()
    ventana_puntachame.title("Playa Punta Chame")
    ventana_puntachame.geometry("700x600")
    ventana_puntachame.configure(bg='#98FB98')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_puntachame, bg='#98FB98')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Playa Punta Chame", font=("Arial", 20, "bold"), bg='#98FB98')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/PanamaOeste/PuntaChame.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#98FB98')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Punta Chame es una hermosa playa de la provincia de Panamá Oeste, popular entre los turistas por su" 
        "tranquilidad y belleza natural. Es ideal para actividades como el kitesurf, paseos en bote y observación" 
        "de aves. Con su extensa franja de arena y aguas claras, Punta Chame también ofrece la posibilidad de relajarse" 
        "y disfrutar de los atardeceres sobre el océano Pacífico."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Kitesurf y deportes acuáticos\n"
        "- Paseos en bote y observación de aves\n"
        "- Extensa playa de arena para relajarse\n"
        "- Atardeceres espectaculares sobre el océano\n"
        "\nPrecio: 25.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_puntachame, bg='#98FB98')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Playa Punta Chame"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_puntachame.destroy)
    boton_volver.pack(side="left", padx=10)
def ElChorroPanoeste():
    ventana_elchorro = tk.Toplevel()
    ventana_elchorro.title("Cascada El Chorro")
    ventana_elchorro.geometry("700x600")
    ventana_elchorro.configure(bg='#98FB98')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_elchorro, bg='#98FB98')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cascada El Chorro", font=("Arial", 20, "bold"), bg='#98FB98')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/PanamaOeste/ElChorro.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#98FB98')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "La Cascada El Chorro, situada cerca de La Chorrera, es una impresionante caída de agua que atrae tanto" 
        "a los aventureros como a quienes buscan relajarse en la naturaleza. Los visitantes pueden hacer una" 
        "caminata hasta la cascada y disfrutar de un refrescante baño en sus aguas. Este lugar es ideal para" 
        "quienes buscan explorar la belleza natural de la región y realizar un picnic en su entorno tranquilo."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Caminata hasta la cascada\n"
        "- Oportunidad de nadar en aguas frescas\n"
        "- Espacios para picnic en un ambiente natural\n"
        "- Observación de la flora y fauna locales\n"
        "\nPrecio: 18.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_elchorro, bg='#98FB98')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cascada El Chorro"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_elchorro.destroy)
    boton_volver.pack(side="left", padx=10)
def MalibuPanoeste():
    ventana_malibu = tk.Toplevel()
    ventana_malibu.title("Playa Malibú")
    ventana_malibu.geometry("700x600")
    ventana_malibu.configure(bg='#98FB98')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_malibu, bg='#98FB98')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Playa Malibú", font=("Arial", 20, "bold"), bg='#98FB98')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/PanamaOeste/PlayaMalibu.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#98FB98')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción 
    descripcion_texto = (
        "Playa Malibú es una playa aislada en la provincia de Panamá Oeste, conocida por sus aguas tranquilas" 
        "y su ambiente relajante. Es ideal para nadar, hacer snorkel y disfrutar de la tranquilidad. Los turistas" 
        "pueden pasar el día en sus arenas doradas, explorando sus alrededores o simplemente relajándose en un entorno" 
        "pacífico lejos de las multitudes."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Espacio para nadar y hacer snorkel\n"
        "- Arena dorada y aguas tranquilas\n"
        "- Exploración de áreas naturales alrededor\n"
        "- Ambiente pacífico para relajarse\n"
        "\nPrecio: 20.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_malibu, bg='#98FB98')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Playa Malibú"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_malibu.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos de Panama Oeste
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

    descripcionembera =(
        "Emberá-Wounaan es una comarca indígena de Panamá. Fue creada en 1983 a partir de dos enclaves ubicados" 
        "en la provincia de Darién, específicamente de los distritos de Chepigana y Pinogana. Su capital es Unión" 
        "Chocó. Su extensión abarca 4383,5 km² y posee una población de 9544 habitantes (2010),la mayoría de estos" 
        "pertenecen a las etnias emberá y wounaan, distribuidas en 40 comunidades.")
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
    menu_embera.add_command(label="Comunidad de Lajas Blancas", command= LajasBlancasEmbera)
    menu_embera.add_command(label="Distrito de Cemaco", command= CemacoEmbera)
    menu_embera.add_command(label="Cascada de Tres Brazos", command= TresBrazosEmbera)
    menu_embera.add_command(label="Comunidad de Arimae", command= ArimaeEmbera)
    
    lugaresEmbera.add_cascade(label="Lugares Turistico de Embera Wounaan que deberias visitar", menu=menu_embera)
    
    boton_regresar = tk.Button(ventana_embera, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_embera.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Embera Wounaan
def LajasBlancasEmbera():
    ventana_lajas = tk.Toplevel()
    ventana_lajas.title("Comunidad de Lajas Blancas")
    ventana_lajas.geometry("700x600")
    ventana_lajas.configure(bg='#9932CC')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_lajas, bg='#9932CC')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Comunidad de Lajas Blancas", font=("Arial", 20, "bold"), bg='#9932CC')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/EmberaWounaan/LajasBlancas.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9932CC')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "También en la provincia de Darién, esta comunidad es accesible a través del río Tuira. En Lajas Blancas," 
        "los visitantes pueden explorar la cultura Emberá en un entorno rodeado de selva y ríos, ideal para paseos" 
        "en canoa, caminatas por senderos naturales y observación de flora y fauna."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Paseos en canoa por el río Tuira\n"
        "- Caminatas por senderos naturales\n"
        "- Observación de flora y fauna local\n"
        "- Interacción con la cultura Emberá\n"
        "\nPrecio: $15.00"

    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_lajas, bg='#9932CC')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Comunidad de Lajas Blancas"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_lajas.destroy)
    boton_volver.pack(side="left", padx=10)     
def CemacoEmbera():
    ventana_cemaco = tk.Toplevel()
    ventana_cemaco.title("Distrito de Cemaco")
    ventana_cemaco.geometry("700x600")
    ventana_cemaco.configure(bg='#9932CC')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_cemaco, bg='#9932CC')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Distrito de Cemaco", font=("Arial", 20, "bold"), bg='#9932CC')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/EmberaWounaan/Cemaco.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9932CC')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Es el distrito más grande de la comarca y un lugar excelente para experimentar la cultura tradicional" 
        "Emberá y Wounaan. Aquí se realizan ferias culturales y eventos donde los turistas pueden ver danzas típicas," 
        "comprar artesanías y aprender sobre las costumbres de estas comunidades."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Participación en ferias culturales y eventos\n"
        "- Exhibición de danzas típicas\n"
        "- Venta de artesanías tradicionales\n"
        "- Charlas sobre costumbres locales\n"
        "\nPrecio: $10.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_cemaco, bg='#9932CC')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Distrito de Cemaco"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_cemaco.destroy)
    boton_volver.pack(side="left", padx=10)
def TresBrazosEmbera():
    ventana_tresbrazos = tk.Toplevel()
    ventana_tresbrazos.title("Cascada de Tres Brazos")
    ventana_tresbrazos.geometry("700x600")
    ventana_tresbrazos.configure(bg='#9932CC')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_tresbrazos, bg='#9932CC')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cascada de Tres Brazos", font=("Arial", 20, "bold"), bg='#9932CC')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/EmberaWounaan/TresBrazos.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9932CC')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Esta es una hermosa cascada ubicada en el territorio Emberá-Wounaan, ideal para hacer senderismo," 
        "nadar y disfrutar del paisaje natural. Muchas excursiones desde las comunidades cercanas incluyen" 
        "visitas a estas cascadas, proporcionando una experiencia refrescante en medio de la naturaleza."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Senderismo hasta la cascada\n"
        "- Oportunidad de nadar en el entorno natural\n"
        "- Observación de la flora y fauna circundante\n"
        "- Excursión guiada por miembros de la comunidad\n"
        "Precio: $20.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_tresbrazos, bg='#9932CC')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cascada de Tres Brazos"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_tresbrazos.destroy)
    boton_volver.pack(side="left", padx=10)
def ArimaeEmbera():
    ventana_arimae = tk.Toplevel()
    ventana_arimae.title("Comunidad de Arimae")
    ventana_arimae.geometry("700x600")
    ventana_arimae.configure(bg='#9932CC')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_arimae, bg='#9932CC')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Comunidad de Arimae", font=("Arial", 20, "bold"), bg='#9932CC')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/EmberaWounaan/Arimae.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9932CC')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Ubicada en la región oriental de la Comarca Emberá-Wounaan, en la provincia de Darién, esta comunidad" 
        "es conocida por su fuerte apego a las tradiciones. Los visitantes pueden aprender sobre la medicina natural," 
        "las técnicas de caza y pesca tradicionales, así como la artesanía elaborada."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Introducción a la medicina natural\n"
        "- Técnicas de caza y pesca tradicionales\n"
        "- Talleres de elaboración de artesanías\n"
        "- Convivencia con la comunidad Emberá\n"
        "\nPrecio: $18.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_arimae, bg='#9932CC')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Comunidad de Arimae"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_arimae.destroy)
    boton_volver.pack(side="left", padx=10)
#FinLugares Turisticos de Embera Wounaan
  
def GunaYala():
    ventana_guna= tk.Toplevel()
    ventana_guna.title("Guna Yala")
    ventana_guna.geometry("600x400")

    title_label = tk.Label(ventana_guna, text="Comarca: Guna Yala", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_guna)
    frame.pack(pady=10)

    descripcionguna =(
        "Guna Yala es una comarca indígena en Panamá, habitada por la etnia guna. Antiguamente la comarca" 
        "se llamó San Blas, hasta 1998 y Kuna Yala, hasta 2010. Los locales la conocen con varios nombres" 
        "como: Dulenega, Yarsuid, Duleyala. Su capital es Gairgirgordub. Limita al norte con el mar"
        "Caribe, al sur con la provincia de Darién y la comarca Emberá Wounnan, al este con Colombia y al" 
        "oeste con la provincia de Colón.")
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
    menu_guna.add_command(label="Archipiélago de San Blas", command= SanBlasGuna)
    menu_guna.add_command(label="Montaña Sagrado de Ibedi", command= IbediGuna)
    menu_guna.add_command(label="Río Diablo",command= RioDiabloGuna )
    menu_guna.add_command(label="Isla Perro Chico", command= IslaPerroGuna )
    
    lugaresGuna.add_cascade(label="Lugares Turistico de Guna Yala que deberias visitar", menu=menu_guna)
    
    boton_regresar = tk.Button(ventana_guna, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_guna.destroy)
    boton_regresar.place(x=450, y=335)
#Inicio Lugares Turisticos de Guna Yala
def SanBlasGuna():  
    ventana_sanblas = tk.Toplevel()
    ventana_sanblas.title("Archipiélago de San Blas")
    ventana_sanblas.geometry("700x600")
    ventana_sanblas.configure(bg='#F08080')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_sanblas, bg='#F08080')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Archipiélago de San Blas", font=("Arial", 20, "bold"), bg='#F08080')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/GunaYala/SanBlas.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#F08080')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Este es el principal atractivo turístico de Guna Yala, ya que está compuesto por un archipiélago de más" 
        "de 360 islas y cayos, de los cuales solo unos pocos están habitados. San Blas es conocido por sus aguas" 
        "cristalinas, playas de arena blanca, y su ambiente tranquilo y natural. Los turistas pueden practicar snorkel," 
        "buceo, y explorar la vida marina en este paraíso."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Snorkel y buceo en aguas cristalinas\n"
        "- Recorrido por playas de arena blanca\n"
        "- Observación de vida marina\n"
        "- Alojamiento en cabañas tradicionales\n"
        "\nPrecio: $30.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_sanblas, bg='#F08080')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Archipiélago de San Blas"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_sanblas.destroy)
    boton_volver.pack(side="left", padx=10) 
def IbediGuna():
    ventana_ibedi = tk.Toplevel()
    ventana_ibedi.title("Montaña Sagrado de Ibedi")
    ventana_ibedi.geometry("700x600")
    ventana_ibedi.configure(bg='#F08080')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_ibedi, bg='#F08080')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Montaña Sagrado de Ibedi", font=("Arial", 20, "bold"), bg='#F08080')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/GunaYala/Ibedi.jpeg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#F08080')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Considerada un sitio sagrado para los gunas, esta montaña tiene gran valor cultural y espiritual." 
        "Los visitantes pueden hacer senderismo con guías locales, aprender sobre las leyendas y tradiciones" 
        "espirituales de la comunidad y disfrutar de vistas panorámicas de la comarca"

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Senderismo guiado con explicación cultural\n"
        "- Narración de leyendas y tradiciones\n"
        "- Vistas panorámicas de la comarca\n"
        "- Conexión con el patrimonio espiritual de los gunas\n"
        "\nPrecio: $25.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_ibedi, bg='#F08080')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Montaña Sagrado de Ibedi"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_ibedi.destroy)
    boton_volver.pack(side="left", padx=10)    
def RioDiabloGuna():
    ventana_riodiablo = tk.Toplevel()
    ventana_riodiablo.title("Río Diablo")
    ventana_riodiablo.geometry("700x600")
    ventana_riodiablo.configure(bg='#F08080')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_riodiablo, bg='#F08080')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Río Diablo", font=("Arial", 20, "bold"), bg='#F08080')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/GunaYala/RioDiablo.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#F08080')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Este río es importante para la vida diaria de las comunidades gunas y es un excelente sitio para explorar" 
        "el paisaje natural de la región. Los visitantes pueden realizar caminatas en los alrededores, disfrutar de" 
        "baños refrescantes en el río y observar la fauna y flora de la selva circundante."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Caminatas por el entorno del río\n"
        "- Oportunidad de nadar en el río\n"
        "- Observación de flora y fauna local\n"
        "- Relato de historias sobre la región\n"
        "\nPrecio: $15.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_riodiablo, bg='#F08080')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Río Diablo"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_riodiablo.destroy)
    boton_volver.pack(side="left", padx=10)   
    
def IslaPerroGuna():
    ventana_perro = tk.Toplevel()
    ventana_perro.title("Isla Perro Chico")
    ventana_perro.geometry("700x600")
    ventana_perro.configure(bg='#F08080')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_perro, bg='#F08080')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Isla Perro Chico", font=("Arial", 20, "bold"), bg='#F08080')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/GunaYala/PerroChico.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#F08080')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Famosa por su arrecife de coral y un barco hundido que se ha convertido en una atracción para quienes disfrutan" 
        "del snorkel. La isla cuenta con cabañas y espacios para acampar, y es un lugar ideal para relajarse y disfrutar" 
        "de la naturaleza."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
    "- Snorkel en el arrecife de coral\n"
    "- Exploración de un barco hundido\n"
    "- Alojamiento en cabañas y espacios de acampada\n"
    "- Actividades recreativas en la playa\n"
    "\nPrecio: $35.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_perro, bg='#F08080')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Isla Perro Chico"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_perro.destroy)
    boton_volver.pack(side="left", padx=10) 
#Fin Lugares Turisticos de Guna Yala

def NgabeBugle():
    ventana_ngabe= tk.Toplevel()
    ventana_ngabe.title("Ngabe-Bugle")
    ventana_ngabe.geometry("600x400")

    title_label = tk.Label(ventana_ngabe, text="Comarca: Ngabe-Bugle", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    frame = tk.Frame(ventana_ngabe)
    frame.pack(pady=10)

    descripcionngabe =("Esta comarca fue creada en 1997 a partir del territorio de Bocas del Toro, Chiriquí y Veraguas." 
    "Su capital es Llano Tugrí (o Buabïti). La comarca está habitada por las etnias indígenas ngäbe y buglé, así como" 
    "campesinos, y habitan en ella 154.355 personas (según el censo del 2010), y su área es de 6968 km².")
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
    menu_ngabe.add_command(label="Cascada La Tulivieja", command= CascadaTuliviejaNgabe)
    menu_ngabe.add_command(label="Cerro Peña Blanca", command= PenaBlancaNgabe)
    menu_ngabe.add_command(label="Cerro Colorado", command= CerroColoradoNgabe)
    menu_ngabe.add_command(label="Distrito de Munä", command= Muna)
    
    lugaresNgabe.add_cascade(label="Lugares Turistico de Ngabe Bugle que deberias visitar", menu=menu_ngabe)
    
    boton_regresar = tk.Button(ventana_ngabe, text="Regresar", width=15, font=("Arial", 12), bg="white", command=ventana_ngabe.destroy)
    boton_regresar.place(x=450, y=335)
    
#Inicio Lugares Turisticos de Ngabe Bugle
def CascadaTuliviejaNgabe():
    ventana_tulivieja = tk.Toplevel()
    ventana_tulivieja.title("Cascada La Tulivieja")
    ventana_tulivieja.geometry("700x600")
    ventana_tulivieja.configure(bg='#9370DB')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_tulivieja, bg='#9370DB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cascada La Tulivieja", font=("Arial", 20, "bold"), bg='#9370DB')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/NgabeBugle/CascadaTulivieja.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9370DB')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Este salto se encuentra ubicado en la comunidad de Soloy dentro de la comarca Ngäbe Buglé."
        "Esta misteriosa cascada se forma de las unión de las quebradas Las Lajas y Magdalena. Según"
        "los originarios de la región, éste es un sitio legendario, el cual durante muchos años se"
        "utilizó para practicar ceremonias y también para efectuar castigos a jóvenes indígenas por actos de desobediencia."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Recorrido hasta la cascada en la comunidad de Soloy\n"
        "- Narración de leyendas sobre el sitio\n"
        "- Oportunidad para nadar en las pozas naturales\n"
        "- Fotografías en un sitio legendario\n"
        "\nPrecio: $12.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_tulivieja, bg='#9370DB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cascada La Tulivieja"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_tulivieja.destroy)
    boton_volver.pack(side="left", padx=10)
    
def PenaBlancaNgabe():
    ventana_penablaca = tk.Toplevel()
    ventana_penablaca.title("Cerro Peña Blanca")
    ventana_penablaca.geometry("700x600")
    ventana_penablaca.configure(bg='#9370DB')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_penablaca, bg='#9370DB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cerro Peña Blanca", font=("Arial", 20, "bold"), bg='#9370DB')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/NgabeBugle/PenaBlanca.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9370DB')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "El cerro de Peña Blanca, que se presenta como la mas emblemática atracción del distrito Munä." 
        "Peña Blanca es un cerro que invita a propios y extranjeros a una aventura extrema y rodeado de" 
        "naturaleza; rodeado rocas que permiten realizar actividades extremas como la escalada y la caminata."
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Escalada y caminata en el cerro\n"
        "- Paisajes naturales rodeados de rocas\n"
        "- Experiencias de aventura extrema\n"
        "- Guías locales para actividades seguras\n"
        "\nPrecio: $25.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_penablaca, bg='#9370DB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cerro Peña Blanca"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_penablaca.destroy)
    boton_volver.pack(side="left", padx=10)    
    
def CerroColoradoNgabe():
    ventana_colorado = tk.Toplevel()
    ventana_colorado.title("Cerro Colorado")
    ventana_colorado.geometry("700x600")
    ventana_colorado.configure(bg='#9370DB')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_colorado, bg='#9370DB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Cerro Colorado", font=("Arial", 20, "bold"), bg='#9370DB')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/NgabeBugle/CerroColorado.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9370DB')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Cerro Colorado es la principal atracción turística que se encuentra al Norte del distrito Nole Duima,"
        "donde se encuentra el segundo yacimiento de cobre más grande del planeta y alberga las ruinas de los" 
        "campamentos construidos en décadas pasadas por los franceses que explotaron la mina. "
    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Visita al yacimiento de cobre\n"
        "- Recorrido por campamentos antiguos\n"
        "- Explicación histórica sobre la minería\n"
        "- Vistas panorámicas del área minera\n"
        "\nPrecio: $15.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_colorado, bg='#9370DB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Cerro Colorado"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_colorado.destroy)
    boton_volver.pack(side="left", padx=10)
    
def Muna():
    ventana_muna = tk.Toplevel()
    ventana_muna.title("Distrito de Munä")
    ventana_muna.geometry("700x600")
    ventana_muna.configure(bg='#9370DB')  # Fondo color turquesa

    # Frame principal para organizar los elementos
    main_frame = tk.Frame(ventana_muna, bg='#9370DB')
    main_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Título de la actividad (dentro de main_frame para mejor control de disposición)
    titulo = tk.Label(main_frame, text="Distrito de Munä", font=("Arial", 20, "bold"), bg='#9370DB')
    titulo.pack(pady=10)

    # Imagen
    try:
        image_path = "imagenes/NgabeBugle/Muna.jpg"  # Ruta a la imagen
        image = Image.open(image_path)  # Cargar la imagen
        image = image.resize((250, 150), Image.LANCZOS)  # Ajustar el tamaño de la imagen
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(main_frame, image=photo, bg='#9370DB')
        image_label.image = photo 
        image_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load image: {e}")

    # Frame para la descripción
    descripcion_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    descripcion_frame.pack(pady=15, side="left", fill="y")

    # Descripción
    descripcion_texto = (
        "Munä es uno de los distritos con diversidad natural, historica y cultural, le ofrece experiencias únicas" 
        "e inigualables, dándoles la oportunidad de tener inolvidables aventuras. Herederos de una cultura ancestral" 
        "Ngäbe Bugle, con de sitios arqueológicos, hogar de las culturas Pre - Hispanicas, vestigios que hasta el momento" 
        "continuan vivos gracias a las costumbres y tradiciones del pueblo Ngäbe y Buglé. Desde los limites con la provincia" 
        "de Chiriqui hasta las montañas y la selva, distrute de una mixtura única de cultura, historia, aventura, naturaleza" 
        "e inimaginable variedad que se complementa a la perfección con la cordialidad del pueblo Ngäbe. Difrute de cada viaje," 
        "diseñado cuidadosamente por nuestro equipo."

    )
    descripcion = tk.Label(descripcion_frame, text=descripcion_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    descripcion.pack()

    # Frame para los detalles de la actividad
    detalles_frame = tk.Frame(main_frame, bg="white", bd=2, relief="solid", padx=15, pady=15, width=300)
    detalles_frame.pack(pady=15, side="right", fill="y")

    # Detalles de la actividad
    detalles_texto = (
        "Incluye:\n"
        "- Exploración de sitios arqueológicos\n"
        "- Observación de vestigios prehispánicos\n"
        "- Interacción con la cultura Ngäbe y Buglé\n"
        "- Aventuras guiadas por la selva\n"
        "\nPrecio: $20.00"
    )
    detalles = tk.Label(detalles_frame, text=detalles_texto, wraplength=280, justify="left", bg="white", font=("Arial", 10))
    detalles.pack()

    # Botones de "RESERVAR" y "VOLVER"
    botones_frame = tk.Frame(ventana_muna, bg='#9370DB')
    botones_frame.pack(pady=20)

    boton_reservar = tk.Button(botones_frame, text="RESERVAR", width=15, font=("Arial", 12), bg="white", command=lambda: Reserva(nombre_actividad="Distrito de Muna"))
    boton_reservar.pack(side="left", padx=10)

    boton_volver = tk.Button(botones_frame, text="VOLVER", width=15, font=("Arial", 12), bg="white", command=ventana_muna.destroy)
    boton_volver.pack(side="left", padx=10)
#Fin Lugares Turisticos de Ngabe Bugle
#Fin Funciones comarcas

# Diccionario para almacenar precios y detalles de actividades
actividades_info = {
    #PROVINCIAS
    #Bocas del Toro
    "Playa Estrella": {
        "precio": 250.00,
        "detalles": (
            "Incluye:\n"
            "- Fotógrafo Profesional\n"
            "- 30 minutos guiados de interacción con delfines\n"
            "- Kit de fotos con delfines\n"
            "- Almuerzo continental\n"
            "- Transporte"
        )
    },
    "GREEN ACRES": {
        "precio": 120.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido guiado por el cultivo de cacao\n"
            "- Degustación de cacao orgánico\n"
            "- Paseo ecológico por la reserva"
        )
    },
    "Bahía de los Delfines": {
        "precio": 250.00,
        "detalles": (
            "Incluye:\n"
            "- Fotógrafo Profesional\n"
            "- 30 minutos guiados de interacción con delfines\n"
            "- Almuerzo continental\n"
            "- Transporte"
        )
    },
    "Aldea de Botellas Plásticas": {
     "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Tour guiado\n"
            "- Taller de reciclaje\n"
            "- Souvenir ecológico"
        )
    },
    #Cócle
    "Zoológico El Níspero": {
        "precio": 10.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido guiado por el zoológico y jardín botánico\n"
            "- Observación de animales como monos, tucanes y ranas doradas\n"
            "- Actividades de conservación\n"
            "- Área educativa sobre especies endémicas"
        )
    },
    "Mariposario del Valle": {
        "precio": 8.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido guiado sobre el ciclo de vida de las mariposas\n"
            "- Observación de diversas especies de mariposas\n"
            "- Talleres de conservación\n"
            "- Interacción con guías especializados"
        )
    },
    "Sendero de la India Dormida": {
        "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Senderismo por ruta escénica con cascadas\n"
            "- Vista panorámica desde la cima\n"
            "- Observación de flora y fauna autóctona\n"
            "- Área educativa sobre especies endémicas"
            "- Acceso a zonas de descanso y fotografía"
        )
    },
    "Serpentario Maravillas Tropicales": {
        "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Obsercación de serpientes nativas y exóticas\n"
            "- Explicaciones sobre biología y conservación\n"
            "- Exhibición de reptiles en ambiente seguro\n"
            "- Interacción con expertos en herpetología"
        )
    },
    #Colón
    "Castillo de San Lorenzo": {
        "precio": 2.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido por las rionas de la fortaleza histórica\n"
            "- Vista panóramica del río y la selva\n"
            "- Explicación de la historica militar y comercial\n"
            "- Esios para fotografía y exploración"
        )
    },
    "Esclusas de Gatún": {
        "precio": 15.00,
        "detalles": (
            "Incluye:\n"
            "- Observación del funcionamiento de las esclusas\n"
            "- Información educativa sobre el Canal de Panamá\n"
            "- Vista de barcos en tránsito\n"
            "- Experiencia en el centro de visitantes"
        )
    },  
    "Esclusas de Agua Clara": {
        "precio": 15.00,
        "detalles": (
            "Incluye:\n"
            "- Vista de las operaciones de tránsito de barcos\n"
            "- Explicación sobre la construcción del canal\n"
            "- Exhibiciones sobre el comercio mundial\n"
            "- Observación de ingeniería en acción"
        )
    }, 
    "Parque Nacional Chagres": {
        "precio": 45.00,
        "detalles": (
            "Incluye:\n"
            "- Caminatas por sendeeros en el bosque tropical\n"
            "- Observación de cascadas y ríos\n"
            "- Información sobre el Camino Real histórico\n"
            "- Actividades de ecoturismo y conservación"
        )
    }, 
    #Chiriquí    
    "Parque Nacional Volcán Barú": {
        "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Senderismo hasta la cima del volcán\n"
            "- Observación de flora y fauna en ambiente volcánico\n"
            "- Puntos de descanso y miradores\n"
            "- Caminatas guiadas por expertos"
        )
    }, 
    "Las Cascadas Perdidas": {
        "precio": 10.00,
        "detalles": (
            "Incluye:\n"
            "- Senderismo por la selva \n"
            "- Descanso junto a las cascadas\n"
            "- Observación de biodiversidad local\n"
            "- Áreas de picnic y fotografía"
        )
    },  
    "Refugio de Vida Silvestre Jungla de Panamá": {
        "precio": 70.00,
        "detalles": (
            "Incluye:\n"
            "- Observación de animales rescatados \n"
            "- Información sobre prgoramas de rescate y rehabilitación\n"
            "- Recorridos guiados por el refugio\n"
            "- Interacción con cuidores de animales"
        )
    }, 
    "Abejas y Mariposas de Boquete": {
        "precio": 30.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido por el centro ecológico \n"
            "- Observación de mariposas y producción de miel orgánica\n"
            "- Jardines diseñados para polinizadores\n"
            "- Charlas educativas sobre la importancia de las abeja"
        )
    }, 
    #Darién
    "Parque Nacional Darién": {
        "precio": 100.00,
        "detalles": (
            "Incluye:\n"
            "- Senderros para eexplorar la selva tropical \n"
            "- Observación de aves y vida silvestre\n"
            "- Información sobre la flora y fauna de la región\n"
            "- Actividades de ecoturismo y conservación"
        )
    },
    "La Palma": {
        "precio": 60.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido por la capital de Darién \n"
            "- Interacción con comunidades ind\n"
            "- Exploración de paisajes naturales\n"
            "- Oportunidad de conocer la cultura local"
        )
    },
    "Yaviza y el Fin de la Carretera Panamericana": {
        "precio": 20.00,
        "detalles": (
            "Incluye:\n"
            "- Vista del punto final de la Carretera Panamericana \n"
            "- Excursiones hacia la selva tropical\n"
            "- Interacción con guías locales sobre la historia de Yaviza\n"
            "- Fotografía de paisajes y flora de la región"
        )
    },
    "Rio Chucunaque": {
        "precio": 120.00,
        "detalles": (
            "Incluye:\n"
            "- Paseos en bote por el río \n"
            "- Oportunidad de pesca en aguas naturales\n"
            "- Observación de vegetación y fauna\n"
            "- Experiencia inmersiva en la naturaleza"
        )
    },
    #Herrera
    "Pesé y sus Destilerías de Ron": {
        "precio": 30.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido guiado por las destilerías locales \n"
            "- Explicación del proceso de favricación del ron\n"
            "- Degustación de diferentes vareiedades de ron\n"
            "- Historia de la destilación en Panamá"
        )
    },
    "Parita y su arquitectura colonial": {
        "precio": 60.00,
        "detalles": (
            "Incluye:\n"
            "- Paseo por calles con arquitectura colonial \n"
            "- Observación de casas antiguasbien conservadas\n"
            "- Explicación de la historia y cultura local\n"
            "- Interacción con guías locales"
        )
    },
    "Museo de Herrera en Chitré": {
        "precio": 5.00,
        "detalles": (
            "Incluye:\n"
            "- Exposiciones sobre la historia de la región \n"
            "- Muestras de tradiciones indígenas y coloniales\n"
            "- Información sobre la colonización y eventos históricos\n"
            "- Recorridos guiados por la exhibiciones"
        )
    },
    "Las Tablas de Sarigua": {
        "precio": 35.00,
        "detalles": (
            "Incluye:\n"
            "- Exploración de restos de antiguos asentamientos indígenas \n"
            "- Observación de flora y fauna autóctona\n"
            "- Senderos en el parquue arqueológico\n"
            "- Charlas sobre la importancia histórica del área"
        )
    },
    #Los Santos
    "Isla Iguana": {
        "precio": 40.00,
        "detalles": (
            "Incluye:\n"
            "- Snorkel y observación de vida marina\n"
            "- Paseo por las playas de arena blanca\n"
            "- Observación de iguanas y otras especies\n"
            "- Senderos naturales en la isla"
        )
    },
    "Pedasí": {
        "precio": 55.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido por arquitectura colonial\n"
            "- Participación de festividades tradicionales\n"
            "- Exploración de playas cercanas\n"
            "- Actividades de cultura localc"
        )
    },
    "Playa Venao": {
        "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Olas ideales para surf y deportes acuáticos\n"
            "- Áreas de camping y restaurantes\n"
            "- Ambiente relajado y natural\n"
            "- Espacios para disfrutar de atardeceres"
        )
    },
    "Museo de la Nacionalidad en Villa": {
     "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Exposiciones sobre la independencia y cultura panameña\n"
            "- Exhibición de artefactos históricos\n"
            "- Información sobre la historia de la región de Azuero\n"
            "- Visitas guiadas por el museo"
        )
    },
    #Panamá
    "Canal de Panamá": {
     "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Entrada al centro de observación\n"
            "- Tour guiado sobre la historia y el funcionamiento del canal\n"
            "- Observación de barcos en las esclusas"
        )
    },
    "Casco Viejo": {
     "precio": 40.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido por las calles históricas\n"
            "- Visita a museos locales\n"
            "- Degustación de platillos típicos"
        )
    },
    "Cerro Ancón": {
     "precio": 30.00,
        "detalles": (
            "Incluye:\n"
            "- Caminata guiada al cerro\n"
            "- Observación de la fauna y flora\n"
            "- Vistas panorámicas"
        )
    },
     "Parque Natural Metropolitano": {
     "precio": 25.00,
        "detalles": (
            "Incluye:\n"
            "- Entrada al parque\n"
            "- Caminata guiada por los senderos principales\n"
            "- Observación de fauna y flora (posibilidad de ver monos, perezosos y aves exóticas)\n"
            "- Acceso a áreas de descanso y miradores"
        )
    },
    #Veraguas
    "Isla Coiba": {
     "precio": 150.00,
        "detalles": (
            "Incluye:\n"
            "- Transporte en bote a la isla\n"
            "- Equipos de snorkel y guía especializado\n"
            "- Almuerzo y refrigerios\n"
            "- Acceso a áreas de descanso y miradores\n"
            "- Posibilidad de avistamiento de fauna marina (tiburones, tortugas, peces tropicales)"
        )
    },
    "Santa Catalina": {
     "precio": 120.00,
        "detalles": (
            "Incluye:\n"
            "- Clases de surf (opcional)\n"
            "- Equipos de surf disponible para alquilar\n"
            "- Excursiones de snorkel y buceo\n"
            "- Transporte a la Isla Coiba (opcional)\n"
            "- Guía especializado en actividades acuáticas"
        )
    },
    "Reserva Forestal La Yeguada": {
     "precio": 50.00,
        "detalles": (
            "Incluye:\n"
            "- Excursiones guiadas\n"
            "- Observación de fauna y flora nativas\n"
            "- Senderismo por rutas escénicas\n"
            "- Guía local con conocimiento ecológico"
        )
    },
    "Parque Nacional Cerro Hoya": {
     "precio": 70.00,
        "detalles": (
            "Incluye:\n"
            "- Caminatas guiadas por la reserva\n"
            "- Observación de vida silvestre\n"
            "- Oportunidades para fotografía de naturaleza\n"
            "- Espacios designados para camping\n"
            "- Guías locales especializados"
        )
    },
    #Panamá Oeste
    "Centro de Visitantes de Miraflores": {
     "precio": 150.00,
        "detalles": (
            "Incluye:\n"
            "- Acceso a las plataformas de observación\n"
            "- Entrada al museo interactivo\n"
            "- Guía turístico"
        )
    },
     "Playa Punta Chame": {
     "precio": 25.00,
        "detalles": (
            "Incluye:\n"
            "- Kitesurf y deportes acuáticos\n"
            "- Paseos en bote y observación de aves\n"
            "- Extensa playa de arena para relajarse\n"
            "- Atardeceres espectaculares sobre el océano"
        )
    },
     "Cascada El Chorro": {
     "precio": 18.00,
        "detalles": (
            "Incluye:\n"
            "- Caminata hasta la cascada\n"
            "- Oportunidad de nadar en aguas frescas\n"
            "- Espacios para picnic en un ambiente natural\n"
            "- Observación de la flora y fauna locales"
        )
    },
    "Playa Malibú": {
     "precio": 20.00,
        "detalles": (
            "Incluye:\n"
            "- Espacio para nadar y hacer snorkel\n"
            "- Arena dorada y aguas tranquilas\n"
            "- Exploración de áreas naturales alrededor\n"
            "- Ambiente pacífico para relajarse"
        )
    },
    #COMARCAS
    #Embera Wounaan
    "Comunidad de Lajas Blancas": {
        "precio": 15.00,
        "detalles": (
            "Incluye:\n"
            "- Paseos en canoa por el río Tuira\n"
            "- Caminatas por senderos naturales\n"
            "- Observación de flora y fauna local\n"
            "- Interacción con la caltura Emberá"
        )
    }, 
    "Distrito de Cemaco": {
        "precio": 10.00,
        "detalles": (
            "Incluye:\n"
            "- Participación en ferias culturales y eventos\n"
            "- Exhibición de danzas típicas\n"
            "- Venta de artesanías tradicionales\n"
            "- Charlas sobre costumbres locales"
        )
    },   
    "Cascada de Tres Brazos": {
        "precio": 20.00,
        "detalles": (
            "Incluye:\n"
            "- Senderismo hasta la cascada\n"
            "- Oportunidad de nadar en el entorno natural\n"
            "- Observación de la flora y fauna circundante\n"
            "- Excursión guiada por miembros de la comunidad"
        )
    },
    "Comunidad de Arimae": {
        "precio": 18.00,
        "detalles": (
            "Incluye:\n"
            "- Introducción a la medivina natural\n"
            "- Técnicas de caza y pesca tradicionales\n"
            "- Tallares de elaboración de artesanías\n"
            "- Convivencia con la comunidad Emberá"
        )
    },
    #Guna Yala
    "Archipiélago de San Blas": {
        "precio": 30.00,
        "detalles": (
            "Incluye:\n"
            "- Snorkel y buceo en aguas cristalinas\n"
            "- Recorrido por playas de arena blanca\n"
            "- Observación de vida marina\n"
            "- Alojamioento en cabañas tradicionales"
        )
    },
    "Montaña Sagrado de Ibedi": {
        "precio": 25.00,
        "detalles": (
            "Incluye:\n"
            "- Senderismo guiado con explicación cultural\n"
            "- Narración de leyendas y tradiciones\n"
            "- Vistas panorámicas de la comarca\n"
            "- Conexión con el patrimonio espiritual de los gunas"
        )
    },
    "Río Diablo": {
        "precio": 15.00,
        "detalles": (
            "Incluye:\n"
            "- Caminatas por el entorno del río\n"
            "- Oportunidad de nadar en el río\n"
            "- Observación de flora y fauna local\n"
            "- Relato de historias sobre la región"
        )
    },
    "Isla Perro Chico": {
        "precio": 35.00,
        "detalles": (
            "Incluye:\n"
            "- Snorkel en el arrecife de coral\n"
            "- Exploración de un barco hundido\n"
            "- Alojamiento en cabañas y espacios de acampada\n"
            "- Actividades recreativas en la playa"
        )
    },
    #Ngabe-Bugle
    "Cascada La Tulivieja": {
        "precio": 12.00,
        "detalles": (
            "Incluye:\n"
            "- Recorrido hasta la cascada en la comunidad de Soloy\n"
            "- Narraci[on de leyendas sobre el sitio\n"
            "- Oportunidad de para nadar en las pozas naturales\n"
            "- Fotografías en un sitio legendario"
        )
    },
    "Cerro Peña Blanca": {
        "precio": 25.00,
        "detalles": (
            "Incluye:\n"
            "- Escalada y caminata en el cerro\n"
            "- Paisajes naturaes rodeados de rocas\n"
            "- Experiencias de aventura extrema\n"
            "- Guías locales para actividades seguras"
        )
    },
    "Cerro Colorado": {
        "precio": 15.00,
        "detalles": (
            "Incluye:\n"
            "- Visita al yacimiento de cobre\n"
            "- Recorrido por campamentos antiguos\n"
            "- Explicación histórica sobre la mineria\n"
            "- Vistas panorámicas del área minera"
        )
    },
    "Distrito de Muna": {
        "precio": 20.00,
        "detalles": (
            "Incluye:\n"
            "- Exploración de sitios arqueológicos\n"
            "- Observación de vestigios prehispánicos\n"
            "- Interacción con la cultura Ngabe y Buglé\n"
            "- Aventuras guiadas por la selva"
        )
    },

}

# Función para obtener información de la actividad
def obtener_info_actividad(nombre_actividad):
    actividad = actividades_info.get(nombre_actividad)
    if actividad:
        return actividad["precio"], actividad["detalles"]
    return None, None

# Estructura para almacenar el historial de pagos y reservas no pagadas
historial_pagos = {}
reservas_no_pagadas = {}

# Función para actualizar el historial de pagos
def actualizar_historial(nombre_actividad, abono, deuda):
    if nombre_actividad not in historial_pagos:
        historial_pagos[nombre_actividad] = []
    historial_pagos[nombre_actividad].append({"Pagado": abono, "Deuda": deuda})

# Función para mostrar el historial de pagos en la factura
def mostrar_historial_pagos(ventana):
    historial_texto = "Historial de Pagos:\n"
    for actividad, pagos in historial_pagos.items():
        historial_texto += f"\nActividad: {actividad}\n"
        for pago in pagos:
            historial_texto += f" - Pagado: ${pago['Pagado']:.2f}, Deuda: ${pago['Deuda']:.2f}\n"
    tk.Label(ventana, text=historial_texto).pack(pady=10)
    
# Función para obtener el subtotal de reservas no pagadas
def obtener_subtotal_reservas_no_pagadas():
    subtotal = sum(reserva["precio_total"] for reserva in reservas_no_pagadas.values())
    return subtotal

# Función para agregar una reserva no pagada
def agregar_reserva_no_pagada(nombre_actividad, cantidad_personas, precio_por_persona):
    precio_total = cantidad_personas * precio_por_persona
    if nombre_actividad in reservas_no_pagadas:
        reservas_no_pagadas[nombre_actividad]["precio_total"] += precio_total
        reservas_no_pagadas[nombre_actividad]["cantidad_personas"] += cantidad_personas
    else:
        reservas_no_pagadas[nombre_actividad] = {"precio_total": precio_total, "cantidad_personas": cantidad_personas}

# Función Reserva
def Reserva(nombre_actividad):
    precio_por_persona, detalles_texto = obtener_info_actividad(nombre_actividad)

    if precio_por_persona is not None:
        ventana_reserva = tk.Toplevel()
        ventana_reserva.title("Reservar Actividad Turística")
        ventana_reserva.geometry("600x700")

        # Variables de datos del cliente
        nombre_var = StringVar()
        nacionalidad_var = StringVar()
        sexo_var = StringVar()
        edad_var = StringVar()
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

        # Preguntar el sexo usando un Combobox
        tk.Label(ventana_reserva, text="Sexo:").pack(pady=5)
        sexo_combobox = ttk.Combobox(ventana_reserva, textvariable=sexo_var)
        sexo_combobox['values'] = ("Masculino", "Femenino")
        sexo_combobox.pack(pady=5)

        # Preguntar la edad
        tk.Label(ventana_reserva, text="Edad:").pack(pady=5)
        tk.Entry(ventana_reserva, textvariable=edad_var).pack(pady=5)

        # Preguntar la identificación personal
        tk.Label(ventana_reserva, text="Identificación Personal:").pack(pady=5)
        tk.Entry(ventana_reserva, textvariable=identificacion_var).pack(pady=5)

        # Preguntar el teléfono
        tk.Label(ventana_reserva, text="Teléfono:").pack(pady=5)
        tk.Entry(ventana_reserva, textvariable=telefono_var).pack(pady=5)

        # Función para manejar el pago
        def realizar_pago():
            try:
                cantidad_personas = int(cantidad_personas_var.get())
                precio_total = cantidad_personas * precio_por_persona
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese un número válido para la cantidad de personas.")
                return

            pagar(nombre_var.get(), identificacion_var.get(), telefono_var.get(),
                  nacionalidad_var.get(), detalles_texto, precio_total,
                  cantidad_personas, int(edad_var.get()), sexo_var.get(), nombre_actividad)

        # Función para manejar el abono
        def abonar():
            ventana_abono = tk.Toplevel()
            ventana_abono.title("Realizar Abono")
            ventana_abono.geometry("400x200")

            abono_var = StringVar()

            tk.Label(ventana_abono, text="Monto a Abonar:").pack(pady=5)
            tk.Entry(ventana_abono, textvariable=abono_var).pack(pady=5)

            def realizar_abono():
                try:
                    abono = float(abono_var.get())
                    if abono > 0:
                        precio_total = int(cantidad_personas_var.get()) * precio_por_persona
                        deuda = max(precio_total - abono, 0)
                        mostrar_factura(
                        nombre_var.get(),               # nombre
                        identificacion_var.get(),        # identificacion
                        telefono_var.get(),              # telefono
                        nacionalidad_var.get(),          # nacionalidad
                        detalles_texto,                  # detalles_reserva
                        int(cantidad_personas_var.get()), # cantidad_personas
                        nombre_actividad,                # nombre_actividad
                        precio_total,                    # precio_total
                        abono                            # abono
                    )
                        ventana_abono.destroy()
                    else:
                        messagebox.showerror("Error", "Ingrese un monto de abono válido.")
                except ValueError:
                    messagebox.showerror("Error", "Por favor, ingrese un monto de abono válido.")

            tk.Button(ventana_abono, text="Confirmar Abono", command=realizar_abono).pack(pady=10)

        def mostrar_factura(nombre, identificacion, telefono, nacionalidad, detalles_reserva, cantidad_personas, nombre_actividad, precio_total, abono):
            ventana_factura = tk.Toplevel()
            ventana_factura.title("Factura")
            ventana_factura.geometry("500x800")

            descuento = precio_total * 0.10  # Descuento del 10%
            total_con_descuento = precio_total - descuento
            deuda = max(total_con_descuento - abono, 0)

            tk.Label(ventana_factura, text="Detalles de la Reserva", font=("Arial", 16, "bold")).pack(pady=10)
            tk.Label(ventana_factura, text="Empresa: HOU PANAMA TOURS S.A", font=("Arial", 12, "bold")).pack(pady=10)
            tk.Label(ventana_factura, text=f"Nombre: {nombre}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Nacionalidad: {nacionalidad}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Identificación: {identificacion}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Teléfono: {telefono}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Actividad: {nombre_actividad}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Detalles:\n{detalles_reserva}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Cantidad de Personas: {cantidad_personas}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Subtotal: ${precio_total:.2f}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Descuento (10%): -${descuento:.2f}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Abono: -${abono:.2f}").pack(pady=5)
            tk.Label(ventana_factura, text=f"Total adeudado: ${deuda:.2f}").pack(pady=5)

            if deuda > 0:
                tk.Label(ventana_factura, text=f"Usted tiene un saldo pendiente de ${deuda:.2f}.").pack(pady=10)
            else:
                tk.Label(ventana_factura, text="Su saldo está al día.").pack(pady=10)
            
            # Botón para cerrar la ventana de pago
            tk.Button(ventana_factura, text="Cerrar", command=ventana_factura.destroy).pack(pady=10)
                
        # Botones de Pagar, Abonar y Añadir Lugar Turístico
        tk.Button(ventana_reserva, text="Pagar", command=realizar_pago).pack(pady=10)
        tk.Button(ventana_reserva, text="Abonar", command=abonar).pack(pady=10)
        tk.Button(ventana_reserva, text="Añadir otro Lugar Turístico", command= ProvinciasComarcas).pack(pady=10)

        # Botón para regresar al menú anterior
        tk.Button(ventana_reserva, text="Regresar", command=ventana_reserva.destroy).pack(pady=10)
        
    else:
        messagebox.showerror("Error", "Actividad no encontrada.")

# Función de pago
def pagar(nombre, identificacion, telefono, nacionalidad, detalles_reserva, precio_total, cantidad_personas, edad, sexo, nombre_actividad):
    ventana_pago = tk.Toplevel()
    ventana_pago.title("Recibo de Pago")
    ventana_pago.geometry("500x800")

    # Calcular el subtotal de reservas no pagadas
    subtotal_reservas = obtener_subtotal_reservas_no_pagadas()
    subtotal = subtotal_reservas + precio_total

    # Aplicar descuentos
    descuento_tercera_persona = 0
    if cantidad_personas >= 3:
        descuento_tercera_persona = subtotal
        descuento_tercera_persona = subtotal * 0.15  # 15% de descuento por la tercera persona
        subtotal -= descuento_tercera_persona

    descuento_total = 0
    if subtotal > 2000:
        descuento_total = subtotal * 0.05  # 5% de descuento si el total es mayor a 2000
        subtotal -= descuento_total

    # Descuento por edad
    descuento_edad = 0
    if (sexo == "Femenino" and edad >= 60) or (sexo == "Masculino" and edad >= 65):
        descuento_edad = subtotal * 0.10  # 10% de descuento por edad
        subtotal -= descuento_edad
        
    # Guardar en el historial de pagos y limpiar las reservas no pagadas
    historial_pagos[nombre_actividad] = [{"Pagado": subtotal, "Deuda": 0}]
    reservas_no_pagadas.clear()

    # Mostrar los detalles del pago
    tk.Label(ventana_pago, text="Detalles de la Reserva", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Label(ventana_pago, text="Empresa: HOU PANAMA TOURS S.A", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(ventana_pago, text=f"Nombre: {nombre}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Nacionalidad: {nacionalidad}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Identificación: {identificacion}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Teléfono: {telefono}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Actividad: {nombre_actividad}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Detalles:\n{detalles_reserva}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Cantidad de Personas: {cantidad_personas}").pack(pady=5)
    tk.Label(ventana_pago, text=f"Subtotal: ${subtotal + descuento_tercera_persona + descuento_total + descuento_edad:.2f}").pack(pady=5)
    
    if descuento_tercera_persona > 0:
        tk.Label(ventana_pago, text=f"Descuento por tercera persona: -${descuento_tercera_persona:.2f}").pack(pady=5)
    
    if descuento_total > 0:
        tk.Label(ventana_pago, text=f"Descuento por compra superior a $2000: -${descuento_total:.2f}").pack(pady=5)

    if descuento_edad > 0:
        tk.Label(ventana_pago, text=f"Descuento por edad: -${descuento_edad:.2f}").pack(pady=5)

    # Mostrar el precio total después de descuentos
    tk.Label(ventana_pago, text=f"Precio Total: ${subtotal:.2f}").pack(pady=10)

    # Mostrar historial de pagos en la factura
    mostrar_historial_pagos(ventana_pago)
    tk.Label(ventana_pago, text=f"Usted ha cancelado\n¡Los esperamos pronto!").pack(pady=10)
    
    # Botón para cerrar la ventana de pago
    tk.Button(ventana_pago, text="Cerrar", command=ventana_pago.destroy).pack(pady=10)
  
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Actividades Turísticas en Panamá")
ventana.geometry("500x300")

frame = tk.Frame(ventana)
frame.pack(pady=10)
    
try:
    image_path = "imagenes/empresas_hou_oficial.jpg"
    image = Image.open(image_path)
    image = image.resize((450, 250), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

# Crear la barra de menú
menu_bar = tk.Menu(ventana)

menu_prin = tk.Menu(menu_bar, tearoff=0)
menu_prin.add_command(label="Presentación", command=Presentacion)
menu_prin.add_command(label="Ver Provincias y Comarcas", command=ProvinciasComarcas)
menu_prin.add_separator() 
menu_prin.add_command(label="Salir", command=ventana.quit)

menu_bar.add_cascade(label="Menu", menu=menu_prin)

ventana.config(menu=menu_bar)

# Ejecutar el bucle principal
ventana.mainloop()
#FinAlgoritmo