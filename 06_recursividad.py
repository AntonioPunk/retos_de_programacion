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

def function_recur(number):
    if number >= 0:
        print(number)    
        function_recur(number - 1)


def factorial(num):
    if number < 0:
        print("Los numeros negativos no tienen factorial")
    elif num <= 1:
        return 1
    else:
        return num * factorial(num - 1)


number = int(input("Introduzca un numero para imprimir,usando\nrecursividad, desde ese numero hasta '0': "))
function_recur(number)

number2 = int(input("Introduzca un numero para calcular su factorial: "))
print(f"El factorial de {number2} es {factorial(number2)}")
