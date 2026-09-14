"""Validacion y conversion de datos ingresados por el usuario."""


def ingresar_numero(mensaje):
    """Pide un numero al usuario hasta que ingresa un valor valido."""
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except ValueError:
            print("Eso no es un numero valido. Intenta de nuevo.")