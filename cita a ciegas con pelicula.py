#cita a ciegas con una película
 
#posición (columna) de cada dato dentro del renglón de una película
DURACION = 0
ANIMO = 1
COMPANIA = 2
RESENA = 3
TITULO = 4
 
#funciones

def limpiar_texto(texto):
    """
    recibe texto escrito por el usuario o un dato de la película
    quita los espacios del inicio y del final, convierte todo a
    minúsculas y reemplaza las vocales con acento por vocales sin acento
    devuelve el texto limpio
    """
    texto = texto.strip()
    texto = texto.lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto

def pedir_datos_usuario():
    """
    Pregunta al usuario sus datos
    recibe tiempo_usuario (valor num entero), animo_usuario (texto) y
    compania_usuario (texto) y los devuelve
    """
    tiempo_usuario = int(input("¿Cuántos minutos tienes disponibles?"))
    animo_usuario = limpiar_texto(input("¿Cómo te sientes?(triste/feliz/\
melancólico/desconectado):"))
    compania_usuario = limpiar_texto(input("¿Con quién verás la película\
(solo/pareja/amigos)?"))
    return tiempo_usuario, animo_usuario, compania_usuario

def calcular_puntaje(animo_pelicula,
                     compania_pelicula,
                     duracion_pelicula,
                     animo_usuario,
                     compania_usuario,
                     tiempo_usuario):
    """
    recibe: animo_pelicula y animo_usuario, compania_pelicula
            y compania_usuario, duracion_pelicula y
            tiempo_usuario
    calcula qué tanto coincide una película con las preferencias
    del usuario, sumando o restando puntos según coincidan ánimo,
    compañía y si la duración cabe en el tiempo disponible
    devuelve: puntaje
    """
    puntaje = 0
    if limpiar_texto(animo_pelicula) == animo_usuario:
        puntaje = puntaje + 1
 
    if limpiar_texto(compania_pelicula) == compania_usuario:
        puntaje = puntaje + 1
 
    # si la duración es mayor al tiempo del usuario se restan puntos
    # para que tenga menos probabilidad de coincidir
    if duracion_pelicula > tiempo_usuario:
        puntaje = puntaje - 10
 
    return puntaje
 
def calcular_puntajes(peliculas, animo_usuario, compania_usuario,
                      tiempo_usuario):
    """
    recibe: la matriz peliculas (un renglón por película)
            y los datos del usuario
    calcula el puntaje de cada película usando calcular_puntaje()
    devuelve: lista puntajes (un puntaje por película, en el mismo orden)
    """
    puntajes = []
    for i in range(len(peliculas)):
        puntaje = calcular_puntaje(peliculas[i][ANIMO],
                                   peliculas[i][COMPANIA],
                                   peliculas[i][DURACION],
                                   animo_usuario, compania_usuario,
                                   tiempo_usuario)
        puntajes.append(puntaje)
    return puntajes
 
def buscar_compatibles(puntajes):
    """
    recibe: lista puntajes
    busca las películas compatibles (que tienen
    puntaje mayor a 0)
    devuelve: lista compatibles con las posiciones de esas películas
    """
    compatibles = []
    for i in range(len(puntajes)):
        if puntajes[i] > 0:
            compatibles.append(i)
    return compatibles
 
def buscar_mejor(puntajes):
    """
    recibe lista puntajes
    busca cuál es el mayor puntaje de la lista
    devuelve la posición de la película con mayor puntaje
    """
    posicion_mejor = 0
    for i in range(len(puntajes)):
        if puntajes[i] > puntajes[posicion_mejor]:
            posicion_mejor = i
    return posicion_mejor
 
def mostrar_opciones(compatibles, peliculas):
    """
    recibe: lista compatibles (posiciones de las películas compatibles)
            y la matriz peliculas
    muestra la reseña de cada película compatible con un número
    (el título queda oculto)
    """
    for n in range(len(compatibles)):
        posicion = compatibles[n]
        print(str(n + 1) + ") Reseña: \"" + peliculas[posicion][RESENA] + "\"")
 
def pedir_opcion(cantidad):
    """
    recibe cantidad de opciones disponibles
    pide al usuario que elija una opción y repite la pregunta
    hasta que sea un número válido
    devuelve: opcion elegida por el usuario
    """
    texto = "Elige el número de tu cita a ciegas (0 si ninguna te convence): "
    opcion = int(input(texto))
    while opcion < 0 or opcion > cantidad:
        print("Opción no válida, elige un número de la lista.")
        opcion = int(input(texto))
    return opcion
 
def mostrar_resultado(puntaje, resena, titulo):
    """Muestra la reseña de la película mas compatible\
       y pregunta al usuario si la quiere ver"""
    if puntaje <= 0:
        print("No hay películas compatibles para ti")
        print("Pero si quieres puedes ver esta opción")
    else:
        print("Tenemos una buena opción para ti")
 
    print("Reseña: \"" + resena + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = limpiar_texto(input())
 
    if respuesta == "si":
        print("Tu película es:", titulo)
    else:
        print("Ok, quizás en otra ocasión")
        

def carga_peliculas(nombre_archivo):
    """
    recibe: nombre_archivo con el nombre del archivo de películas
    lee el archivo donde cada linea es una pelicula con sus datos
    separados por tabulador: duración, ánimo, compañía, reseña, título
    devuelve: matriz peliculas (un renglón por película)
    """
    peliculas = []
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    for linea in archivo:
        campos = linea.strip().split("\t")
        duracion = int(campos[0])
        renglon = [duracion, campos[1], campos[2], campos[3], campos[4]]
        peliculas.append(renglon)
    archivo.close()
    return peliculas

#Datos de las películas
#se cargan desde peliculas.txt: cada línea es una película con sus datos
#separados por tabulador (duración, ánimo, compañía, reseña, título)
PELICULAS = carga_peliculas("peliculas.txt")

def elegir_pelicula(puntajes, peliculas):
    """
    recibe: puntajes (lista de números) y la matriz peliculas.
    muestra las reseñas de las películas compatibles, deja que el
    usuario elija una y revela su título
    no devuelve nada
    """
    compatibles = buscar_compatibles(puntajes)

    if len(compatibles) == 0:
        # si no hay ninguna compatible se ofrece la de mayor puntaje
        mejor = buscar_mejor(puntajes)
        mostrar_resultado(puntajes[mejor], peliculas[mejor][RESENA],
                          peliculas[mejor][TITULO])
    else:
        # si hay compatibles, el usuario elige cuál quiere ver
        print("Estas son tus citas a ciegas:")
        mostrar_opciones(compatibles, peliculas)
        opcion = pedir_opcion(len(compatibles))

        if opcion == 0:
            print("Ok, quizás en otra ocasión")
        else:
            pelicula = compatibles[opcion - 1]
            print("Tu película es:", peliculas[pelicula][TITULO])
#parte principal
repetir = "si"

while repetir == "si":

    #entrada de datos del usuario
    tiempo_usuario, animo_usuario, compania_usuario = pedir_datos_usuario()

    #Cálculo de puntajes
    puntajes = calcular_puntajes(PELICULAS, animo_usuario,
                                 compania_usuario, tiempo_usuario)

    elegir_pelicula(puntajes, PELICULAS)

    repetir = limpiar_texto(input("¿Quieres buscar otra película? (si/no): "))

print("Adiós")
