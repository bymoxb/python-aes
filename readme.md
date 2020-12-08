# Cifrado de archivos con AES

Este es un sencillo programa en python para cifrar archivos con AES, utiliza el paquete [pycrypto](https://pypi.org/project/pycrypto/) para el cifrado.

Caracteristicas del cifrado:

* Llave de 16 bytes
* Vector de inicialización aleatorio de 16 bytes

## Capturas

![Menu](src/1.png "Menu")

![Cifrado de archivo](src/2.png "Cifrando de archivo")

![Descifrado de archivo](src/3.png "Descifrado de archivo")

## Instalación

```bash
# Instalar paquetes
pip install -r requirements.txt

# Ejecutar el programa
python main.py
```

## Recomendaciones

Usar [virtualenv](https://github.com/pypa/virtualenv) antes de instalar los paquetes.
