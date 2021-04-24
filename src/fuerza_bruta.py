"""
Uso: Ataque de fuerza bruta
Creador: Andrés Hernández Mata
Version: 1.0.0
Python: 3.9.1
Fecha: 24 Abril 2020
"""

import random
import getpass
import time
from datetime import datetime
import os

os.system('cls')

# Recibe una entrada del usuario y almacénala en una variable
password = getpass.getpass('Ingrese la contraseña: ')
# Define un arreglo con el alfabeto a utilizar
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
# Inicializa una cadena temporal que servirá para armar el texto generado de manera aleatoria
cadena = ''
# Registra en una variable la hora antes de comenzar la prueba de fuerza bruta.
inicio = datetime.now()
intentos = 1

print('\033[0;32m[INFO] Espere un momento... \033[0;0m')
while cadena != password:
    cadena = ''
    for simbolo in password:
        indice = random.randint(0,26)        
        cadena+=alfabeto[indice]
    intentos+=1
final = datetime.now()
tiempo = final - inicio
time.sleep(1)
print('\033[0;32m[INFO] Intentos: \033[0;0m', intentos)
time.sleep(1)
print('\033[1;31m[INFO] Contraseña: \033[0;0m', cadena)
time.sleep(1)
print('\033[0;32m[INFO] Tiempo: \033[0;0m', tiempo)


