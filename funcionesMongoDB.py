import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://usuario:usuario@proyectomongodb.fpedozi.mongodb.net/?retryWrites=true&w=majority&appName=ProyectoMongoDB"

cliente = MongoClient(uri)
db = cliente.proyecto
eurovision = db.eurovision

def probarconexion():
    try:
        cliente.admin.command('ping')
        print("\nConexión exitosa a la base de datos.\nPuede comenzar a usar el programa.")
    except Exception as e:
        print(e)

def cerrarcliente():
    cliente.close()


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
    
    documentos = {{"year": {"$and": [{"$lte": year1},{"$gte": year2}]}}}
    resultado = eurovision.delete_many(documentos)
    return resultado

def eliminar():
    opcion = menu_eliminar()
    while opcion != 3:
        if opcion == 1:
            eliminaruno()
        elif opcion == 2:
            eliminarvarios()
        else:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
            opcion = menu_eliminar()
        opcion = 3

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

def lecturafichero(ruta):
    try:
        fichero = open(ruta)
        lineas = fichero.readlines()
        fichero.close
        documento = []
        for linea in lineas:
            documento.append(linea)
    except:
        print("Error en la lectura del fichero.")
        return documento

def insertaruno():
    try:
        ruta = input("Indica la ruta absoluta al documento que quieres añadir: ")
        documento = lecturafichero(ruta)
        resultado = eurovision.insert_one(documento)
    except:
        print("Error al insertar el documento.")
    return resultado

def insertarvarios():
    try:
        ruta = input("Indica la ruta absoluta al fichero con los documentos que quieres añadir: ")
        documentos = lecturafichero(ruta)
        resultado = eurovision.insert_many(documentos)
    except:
        print("Error al insertar el documento.")
    return resultado

def insertar():
    opcion = menu_insertar()
    while opcion != 3:
        if opcion == 1:
            insertaruno()
        elif opcion == 2:
            insertarvarios()
        else:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
            opcion = menu_insertar()
        opcion = 3

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
    ruta = input("Indica la ruta absoluta al documento que quieres actualizar: ")
    actualizacion = lecturafichero(ruta)
    while True:
        try:
            year = int(input("¿Qué año vas a actualizar? "))
            break
        except:
            print("Error. Indica el año correctamente.")
    while True:
        try:
            campo = input("¿Qué campo vas a actualizar?")
            break
        except:
            print("Error. Indica el campo correctamente.")
    try:
        documento = {"year": year}
        actualizar = {"$set": {campo: actualizacion}}
        result = eurovision.update_one(documento, actualizar)
    except:
        print("Error al actualizar.")
    return result

def actualizarvarios():
    while True:
        try:
            year = int(input("¿Desde qué año (hacia atrás) quieres actualizar la información? "))
            break
        except:
            print("Error. Indica el año correctamente.")
    while True:
        try:
            campo = input("¿Qué campo quieres actualizar? ")
            actualizacion = input("Indica el nuevo valor para el campo: ")
            break
        except:
            print("Hay un error en los datos aportados.")
    try:
        documento = {"year": year}
        actualizar = {"$set": {campo, actualizacion}}
        result = eurovision.update_many(documento, actualizar)
    except:
        print("Error al actualizar.")
    return result

def actualizar():
    opcion = menu_actualizar()
    while opcion != 3:
        if opcion == 1:
            actualizaruno()
        elif opcion == 2:
            actualizarvarios()
        elif opcion == 3:
            opcion = menu()
        else:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
            opcion = menu_actualizar()
        opcion = 3

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

def find(documento,filtro,orden):
    try:
        if orden != 0:
            cursor = eurovision.find(documento,filtro).sort(orden)
        else:
            cursor = eurovision.find(documento,filtro)
        num_docs = 0
        for documento in cursor:
            num_docs += 1
            print(documento)
        print()
        print("Nº de documentos: " + str(num_docs))
    except Exception as e:
        print("Error en la consulta.\n" + str(e))
        cursor = False
    return cursor

def aggregate(agregacion):
    try:
        cursor = eurovision.aggregate(agregacion)
        num_docs = 0
        for documento in cursor:
            num_docs += 1
            print(documento)
        print()
        print("Nº de documentos: " + str(num_docs))
    except Exception as e:
        print("Error en la consulta.\n" + str(e))
        cursor = False
    return cursor

def consulta1():
    documento = ({})
    filtro = {"year":1, "country":1, "city": 1, "_id":0}
    orden = {"year": 1}
    cursor = find(documento,filtro,orden)
    return cursor

def consulta2():
    countries = {"AL":"Albania","AD":"Andorra","AM":"Armenia","AU":"Australia","AT":"Austria","AZ":"Azerbaijan","BY":"Belarus","BE":"Belgium","BA":"Bosnia and Herzegovina","BG":"Bulgaria","HR":"Croatia","CY":"Cyprus","CZ":"Czechia","DK":"Denmark","EE":"Estonia","FI":"Finland","FR":"France","GE":"Georgia","DE":"Germany","GR":"Greece","HU":"Hungary","IS":"Iceland","IE":"Ireland","IL":"Israel","IT":"Italy","KZ":"Kazakhstan","LV":"Latvia","LT":"Lithuania","LU":"Luxembourg","MT":"Malta","MD":"Moldova","MC":"Monaco","ME":"Montenegro","MA":"Morocco","NL":"Netherlands","MK":"North Macedonia","NO":"Norway","PL":"Poland","PT":"Portugal","RO":"Romania","RU":"Russia","SM":"San Marino","RS":"Serbia","CS":"Serbia and Montenegro","SK":"Slovakia","SI":"Slovenia","ES":"Spain","SE":"Sweden","CH":"Switzerland","TR":"Turkey","UA":"Ukraine","GB":"United Kingdom","GB-WLS":"Wales","YU":"Yugoslavia"}
    pais = input("País: ")
    while pais not in countries.values():
        pais = input("El país no se encuetra en la lista. Recuerda que debes indicar el nombre en inglés: ")
    for cod,country in countries.items():
        if pais == country:
            codpais = cod
    documento = {"country": codpais}
    filtro = {"year":1, "city":1, "presenters":1, "_id":0}
    orden = {"year": -1}
    cursor = find(documento,filtro,orden)
    return cursor

def consulta3():
    while True:
        try:
            year = int(input("Año: "))
            break
        except:
            print("Error en el año. Indica un año correcto: ")
    documento = {"year": year}
    filtro = {"contestants.song":1,"contestants.artist":1,"_id":0}
    cursor = find(documento,filtro,0)
    return cursor

def consulta4():
    while True:
        try:
            year = int(input("Año: "))
            bpmmin = int(input("BPM mínimo: "))
            bpmmax = int(input("BPM máximo: "))
            break
        except:
            print("Error. Indica datos correctos: ")
    unwind = {"$unwind": "$contestants"}
    match = {"$match": {"year": year, "contestants.bpm":{"$gt": bpmmin, "$lt": bpmmax}}}
    sort = {"$sort": {"contestants.bpm": -1}}
    project = {"$project": {"contestants.artist": 1, "contestants.bpm": 1, "contestants.song": 1, "_id": 0}}
    agregacion = [unwind, match, sort, project]
    cursor = aggregate(agregacion)
    return cursor

def consulta5():
    while True:
        try:
            puntos = int(input("Puntuación: "))
            break
        except:
            print("Error. Indica una puntuación correcta: ")
    rounds = {"$unwind": "$rounds"}
    performances = {"$unwind": "$rounds.performances"}
    scores = {"$unwind": "$rounds.performances.scores"}
    match = {"$match": {"rounds.performances.scores.points": {"$gt": puntos}}}
    project = {"$project": {"rounds.performances.contestantId": 1, "year": 1, "rounds.performances.scores.points": 1, "_id": 0}}
    sort = {"$sort": {"rounds.performances.scores.points": 1}}
    agregacion = [rounds, performances, scores, match, project, sort]
    cursor = aggregate(agregacion)
    return cursor

def consulta6():
    while True:
        try:
            nombre = input("Nombre: ")
            break
        except:
            print("Error en el nombre. Indica un nombre correcto: ")
    documento = {"presenters": nombre }
    filtro = {"year": 1,"presenters":1, "_id":0}
    cursor = find(documento,filtro,0)
    return cursor

def consulta7():
    while True:
        try:
            nombre = input("Nombre: ")
            break
        except:
            print("Error en el nombre. Indica un nombre correcto: ")
    documento = {"presenters":[nombre] }
    filtro = {"year": 1,"presenters":1, "_id":0}
    cursor = find(documento,filtro,0)
    return cursor

def consulta8():
    while True:
        try:
            cont = int(input("Cantidad de nombres: "))
            break
        except:
            print("Error. Indica una cantidad correcta.")
    nombres = []
    for i in range (0,cont):
        nombre = input("Nombre: ")
        nombres.append(nombre)
    documento = {"presenters": {"$all": nombres} }
    filtro = {"year": 1,"presenters":1, "_id":0}
    cursor = find(documento,filtro,0)
    return cursor

def consulta9():
    while True:
        try:
            nombre = input("Nombre: ")
            break
        except:
            print("Error en el nombre. Indica un nombre correcto: ")
    documento = {"contestants.artist": nombre}
    filtro = {"year": 1, "_id":0}
    cursor = find(documento,filtro,0)
    return cursor

def consulta10():
    while True:
        try:
            cadena = input("Cadena: ")
            break
        except:
            print("Error en el nombre. Usa las siglas de la cadena: ")
    documento = {"contestants.broadcaster": cadena}
    filtro = {"year": 1, "_id":0}
    orden = {"year": -1}
    cursor = find(documento,filtro,orden)
    return cursor

def consulta11():
    while True:
        try:
            mes = int(input("Mes: "))
            break
        except:
            print("Error en el mes. Indica el valor numérico del mes. ")
    rounds = {"$unwind": "$rounds"}
    date = {"$unwind": "$rounds.date"}
    match = {"$match": 
			    {"$expr": 
				    {"$ne": 
                        [{"$month": 
						    {"$dateFromString": 
							    {"dateString":'$rounds.date'}
                                }
                            },
                        mes]
                    }
                }
            }
    project = {"$project": {"year": "$year", "_id":0}}
    sort = {"$sort": {"year": -1}}
    limit = {"$limit": 3}
    agregacion = [rounds, date, match, project, sort,limit]
    cursor = aggregate(agregacion)
    return cursor

def consulta12():
    while True:
        try:
            puntos = int(input("Puntuación: "))
            break
        except:
            print("Error. Indica una puntuación correcta: ")
    rounds = {"$unwind": "$rounds"}
    performances = {"$unwind": "$rounds.performances"}
    scores = {"$unwind": "$rounds.performances.scores"}
    match = {"$match": {"rounds.performances.scores.points": {"$gt": puntos}}}
    group = {"$group": {"_id": "$year", "CancionesMas"+str(puntos): {"$count": {}}}}
    agregacion = [rounds, performances, scores, match, group]
    cursor = aggregate(agregacion)
    return cursor

def consulta13():
    unwind = {"$unwind": "$contestants"}
    group = {"$group": {"_id": "$contestants.broadcaster", "Participaciones": {"$count":{}}}}
    agregacion = [unwind, group]
    cursor = aggregate(agregacion)
    return cursor

def consultar():
    opcion = menu_consultar()
    while opcion != 14:
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
        else:
            print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
            opcion = menu_consultar()
        opcion = 14