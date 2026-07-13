import os

NOMBRE_ARCHIVO = "notas.txt"

def guardar_registro_calificacion(nombre_estudiante, calificacion1, calificacion2, calificacion3):
    """
    Calcula el promedio de un estudiante, determina si aprobó y
    guarda el registro en un archivo.
    """
    if nombre_estudiante != "" and all(c >= 0 for c in [calificacion1, calificacion2, calificacion3]):
        
        promedio = (calificacion1 + calificacion2 + calificacion3) / 3
        estado = "APROBADO" if promedio >= 7 else "REPROBADO"

        # Usamos 'with open' para asegurar que el archivo se cierre automáticamente.
        # Usamos f-string para una escritura más limpia y formateamos el promedio.
        with open(NOMBRE_ARCHIVO, "a") as archivo:
            archivo.write(
                f"{nombre_estudiante},{calificacion1},{calificacion2},"
                f"{calificacion3},{promedio:.2f},{estado}\n"
            )

        print("Registro guardado")

    else:
        print("Datos incorrectos: el nombre no puede estar vacío y las calificaciones deben ser positivas.")

def listar_registros():
    """Lee y muestra todos los registros del archivo de calificaciones."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("No existen registros para mostrar.")
        return

    # 'with open' asegura el cierre del archivo incluso si hay errores.
    with open(NOMBRE_ARCHIVO, "r") as archivo:
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


def generar_reporte_aprobados():
    """Cuenta y muestra el total de estudiantes aprobados y reprobados."""
    if not os.path.exists(NOMBRE_ARCHIVO):
        print("No existen registros para generar un reporte.")
        return

    aprobados = 0
    reprobados = 0

    with open(NOMBRE_ARCHIVO, "r") as archivo:
        for linea in archivo:
            try:
                # Leemos solo la parte que necesitamos (el estado)
                datos_registro = linea.strip().split(",")
                if datos_registro[5] == "APROBADO":
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
