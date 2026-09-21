#cita a ciegas con una película

#funciones
def pedir_datos_usuario():
    """Pregunta al usuario sus datos y los devuelve"""
    tiempo_usuario= int(input("¿Cuántos minutos tienes disponibles?"))
    animo_usuario= input("¿Cómo te sientes? (triste/feliz/melancólico/desconectado):")
    compania_usuario= input("¿Con quién verás la película (solo/pareja/amigos)?")
    return tiempo_usuario, animo_usuario, compania_usuario

def calcular_puntaje(animo_pelicula, compania_pelicula, duracion_pelicula, animo_usuario, compania_usuario, tiempo_usuario):
    """Calcula el puntaje de una película según que tanto coincide con el usuario"""
    puntaje=0
    
    if animo_pelicula==animo_usuario:
        puntaje = puntaje + 1

    if compania_pelicula==compania_usuario:
        puntaje = puntaje + 1

# si la duración es mayor al tiempo del usuario se restan puntos
# para que tenga menos probabilidad de coincidir
    if duracion_pelicula > tiempo_usuario:
        puntaje = puntaje - 10

    return puntaje 

def mostrar_resultado(puntaje, resena, titulo):
    """Muestra la reseña de la película mas compatible y pregunta al usuario si la quiere ver"""
    if puntaje <= 0:
        print("No hay películas compatibles para ti")
        print("Pero si quieres puedes ver esta opción")
    else:
        print("Tenemos una buena opción para ti")

    print("Reseña: \"" + resena + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()

    if respuesta=="si":
        print("Tu película es:", titulo)
    else:
        print("Ok, quizás en otra ocasión")

#parte principal del programa
#entrada de datos del uausario
tiempo_usuario, animo_usuario, compania_usuario = pedir_datos_usuario()
              
#Datos de las películas
#película 1
duracion1= 106
animo1="melancólico"
compania1="amigos"
resena1= "fun road trip for the whole family!"
titulo1= "Y tú mamá también (2001)"

#pelicula 2
duracion2= 90
animo2="feliz"
compania2="amigos"
resena2= "Hacen exactamente el mismo chiste durante una hora y media y te sigue dando risa"
titulo2= "Una película de huevos (2006)"

#pelicula 3
duracion3= 120
animo3="triste"
compania3="pareja"
resena3= "we cannot let Mr Beast ever see this film"
titulo3= "They shoot horses, don´t they? (1969)"

#pelicula 4
duracion4= 120
animo4= "desconectado"
compania4= "solo"
resena4= "el que rie al último rie mejor"
titulo4= "Oldboy (2003)"

#pelicula 5
duracion5=117
animo5="feliz"
compania5= "amigos"
resena5="the twink mary poppins gives us a cinematic experience about diabetes"
titulo5="Wonka (2023)"

#Cálculo de puntajes usando la función calcular_puntaje()
puntaje1 = calcular_puntaje(animo1, compania1, duracion1, animo_usuario, compania_usuario, tiempo_usuario)
puntaje2 = calcular_puntaje(animo2, compania2, duracion2, animo_usuario, compania_usuario, tiempo_usuario)
puntaje3 = calcular_puntaje(animo3, compania3, duracion3, animo_usuario, compania_usuario, tiempo_usuario)
puntaje4 = calcular_puntaje(animo4, compania4, duracion4, animo_usuario, compania_usuario, tiempo_usuario)
puntaje5 = calcular_puntaje(animo5, compania5, duracion5, animo_usuario, compania_usuario, tiempo_usuario)

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
    mostrar_resultado(mejor_puntaje, resena1, titulo1)

if mejor_pelicula == 2:
    mostrar_resultado(mejor_puntaje, resena2, titulo2)

if mejor_pelicula == 3:
    mostrar_resultado(mejor_puntaje, resena3, titulo3)

if mejor_pelicula == 4:
    mostrar_resultado(mejor_puntaje, resena4, titulo4)

if mejor_pelicula == 5:
    mostrar_resultado(mejor_puntaje, resena5, titulo5)


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
