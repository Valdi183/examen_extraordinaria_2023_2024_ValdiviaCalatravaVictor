""" 
Este archivo contiene a la clase Carrera que hereda de coche que crea una lista con todos los coches y tiene varios metodos 
de forma que se puedan agregar coches a la lista (participantes de la carrera), iniciar la  carrera y decidir
el ganador.
"""

from coche import Coche

class Carrera(Coche):
    def __init__(self):
        self.coches = []

    def agregar_coche(self, coche):
        self.coches.append(coche)

    def iniciar_carrera(self, duracion, intervalo):
        tiempo_actual = 0.0

        while tiempo_actual < duracion:
            print(f"\nTiempo: {tiempo_actual:.2f}")
            for coche in self.coches:
                coche.mover(intervalo)
                print(coche)
            tiempo_actual += intervalo

        # Determinar el ganador
        ganador = max(self.coches, key=lambda coche: coche.posicion)
        print(f"\nGanador: {ganador.nombre} - Posición final: {ganador.posicion:.2f}")