import os

ruta = r'C:\Users\helve\Documents\CAJAS SIN RENOMBRAR\YEIMI_934_HLP2\934'
archivos = os.listdir(ruta)

# Encontrar el primer archivo que no empiece con "_"
nombre_encontrado = ''
for archivo in archivos:
    if not archivo.startswith('_'):
        nombre_encontrado = os.path.splitext(archivo)[0]
        break

# Renombrar los archivos que empiezan con "_"
if nombre_encontrado:
    for i, archivo in enumerate(archivos):
        if archivo.startswith('_'):
            nuevo_nombre = f"{nombre_encontrado}_{str(i+1).zfill(3)}{os.path.splitext(archivo)[1]}"
            os.rename(os.path.join(ruta, archivo), os.path.join(ruta, nuevo_nombre))
