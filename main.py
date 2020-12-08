import os
from time import sleep
from Cifrado import Cifrado


def clear(): return os.system('clear')


def obtener_archivo():
    while True:
        ruta = input('Ruta del archivo: ')
        if not os.path.isfile(ruta):
            print('El archivo no existe!')
        else:
            break

    return ruta


while True:
    clear()
    print('#### ENCRIPTAR ARCHIVOS CON AES ####')

    str_ = 'Escriba el número de la opción que desee realizar.\n[1]\tEncriptar un archivo\n[2]\tDesencriptar un archivo\n[3]\tSalir\nOpción: '
    opcion = int(input(str_))

    bytes_vector_inicializacion = 16

    if opcion == 1:
        print('\nComplete la siguiente información')

        ruta = obtener_archivo()

        while True:
            llave = input('Llave: ')
            llave_confir = input('Confime la llave: ')

            if llave != llave_confir:
                print('Las llaves no coinciden!')
            else:
                break

        nombre_nuevo_archivo = input('Nombre nuevo archivo (sin extensión): ')

        cifrado_aes = Cifrado(bytes_vector_inicializacion, llave)

        cifrado_aes.encriptar_archivo(ruta, nombre_nuevo_archivo)

        print('\nArchivo cifrado correctamente!\nRuta: '+ruta+'.enc\nEspere...')
        sleep(5)

    elif opcion == 2:

        ruta = obtener_archivo()

        llave = input('Llave: ')

        cifrado_aes = Cifrado(bytes_vector_inicializacion, llave)

        cifrado_aes.des_encriptar_archivo(ruta)

        print('\nArchivo descifrado correctamente!\nRuta: '+ruta+'\nEspere...')
        sleep(5)

    elif opcion == 3:
        exit()
