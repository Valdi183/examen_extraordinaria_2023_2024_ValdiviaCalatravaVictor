"""
Este archivo contiene la clase Coche que define el coche (con sus atributos correspondientes de la clase init)
y ademas una funcion dentro de la clase Coche que se encarga de mover el coche cambiando su velocidad y posicion.
Por ultimo la clase str que devuelve el nombre del coche y la posicion que ocupa
"""

class Coche:
    def __init__(self, nombre, velocidad_maxima, aceleracion):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.aceleracion = aceleracion
        self.posicion = 0.0
        self.velocidad = 0.0

    def mover(self, tiempo):
        # Actualiza la velocidad del coche
        nueva_velocidad = self.velocidad + self.aceleracion * tiempo
        if nueva_velocidad > self.velocidad_maxima:
            nueva_velocidad = self.velocidad_maxima
        self.velocidad = nueva_velocidad

        # Actualiza la posición del coche
        self.posicion += self.velocidad * tiempo

    def __str__(self):
        return f"{self.nombre} - Posición: {self.posicion:.2f}"