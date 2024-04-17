import random

def adivinar_numero_secreto():
    numero_secreto = random.randint(1,50)
    vidas = 5
    print ("¡Bienvenido!")
    print ("Para este juego la computadora eligió un número aleatorio entre 1 y 50, cuentas con 5 vidas para adivinarlo. La computadora te ayudará. ¡Suerte!")
    
    while vidas > 0:
        eleccion_user = int(input("Ingresá un numero del 1 al 50 ->"))
        if eleccion_user > numero_secreto:
            print ("El número secreto es menor. Intentá otra vez")
            vidas -= 1
            print (f"Te quedan {vidas} vidas")
        elif eleccion_user < numero_secreto:
            print ("El número secreto es mayor. Intentá otra vez")
            vidas -= 1
            print (f"Te quedan {vidas} vidas")
        else:
            print ("¡Felicitaciones! Adivinaste el número secreto")
            break
    if vidas == 0:
        print (f"Te quedaste sin vidas ☹. El número secreto era {numero_secreto}")
        
        
def revancha():
    while True:
        adivinar_numero_secreto()
        jugar_de_nuevo = input("Querés jugar otra vez (s/n) ->")
        if jugar_de_nuevo != "s":
            print ("Gracias por jugar, hasta la próxima")
            break

revancha()