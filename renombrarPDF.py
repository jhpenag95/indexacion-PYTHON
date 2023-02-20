import os

ruta = r'C:\Users\helve\Documents\CAJAS SIN RENOMBRAR\YEIMI_934_HLP2\934'
archivos = os.listdir(ruta)

 # Encontrar el primer archivo que no comienza con _
primer_archivo = None
for archivo in archivos:
     if archivo[0] != '_':
         primer_archivo = archivo
         break

 # Renombrar los archivos consecutivos con _
if primer_archivo:
     consecutivo = 1
     nombre_base = primer_archivo.split('.')[0]
     reset_contador = False  # variable para reiniciar el contador
     for i in range(archivos.index(primer_archivo) + 1, len(archivos)):
         archivo = archivos[i]
         if archivo[0] == '_':
             if reset_contador:
                 consecutivo = 1
                 reset_contador = False
             nuevo_nombre = f"{nombre_base}_{consecutivo:03d}.pdf"
             os.rename(os.path.join(ruta, archivo), os.path.join(ruta, nuevo_nombre))
             consecutivo += 1
         else:
             # Encontramos otro archivo sin _
             primer_archivo = archivo
             reset_contador = True  # establecer en True para reiniciar el contador
             nombre_base = primer_archivo.split('.')[0]

             # Renombrar los archivos consecutivos con el nuevo nombre base
             consecutivo = 1
             for j in range(i, len(archivos)):
                 archivo = archivos[j]
                 if archivo[0] == '_':
                     nuevo_nombre = f"{nombre_base}_{consecutivo:03d}.pdf"
                     os.rename(os.path.join(ruta, archivo), os.path.join(ruta, nuevo_nombre))
                     consecutivo += 1
                 else:
                     break
