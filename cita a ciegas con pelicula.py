#cita a ciegas con una película

#funciones
def pedir_datos_usuario():
    """
    Pregunta al usuario sus datos
    recibe tiempo_usuario (valor num entero), animo_usuario (texto) y
    compania_usuario (texto) y los devuelve
    """
    tiempo_usuario = int(input("¿Cuántos minutos tienes disponibles?"))
    animo_usuario = input("¿Cómo te sientes?(triste/feliz/\
melancólico/desconectado):")
    compania_usuario = input("¿Con quién verás la película\
(solo/pareja/amigos)?")
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
    if animo_pelicula == animo_usuario:
        puntaje = puntaje + 1
 
    if compania_pelicula == compania_usuario:
        puntaje = puntaje + 1
 
    # si la duración es mayor al tiempo del usuario se restan puntos
    # para que tenga menos probabilidad de coincidir
    if duracion_pelicula > tiempo_usuario:
        puntaje = puntaje - 10
 
    return puntaje
 
def calcular_puntajes(animos, companias, duraciones,
                      animo_usuario, compania_usuario, tiempo_usuario):
    """
    recibe: las listas animos, companias y duraciones de las películas
            y los datos del usuario
    calcula el puntaje de cada película usando calcular_puntaje()
    devuelve: lista puntajes (un puntaje por película, en el mismo orden)
    """
    puntajes = []
    for i in range(len(animos)):
        puntaje = calcular_puntaje(animos[i], companias[i], duraciones[i],
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
 
def mostrar_opciones(compatibles, resenas):
    """
    recibe: lista compatibles (posiciones de las películas compatibles)
            y lista resenas 
    muestra la reseña de cada película compatible con un número
    (el título queda oculto)
    """
    for n in range(len(compatibles)):
        posicion = compatibles[n]
        print(str(n + 1) + ") Reseña: \"" + resenas[posicion] + "\"")
 
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
    respuesta = input()
 
    if respuesta == "si":
        print("Tu película es:", titulo)
    else:
        print("Ok, quizás en otra ocasión")
 
#Datos de las películas
#cada lista guarda un dato de las películas, y la posición indica la película:

DURACIONES = [106, 90, 120, 120, 117,
              108, 122, 126, 125, 120,
              89, 99, 103, 137, 95]
ANIMOS = ["melancólico", "feliz", "triste", "desconectado", "feliz",
          "melancólico", "feliz", "melancólico", "desconectado",
          "desconectado", "triste", "feliz", "feliz", "triste", "triste"]
COMPANIAS = ["amigos", "amigos", "pareja", "solo", "amigos",
             "pareja", "pareja", "solo", "pareja", "amigos",
             "solo", "amigos", "solo", "solo", "amigos"]
RESENAS = ["fun road trip for the whole family!",
           "Hacen exactamente el mismo chiste\
 durante una hora y media y te sigue dando risa",
           "we cannot let Mr Beast ever see this film",
           "el que rie al último rie mejor",
           "the twink mary poppins gives us a cinematic\
 experience about diabetes",
           "No me puedo imaginar querer borrar a Kate Winslet de mi memoria",
           "The film equivalent of rolling down a big hill or carving your\
 name into the sand when you were little",
           "Un hombre solitario se enamora de la voz de su\
 asistente virtual",
           "Una niña atrapada en un mundo de espíritus donde nada es\
 lo que parece",
           "Dos horas de persecución a toda velocidad\
 en medio del desierto",
           "Dos hermanos intentan sobrevivir mientras el mundo\
 a su alrededor se derrumba",
           "Un tipo ordinario descubre que el apocalipsis zombi\
 no arruinará su plan de ir al bar",
           "Un oso amable y su sombrero rojo demuestran que\
 la bondad sí funciona",
           "Un hombre regresa a su pueblo y se enfrenta\
 a lo que intentó dejar atrás",
           "Todas las emociones de una niña discuten en su\
 cabeza durante una mudanza"]
TITULOS = ["Y tú mamá también (2001)",
           "Una película de huevos (2006)",
           "They shoot horses, don´t they? (1969)",
           "Oldboy (2003)",
           "Wonka (2023)",
           "Eternal Sunshine of the Spotless Mind (2004)",
           "Amélie (2001)",
           "Her (2013)",
           "El viaje de Chihiro (2001)",
           "Mad Max: Furia en el camino (2015)",
           "La tumba de las luciérnagas (1988)",
           "Shaun of the Dead (2004)",
           "Paddington 2 (2017)",
           "Manchester by the Sea (2016)",
           "Intensamente (2015)"]
 
#parte principal 
repetir = "si"
 
while repetir == "si":
 
    #entrada de datos del usuario
    tiempo_usuario, animo_usuario, compania_usuario = pedir_datos_usuario()
 
    #Cálculo de puntajes: una lista con el puntaje de cada película
    puntajes = calcular_puntajes(ANIMOS, COMPANIAS, DURACIONES,
                                 animo_usuario, compania_usuario,
                                 tiempo_usuario)
 
    #Buscar las películas compatibles (puntaje mayor a 0)
    compatibles = buscar_compatibles(puntajes)
 
    if len(compatibles) == 0:
        #si no hay ninguna compatible se ofrece la de mayor puntaje
        mejor = buscar_mejor(puntajes)
        mostrar_resultado(puntajes[mejor], RESENAS[mejor], TITULOS[mejor])
    else:
        #si hay compatibles, el usuario elige cuál quiere ver
        print("Estas son tus citas a ciegas:")
        mostrar_opciones(compatibles, RESENAS)
        opcion = pedir_opcion(len(compatibles))
 
        if opcion == 0:
            print("Ok, quizás en otra ocasión")
        else:
            pelicula = compatibles[opcion - 1]
            print("Tu película es:", TITULOS[pelicula])
 
    repetir = input("¿Quieres buscar otra película? (si/no): ")
 
print("¡Gracias por usar el programa!")
 
