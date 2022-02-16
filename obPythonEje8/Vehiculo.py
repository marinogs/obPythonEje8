# OpenBootcamp Curso Python Ejercicio 8

# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del
# archivo. Para ello, tendréis que acceder dos veces al archivo creado.
#
# Por último, tendréis que crear otro archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.

class Vehiculo:
    color = ""
    numeroPuertas = 0
    numeroRuedas = 0

    def __init__(self, color, puertas, ruedas):
        self.color = color
        self.numeroPuertas = puertas
        self.numeroRuedas = ruedas
