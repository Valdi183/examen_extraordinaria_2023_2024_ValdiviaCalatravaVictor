"""
Este es el ejercicio_2 del examen. Se trata de un programa que calcula los factores primos de un numero
cualquiera mayor a 1 introducido por el usuario
"""
# Esta funcion verifica si el numero es o no primo
def verificar_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Esta funcion se encarga de factorizar el numero dado por el usuario
def factores_primos(num):
    factores = []
    divisor = 2
    while num > 1:
        while num % divisor == 0:
            factores.append(divisor)
            num //= divisor
        divisor += 1
        if divisor * divisor > num:
            if num > 1:
                factores.append(num)
            break
    return factores


# Esta funcion pide al usuario un numero entero mayor que 1 y verifica los posibles errores de inputs
def main():
    while True:
        try:
            num = int(input("Introduce un número entero mayor a 1: "))
            if num <= 1:
                raise ValueError("El número debe ser mayor a 1.")
            break
        except ValueError as e:
            print(e)
            continue
    factores = factores_primos(num)
    print(f"Los factores primos de {num} son: {factores}")

# LLama a la función que ejecuta el programa, si esta se encuentra en el archivo original
if __name__ == "__main__":
    main()