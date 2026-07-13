import os

ARCHIVO = "notas.txt"

def p(n, c1, c2, c3):

    if n != "" and c1 >= 0 and c2 >= 0 and c3 >= 0:
        
        pr = (c1 + c2 + c3) / 3

        if pr >= 7:
            e = "APROBADO"
        else:
            e = "REPROBADO"

        f = open(ARCHIVO, "a")

        f.write(
            n + "," +
            str(c1) + "," +
            str(c2) + "," +
            str(c3) + "," +
            str(pr) + "," +
            e + "\n"
        )

        f.close()

        print("Registro guardado")

    else:
        print("Datos incorrectos")

def l():

    if os.path.exists(ARCHIVO):

        f = open(ARCHIVO)

        print("-" * 70)
        for x in f:

            d = x.strip().split(",")

            print(
                d[0],
                d[1],
                d[2],
                d[3],
                d[4],
                d[5]
            )

        f.close()

    else:
        print("No existen registros")

def r():

    if os.path.exists(ARCHIVO):

        f = open(ARCHIVO)

        aprobados = 0
        reprobados = 0

        for x in f:

            d = x.strip().split(",")

            if d[5] == "APROBADO":
                aprobados += 1
            else:
                reprobados += 1

        f.close()

        print("Aprobados:", aprobados)
        print("Reprobados:", reprobados)

p("Ana", 8, 9, 10)
p("Luis", 5, 6, 4)
p("Carlos", 7, 8, 6)

l()

r()