"""
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
"""

def countdown(number):
    if number >= 0:
        print(number)    
        countdown(number - 1)


def factorial(number):
    if number < 0:
        print("Los números negativos no tienen factorial")
    elif number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


def fibonacci(position):
    if position == 0:
        print("La posición ha de ser mayor que '0'")
    elif position == 1:
        return 0
    elif position == 2:
        return 1
    else:
        return fibonacci(position - 1) + fibonacci(position - 2)


number = int(input("Introduzca un número para imprimir, usando\nrecursividad, desde ese número hasta '0': "))
countdown(number)

number = int(input("Introduzca un número para calcular su factorial: "))
print(f"El factorial de {number} es {factorial(number)}")

number = int(input("Introduzca una posición para calcular su valor en la serie de Fibonacci: "))
print(f"El valor de la posición {number} en la serie es {fibonacci(number)}")