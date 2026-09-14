"""Punto de entrada de la calculadora por consola."""

from calculadora import dividir, multiplicar, restar, sumar
from validaciones import ingresar_divisor, ingresar_numero


def main():
    """Muestra el menu y ejecuta operaciones hasta que el usuario sale."""
    while True:
        print("===== CALCULADORA =====")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir")

        opcion = input("\nElegi una opcion: ")

        if opcion == "5":
            print("Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opcion invalida.")
            continue

        a = ingresar_numero("Ingresa el primer numero: ")

        if opcion == "4":
            b = ingresar_divisor("Ingresa el segundo numero: ")
        else:
            b = ingresar_numero("Ingresa el segundo numero: ")

        if opcion == "1":
            resultado = sumar(a, b)
        elif opcion == "2":
            resultado = restar(a, b)
        elif opcion == "3":
            resultado = multiplicar(a, b)
        elif opcion == "4":
            resultado = dividir(a, b)

        print("El resultado es:", resultado)


if __name__ == "__main__":
    main()