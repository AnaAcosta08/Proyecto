#cita a ciegas con una película

#entrada de datos del usuario
tiempo_usuario= int(input("¿Cuántos minutos tienes disponibles?"))
animo_usuario= input("¿Cómo te sientes? (triste/feliz/melancólico/desconectado):")
compania_usuario= input("¿Con quién verás la película (solo/pareja/amigos)?")

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

#Cálculo de puntajes

#Película 1
puntaje1=0
if animo1==animo_usuario:
    puntaje1= puntaje1 + 1
    
if compania1==compania_usuario:
    puntaje1=puntaje1 + 1
    
#Pelicula 2
puntaje2= 0
if animo2==animo_usuario:
    puntaje2=puntaje2 + 1
    
if compania2==compania_usuario:
    puntaje2=puntaje2 + 1
    
#pelicula 3
puntaje3 = 0
if animo3==animo_usuario:
    puntaje3=puntaje3 + 1

if compania3==compania_usuario:
    puntaje3=puntaje3 + 1
    
#pelicula 4
puntaje4 = 0
if animo4==animo_usuario:
    puntaje4=puntaje4 + 1
    
if compania4==compania_usuario:
    puntaje4=puntaje4 + 1
    
#pelicula 5
puntaje5=0
if animo5==animo_usuario:
    puntaje5=puntaje5 + 1
    
if compania5==compania_usuario:
    puntaje5=puntaje5 + 1
    
#duracion de la pelicula.
#si la duracion es mayor al tiempo del usuario se restará puntos al puntaje
#para que tenga menos probabilidad de coincidir
    
if duracion1 > tiempo_usuario:
    puntaje1 = puntaje1 - 10

if duracion2 > tiempo_usuario:
    puntaje2 = puntaje2 - 10

if duracion3 > tiempo_usuario:
    puntaje3 = puntaje3 - 10

if duracion4 > tiempo_usuario:
    puntaje4 = puntaje4 - 10

if duracion5 > tiempo_usuario:
    puntaje5 = puntaje5 - 10
    
# Encontrar la película con mayor puntaje
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
    
# Como al iniciar declaré la variable mejor_puntaje= puntaje1,
#aunque todas las películas me den un valor menor a 1 en puntaje, me dará como mejor opción la película 1.
# para evitar esto añadí una condicional para imrpimir un texto que indique que no hay coincidencias.
if mejor_puntaje <= 0:
    print("No hay películas que coincidan muy bien con tus criterios.")
    print("Pero si quieres, puedes ver esta opción:")
else:
    print("Tenemos una buena opción para ti:")
    
# Mostrar la película elegida
if mejor_pelicula == 1:
    print("Reseña: \"" + resena1 + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()
    if respuesta =="si":
        print("Tu película es:", titulo1)
    else:
        print("Ok, quizás otra vez.")

if mejor_pelicula == 2:
    print("Reseña: \"" + resena2 + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()
    if respuesta == "si":
        print("Tu película es:", titulo2)
    else:
        print("Ok, quizás otra vez.")

if mejor_pelicula == 3:
    print("Reseña: \"" + resena3 + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()
    if respuesta == "si":
        print("Tu película es:", titulo3)
    else:
        print("Ok, quizás otra vez.")

if mejor_pelicula == 4:
    print("Reseña: \"" + resena4 + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()
    if respuesta == "si":
        print("Tu película es:", titulo4)
    else:
        print("Ok, quizás otra vez.")

if mejor_pelicula == 5:
    print("Reseña: \"" + resena5 + "\"")
    print("¿Quieres ver esta película? (si/no): ")
    respuesta = input()
    if respuesta == "si":
        print("Tu película es:", titulo5)
    else:
        print("Ok, quizás otra vez.")
    

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


