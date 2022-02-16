# OpenBootcamp Curso Pyhton Ejercicio 7

# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar,
# multiplicar y dividir.
#
# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que
# mostrarlos por consola.

from Calculadora import Calculadora

a = 10
b = 5
calculadora = Calculadora()
print("La suma de", a, "mas", b, "es", calculadora.sumar(a, b))
print("La resta de", a, "menos", b, "es", calculadora.restar(a, b))
print("La multiplicación de", a, "por", b, "es", calculadora.multiplicar(a, b))
print("La división de", a, "entre", b, "es", int(calculadora.dividir(a, b)))

