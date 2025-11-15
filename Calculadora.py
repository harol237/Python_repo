"""
                        ------ CALCULADORA TRADITIONAL ------------
Este programa es una calculadora simple en Python que permite al usuario realizar operaciones matemáticas básicas:
Suma, Resta, Multiplicación, División normal, División entera, Potencia, Resto o módulo.
"""
print (" --- CALCULADORA TRADITIONAL ---")


seguir = "s"
while seguir == "s":
    a= float(input("Introduce el primer valor que quieras calcular: \n"))
    b= float(input("Introduce el segundo valor que quieras calcular: \n"))
    op = input (" Introduce la operacion que quieras realizar: + - * / // ** % :")
    
    if op == '+' :
        print (a+b)
    elif op == '-':
        print (a-b)
    elif op == '*':
        print (a*b)
    elif op == '/':
        if b == 0:
            print(" Error: no se puede dividir entre cero")
        else :
            print(f" Resultado: {a/b} ")
    elif op == '//':
        if b == 0:
            print(" Error: no se puede dividir entre cero")
        else :
            print(f"Resultado: {a // b}")
    elif op == '**':
        if b == 0:
            print(" Error: no se puede dividir entre cero")
        else :
            print(f" Resultado: {a/b} ")
        print(f"Resultado: {a ** b}")
    elif op == '%':
        print(f"Resultado: {a%b}")
    else:
        print (" Valor introducido no valido ")
        
    seguir = input(" Quieres hacer otra operación? (s/n): ")

print("Gracias por usar la calculadora")