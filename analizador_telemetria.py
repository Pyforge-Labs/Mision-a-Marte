with open("telemetria.txt", "r") as tl:
    filas = [linea.split(",") for linea in tl.read().splitlines()]

for i, fila in enumerate(filas):
    for j, elemento in enumerate(fila):
        filas[i][j] = elemento.strip()

for fila in filas:
    try:
        fila[2] = float(fila[2])
        if -50 < fila[2] < 100:
            pass
        else:
            fila[2] = None  
    except ValueError:
        fila[2] = None

print(filas)