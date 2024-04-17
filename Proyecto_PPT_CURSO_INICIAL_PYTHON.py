import random

def partida ():
    opciones = ['piedra', 'papel', 'tijeras']
    elección_computadora = random.choice(opciones)

    while True:
        elección_user = input("Elige piedra, papel o tijeras -> ")
        if elección_user not in opciones:
            print("Elección no valida, recuerda atenerte a las opciones")
        else:
            break

    if elección_user == elección_computadora:
        print("Tu elección:", elección_user)
        print("Elección de la computadora:", elección_computadora)
        print("Empate :/")
    elif elección_user == "piedra" and elección_computadora == "tijeras" or elección_user == "tijeras" and elección_computadora == "papel" and elección_user == "papel" and elección_computadora == "piedra":
        print("Tu elección:", elección_user)
        print("Elección de la computadora:", elección_computadora)
        print("¡Ganaste! :)")
    else:
        print("Tu elección:", elección_user)
        print("Elección de la computadora:", elección_computadora)
        print("Perdiste :(")
    

def revancha():
    while True:
        partida()
        volver_a_jugar = input("¿Revancha? (s/n) -> ")
        if volver_a_jugar != 's':
            print ("Buen juego, hasta la próxima")
            break

revancha()