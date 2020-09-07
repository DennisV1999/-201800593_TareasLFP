import os

status = 0
inputstring = ""

def main():
    global inputstring
    inputstring = input("Ingrese la cadena a evaluar.")
    charlist = list(inputstring)
    for each in charlist:
        switch(status,each)

def estado0(charinput):
    global status
    if charinput == '_':
        status = 1
    elif charinput.isalpha():
        

def estado1(charinput):
    print("")

def estado2(charinput):
    print("")

def estado3(charinput):
    print("")

def estado4(charinput):
    print("") 

def switch(arg, charinput):
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