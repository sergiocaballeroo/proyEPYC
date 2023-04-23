import re
from math import ceil

ASCII="(?|A)"
IMM="(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BITA|bita|BITB|bitb|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|SUBA|suba|SUBB|subb|SUBD|subd)"
DIR="(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BCLR|bclr|BITA|bita|BITB|bitb|BRCLR|brclr|BRSET|brset|BSET|bset|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|JSR|jsr|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|STAA|staa|STAB|stab|STD|std|STS|sts|STX|stx|STY|sty|SUBA|suba|SUBB|subb|SUBD|subd)"
nombre_archivo=input("Ingresa el nombre del archivo ")
nombreASC = nombre_archivo + ".ASC"
nombreArchLST = nombre_archivo + ".LST"

def archivoLST():
    try:
        archivoLST = open(nombreArchLST, "w")
        archivoLST.write(".")
        archivoLST.close()
        print("Archivo LST creado con exito")
    except FileNotFoundError:
        print("El archivo no se pudo crear debido a un problema externo")

def contarLineas():
    archivo_original = open(nombreASC, "r")
    #Inicializamos contador de líneas
    archivoLST = open(nombreArchLST, "w")
    contLineas = 0
    for lineasCont in archivo_original:
        contLineas += 1
        archivoLST.write(str(contLineas)+ "\n")
    archivo_original.close()
    archivoLST.close()
    print("El archivo tiene", contLineas, "lineas")
          
def archivoError():
    print("Hola")

def Encontrar_ascii(lineas):
    if "#'" in linea:
            index = linea.find("#'") +2
            simbolos = linea[index:-1]
            for simbolo in simbolos:
                valor_decimal = ord(simbolo)
                print(valor_decimal)
    return 

patron = "(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BITA|bita|BITB|bitb|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|SUBA|suba|SUBB|subb|SUBD|subd)"

with open('START.ASC', 'r', buffering=1024) as archivo:
    for linea in archivo:
        # Buscar coincidencias del patrón en la línea actual
        if re.search(IMM, linea):
            # Realizar acciones con las coincidencias encontradas  
            print(linea)  
            Encontrar_ascii(linea)
        elif re.search(DIR, linea):
            # Realizar acciones con las coincidencias encontradas  
            print(linea)  
            Encontrar_ascii(linea)
            archivoLST()
            contarLineas()
           

