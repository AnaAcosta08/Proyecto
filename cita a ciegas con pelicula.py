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
    recibe: animo_pelicula y animo_usuario (texto), compania_pelicula
            y compania_usuario (texto), duracion_pelicula y
            tiempo_usuario (numérico)
    calcula qué tanto coincide una película con las preferencias
    del usuario, sumando o restando puntos según coincidan ánimo,
    compañía y si la duración cabe en el tiempo disponible
    devuelve: puntaje (numérico)
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

#parte principal del programa
#entrada de datos del uausario
tiempo_usuario, animo_usuario, compania_usuario = pedir_datos_usuario()
              
#Datos de las películas
#película 1
DURACION_1 = 106
ANIMO_1 = "melancólico"
COMPANIA_1 = "amigos"
RESENA_1 = "fun road trip for the whole family!"
TITULO_1 = "Y tú mamá también (2001)"

#pelicula 2
DURACION_2 = 90
ANIMO_2 = "feliz"
COMPANIA_2 = "amigos"
RESENA_2 = "Hacen exactamente el mismo chiste\
 durante una hora y media y te sigue dando risa"
TITULO_2 = "Una película de huevos (2006)"

#pelicula 3
DURACION_3 = 120
ANIMO_3 = "triste"
COMPANIA_3 = "pareja"
RESENA_3 = "we cannot let Mr Beast ever see this film"
TITULO_3 = "They shoot horses, don´t they? (1969)"

#pelicula 4
DURACION_4 = 120
ANIMO_4 = "desconectado"
COMPANIA_4 = "solo"
RESENA_4 = "el que rie al último rie mejor"
TITULO_4 = "Oldboy (2003)"

#pelicula 5
DURACION_5 = 117
ANIMO_5 = "feliz"
COMPANIA_5 = "amigos"
RESENA_5 = "the twink mary poppins gives us a cinematic\
 experience about diabetes"
TITULO_5 = "Wonka (2023)"

#Cálculo de puntajes usando la función calcular_puntaje()
puntaje1 = calcular_puntaje(ANIMO_1, COMPANIA_1, DURACION_1, animo_usuario,
                            compania_usuario, tiempo_usuario)
puntaje2 = calcular_puntaje(ANIMO_2, COMPANIA_2, DURACION_2, animo_usuario,
                            compania_usuario, tiempo_usuario)
puntaje3 = calcular_puntaje(ANIMO_3, COMPANIA_3, DURACION_3, animo_usuario,
                            compania_usuario, tiempo_usuario)
puntaje4 = calcular_puntaje(ANIMO_4, COMPANIA_4, DURACION_4, animo_usuario,
                            compania_usuario, tiempo_usuario)
puntaje5 = calcular_puntaje(ANIMO_5, COMPANIA_5, DURACION_5, animo_usuario,
                            compania_usuario, tiempo_usuario)

#Encontrar la película  con mayor puntaje
mejor_puntaje = puntaje1
mejor_pelicula = 1

if puntaje2 > mejor_puntaje:
    mejor_puntaje = puntaje2
    mejor_pelicula = 2

if puntaje3 > mejor_puntaje:
    mejor_puntaje = puntaje3
    mejor_pelicula = 3

if puntaje4 > mejor_puntaje:
    mejor_puntaje = puntaje4
    mejor_pelicula = 4

if puntaje5 > mejor_puntaje:
    mejor_puntaje = puntaje5
    mejor_pelicula = 5

#Mostrar la película elegida, usando la función mostrar_resultado()
if mejor_pelicula == 1:
    mostrar_resultado(mejor_puntaje, RESENA_1, TITULO_1)

if mejor_pelicula == 2:
    mostrar_resultado(mejor_puntaje, RESENA_2, TITULO_2)

if mejor_pelicula == 3:
    mostrar_resultado(mejor_puntaje, RESENA_3, TITULO_3)

if mejor_pelicula == 4:
    mostrar_resultado(mejor_puntaje, RESENA_4, TITULO_4)

if mejor_pelicula == 5:
    mostrar_resultado(mejor_puntaje, RESENA_5, TITULO_5)


#Notas sobre este avance

#La base de datos de películas aún es muy pequeña por lo que en muchas
#combinaciones de tiempo, ánimo y compañía el programa indica que
#no hay películas que coincidan muy bien.
#debido a esto, a veces la película recomendada no coincide al 100% con
#los datos ingresados del usuario y no es común que haya varias opciones
#con puntajes similares para elegir.
#mi objetivo es que conforme aprenda más herramientas planeo ampliar
#la base de datos y hacer que el programa muestre varias reseñas para que
#el usuario elija y poder hacer mi idea original.
