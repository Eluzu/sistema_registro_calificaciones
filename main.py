import os

NOMBRE_ARCHIVO = "notas.txt"

# --- Constantes Globales ---
CALIFICACION_MINIMA_APROBATORIA = 7
ESTADO_APROBADO = "APROBADO"
ESTADO_REPROBADO = "REPROBADO"

def guardar_registro_calificacion(nombre_estudiante: str, calificacion1: float, calificacion2: float, calificacion3: float) -> None:
    """
    Calcula el promedio de un estudiante, determina si aprobó y
    guarda el registro en un archivo.

    Args:
        nombre_estudiante (str): El nombre del estudiante.
        calificacion1 (float): La primera calificación.
        calificacion2 (float): La segunda calificación.
        calificacion3 (float): La tercera calificación.
    """

    if nombre_estudiante != "" and all(c >= 0 for c in [calificacion1, calificacion2, calificacion3]):
        
        promedio = (calificacion1 + calificacion2 + calificacion3) / 3
        estado = ESTADO_APROBADO if promedio >= CALIFICACION_MINIMA_APROBATORIA else ESTADO_REPROBADO

        # Usamos 'with open' para asegurar que el archivo se cierre automáticamente
        # y f-strings para una escritura de datos más limpia.
        with open(NOMBRE_ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{nombre_estudiante},{calificacion1},{calificacion2},"
                f"{calificacion3},{promedio:.2f},{estado}\n"
            )

        print("Registro guardado")

    else:
        print(f"Datos incorrectos para '{nombre_estudiante}': el nombre no puede estar vacío y las calificaciones deben ser positivas.")

def listar_registros() -> None:
    """Lee y muestra todos los registros del archivo de calificaciones en formato de tabla.

    Si el archivo no existe, imprime un mensaje informativo.
    Maneja y advierte sobre líneas con formato incorrecto en el archivo.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("No existen registros para mostrar.")
        return

    # 'with open' asegura el cierre del archivo incluso si hay errores.
    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        print("-" * 80)
        print(f"{'NOMBRE':<20} | {'C1':>5} | {'C2':>5} | {'C3':>5} | {'PROMEDIO':>10} | {'ESTADO':>12}")
        print("-" * 80)
        for linea in archivo:
            try:
                # Desempaquetado de la lista para mayor claridad
                nombre, c1, c2, c3, promedio, estado = linea.strip().split(",")
                print(f"{nombre:<20} | {c1:>5} | {c2:>5} | {c3:>5} | {promedio:>10} | {estado:>12}")
            except ValueError:
                print(f"Advertencia: Se omitió una línea con formato incorrecto: {linea.strip()}")
    print("-" * 80)


def generar_reporte_aprobados() -> None:
    """Cuenta y muestra un resumen del total de estudiantes aprobados y reprobados.

    Si el archivo no existe, imprime un mensaje informativo.
    Maneja y advierte sobre líneas con formato incorrecto al procesar el reporte.
    """
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("No existen registros para generar un reporte.")
        return

    aprobados = 0
    reprobados = 0

    with open(NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            try:
                # Leemos solo la parte que necesitamos (el estado)
                datos_registro = linea.strip().split(",")
                if datos_registro[5] == ESTADO_APROBADO:
                    aprobados += 1
                else:
                    reprobados += 1
            except (IndexError, ValueError):
                print(f"Advertencia: Se omitió una línea con formato incorrecto al generar el reporte: {linea.strip()}")

    print("\n--- Reporte Final ---")
    print(f"Total de Aprobados:  {aprobados}")
    print(f"Total de Reprobados: {reprobados}")
    print("---------------------\n")


# --- Ejecución del programa ---
# Limpiamos el archivo al inicio para una demostración limpia
if os.path.exists(NOMBRE_ARCHIVO):
    os.remove(NOMBRE_ARCHIVO)

guardar_registro_calificacion("Ana", 8, 9, 10)
guardar_registro_calificacion("Luis", 5, 6, 4)
guardar_registro_calificacion("Carlos", 7, 8, 6)

listar_registros()

generar_reporte_aprobados()
