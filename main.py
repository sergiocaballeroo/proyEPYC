import re
from math import ceil

patron = r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BITA|bita|BITB|bitb|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|SUBA|suba|SUBB|subb|SUBD|subd)"

with open('START.ASC', 'r', buffering=1024) as archivo:
    for linea in archivo:
        #Buscar coincidencias del patrón en la línea actual
        if re.search(patron, linea):
            #Realizar acciones con las coincidencias encontradas
            print(linea)

    for linea2 in archivo:    
        if "#'" in linea2:
            index = linea2.find("#'") +2
            simbolos = linea2[index:-1]
            for simbolo in simbolos:
                valor_decimal = ord(simbolo)
                print(valor_decimal)