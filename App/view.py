"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import list as lt
"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________
recursionLimit=1000001

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información:")
    print("3- Calcular clusters:")
    print("4- Estaciones fuertemente conectadas:")
    print("5- Estaciones criticas: ")
    print("6- Recomendar ruta: ")
    print("7- Rutas de interes turistico: ")
    print("8- Rutas Circulares: ")
    print("0- Salir")
    print("*******************************************")


def optionTwo():
    print("\nCargando información de citibike....")
    controller.loadTrips(cont)
    numedges = controller.totalConnections(cont)
    numvertex = controller.totalStops(cont)
    print('Numero de vertices: ' + str(numvertex))
    print('Numero de arcos: ' + str(numedges))
    print('El limite de recursion actual: ' + str(sys.getrecursionlimit()))
    sys.setrecursionlimit(recursionLimit)
    print('El limite de recursion se ajusta a: ' + str(recursionLimit))
    

def optionThree():
    print('El número de clusters es: ' +
          str(controller.num_scc(cont)))

def optionFour():
    vertice1=input("Ingrese la Estacion 1:")
    vertice2=input("Ingrese la Estacion 2:")
    los_2=controller.scc_1(cont,vertice1,vertice2)
    if los_2==False:
        print("Las estaciones no estan fuertemente conectadas...")
    else: 
        print("Las estaciones estan fuertemente conectadas...")
def optionFive():
    estaciones=controller.estaciones_criticas(cont)
    
    print("Las estaciones top de llegda son:")
    for i in range (0,3):
        print(estaciones[i])
    print("Las estaciones top de salida son:")
    for i in range (3,6):
        print(estaciones[i])
    print("Las estaciones menos usadas son:")
    for i in range (6,9):
        print(estaciones[i])

def optionSeven():
    l1=input("Ingrese la latitud inicial: ")
    L1=input("Ingrese la longitud inicial: ")
    l2=input("Ingrese la latitud final: ")
    L2=input("Ingrese la longitud final: ")
    path_,estacion_salida,estacion_llegada,costo= controller.ruta_interes(cont,l1,L1,l2,L2)
    print("la estacion mas cercana a la cordenada inicial es: ",estacion_salida)
    print("la estacion mas cercana a la cordenada final es: ",estacion_llegada)
    print("El tiempo para llegar a la estacion final es: ",costo)
    print("***************************************")
    print("Las estaciones en la ruta son: ")
    iterador=it.newIterator(path_)
    while it.hasNext(iterador):
        element=it.next(iterador)
        print(element)
    
def optionSix():
    rango=input("ingrese el rango de edad: ")
    path_,estacion_salida,estacion_llegada,costo=controller.recomendar_rutas(cont,rango)
    if path_ is None: 
        print("No hay estaciones de salida ni llegada para ese rango de edad")
    elif path_ == 0:
        print("La estacion de salida recomendada es: ",estacion_salida)
        print("La estacion de llegada recomendada es: ",estacion_llegada)
        print("El tiempo estimado de viaje es:", costo)
    else:
        print("La estacion de salida recomendada es: ",estacion_salida)
        print("La estacion de llegada recomendada es: ",estacion_llegada)
        print("El tiempo estimado de viaje es:", costo)
        print("***************************************")
        print("Las estaciones en la ruta son: ")
        iterador=it.newIterator(path_)
        while it.hasNext(iterador):
            element=it.next(iterador)
            print(element)


def optionOcho():
    tiempo=input("ingrese_tiempo en minutos: ")
    estacion=input("ingrese_estacion inicial: ")
    dfs=controller.ruta_circular(cont,tiempo,estacion)
    print(dfs)
    if lt.isEmpty(dfs):
        print("No se han encontrado rutas circulares en el tiempo disponible...")
    else:
        tamaño=lt.size(dfs)
        print("Se encontraron",tamaño,"rutas circulares..." )
        print("Estas son las rutas circulares encontradas: \n")
    
        iterador=it.newIterator(dfs)
        while it.hasNext(iterador):
            diccionario=it.next(iterador)
            peso=diccionario["Peso"]/60
            lista=diccionario["ruta"]
            for i in lista:
                print(i)
            print(lista[0])
            print("La duracion estimada del viaje es:",round(peso,2),"minutos")
            print("************************"*2)


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.iniciar_catalog()

    elif int(inputs[0]) == 2:
        executiontime = timeit.timeit(optionTwo, number=1)
        print("Tiempo de ejecución: " + str(executiontime))

    elif int(inputs[0]) == 3:
        executiontime = timeit.timeit(optionThree, number=1)
        print("Tiempo de ejecución: " + str(executiontime))
    
    elif int(inputs[0])==4:
        executiontime = timeit.timeit(optionFour, number=1)
        print("Tiempo de ejecucion: " + str(executiontime) )
    
    elif int(inputs[0])==5:
        executiontime = timeit.timeit(optionFive, number=1)
        print("Tiempo de ejecucion: " + str(executiontime) )
    elif int(inputs[0])==6:
        executiontime = timeit.timeit(optionSix, number=1)
        print("Tiempo de ejecucion: " + str(executiontime) )
    elif int(inputs[0])==7:
        executiontime = timeit.timeit(optionSeven, number=1)
        print("Tiempo de ejecucion: " + str(executiontime) )
    elif int(inputs[0])==8:
        executiontime = timeit.timeit(optionOcho, number=1)
        print("Tiempo de ejecucion: " + str(executiontime) )

    else:
        sys.exit(0)
sys.exit(0)


"""
Menu principal
"""

