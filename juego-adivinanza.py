
import random
numero_secreto= random.randint(0,100)
cant_intentos=0
cant_max_intentos=5
adivinado= False

print("¡Bienvenido al juego de adivinar el número secreto!")

while not adivinado:
    if not  cant_intentos < cant_max_intentos:
        print("¡Has agotado tus intentos! El número secreto era:", numero_secreto)
        break
    entrada=input("Introduce un número del 1 al 99: ") 
    numero= int(entrada)
    if numero == numero_secreto:
        print("¡Felicitaciones, has adivinado en número secreto!")
        adivinado= True
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número secreto es menor al ingresado")
    cant_intentos += 1
