import pickle
from os.path import getsize


def menu():
    print("\x1b[1;35m"+'-'*80+"\x1b[0;m")
    print('\t''\t''\t'"\x1b[1;35m"+"Menu de opciones"+"\x1b[0;m")
    print("\x1b[1;35m"+'-'*80+"\x1b[0;m")
    print("1) Mostrar listado de participantes")
    print("2) Mostrar pais (o paises) con mayor cantidad de campeonatos ganados")
    print("3) Mostrar cantidad de campeones por confederacion")
    print("4) Generar archivo con los participantes de alguna confederacion")
    print("5) Buscar registro de confederacion")
    print("6) Armar fixture del proximo mundial")
    print("7) Buscar pais en el fixture")
    print("0) Salir")
    print()


def titulos():
    renglon = "{:<30} {:<18} {:<7} {}".format("Pais: |", "Confederacion: |", "Puntos: |", "Titulos:")
    return renglon


def titulos_2():
    renglon = "{:<30} {:<7} {}".format("Pais: |", "Puntos: |", "Titulos:")
    return renglon


def mostrar_participantes(vector):
    for seleccion in vector:
        print("\x1b[1;34m"+titulos()+"\x1b[0;m")
        print(seleccion)
    print()


def leer_mayores(vector_mayores):
    if len(vector_mayores) == 1:
        print()
        print("\x1b[1;36m"+"Seleccion con mas titulos:")
        print("*"*30+"\x1b[0;m")
    else:
        print("\x1b[1;33m"+"Selecciones con mas titulos:")
        print("*"*27+"\x1b[0;m")
    mostrar_participantes(vector_mayores)


def campeones_confederacion(vector_conteo):
    print()
    print("\x1b[1;36m"+"Cantidad de campeones por confederacion:")
    print("*"*42+"\x1b[0;m")
    tupla_confederaciones = "UEFA:", "CONMEBOL:", "CONCACAF:", "CAF:", "AFC:", "OFC:"
    for i in range(len(vector_conteo)):
        print("\x1b[1;32m"+tupla_confederaciones[i]+"\x1b[0;m", vector_conteo[i])
    print()


def confederaciones():
    print()
    print("\x1b[1;35m"+"CONFEDERACIONES"+"\x1b[0;m")
    print("\x1b[1;35m"+"*"*30+"\x1b[0;m")
    print("\x1b[1;36m"+ '0) UEFA'+"\x1b[0;m")
    print("\x1b[1;36m"+ '1) CONMEBOL'+"\x1b[0;m")
    print("\x1b[1;36m"+ '2) CONCACAF'+"\x1b[0;m")
    print("\x1b[1;36m"+ '3) CAF'+"\x1b[0;m")
    print("\x1b[1;36m"+ '4) AFC'+"\x1b[0;m")
    print("\x1b[1;36m"+ '5) OFC'+"\x1b[0;m")
    print("\x1b[1;36m"+ '-1) SALIR'+"\x1b[0;m")
    print()


def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "rb")
    peso = getsize(nombre_archivo)
    while archivo.tell() < peso:
        registro = pickle.load(archivo)
        print("\x1b[1;34m"+titulos_2()+"\x1b[0;m")
        print(registro)
    archivo.close()


def leer_fixture(fixture):
    grupos = "{:>17} {:>20} {:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format(
                                                "Grupo A", "Grupo B", "Grupo C",
                                                "Grupo D", "Grupo E", "Grupo F",
                                                "Grupo G", "Grupo H")

    print("\x1b[1;36m"+grupos+"\x1b[0;m")
    for i in range(len(fixture)):
        renglon = "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
                                                    fixture[i][0], fixture[i][1],
                                                      fixture[i][2],fixture[i][3],
                                                      fixture[i][4], fixture[i][5],
                                                      fixture[i][6], fixture[i][7])
        print("\x1b[1;35m"+"Equipo "+str(i + 1)+": "+"\x1b[0;m"+renglon)


def leer_ubicacion(ubicacion):
    tupla_grupos = "Grupo A", "Grupo B", "Grupo C", "Grupo D", "Grupo E", \
                       "Grupo F", "Grupo G", "Grupo H"
    if ubicacion == -1:
        print("\x1b[1;31m"+"No se encontro el pais en el fixture"+"\x1b[0;m")
    else:
        print("\x1b[1;33m"+"El pais forma parte del grupo "+tupla_grupos[ubicacion]+"\x1b[0;m")
