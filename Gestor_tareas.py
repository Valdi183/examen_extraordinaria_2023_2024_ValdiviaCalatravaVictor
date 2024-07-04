"""
Este archivo contiene a la clase GestorDeTareas que hereda de Tareas para poder agregar, eliminar, o mostrar
tareas al usuario. Para ello se crea una lista que contendrá las tareas, despues se crea una clase para cada
accion. En agrgar tareas se añade la tarea a la lista, en eliminar tareas se elimina de la lista la tarea que
que se quiera (poniendo su titulo y buscandolo en la lista) y para mostrarla se itera sobre la lista de tareas
mostrando cada elemento.
"""

from Tareas import Tarea

class GestorDeTareas(Tarea):
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion=""):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{titulo}' agregada exitosamente.")

    def eliminar_tarea(self, titulo):
        for tarea in self.tareas:
            if tarea.titulo == titulo:
                self.tareas.remove(tarea)
                print(f"Tarea '{titulo}' eliminada exitosamente.")
                return
        print(f"Tarea con título '{titulo}' no encontrada.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas para mostrar.")
        else:
            for tarea in self.tareas:
                print(tarea)
                print("-" * 20)