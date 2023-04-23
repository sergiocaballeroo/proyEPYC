
import re
from math import ceil


#Para compilar la expresión regular que busca los EQU	
EQU = re.compile(r'\w+(\s)+(EQU)(\s)+\$\d+')
#Para compilar la expresión regular que busca los ORG	
ORG = re.compile(r'(\s)+(ORG)(\s)+\$\d+')
#Para compilar la expresión regular que busvca los FCB	
FCB = re.compile(r'(\s)+(FCB|fcb)(\s)+\$\w+\d+,\$\w+\d+')
#Para compilar la expresión regular que busvca los END	
END = re.compile(r'(\s)+(END|end|End)(\s)+\$\d+')
#Para compilar la expresión regular que busca los comentarios	
COMETARIOS = re.compile(r'(\*(\s+\w+)+\s\-(\w+\s)+\w+\-)|(\*(\s+\w+)+\s+\w+\-\w+)|(\*(\s+\w+)+\s+\(\w+((\s+\w+)+)*\))|(\*(\w+\s)+)(\*\s(\w+\s)+)|((\*\s(\w+\s{1,3})+))|(\*\s(\w+\s)+)|(\*(\ \s{1,5})(\w+\s)+)|(\*(\w+\s)+)|(\*+)')


IMM=re.compile(r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BITA|bita|BITB|bitb|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|SUBA|suba|SUBB|subb|SUBD|subd)([ ]*)([#])([$])"
)
D_IMM = {
    "ADCA": "89",
    "ADCB": "C9",
    "ADDA": "8B",
    "ADDB": "CB",
    "ADDD": "C3",
    "ANDA": "84",
    "ANDB": "C4",
    "BITA": "85",
    "BITB": "C5",
    "CMPA": "81",
    "CMPB": "C1",
    "CPD": "1A 83",
    "CPX": "8C",
    "CPY": "18 8C",
    "EORA": "88",
    "EORB": "C8",
    "LDAA": "86",
    "LDAB": "C6",
    "LDD": "CC",
    "LDS": "8E",
    "LDX": "CE",
    "LDY": "18 CE",
    "ORAA": "8A",
    "ORAB": "CA",
    "SBCA": "82",
    "SBCB": "C2",
    "SUBA": "80",
    "SUBB": "C0",
    "SUBD": "83",
}

DIR=re.compile(r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|BCLR|bclr|BITA|bita|BITB|bitb|BRCLR|brclr|BRSET|brset|BSET|bset|CMPA|cmpa|CMPB|cmpb|CPD|cpd|CPX|cpx|CPY|cpy|EORA|eora|EORB|eorb|JSR|jsr|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|ORAA|oraa|ORAB|orab|SBCA|sbca|SBCB|sbcb|STAA|staa|STAB|stab|STD|std|STS|sts|STX|stx|STY|sty|SUBA|suba|SUBB|subb|SUBD|subd)([ ]*)([$])")
D_DIR = {
    "ADCA": "99",
    "ADCB": "D9",
    "ADDA": "9B",
    "ADDB": "DB",
    "ADDD": "D3",
    "ANDA": "94",
    "ANDB": "D4",
    "BCLR": "15",
    "BITA": "95",
    "BITB": "D5",
    "BRCLR": "13",
    "BRSET": "12",
    "BSET": "14",
    "CMPA": "91",
    "CMPB": "D1",
    "CPD": "1A 93",
    "CPX": "9C",
    "CPY": "18 9C",
    "EORA": "98",
    "EORB": "D8",
    "JSR": "9D",
    "LDAA": "96",
    "LDBA": "D6",
    "LDD": "DC",
    "LDS": "9E",
    "LDX": "DE",
    "LDY": "18 DE",
    "ORAA": "9A",
    "ORAB": "DA",
    "SBCA": "92",
    "SBCB": "D2",
    "STAA": "97",
    "STAB": "D7",
    "STD": "DD",
    "STS": "9F",
    "STX": "DF",
    "STY": "18 DF",
    "SUBA": "90",
    "SUBB": "D0",
    "SUBD": "93"
}

IDX_Y=re.compile(r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|ASL|asl|ASR|asr|BCLR|bclr|BITA|bita|BITB|bitb|BRCLR|brclr|BRSET|brset|BSET|bset|CLR|clr|CMPA|cmpa|CMPB|cmpb|COM|com|CPD|cpd|CPX|cpx|CPY|cpy|DEC|dec|EORA|eora|EORB|eorb|INC|inc|JMP|jmp|JSR|jsr|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|LSL|lsl|LSR|lsr|NEG|neg|ORAA|oraa|ORAB|orab|ROL|rol|ROR|ror|SBCA|sbca|SBCB|sbcb|STAA|staa|STAB|stab|STD|std|STS|sts|STX|stx|STY|sty|SUBA|suba|SUBB|subb|SUBD|subd|TST|tst)([ ]*)([$])(\w)([,])([y])")
D_IND_Y = {
    "ADCA": "18 A9",
    "ADCB": "18 E9",
    "ADDA": "18 AB",
    "ADDB": "18 EB",
    "ADDD": "18 E3",
    "ANDA": "18 A4",
    "ANDB": "18 E4",
    "ASL": "18 68",
    "ASR": "18 67",
    "BCLR": "18 1D",
    "BITA": "18 A5",
    "BITB": "18 E5",
    "BRCLR": "18 1F",
    "BRSET": "18 1E",
    "BSET": "18 1C",
    "CLR": "18 6F",
    "CMPA": "18 A1",
    "CMPB": "18 E1",
    "COM": "18 63",
    "CPD": "CD A3",
    "CPX": "CD AC",
    "CPY": "18 AC",
    "DEC": "18 6A",
    "EORA": "18 A8",
    "EORB": "18 E8",
    "INC": "18 6C",
    "JMP": "18 6E",
    "JSR": "18 AD",
    "LDAA": "18 A6",
    "LDAB": "18 E6",
    "LDD": "18 EC",
    "LDS": "18 AE",
    "LDX": "CD EE",
    "LDY": "18 EE",
    "LSL": "18 68",
    "LSR": "18 64",
    "NEG": "18 60",
    "ORAA": "18 AA",
    "ORAB": "18 EA",
    "ROL": "18 69",
    "ROR": "18 66",
    "SBCA": "18 A2",
    "SBCB": "18 E2",
    "STAA": "18 A7",
    "STAB": "18 E7",
    "STD": "18 ED",
    "STS": "18 AF",
    "STX": "CD EF",
    "STY": "18 EF",
    "SUBA": "18 A0",
    "SUBB": "18 E0",
    "SUBD": "18 A3",
    "TST": "18 6D"
}

IDX_X=re.compile(r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|ASL|asl|ASR|asr|BCLR|bclr|BITA|bita|BITB|bitb|BRCLR|brclr|BRSET|brset|BSET|bset|CLR|clr|CMPA|cmpa|CMPB|cmpb|COM|com|CPD|cpd|CPX|cpx|CPY|cpy|DEC|dec|EORA|eora|EORB|eorb|INC|inc|JMP|jmp|JSR|jsr|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|LSL|lsl|LSR|lsr|NEG|neg|ORAA|oraa|ORAB|orab|ROL|rol|ROR|ror|SBCA|sbca|SBCB|sbcb|STAA|staa|STAB|stab|STD|std|STS|sts|STX|stx|STY|sty|SUBA|suba|SUBB|subb|SUBD|subd|TST|tst)([ ]*)([$])(\W)([,])([X])")
D_IND_X = {
    "ADCA": "A9",
    "ADCB": "E9",
    "ADDA": "AB",
    "ADDB": "EB",
    "ADDD": "E3",
    "ANDA": "B4",
    "ANDB": "E4",
    "ASL": "68",
    "ASR": "67",
    "BCLR": "1D",
    "BITA": "A5",
    "BITB": "E5",
    "BRCLR": "1F",
    "BRSET": "1E",
    "BSET": "1C",
    "CLR": "6F",
    "CMPA": "A1",
    "CMPB": "E1",
    "COM": "63",
    "CPD": "1A A3",
    "CPX": "AC",
    "CPY": "1A AC",
    "DEC": "6A",
    "EORA": "A8",
    "EORB": "E8",
    "INC": "6C",
    "JMP": "6E",
    "JSR": "AD",
    "LDAA": "A6",
    "LDAB": "E6",
    "LDD": "EC",
    "LDS": "AE",
    "LDX": "EE",
    "LDY": "1A EE",
    "LSL": "68",
    "LSR": "64",
    "NEG": "60",
    "ORAA": "AA",
    "ORAB": "EA",
    "ROL": "69",
    "ROR": "66",
    "SBCA": "A2",
    "SBCB": "E2",
    "STAA": "A7",
    "STAB": "E7",
    "STD": "ED",
    "STS": "AF",
    "STX": "EF",
    "STY": "1A EF",
    "SUBA": "A0",
    "SUBB": "E0",
    "SUBD": "A3",
    "TST": "6D"
}

EXT =re.compile(r"(ADCA|adca|ADCB|adcb|ADDA|adda|ADDB|addb|ADDD|addd|ANDA|anda|ANDB|andb|ASL|asl|ASR|asr|BITA|bita|BITB|bitb|CLR|clr|CMPA|cmpa|CMPB|cmpb|COM|com|CPD|cpd|CPX|cpx|CPY|cpy|DEC|dec|EORA|eora|EORB|eorb|INC|inc|JMP|jmp|JSR|jsr|LDAA|ldaa|LDAB|ldab|LDD|ldd|LDS|lds|LDX|ldx|LDY|ldy|LSL|lsl|LSR|lsr|NEG|neg|ORAA|oraa|ORAB|orab|ROL|rol|ROR|ror|SBCA|sbca|SBCB|sbcb|STAA|staa|STAB|stab|STD|std|STS|sts|STX|stx|STY|sty|SUBA|suba|SUBB|subb|SUBD|subd|TST|tst)([ ]*)($)(\w{4})")
D_EXT = {
    "ADCA": "B9",
    "ADCB": "F9",
    "ADDA": "BB",
    "ADDB": "FB",
    "ADDD": "F3",
    "ANDA": "B4",
    "ANDB": "F4",
    "ASL": "78",
    "ASR": "77",
    "BITA": "B5",
    "BITB": "F5",
    "CLR": "7F",
    "CMPA": "B1",
    "CMPB": "F1",
    "COM": "73",
    "CPD": "1A B3",
    "CPX": "BC",
    "CPY": "18 BC",
    "DEC": "7A",
    "EORA": "B8",
    "EORB": "F8",
    "INC": "7C",
    "JMP": "7E",
    "JSR": "BD",
    "LDAA": "B6",
    "LDAB": "F6",
    "LDD": "FC",
    "LDS": "BE",
    "LDX": "FE",
    "LDY": "18 FE",
    "LSL": "78",
    "LSR": "74",
    "NEG": "70",
    "ORAA": "BA",
    "ORAB": "FA",
    "ROL": "79",
    "ROR": "76",
    "SBCA": "B2",
    "SBCB": "F2",
    "STAA": "B7",
    "STAB": "F7",
    "STD": "FD",
    "STS": "BF",
    "STX": "FF",
    "STY": "FF",
    "SUBA": "B0",
    "SUBB": "F0",
    "SUBD": "B3",
    "TST": "7D",
}

INH = re.compile(r"(ABA|aba|ABX|abx|ABY|aby|ASLA|asla|ASLB|aslb|ASLD|asld|ASRA|asra|ASRB|asrb|CBA|cba|CLC|clc|CLI|cli|CLRA|clra|CLRB|clrb|CLV|clv|COMA|coma|COMB|comb|DAA|daa|DECA|deca|DECB|decb|DES|des|DEX|dex|DEY|dey|FDIV|fdiv|IDIV|idiv|INCA|inca|INCB|incb|INS|ins|INX|inx|INY|iny|LSLA|lsla|LSLB|lslb|LSLD|lsld|LSRA|lsra|LSRB|lsrb|LSRD|lsrd|MUL|mul|NEGA|nega|NEGB|negb|NOP|nop|PSHA|psha|PSHB|pshb|PSHX|pshx|PSHY|pshy|PULA|pula|PULB|pulb|PULX|pulx|PULY|puly|ROLA|rola|ROLB|rolb|RORA|rora|RORB|rorb|RTI|rti|RTS|rts|SBA|sba|SEC|sec|SEI|sei|SEV|sev|STOP|stop|SWI|swi|TAB|tab|TAP|tap|TETS|tets|TPA|tpa|TSTA|tsta|TSTB|tstb|TSX|tsx|TSY|tsy|TXS|txs|TYS|tys|WAI|wai|XGDX|xgdx|XGDY|xgdy)")
D_INH = {
    "ABA": "1B",
    "ABX": "3A",
    "ABY": "18 3A",
    "ASLA": "48",
    "ASLB": "58",
    "ASLD": "5",
    "ASRA": "47",
    "ASRB": "57",
    "CBA": "11",
    "CLC": "0C",
    "CLI": "0E",
    "CLRA": "4F",
    "CLRB": "5F",
    "CLV": "0A",
    "COMA": "43",
    "COMB": "53",
    "DAA": "19",
    "DECA": "4A",
    "DECB": "5A",
    "DES": "34",
    "DEX": "09",
    "DEY": "18 09",
    "FDIV": "03",
    "IDIV": "02",
    "INCA": "4C",
    "INCB": "5C",
    "INS": "31",
    "INX": "08",
    "INY": "18 08",
    "LSLA": "48",
    "LSLB": "58",
    "LSLD": "05",
    "LSRA": "44",
    "LSRB": "54",
    "LSRD": "04",
    "MUL": "3D",
    "NEGA": "40",
    "NEGB": "50",
    "NOP": "01",
    "PSHA": "36",
    "PSHB": "37",
    "PSHX": "3C",
    "PSHY": "18 3C",
    "PULA": "32",
    "PULB": "33",
    "PULX": "38",
    "PULY": "18 38",
    "ROLA": "49",
    "ROLB": "59",
    "RORA": "46",
    "RORB": "56",
    "RTI": "3B",
    "RTS": "39",
    "SBA": "10",
    "SEC": "OD",
    "SEI": "OF",
    "SEV": "OB",
    "STOP": "CF",
    "SWI": "3F",
    "TAB": "16",
    "TAP": "06",
    "TBA": "17",
    "TETS": "00",
    "TPA": "07",
    "TSTA": "4D",
    "TSTB": "5D",
    "TSX": "30",
    "TSY": "18 30",
    "TXS": "35",
    "TYS": "18 35",
    "WAI": "3E",
    "XGDX": "8F",
    "XGDY": "18 8F",
}

REL = re.compile(r"(BCC|bcc|BCS|bcs|BEQ|beq|BGE|bge|BGT|bgt|BHI|bhi|BHS|bhs|BLE|ble|BLO|blo|BLS|bls|BLT|blt|BMI|bmi|BNE|bne|BPL|bpl|BRA|bra|BRN|brn|BSR|bsr|BVC|bvc|BVS|bvs)")
D_REL = {
    "BCC": "24",
    "BCS": "25",
    "BEQ": "27",
    "BGE": "2C",
    "BGT": "2E",
    "BHI": "22",
    "BHS": "24",
    "BLE": "2F",
    "BLO": "25",
    "BLS": "23",
    "BLT": "2D",
    "BMI": "2B",
    "BNE": "26",
    "BPL": "2A",
    "BRA": "20",
    "BRN": "21",
    "BSR": "8D",
    "BVC": "28",
    "BVS": "29"
}

nombre_archivo="START"
nombreASC = nombre_archivo + ".ASC"
nombreArchLST = nombre_archivo + ".LST"

def ArchLST():
    with open(nombreASC, "r") as archivo:
        lineas = archivo.readlines()
        num_lineas = len(lineas)

    with open(nombreArchLST, "w") as archivo:
        for i in range(num_lineas):
            archivo.write(f"{i+1}: {lineas[i]}")

def Errores(linea):
    
    with open("ERRORES.txt", "w") as E:
        #ERROR VARIABLE
        if "EQU" or "equ" in linea: 
            E.write("") 
        else:
            E.write("001 VARIABLE INEXISTENTE")
        #ERROR CONSTANTE
        if "#" and "EQU" or "equ" in linea:
            E.write("")
        else:
            E.write("002 CONSTANTE INEXISTENTE")
        
        #ERROR END
        if "END" in linea:
            E.write("")
        else:

            E.write("010 NO SE ENCUENTRA END :")

    
def Encontrar_ascii(linea):
    if "#'" in linea:
        index = linea.find("#'") + 2
        simbolos = linea[index:-1]
        for simbolo in simbolos:
            valor_decimal = ord(simbolo)
            print(valor_decimal)
    return

def Encontrar_ORG(linea):
    if "ORG" in linea:
        index = linea.find("ORG") 
        inicio = linea[index:+25]
        print(str(inicio))
        return str(inicio)

def main():
    with open('START.ASC', 'r', buffering=1024) as archivo:
        for linea in archivo:
            if re.search(EQU,linea):
                print(linea)
            if re.search(ORG,linea):
                print(linea) 
            if re.search(FCB,linea):
                print(linea) 
            if re.search(COMETARIOS,linea):
                print(linea)   
            # Buscar coincidencias del patrón en la línea actual
            if re.search(IMM, linea):
                print("IMM")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            elif re.search(DIR, linea):
                print("DIR")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            elif re.search(IDX_Y, linea):
                print("IDX_Y")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            elif re.search(IDX_X, linea):
                print("IDX_X")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            elif re.search(EXT, linea):
                print("EXT")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea) 
            elif re.search(INH, linea):
                print("INH")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            elif re.search(REL, linea):
                print("REL")
                # Realizar acciones con las coincidencias encontradas  
                print(linea)  
                Encontrar_ascii(linea)
            #idx=Encontrar_ORG(linea)
        
    #print(str(idx))
    ArchLST()
    Errores(linea)
main()