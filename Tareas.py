"""
Este archivo del ejercicio 3 contiene la clase Tarea
"""

class Tarea:
    def __init__(self, titulo:str, descripción = ""):
        self.titulo = titulo
        self.descripcion = descripción

    def __str__(self):
        return f"Título: {self.titulo}\nDescripción: {self.descripcion}"
