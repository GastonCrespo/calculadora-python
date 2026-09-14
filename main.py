"""Punto de entrada de la calculadora por consola."""

from calculadora import dividir, multiplicar, restar, sumar


def main():
    """Muestra el menu y ejecuta una operacion."""
    print("===== CALCULADORA =====")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")

    opcion = input("\nElegi una opcion: ")

    primer_numero = input("Ingresa el primer numero: ")
    segundo_numero = input("Ingresa el segundo numero: ")

    a = float(primer_numero)
    b = float(segundo_numero)

    if opcion == "1":
        resultado = sumar(a, b)
    elif opcion == "2":
        resultado = restar(a, b)
    elif opcion == "3":
        resultado = multiplicar(a, b)
    elif opcion == "4":
        resultado = dividir(a, b)
    else:
        print("Opcion invalida.")
        return

    print("El resultado es:", resultado)


if __name__ == "__main__":
    main()