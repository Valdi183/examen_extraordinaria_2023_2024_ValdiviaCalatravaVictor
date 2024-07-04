"""
El archivo main ejecuta el programa para gestionar tareas heredando de la clase creada anteriormente para
poder agregar, eliminar y mostrar tareas. Para ello se le muestra un menu al usuario con las distintas opciones.
La función main es la que ejecuta las acciones que le pida el usuario 
"""

from Gestor_tareas import GestorDeTareas

def mostrar_menu():
    print("\nMenú de Gestión de Tareas")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Mostrar tareas")
    print("4. Salir")

def main():
    gestor = GestorDeTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea (opcional): ")
            gestor.agregar_tarea(titulo, descripcion)
        elif opcion == "2":
            titulo = input("Ingrese el título de la tarea a eliminar: ")
            gestor.eliminar_tarea(titulo)
        elif opcion == "3":
            gestor.mostrar_tareas()
        elif opcion == "4":
            print("Saliendo del programa")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()