
import Objetos

def main():
    object1 = Objetos.Objetos("Dennis",20,True,2000)
    object2 = Objetos.Objetos("Luis",25,True,2300)
    object3 = Objetos.Objetos("Leslie",23,True,2444)
    object4 = Objetos.Objetos("Juan",20,False,2333)
    object5 = Objetos.Objetos("Renee",20,True,5312)
    object6 = Objetos.Objetos("Jessica",20,False,4455)
    object7 = Objetos.Objetos("Sarah",19,True,12345)
    object8 = Objetos.Objetos("Carlos",27,True,3333)
    object9 = Objetos.Objetos("Cesar",19,False,4682)
    object10 = Objetos.Objetos("Francisco",21,True,6532)

    listaobjetos = [object1,object2,object3,object4,object5,object6,object7,object8,object9,object10]
    rows = rowGenerator(listaobjetos)

    html_string = """ 
        <html>    
            <body>
                <table style="text-align:center;">
                    <tr>
                        <th>Nombre</th>
                        <th>Edad</th>
                        <th>Activo</th>
                        <th>Saldo</th>
                    </tr>
                    """+rows+"""       
                </table>
            </body>
        </html>
    """

    report = open('reporte.html', 'w')
    report.write(html_string)
    report.close()


def rowGenerator(listgiven):
    rows = ""
    for x in listgiven:
        newrow = """
        <tr>    
            <td>"""+x.getNombre()+"""</td>
            <td>"""+str(x.getEdad())+"""</td>
            <td>"""+str(x.isActivo())+"""</td>
            <td>"""+str(x.getSaldo())+"""</td> 
        </tr>
        """
        rows += newrow
    return rows


if __name__ == "__main__":
    main()