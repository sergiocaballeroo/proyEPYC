def open_file():
    nombre_archivo = input("Ingresa el nombre del archivo")
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

print(contenido)
