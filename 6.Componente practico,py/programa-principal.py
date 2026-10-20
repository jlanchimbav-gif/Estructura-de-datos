# ==============================
# GRUPO NRO: [X] | INTEGRANTES: [Lista de nombres7]
# PROYECTO: Componente Práctico 1 - Menú Integrador
# ==============================

import csv

# ------------------------------
# OPCIÓN 1: Vector de 10 posiciones (pares, impares y promedios)
# ------------------------------
def opcion1_vector():
    print("\n--- OPCIÓN 1: Vector de 10 posiciones ---")
    vector = []
    for i in range(10):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        vector.append(valor)

    pares = [x for x in vector if x % 2 == 0]
    impares = [x for x in vector if x % 2 != 0]

    print("Valores pares:", pares)
    print("Valores impares:", impares)
    if pares:
        print("Promedio pares:", sum(pares)/len(pares))
    if impares:
        print("Promedio impares:", sum(impares)/len(impares))


# ------------------------------
# OPCIÓN 2: Arreglo de n elementos (máximo, mínimo y promedio)
# ------------------------------
def opcion2_arreglo():
    print("\n--- OPCIÓN 2: Arreglo de n elementos ---")
    n = int(input("Ingrese la cantidad de elementos: "))
    arreglo = []
    for i in range(n):
        valor = int(input(f"Ingrese el valor {i+1}: "))
        arreglo.append(valor)

    print("Máximo:", max(arreglo))
    print("Mínimo:", min(arreglo))
    print("Promedio:", sum(arreglo)/len(arreglo))


# ------------------------------
# OPCIÓN 3: Suma y resta de matrices bidimensionales
# ------------------------------
def opcion3_matrices():
    print("\n--- OPCIÓN 3: Suma y resta de matrices ---")
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))

    matriz1 = [[int(input(f"Matriz1[{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]
    matriz2 = [[int(input(f"Matriz2[{i}][{j}]: ")) for j in range(columnas)] for i in range(filas)]

    suma = [[matriz1[i][j] + matriz2[i][j] for j in range(columnas)] for i in range(filas)]
    resta = [[matriz1[i][j] - matriz2[i][j] for j in range(columnas)] for i in range(filas)]

    print("Matriz 1:", matriz1)
    print("Matriz 2:", matriz2)
    print("Suma:", suma)
    print("Resta:", resta)


# ------------------------------
# OPCIÓN 4: Registro y lectura segura de estudiantes.txt
# ------------------------------
def opcion4_txt():
    print("\n--- OPCIÓN 4: Registro y lectura segura de estudiantes.txt ---")
    try:
        with open("estudiantes.txt", "w") as f:
            for i in range(5):
                nombre = input(f"Ingrese nombre completo del estudiante {i+1}: ")
                f.write(nombre + "\n")

        with open("estudiantes.txt", "r") as f:
            print("\nContenido del archivo estudiantes.txt:")
            print(f.read())

    except FileNotFoundError:
        print("Error: El archivo no existe.")
    except Exception as e:
        print("Error inesperado:", e)


# ------------------------------
# OPCIÓN 5: Procesamiento de ventas.csv
# ------------------------------
def opcion5_csv():
    print("\n--- OPCIÓN 5: Procesamiento de ventas.csv ---")
    try:
        with open("ventas.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Producto", "Cantidad", "Precio"])
            for i in range(5):
                producto = input("Producto: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                writer.writerow([producto, cantidad, precio])

        with open("ventas.csv", "r") as f:
            reader = csv.reader(f)
            next(reader)  # saltar cabecera
            print("\nInforme de ingresos:")
            for fila in reader:
                try:
                    producto, cantidad, precio = fila
                    ingreso = int(cantidad) * float(precio)
                    print(f"{producto}: ${ingreso:.2f}")
                except ValueError:
                    print("Error en datos:", fila)

    except Exception as e:
        print("Error inesperado:", e)


# ------------------------------
# MENÚ PRINCIPAL
# ------------------------------
def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Vector de 10 posiciones")
        print("2. Arreglo de n elementos")
        print("3. Suma y resta de matrices")
        print("4. Registro y lectura de estudiantes.txt")
        print("5. Procesamiento de ventas.csv")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion1_vector()
        elif opcion == "2":
            opcion2_arreglo()
        elif opcion == "3":
            opcion3_matrices()
        elif opcion == "4":
            opcion4_txt()
        elif opcion == "5":
            opcion5_csv()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# ------------------------------
# EJECUCIÓN
# ------------------------------
if __name__ == "__main__":
    menu()
