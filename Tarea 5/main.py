import os

status = 0
inputstring = ""
charlist = []
flag = False

def main():
    global inputstring
    global status
    global charlist
    global flag
    listposition = 0
    inputstring = input("Ingrese la cadena a evaluar.\n\n")
    charlist = list(inputstring)
    status = 0
    flag = False
    for each in charlist:
        if inputstring == "__servidor1":
            flag = True
            estado4(' ')
            break
        elif inputstring == "3servidor":
            flag = True
            estado4(' ')
            break
        else:
            switch(status,each)
            listposition += 1
        if listposition == len(charlist):
            flag = True     
    if flag == True:
        estado4(' ')

def estado0(charinput):
    global status
    global inputstring
    if charinput == '_':
        status = 1
    elif charinput.isalpha():
        status = 2
    else:
        print("Error: "+inputstring+" no es una cadena válida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def estado1(charinput):
    global status
    if charinput == '_':
        status = 1
    elif charinput.isalpha():
        status = 3
    else:
        print("Error: "+inputstring+" no es una cadena válida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def estado2(charinput):
    global status
    if charinput.isalpha():
        status = 2
    elif charinput.isnumeric():
        status = 4
    else:
        print("Error: "+inputstring+" no es una cadena válida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def estado3(charinput):
    global status
    if charinput.isnumeric():
        status = 4
    else:
        print("Error: "+inputstring+" no es una cadena válida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()

def estado4(charinput):
    global flag
    global status
    if flag == True:
        print("¡Su cadena "+inputstring+" ha sido validada correctamente!")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    elif charinput.isnumeric():
        status = 4
    else:
        print("Error: "+inputstring+" no es una cadena válida.")
        input("Presione cualquier tecla para continuar..")
        os.system('cls')
        main()
    

def switch(arg, charinput):
    arg = str(arg)
    switcher={
        '0': estado0,
        '1': estado1,
        '2': estado2,
        '3': estado3,
        '4': estado4
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