
"""
Programa: Preferencias musicales 

Tema: Música
Este programa pide al usuario datos sobre sus hábitos y gustos musicales,realiza operaciones simples, usa tipos de variables y constantes,
y muestra los resultados al usuario.

Variables utilizadas:
- nombre (str): nombre del usuario
- edad (int): edad del usuario
- escucha_diaria (float): horas que escucha música al día
- artista_favorito (str): nombre de su artista favorito
- MAYOR_EDAD (constante int): edad legal de mayoría (18)

Mi código Pide datos al usuario, muestra información en pantalla, usa conversiones de datos, aplica operadores aritméticos, de comparación y lógicos
"""
# Titulo 
print("Bienvenido a mi mundo musical\n")

# Constante
MAYOR_EDAD = 18

# Solicitud de datos al usuario
nombre = input("Cómo te llamas? ")
edad = int(input("Cuántos años tienes? "))
escucha_diaria = float(input("Cuántas horas al día escuchas música? "))
artista_favorito = input("Quién es tu artista favorito/a? ")
tipo_musica = input(" ¿Qué tipo de música escuchas? ")

# Operaciones con variables
horas_semanales = escucha_diaria * 7
es_mayor = edad >= MAYOR_EDAD
escucha_mucho = escucha_diaria > 3.0

# Impresión
print("\n Hola,", nombre)
print("Tienes", edad, "años y escuchas aproximadamente", horas_semanales, "horas de música por semana.")
print("Tu artista favorito/a es:", artista_favorito)
print("Escuchas musica de tipo:",tipo_musica)

 
if es_mayor and escucha_mucho:
    print("Eres mayor de edad y un verdadero amante de la música. 🎶")
elif es_mayor and not escucha_mucho:
    print("Eres mayor de edad pero podrías escuchar un poco más de música. 😉")
else:
    print("Aún eres menor, ¡pero buena elección musical! 👍")


edad_str = str(edad)
print("Tu edad como texto sería: " + edad_str)