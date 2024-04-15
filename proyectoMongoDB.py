import funcionesMongoDB

funcionesMongoDB.probarconexion()

opcion = funcionesMongoDB.menu()

while opcion != 0:
    if opcion == 1:
        funcionesMongoDB.eliminar()


    elif opcion == 2:
        funcionesMongoDB.insertar()


    elif opcion == 3:
        funcionesMongoDB.actualizar()


    elif opcion == 4:
        funcionesMongoDB.consultar()

    else:
        print("Error. Por favor, indica el número de la opción del menú que quieres ejectuar: ")
    opcion = funcionesMongoDB.menu()

funcionesMongoDB.cerrarcliente()