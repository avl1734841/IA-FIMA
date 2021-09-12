"""
Actividad 2 Ejercicios Introduccion Python, 2da parte
Andrés Villalobos López
1734841
Sabatinos N1
"""

print("Ejercicio 2")

#usando input los jugadores elijen entre piedra papel o tijera
x = input("Jugador 1: ")
y = input("Jugador 2: ")

#utilizamos un if para poner la condicion de empate
if (x == y):
    print("Empate")
    
#para las demas condiciones se utilizan elif y if
elif x == "piedra":
    if y == "tijera":
        print("Jugador 1 gana, Piedra le gana a tijera")
    elif x == "piedra":
        if y == "papel":
            print("jugador 2 gana, papel le gana a piedra")

elif x == "papel":
    if y == "piedra":
        print("Jugador 1 gana, Papel le gana a piedra")
    elif  x == "papel":
        if y == "tijera":
            print("Jugador 2 gana, tijera le gana a papel")
       

elif x == "tijera":
    if y == "papel":
        print("Jugador 1 gana, Tijera le gana a papel")
    elif x == "tijera":
        if y == "piedra":
            print("Jugador 2 gana, piedra le gana a tijera")
       
