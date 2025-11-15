# EJERCICIO COMPLETO: DOMINANDO LOS OPERADORES EN PYTHON
# Completa los espacios, responde las preguntas y corrige los errores

# ========== PARTE 1: OPERADORES ARITMÉTICOS ==========
print("=== PARTE 1: Operadores Aritméticos ===")

num1 = 20
num2 = 6

resultado_suma = num1 + num2          # Debe dar 26
resultado_resta = num1 - num2         # Debe dar 14
resultado_mult = num1 * num2          # Debe dar 120
resultado_div = num1 / num2           # Debe dar 3.33...
resultado_div_entera = num1 // num2   # Debe dar 3
resultado_modulo = num1 % num2        # Debe dar 2
resultado_potencia = num1 ** num2     # Debe dar 64,000,000

# Corrige el error en esta expresión
resultado_corregido = 10 + 5 * 2      # Resultado actual: 20
# ¿Cómo lo corregirías para que dé 30? resultado_corregido = (10 + 5) * 2    Ahora el resultado es 30

# ========== PARTE 2: OPERADORES DE COMPARACIÓN ==========
print("\n=== PARTE 2: Operadores de Comparación ===")

a = 15
b = 10
c = 15

# Escribe el resultado esperado (True/False)
comp1 = a > b          # True
comp2 = a == c         # True
comp3 = b != a         # True
comp4 = a <= c         # False
comp5 = 20 >= a        # True

# Explica qué hace esta expresión combinada
edad = 25
altura = 175
expresion_compleja = (edad >= 18) and (altura > 160)
# Explicación de la epresión: Verifica si la persona es mayor de edad y tambien si mide más de 160 cm

# ========== PARTE 3: OPERADORES LÓGICOS ==========
print("\n=== PARTE 3: Operadores Lógicos ===")

# Completa con and, or, not
es_fin_de_semana = True
tengo_dinero = False
hace_buen_tiempo = True

puedo_salir = es_fin_de_semana and (tengo_dinero or hace_buen_tiempo)
# ¿Cuándo puedo salir?
# Puedo salir si es_fin_de_semana y si tengo_dinero o hace_buen_tiempp

es_adulto = True
es_estudiante = False
tiene_descuento = not es_estudiante or (edad > 65)
# ¿Quién tiene descuento?
# Tiene descuento quien NO es estudiante o es mayor de 65 años

# ========== PARTE 4: OPERADORES DE ASIGNACIÓN ==========
print("\n=== PARTE 4: Operadores de Asignación ===")

x = 10
y = 5
z = 2

x = x + (y * z)             # x = 10 + (5 * 2) = 20
# ¿Cuál es el valor final de x? 20

# ========== PARTE 5: EXPRESIONES COMPLEJAS ==========
print("\n=== PARTE 5: Expresiones Complejas ===")

precio = 100
descuento = 20
iva = 21
es_cliente_frecuente = True
tiene_cupon = False

# Expresión 1: Calcula el precio final con descuento e IVA
precio_final = (precio - descuento) * (1 + iva/100)
# Explica paso a paso:
# - Se resta el descuento: 100 - 20 = 80
# - Se aplica el IVA: 80 * (1 + 0.21) = 96.8
# al final tenemos: 96.8

# Expresión 2: Condición compleja para descuento extra
descuento_extra = es_cliente_frecuente or (tiene_cupon and (precio > 50))
# ¿Cuándo hay descuento extra?
# Hay descuento extra si el cliente es frecuente o si tiene cupón y que el precio supera 50

# Expresión 3: Múltiples condiciones
puede_comprar = (precio_final <= 150) and (tiene_cupon or es_cliente_frecuente)
# ¿Quién puede comprar?
# Puede comprar quien tiene el precio final menor o igual a 150 y si es cliente frecuente o tiene cupón

# ========== PARTE 6: CORRECCIÓN DE ERRORES ==========
print("\n=== PARTE 6: Corrección de Errores ===")

# 1. resultado = 10 + * 5           # Error: (*) no puede ir tras el (+)
#    Corrección: resultado = 10 + 5

# 2. if edad = 18:                  # Error: = es asignación y no comparación
#    Corrección: if edad == 18:

# 3. valor = "10" + 5               # Error: no se puede sumar (str) con (int)
#    Corrección: valor = int("10") + 5  

# 4. if a > b and or c:             # Error: sintaxis incorrecta con "and or" 
#    Corrección: if a > b and c: ou bien if a > b or c:

print("\n¡Ejercicio completado! Revisa todas tus respuestas.")