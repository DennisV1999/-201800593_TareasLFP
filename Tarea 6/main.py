import os

entrada = """(
    <
        [atributo_numerico] = 45.09,
        [atributo_cadena] = "hola mundo",
        [atributo_booleano] = true
    >,
    <
        [atributo_numerico] = 4,
        [atributo_cadena] = "adios mundo",
        [atributo_booleano] = false
    >,
    <
        [atributo_numerico] = -56.4,
        [atributo_cadena] = "este es otro ejemplo, las cadenas pueden ser muy largas",
        [atributo_booleano] = false
    >
)"""

status = 0
charlist = []
tokenlist = []
tokenaux = ""
breakflag = False

def main():
    global status
    global charlist
    global entrada
    global breakflag
    charlist = list(entrada)
    for each in charlist:
        if not each.isspace() or status == 8:
            if breakflag == False:
                switch(status, each)
            else:
                break
    if status == 13:
        estado13()
    
def estado0(charinput):
    global status
    global tokenlist
    if charinput == '(':
        status = 1
        tokenlist.append(charinput+" ---> Paréntesis izquierdo")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado1(charinput):
    global status
    global tokenlist
    if charinput == '<':
        status = 2
        tokenlist.append(charinput+" ---> Menor qué")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado2(charinput):
    global status
    global tokenlist
    if charinput == '[':
        status = 3
        tokenlist.append(charinput+" ---> Corchete Izquierdo")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado3(charinput):
    global status
    global tokenlist
    global tokenaux
    if charinput.isnumeric() or charinput.isalpha() or charinput == '_':
        status = 3
        tokenaux += charinput
    elif charinput == ']':
        status = 4
        tokenlist.append(tokenaux+" ---> Nombre de atributo")
        tokenaux = ""
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado4(charinput):
    global status
    global tokenlist
    if charinput == '=':
        status = 5
        tokenlist.append(charinput+" ---> Igual")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado5(charinput):
    global status
    global tokenlist
    global tokenaux
    if charinput.isnumeric() or charinput == '-':
        status = 6
        tokenaux += charinput
    elif charinput == '"':
        status = 8
        tokenaux += charinput
    elif charinput.isalpha():
        tokenaux += charinput
    elif tokenaux == "true":
            status = 10
            tokenlist.append(tokenaux+" ---> Verdadero")
            tokenaux = ""
            estado10(charinput)  
    elif tokenaux == "false":
            status = 11
            tokenlist.append(tokenaux+" ---> Falso")
            tokenaux = ""
            estado11(charinput)
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado6(charinput):
    global status
    global tokenlist
    global tokenaux
    global breakflag
    if charinput.isnumeric():
        tokenaux += charinput
    elif charinput == '.':
        status = 7
        tokenaux += charinput
    elif charinput == ',':
        status = 2
        if "-" in tokenaux:
            tokenlist.append(tokenaux+" ---> Número Entero Negativo")
        else:
            tokenlist.append(tokenaux+" ---> Número Entero")
        tokenlist.append(charinput+" ---> Coma")
        tokenaux = ""
    elif charinput == '>':
        status = 12
        if "-" in tokenaux:
            tokenlist.append(tokenaux+" ---> Número Entero Negativo")
        else:
            tokenlist.append(tokenaux+" ---> Número Entero")
        tokenlist.append(charinput+" ---> Mayor Que")
        tokenaux = ""
    elif not tokenaux.startswith("-") and "-" in tokenaux:
        breakflag = True
        print("Error en "+tokenaux+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado7(charinput):
    global status
    global tokenlist
    global tokenaux
    global breakflag
    if charinput.isnumeric():
        tokenaux += charinput
    elif charinput == ',':
        status = 2
        if "-" in tokenaux:
            tokenlist.append(tokenaux+" ---> Número Real Negativo")
        else:
            tokenlist.append(tokenaux+" ---> Número Real")
        tokenlist.append(charinput+" ---> Coma")
        tokenaux = ""
    elif charinput == '>':
        status = 12
        if "-" in tokenaux:
            tokenlist.append(tokenaux+" ---> Número Real Negativo")
        else:
            tokenlist.append(tokenaux+" ---> Número Real")
        tokenlist.append(charinput+" ---> Mayor Que")
        tokenaux = ""
    elif not tokenaux.startswith("-") and "-" in tokenaux:
        breakflag = True
        print("Error en "+tokenaux+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado8(charinput):
    global status
    global tokenlist
    global tokenaux
    if not charinput == '"':
        tokenaux += charinput
    else:
        status = 9
        tokenaux += charinput
        tokenlist.append(tokenaux+" ---> Cadena")
        tokenaux = ""

def estado9(charinput):
    global status
    global tokenlist
    if charinput == ',':
        status = 2
        tokenlist.append(charinput+" ---> Coma")
    elif charinput == '>':
        status = 12
        tokenlist.append(charinput+" ---> Mayor Que")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado10(charinput):
    global status
    global tokenlist
    if charinput == ',':
        status = 2
        tokenlist.append(charinput+" ---> Coma")
    elif charinput == '>':
        status = 12
        tokenlist.append(charinput+" ---> Mayor Que")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado11(charinput):
    global status
    global tokenlist
    if charinput == ',':
        status = 2
        tokenlist.append(charinput+" ---> Coma")
    elif charinput == '>':
        status = 12
        tokenlist.append(charinput+" ---> Mayor Que")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado12(charinput):
    global status
    global tokenlist
    if charinput == ',':
        status = 1
        tokenlist.append(charinput+" ---> Coma")
    elif charinput == ')':
        status = 13
        tokenlist.append(charinput+" ---> Paréntesis Derecho")
    else:
        print("Error en "+charinput+" revise que la entrada esté bien escrita.")
        input("Presione cualquier tecla para continuar..")

def estado13():
    global tokenlist
    for each in tokenlist:
        print(each)
    print("\n¡Cadena analizada exitósamente!")
    input("Presione cualquier tecla para continuar..")

def switch(arg, charinput):
    arg = str(arg)
    switcher={
        '0': estado0,
        '1': estado1,
        '2': estado2,
        '3': estado3,
        '4': estado4,
        '5': estado5,
        '6': estado6,
        '7': estado7,
        '8': estado8,
        '9': estado9,
        '10': estado10,
        '11': estado1,
        '12': estado12
    }
    if arg not in switcher:
        print("Opción Invalida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    else:
        func = switcher.get(arg, lambda: "Opción Invalida")
        return func(charinput)

if __name__ == "__main__":
    main()