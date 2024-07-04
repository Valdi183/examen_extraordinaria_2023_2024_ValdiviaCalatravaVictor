"""
Este archivo ejecuta el programa final, creando los coches correspondientes que participaran en la carrera
y define los parametros necesarios para iniciar la carrera. El programa muestra cada segundo la posición de
todos los coches. En el ultimo tiempo, se decide el ganador, que será el que ocupe la posición más alta de 
entre los tres coches participantes
"""

from coche import Coche
from carrera import Carrera

def main():
    # Crear coches
    coche1 = Coche(nombre="Coche1", velocidad_maxima=150.0, aceleracion=5.0)
    coche2 = Coche(nombre="Coche2", velocidad_maxima=160.0, aceleracion=4.5)
    coche3 = Coche(nombre="Coche3", velocidad_maxima=155.0, aceleracion=4.8)

    # Crear carrera y agregar coches
    carrera = Carrera()
    carrera.agregar_coche(coche1)
    carrera.agregar_coche(coche2)
    carrera.agregar_coche(coche3)

    # Iniciar la carrera
    duracion = 20.0  # Duración total de la carrera en segundos
    intervalo = 1.0  # Intervalo de tiempo en segundos
    carrera.iniciar_carrera(duracion, intervalo)

if __name__ == "__main__":
    main()