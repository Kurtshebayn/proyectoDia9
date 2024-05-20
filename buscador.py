import os
import re
from datetime import date
import time
import math

ruta = 'C:\\Users\\Sebastian\\Desktop\\Python\\proyectoDia9\\Mi_Gran_Directorio'


def buscador_numeros():
    contador = 0
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        sub = carpeta
        for arch in archivo:
            ruta_archivo = sub + '\\' + arch
            archivo_texto = open(ruta_archivo,'r')
            contenido_archivo = archivo_texto.read()
            patron = r'N\D{3}-\d{5}'
            verificar = re.search(patron,contenido_archivo)
            if verificar:
                print(f'{arch}\t\t {verificar.group()}')
                contador += 1
            archivo_texto.close()
    return contador

print('-'*50)
fecha = date.today()
fecha_corregida = fecha.strftime("%d/%m/%Y")
print(f'fecha de búsqueda: {fecha_corregida}\n')
print('ARCHIVO\t\t\t\t NRO. SERIE')
print('-------\t\t\t\t ----------')
inicio = time.time()
coincidencias = buscador_numeros()
final = time.time()
print(f'\nNúmeros encontrados: {coincidencias}')
tiempo = math.ceil(final - inicio)
print(f'Duración de la búsqueda: {tiempo} segundos')
print('-'*50)


