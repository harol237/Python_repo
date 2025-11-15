  
import random  # Importa el módulo que genera números aleatorios

Nsecreto = random.randint(1, 100)
# variable 
intentos = 5 

print("Piensa en un número entre 1 y 100... Tienes", intentos, "intentos")  # Genera un número secreto entre 1 y 100
# esa bucle se genera mientras que el cliente tiene intentos
while intentos > 0:
    intentos -= 1
    numero = int(input("Ingresa tu número: "))

    if numero == Nsecreto:
        print(" Super !!!! Adivinaste el número secreto ")
        break
    
    else:
        print("Casi estàs.. sigues así")

if intentos == 0 and numero != Nsecreto:
    print(" Ya no te quedan intentos... El número era:", Nsecreto) 