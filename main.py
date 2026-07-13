import os

NOMBRE_ARCHIVO = "notas.txt"

def guardar_registro_calificacion(nombre_estudiante, calificacion1, calificacion2, calificacion3):

    if nombre_estudiante != "" and calificacion1 >= 0 and calificacion2 >= 0 and calificacion3 >= 0:
        
        promedio = (calificacion1 + calificacion2 + calificacion3) / 3

        if promedio >= 7:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        archivo = open(NOMBRE_ARCHIVO, "a")

        archivo.write(
            nombre_estudiante + "," +
            str(calificacion1) + "," +
            str(calificacion2) + "," +
            str(calificacion3) + "," +
            str(promedio) + "," +
            estado + "\n"
        )

        archivo.close()

        print("Registro guardado")

    else:
        print("Datos incorrectos")

def listar_registros():

    if os.path.exists(NOMBRE_ARCHIVO):

        archivo = open(NOMBRE_ARCHIVO)

        print("-" * 70)
        for linea in archivo:

            datos_registro = linea.strip().split(",")

            print(
                datos_registro[0],
                datos_registro[1],
                datos_registro[2],
                datos_registro[3],
                datos_registro[4],
                datos_registro[5]
            )

        archivo.close()

    else:
        print("No existen registros")

def generar_reporte_aprobados():

    if os.path.exists(NOMBRE_ARCHIVO):

        archivo = open(NOMBRE_ARCHIVO)

        aprobados = 0
        reprobados = 0

        for linea in archivo:

            datos_registro = linea.strip().split(",")

            if datos_registro[5] == "APROBADO":
                aprobados += 1
            else:
                reprobados += 1
        
        archivo.close()

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)

guardar_registro_calificacion("Ana", 8, 9, 10)
guardar_registro_calificacion("Luis", 5, 6, 4)
guardar_registro_calificacion("Carlos", 7, 8, 6)

listar_registros()

generar_reporte_aprobados()