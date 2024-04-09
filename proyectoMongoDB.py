import funcionesMongoDB

opcion = funcionesMongoDB.menu()

while opcion != 0:
    if opcion == 1:
        funcionesMongoDB.menu_eliminar()
        funcionesMongoDB.menu()

    if opcion == 2:
        funcionesMongoDB.menu_insertar()
        funcionesMongoDB.menu()

    if opcion == 3:
        funcionesMongoDB.menu_actualizar()
        funcionesMongoDB.menu()

    if opcion == 4:
        funcionesMongoDB.menu_consultar()
        funcionesMongoDB.menu()