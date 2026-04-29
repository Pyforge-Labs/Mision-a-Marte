passElements = 0
passNone = 0

with open("telemetria.txt", "r") as tl:
    filas = [linea.split(",") for linea in tl.read().splitlines()]

for i, fila in enumerate(filas):
    for j, elemento in enumerate(fila):
        filas[i][j] = elemento.strip()

for fila in filas:
    try:
        fila[2] = float(fila[2])
        if -50 < fila[2] < 100:
            passElements += 1   
        else:
            passNone += 1      
            fila[2] = None  
    except (ValueError, IndexError):
        passNone += 1          
        if len(fila) > 2:
            fila[2] = None

print("\n=== RESULTADOS ===")
print(f"Lecturas válidas  : {passElements}")
print(f"Lecturas inválidas: {passNone}")

print("\n=== DATOS PROCESADOS ===")
for fila in filas:
    print(fila)