from soporte import *
from lectura import *
from os.path import exists



def principal():
    vector_selecciones = []
    fixture = []
    vector_confederacion = []
    nombre_archivo = ""
    cargar_vector(vector_selecciones)
    salir = False

    while not salir:
        menu()
        opcion = cargar_entre(0, 7, "Elija su opcion: ")

        if opcion == 1:
            mostrar_participantes(vector_selecciones)

        if opcion == 2:
            vector_mayores = buscar_mayor(vector_selecciones)
            leer_mayores(vector_mayores)

        if opcion == 3:
            vector_conteo = contar_campeones(vector_selecciones)
            campeones_confederacion(vector_conteo)

        if opcion == 4:
            confederaciones()
            x = cargar_entre(-1, 5, "Elija la confederacion que desee procesar: ")
            if x != -1:
                vector_confederacion = generar_vector(vector_selecciones, x)
                nombre_archivo = nombrar_archivo(x)
                generar_archivo(vector_confederacion, nombre_archivo)
                print("\x1b[1;36m"+"Archivo generado: "+nombre_archivo)
                print("Cantidad de registros: "+str(len(vector_confederacion))+"\x1b[0;m")
                print()

        if opcion == 5:
            confederaciones()
            x = cargar_entre(-1, 5, "Elija el numero de confederacion de la cual desea buscar su archivo: ")
            nombre_archivo = nombrar_archivo(x)
            if x == -1:
                pass
            elif not exists(nombre_archivo):
                vector_confederacion = generar_vector(vector_selecciones, x)
                generar_archivo(vector_confederacion, nombre_archivo)
                leer_archivo(nombre_archivo)
            else:
                leer_archivo(nombre_archivo)

        if opcion == 6:
            anfitrion = validar_anfitrion(vector_selecciones)
            if anfitrion != -1:
                fixture = generar_fixture(anfitrion, vector_selecciones)
                leer_fixture(fixture)

        if opcion == 7:
            if len(fixture) > 0:
                pais = input("\x1b[1;32m"+"Ingrese el nombre del pais que desee buscar: "+"\x1b[0;m")
                ubicacion = buscar_fixture(fixture, pais)
                leer_ubicacion(ubicacion)
            else:
                print("\x1b[1;31m"+"Error, no se cargo el fixture (utilizar opcion 6)"+"\x1b[0;m")
            print()

        if opcion == 0:
            salir = True


if __name__ == "__main__":
    principal()
