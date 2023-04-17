nombre_archivo = input("Ingresa el nombre del archivo: ")

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe")
except:
    print("Ocurrió un error al abrir el archivo")

IMM=r"^(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BITA|bita|BITB|bitb|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|SUBA|suba|SUBB|subb|SUBD|subd)"
mnemonicos = re.findall(IMM, contenido)

# Imprime los mnemónicos de 68HC11 encontrados
print("Mnemónicos encontrados:", mnemonicos)