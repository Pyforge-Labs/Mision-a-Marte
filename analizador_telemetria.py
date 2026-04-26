with open("telemetria.txt", "r") as tl:
    filas = [linea.split(",") for linea in tl.read().splitlines()]

for i, fila in enumerate(filas):
    for j, elemento in enumerate(fila):
        filas[i][j] = elemento.strip()

print(filas)