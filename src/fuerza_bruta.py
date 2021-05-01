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
try:
    while(True):        
        password = getpass.getpass('Ingrese la contraseña: ')
        if password != '':
            break
        print(datetime.now(), '\033[0;91m [ERROR] La contraseña es un campo obligatorio \033[0;0m')
except Exception as error:
    print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
    print(error)

# Define un arreglo con el alfabeto a utilizar ,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
# Inicializa una cadena temporal que servirá para armar el texto generado de manera aleatoria
cadena = ''
# Registra en una variable la hora antes de comenzar la prueba de fuerza bruta.
inicio = datetime.now()
intentos = 1

try:
    while cadena != password:
        cadena = ''
        for simbolo in password:
            indice = random.randint(0,26)        
            cadena+=alfabeto[indice]
        intentos+=1
        os.system("cls")
        print(datetime.now(), '\033[0;32m[INFO] Espere un momento... \033[0;0m')
        print(datetime.now(), '\033[0;32m[INFO] Intentos: \033[0;0m', intentos)
    time.sleep(0)
    final = datetime.now()
    tiempo = final - inicio
    time.sleep(1)
    print(datetime.now(), '\033[1;31m[INFO] Contraseña: \033[0;0m', cadena)
    print(datetime.now(), '\033[0;32m[INFO] Tiempo: \033[0;0m', tiempo)
except Exception as error:
    print(datetime.now(), '\033[0;91m [ERROR] Ha ocurrido un error ')
    print(error)


