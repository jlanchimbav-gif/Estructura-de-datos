"""
Ejercicio 1: Gestión de persistencia y lectura en archivos planos (.txt)

Programa que:
  1. Escribe en 'estudiantes.txt' los nombres completos de cinco (5)
     estudiantes universitarios (un registro por línea).
  2. Lee el archivo en modo lectura y muestra su contenido en consola.
  3. Controla excepciones con try-except (FileNotFoundError y errores
     generales de E/S) para que el programa no termine de forma abrupta.

Compatible con Google Colab y ejecución local.
"""

NOMBRE_ARCHIVO = "estudiantes.txt"
CANTIDAD_ESTUDIANTES = 5


def solicitar_estudiantes(cantidad):
    """Solicita por consola los nombres completos de los estudiantes.

    Valida que cada nombre no esté vacío y tenga al menos nombre y apellido.
    """
    estudiantes = []
    print(f"Ingrese los nombres completos de {cantidad} estudiantes.\n")
    while len(estudiantes) < cantidad:
        try:
            nombre = input(f"Estudiante {len(estudiantes) + 1} de {cantidad}: ").strip()
            nombre = " ".join(nombre.split())  # normaliza espacios
            if len(nombre.split()) < 2:
                raise ValueError("Debe ingresar al menos un nombre y un apellido.")
            estudiantes.append(nombre.title())
        except ValueError as error:
            print(f"  [Entrada inválida] {error}")
        except (EOFError, KeyboardInterrupt):
            print("\n  [Aviso] Entrada interrumpida. Se detiene la captura de datos.")
            break
    return estudiantes


def escribir_archivo(nombre_archivo, estudiantes):
    """Crea el archivo y guarda un estudiante por línea (modo escritura)."""
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for estudiante in estudiantes:
                archivo.write(estudiante + "\n")
        print(f"\n[OK] Se guardaron {len(estudiantes)} registros en '{nombre_archivo}'.")
        return True
    except PermissionError:
        print(f"[Error] No hay permisos para escribir en '{nombre_archivo}'.")
    except OSError as error:
        print(f"[Error de E/S] No fue posible escribir el archivo: {error}")
    return False


def leer_archivo(nombre_archivo):
    """Lee el archivo de forma segura y muestra su contenido en consola."""
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"[Error] El archivo '{nombre_archivo}' no fue localizado.")
    except Exception as error:  # fallos generales del sistema
        print(f"[Error general] Ocurrió un problema al leer el archivo: {error}")
    else:
        print(f"\n=== Contenido de '{nombre_archivo}' ===")
        for numero, estudiante in enumerate(lineas, start=1):
            print(f"{numero}. {estudiante}")
        print(f"=== Total de registros: {len(lineas)} ===")
    finally:
        print("[Info] Proceso de lectura finalizado.")


def main():
    estudiantes = solicitar_estudiantes(CANTIDAD_ESTUDIANTES)
    if estudiantes and escribir_archivo(NOMBRE_ARCHIVO, estudiantes):
        leer_archivo(NOMBRE_ARCHIVO)

    # Demostración del control de excepciones: archivo inexistente
    print("\n--- Prueba de FileNotFoundError (archivo inexistente) ---")
    leer_archivo("archivo_que_no_existe.txt")


if __name__ == "__main__":
    main()






