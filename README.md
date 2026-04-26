# Reto: Analizador de Telemetría de la NASA – Misión a Marte

## Explicación del reto

Acabas de completar los fundamentos de Python: variables, tipos de datos, strings, booleanos, `None`, conversiones, slices, `split()`, `replace()`, etc. ¡Felicidades! Pero en el mundo real los datos no están escritos a mano en el código; vienen de archivos, sensores, APIs o bases de datos. La NASA no teclea la telemetría línea por línea.

**Tu misión** (si decides aceptarla):  
Eres ingeniero de control de la misión *Perseverance 2*. Tienes un archivo de texto (`telemetria.txt`) que contiene lecturas de sensores del rover en Marte. Cada línea tiene este formato:

timestamp, sensor, valor, unidad
Ejemplo:
2025-04-26T12:00:00, temperatura, 22.5, C
2025-04-26T12:01:00, presion, 101.3, hPa
2025-04-26T12:02:00, temperatura, -999, C


Debes **investigar por tu cuenta** cómo leer ese archivo, procesar sus líneas, limpiar datos erróneos, extraer información útil y generar un reporte.  
El reto **no te da el código para leer archivos** – tendrás que buscar en la documentación oficial de Python, en tutoriales o en foros cómo usar `open()`, `with`, `readlines()`, manejo de excepciones (`try/except`) y quizás el módulo `csv`.  

Además, deberás aplicar todo lo que ya sabes:  
- Separar strings (`split`)  
- Convertir tipos (`float()`, `str()`)  
- Usar `None` para valores inválidos  
- Comparar booleanos  
- Acumular sumas y contadores  
- Utilizar colecciones (listas, diccionarios) – aunque no están en tu lista de temas, ¡son el siguiente paso natural y deberás estudiarlos por tu cuenta!

## ¿Por qué existe este reto?

Porque en programación **saber buscar información es tan importante como saber escribir código**.  
Los cursos te dan una base, pero los problemas reales siempre requieren que amplíes tu conocimiento.  
Con este reto practicarás:

- **Lectura y escritura de archivos** (no visto en tu lista).
- **Manejo básico de excepciones** (para cuando un archivo no existe o un valor no es convertible a número).
- **Uso de diccionarios** para agrupar datos por sensor.
- **Pensamiento analítico**: ¿cómo detectar un valor erróneo? (temperatura > 100 o < -50 en Marte no tiene sentido).
- **Generación de reportes** en texto plano.

Además, simula una situación real donde los datos vienen “sucios” y hay que limpiarlos antes de analizarlos.

## Definition of Done (Criterios de aceptación)

Tu programa `analizador_telemetria.py` se considerará completo cuando **cumpla TODOS estos puntos**:

1. **Lee el archivo** `telemetria.txt` que está en la misma carpeta.  
   - Si el archivo no existe, muestra un mensaje claro y termina el programa (sin errores de Python).  
   - Usa `with open(...) as ...` para asegurar que el archivo se cierre correctamente.

2. **Procesa cada línea** no vacía:  
   - Ignora líneas que no tengan exactamente 4 campos después de `split(',')`.  
   - Elimina espacios en blanco alrededor de cada campo (usa `.strip()`).  
   - El `timestamp` lo conservas como string, pero debes eliminar posibles comillas si las hubiera.

3. **Maneja valores inválidos**  
   - Intenta convertir el campo `valor` a `float`.  
   - Si la conversión falla (por ejemplo, `"---"` o `"N/A"`), asigna `None` a ese valor.  
   - Si el valor convertido es un número, pero para el sensor `"temperatura"` está fuera del rango realista **[-50, 100]**, también asigna `None` (considera que es una lectura errónea).

4. **Calcula las siguientes métricas** (usando solo valores válidos, ignorando `None`):  
   - Número total de lecturas procesadas (líneas válidas en formato).  
   - Número de lecturas con valor inválido (`None`).  
   - Lista de sensores únicos (sin duplicados).  
   - Por cada sensor, cuántas lecturas válidas tiene.  
   - Para el sensor `"temperatura"`:  
     - Temperatura máxima, mínima y promedio (solo valores válidos).  
     - Si no hay ninguna lectura válida de temperatura
