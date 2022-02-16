# OpenBootcamp Curso Python Ejercicio 8

# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del
# archivo. Para ello, tendréis que acceder dos veces al archivo creado.
#
# Por último, tendréis que crear otro archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella,
# lo guardaréis en un archivo y luego lo cargamos.

from Vehiculo import Vehiculo


def main():
    crear = open("archivo.txt", "w")
    crear.write("OpenBootcamp")
    crear.close()

    leer = open("archivo.txt", "r")
    dato = leer.read()
    print(dato)
    leer.close()

    coche = Vehiculo("Rojo", 5, 4)

    nombreFileCoche = "cocheFile.txt"

    cocheFileCrea = open(nombreFileCoche, "w")
    cocheFile = open(nombreFileCoche, "a")
    cocheFile.write(f'El coche es de color {coche.color}.\n')
    cocheFile.write(f'El coche tiene {coche.numeroPuertas} puertas.\n')
    cocheFile.write(f'El coche tiene {coche.numeroRuedas} ruedas.')
    cocheFileCrea.close()
    cocheFile.close()

    cocheFileLeer = open(nombreFileCoche, "r")

    datos = None
    while datos != "":
        datos = cocheFileLeer.readline()
        print(datos)

    cocheFileLeer.close()


if __name__ == '__main__':
    main()
