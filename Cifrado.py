import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256


class Cifrado:

    def __init__(self, numero_bytes, contraseña):
        """Cifra un archivo con AES, con una contraseña, y un vector de inicialización aleatorio.

        :Parameters:
            numero_bytes : integer
                El número de bytes del tamaño del vector de inicialización.
            contraseña : string
                La contraseña es la llave antes de ser transformada a bytes.
        """

        self.vector_inicializacion = os.urandom(numero_bytes)
        self.llave = SHA256.new(contraseña.encode('utf-8')).digest()

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encriptar(self, mensaje, key, key_size=256):
        mensaje = self.pad(mensaje)
        encriptador = AES.new(key, AES.MODE_CBC, self.vector_inicializacion)
        return self.vector_inicializacion + encriptador.encrypt(mensaje)

    def des_encriptar(self, contenido_cifrado):
        iv = contenido_cifrado[:AES.block_size]
        encriptador = AES.new(self.llave, AES.MODE_CBC, iv)
        contenido_archivo = encriptador.decrypt(
            contenido_cifrado[AES.block_size:])
        return contenido_archivo.rstrip(b"\0")

    def nombrar_archivo(self, archivo, nombre_archivo_cifrado=None):
        archivo_cifrado = archivo
        if nombre_archivo_cifrado:
            ruta = os.path.dirname(archivo)
            extension = os.path.splitext(archivo)
            archivo_cifrado = os.path.join(
                ruta, nombre_archivo_cifrado+extension[1]+'.enc')

        return archivo_cifrado

    def encriptar_archivo(self, archivo, nombre_archivo_cifrado=None):
        """Encriptar un archivo

        :Parameters:
          archivo : string
            Ruta del archivo a encriptar.
          nombre_archivo_cifrado : string
            Nombre con el que se guardará el nuevo archivo encriptado.
        """
        with open(archivo, 'rb') as fo:
            contenido_archivo = fo.read()
        enc = self.encriptar(contenido_archivo, self.llave)

        archivo_cifrado = self.nombrar_archivo(archivo, nombre_archivo_cifrado)

        with open(archivo_cifrado, 'wb') as fo:
            fo.write(enc)

    def des_encriptar_archivo(self, archivo):
        """Encriptar un archivo

        :Parameters:
          archivo : string
            Ruta del archivo encriptado.
        """
        with open(archivo, 'rb') as fo:
            contenido_cifrado = fo.read()

        dec = self.des_encriptar(contenido_cifrado)

        with open(archivo[:-4], 'wb') as fo:
            fo.write(dec)
