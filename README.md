# Calculadora por consola

Proyecto educativo: una calculadora que funciona por consola, escrita en Python puro (sin librerías externas).

## Funcionalidades

- Sumar, restar, multiplicar y dividir.
- Validación de números: rechaza entradas no numéricas con un mensaje claro.
- Control de la división por cero.
- Menú interactivo que permite hacer varias operaciones sin reiniciar.
- Opción para salir del programa.

## Requisitos

- Python 3 (las pruebas usan `unittest`, incluido en la instalación estándar).

## Instalación y uso

Cloná el repositorio y ejecutá el programa desde la raíz:

```bash
git clone <url-del-repositorio>
cd calculadora-python
python main.py
```

En el menú, elegí una operación del 1 al 5:

```
===== CALCULADORA =====
1) Sumar
2) Restar
3) Multiplicar
4) Dividir
5) Salir

Elegi una opcion:
```

## Ejecutar las pruebas

Desde la raíz del proyecto:

```bash
python -m unittest -v
```

## Estructura del proyecto

```
calculadora-python/
├── main.py                  # Menú e interacción con el usuario
├── calculadora.py           # Funciones matemáticas puras
├── validaciones.py          # Validación y conversión de entradas
├── tests/
│   ├── __init__.py          # Convierte tests/ en un paquete importable
│   └── test_calculadora.py  # Pruebas automáticas de las operaciones
└── README.md                # Este archivo
```

## Responsabilidades de cada módulo

- `main.py`: muestra el menú, pide la opción y los números, y muestra el resultado.
- `calculadora.py`: las cuatro funciones matemáticas (`sumar`, `restar`, `multiplicar`, `dividir`). No interactúan con el usuario.
- `validaciones.py`: pide números al usuario hasta obtener un valor válido (`ingresar_numero`) y un divisor distinto de cero (`ingresar_divisor`).
- `tests/test_calculadora.py`: verifica con `unittest` que las operaciones matemáticas devuelven los resultados esperados.