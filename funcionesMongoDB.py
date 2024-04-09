import pymongo

cliente = MongoClient('localhost')
db = cliente.proyecto
eurovision = db.eurovision


def menu():
    while True:
        try:
            opcion=int(input('''
Menú
=========================
1. Eliminar documentos
2. Insertar documentos
3. Actualizar documentos
4. Consultar documentos
0. Salir
                     
'''))
            break
        except:
            print("Error. Por favor indica el número de la opción del menú que quieres ejecutar:")
    return opcion

def menu_eliminar():
    while True:
        try:
            opcion=int(input('''
Eliminar documentos
============================================================
1. Eliminar el documento correspondiente a un año
2. Eliminar el documento correspondiente a un rango de años
3. Volver
                             
'''))
            break
        except:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
    return opcion

def eliminaruno():
    try:
        year = int("Indica el año que quieres eliminar: ")
    except:
        print("Ha habido un error. Por favor, indica el año correctamente: ") 

    documento = {"year": year}
    resultado = eurovision.delete_one(documento)
    return resultado

def eliminarvarios():
    try:
        year1 = int("Indica el año mayor: ")
        year2 = int("Indica el año menor: ")
    except:
        print("Ha habido un error. Por favor, indica los años correctamente: ")
    
    documentos = {{"year": {"$lte": year1},{"$gte": year2}}}
    resultado = eurovision.delete_many(documentos)
    return resultado

def eliminar(opcion):
    opcion = menu_eliminar()
    if opcion == 1:
        eliminaruno()
    elif opcion == 2:
        eliminarvarios()
    elif opcion == 3:
        opcion = menu()
    else:
        print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
        opcion = menu_eliminar()

def menu_insertar():
    while True:
        try:
            opcion=int(input('''
Insertar documentos
===============================
1. Insertar un documento
2. Insertar varios documentos
3. Volver
                             
'''))
            break
        except:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
    return opcion

def insertaruno():
    return

def insertarvarios():
    return

def insertar(opcion):
    opcion = menu_insertar()
    if opcion == 1:
        insertaruno()
    elif opcion == 2:
        insertarvarios()
    elif opcion == 3:
        menu()
    else:
        print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
        opcion = menu_insertar()

def menu_actualizar():
    while True:
        try:
            opcion=int(input('''
Actualizar documentos
=================================
1. Actualizar un documento
2. Actualizar varios documentos
3. Volver
                             
'''))
            break
        except:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
    return opcion

def actualizaruno():
    return

def actualizarvarios():
    return

def actualizar(opcion):
    opcion = menu_actualizar()
    if opcion == 1:
        actualizaruno()
    elif opcion == 2:
        actualizarvarios()
    elif opcion == 3:
        opcion = menu()
    else:
        print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
        opcion = menu_actualizar()

def menu_consultar():
    while True:
        try:
            opcion=int(input('''
Consultar documentos
=====================
1. Mostrar el país organizador del festival y la ciudad anfitriona cada año desde el inicio hasta la actualidad.
2. Listar la ciudad, el año y los presentadores de cada edición que se ha celebrado en un país desde la más reciente hasta la más antigua.
3. Mostrar el nombre de todas las canciones y participantes de un año.
4. Listar todas las canciones dentro de un rango de ritmo que participaron en un año con el nombre del artista.
5. Mostrar todas las canciones que hayan obtenido más de una cantidad de puntos en total junto con el Id del participante y el año.
6. Mostrar los años en los que una persona estuvo entre los presentadores de la gala.
7. Mostrar los años en los que una persona presentó la gala en solitario.                            
8. Mostrar los años en los que varias personas estuvieron entre los presentadores de la gala.
9. Listar los años en los que una persona ha participado en Eurovision.
10. Mostrar todos los años en los que una cadena ha participado en Eurovision.
11. Mostrar una lista de los últimos años en los que el festival no se celebró en un mes concreto.
12. Contar el número de canciones con más de un determinado número de puntos cada año.
13. Contar las participaciones de cada cadena en el festival. 
14. Volver                                                                                                                                                                                                          
                                                                                       
'''))
            break
        except:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
    return opcion

def consulta1():
    return

def consulta2():
    return

def consultar(opcion):
    opcion = menu_consultar()
    if opcion == 1:
        consulta1()
    elif opcion == 2:
        consulta2()
    elif opcion == 3:
        consulta3()
    elif opcion == 4:
        consulta4()
    elif opcion == 5:
        consulta5()
    elif opcion == 6:
        consulta6()
    elif opcion == 7:
        consulta7()
    elif opcion == 8:
        consulta8()
    elif opcion == 9:
        consulta9()
    elif opcion == 10:
        consulta10()
    elif opcion == 11:
        consulta11()
    elif opcion == 12:
        consulta12()
    elif opcion == 13:
        consulta13()
    elif opcion == 14:
        opcion = menu()
    else:
        print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
        opcion = menu_consultar()

cliente.close()