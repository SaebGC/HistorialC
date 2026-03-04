import os 
from colorama import init, Fore, Style

init()

print("Calculadora sencilla")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b 

historial = []

while True: 
    print("Seleccione una funcion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar") 
    print("4. Dividir")
    print("5. Salir")
    print("6. Historial")

    opcion = input("Ingrese su opcion (1/2/3/4/5/6): ")
    if opcion == '5':
        print("Saliendo de la calculadora.")
        break

    elif opcion == '6':
        if len(historial) == 0:
            print("No hay operaciones aun.")
        else:
            for i, entrada in enumerate(historial, 1):
                print(f"{i}. {entrada}")
        
    else:
    
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
 
        if opcion == '1':
            print(Fore.GREEN + f"Resultado: {sumar(num1, num2)}" + Style.RESET_ALL)
            historial.append(f"{num1} + {num2} = {sumar(num1, num2)}")
            
        elif opcion == '2':
                print(Fore.RED + f"Resultado: {restar(num1, num2)}" + Style.RESET_ALL)
                historial.append(f"{num1} - {num2} = {restar(num1, num2)}")

        elif opcion == '3':
                print(Fore.BLUE + f"Resultado: {multiplicar(num1, num2)}" + Style.RESET_ALL)
                historial.append(f"{num1} * {num2} = {multiplicar(num1, num2)}")

        elif opcion == '4':
            if num2 == 0:
                print(Fore.RED + "Error: No se puede dividir por cero." + Style.RESET_ALL)
                historial.append(f"{num1} / {num2} = Error (division por cero)")
            print(Fore.YELLOW + f"Resultado: {dividir(num1, num2)}" + Style.RESET_ALL)
            historial.append(f"{num1} / {num2} = {dividir(num1, num2)}")

        else:
            print("Opcion no valida. Por favor, intente de nuevo.")

        input ("Presione cualquier tecla para reiniciar...")
        os.system('clear')  

