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
import math
import config

from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.DataStructures import edge as e
from DISClib.Algorithms.Sorting import insertionsort as sort
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import stack as st
from DISClib.Algorithms.Graphs import dfs 

assert config



"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo
def new_graph():
    citibike={}
    citibike["graph"] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=compareStations)

    citibike['Estaciones']=m.newMap(numelements=2107,
                                     maptype='PROBING',
                                     comparefunction=compararEstaciones)
    
    return(citibike)

def addTrip(citibike, trip):
    """
    """
    origin = trip['start station id']
    destination = trip['end station id']
    duration = int(trip['tripduration'])
    addStation(citibike, origin)
    addStation(citibike, destination)
    addConnection(citibike, origin, destination, duration)
    entry_org=m.get(citibike["Estaciones"],origin)
    if entry_org is None:
        name=trip['start station name']
        Latitud_1=trip["start station latitude"]
        Longitud_1=trip["start station longitude"]
        entry_org2=newEstacion(name,Latitud_1,Longitud_1)
        m.put(citibike["Estaciones"],origin,entry_org2)
    else:
        entry_org2=me.getValue(entry_org)
    entry_dest=m.get(citibike["Estaciones"],destination)
    if entry_dest is None:
        name_2=trip['end station name']
        Latitud_2=trip["end station latitude"]
        Longitud_2=trip["end station longitude"]
        entry_dest2=newEstacion(name_2,Latitud_2,Longitud_2)
        m.put(citibike["Estaciones"],destination,entry_dest2)
    else:
        entry_dest2=me.getValue(entry_dest)
    agregar_edades_salida(entry_org2,trip)
    agregar_edades_llegada(entry_dest2,trip)
    entry_org2["viajes_salida"]+=1
    entry_dest2["viajes_llegada"]+=1
    

def agregar_edades_salida(entry, trip):

    año=trip["birth year"]
    edad=2018-int(año)
    if 0<edad<=10: 
        entry_=om.get(entry["Edades_salida"],"0-10")
        if entry_ is None:
            om.put(entry["Edades_salida"],"0-10",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"0-10",value)
    elif 11<=edad<=20:
        entry_=om.get(entry["Edades_salida"],"11-20")
        if entry_ is None:
            om.put(entry["Edades_salida"],"11-20",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"11-20",value)
    elif 21<=edad<=30:
        entry_=om.get(entry["Edades_salida"],"21-30")
        if entry_ is None:
            om.put(entry["Edades_salida"],"21-30",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"21-30",value)
    elif 31<=edad<=40:
        entry_=om.get(entry["Edades_salida"],"31-40")
        if entry_ is None:
            om.put(entry["Edades_salida"],"31-40",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"31-40",value)
    elif 41<=edad<=50:
        entry_=om.get(entry["Edades_salida"],"41-50")
        if entry_ is None:
            om.put(entry["Edades_salida"],"41-50",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"41-50",value)
    elif 51<=edad<=60:
        entry_=om.get(entry["Edades_salida"],"51-60")
        if entry_ is None:
            om.put(entry["Edades_salida"],"51-60",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"51-60",value)
    else:
        entry_=om.get(entry["Edades_salida"],"60+")
        if entry_ is None:
            om.put(entry["Edades_salida"],"60+",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_salida"],"60+",value)
    

def agregar_edades_llegada(entry, trip):

    año=trip["birth year"]
    edad=2018-int(año)
    if 0<edad<=10: 
        entry_=om.get(entry["Edades_llegada"],"0-10")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"0-10",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"0-10",value)
    elif 11<=edad<=20:
        entry_=om.get(entry["Edades_llegada"],"11-20")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"11-20",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"11-20",value)
    elif 21<=edad<=30:
        entry_=om.get(entry["Edades_llegada"],"21-30")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"21-30",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"21-30",value)
    elif 31<=edad<=40:
        entry_=om.get(entry["Edades_llegada"],"31-40")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"31-40",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"31-40",value)
    elif 41<=edad<=50:
        entry_=om.get(entry["Edades_llegada"],"41-50")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"41-50",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"41-50",value)
    elif 51<=edad<=60:
        entry_=om.get(entry["Edades_llegada"],"51-60")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"51-60",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"51-60",value)
    else:
        entry_=om.get(entry["Edades_llegada"],"60+")
        if entry_ is None:
            om.put(entry["Edades_llegada"],"60+",1)
        else:
            value=me.getValue(entry_)
            value+=1
            om.put(entry["Edades_llegada"],"60+",value)
    


def addStation(citibike, stationid):
    """
    Adiciona una estación como un vertice del grafo
    """
    if not gr.containsVertex(citibike ["graph"], stationid):
            gr.insertVertex(citibike ["graph"], stationid)
    return citibike

def addConnection(citibike, origin, destination, duration):
    """
    Adiciona un arco entre dos estaciones
    """
    edge = gr.getEdge(citibike ["graph"], origin, destination)
    if edge is None:
        gr.addEdge(citibike["graph"], origin, destination, duration)
    else:
        e.updateAverageWeigth(edge,duration)
    
    return citibike


def newEstacion(Nombre,Latitud,Longitud):
    
    Estacion = {'Nombre': Nombre, 'Latitud': Latitud, "Longitud": Longitud, "viajes_salida":0 , "viajes_llegada": 0}


    Estacion["Edades_salida"]=om.newMap(omaptype='RBT',
                                      comparefunction=compararEdades)
    Estacion["Edades_llegada"]=om.newMap(omaptype='RBT',
                                      comparefunction=compararEdades)

    return Estacion 

# ==============================
# Funciones de consulta
# ==============================

def numSCC(graph):
    sc = scc.KosarajuSCC(graph["graph"])
    return scc.connectedComponents(sc)

def sameCC(sc, station1, station2):
    return scc.stronglyConnected(sc["graph"], station1, station2)

def num_vertices(graph):
    return gr.numVertices(graph["graph"])

def num_edges(graph):
    return gr.numEdges(graph["graph"])

def estaciones_criticas(citibike):
    
    listavertices=lt.newList("ARRAY_LIST")
    grafo=citibike["graph"]
    
    vertices=gr.vertices(grafo)
    iterador=it.newIterator(vertices)
    while it.hasNext(iterador):
        elemento=it.next(iterador)
        entry=m.get(citibike["Estaciones"],elemento)
        valor=me.getValue(entry)
        indegree=valor["viajes_llegada"]
        outdegree=valor["viajes_salida"]
        menor_ut=indegree+outdegree
        estacion={}
        estacion["Estacion"]=elemento
        estacion["indegree"]=indegree
        estacion["outdegree"]=outdegree
        estacion["menor_ut"]=menor_ut
        lt.addLast(listavertices,estacion)
    
    lista=[]
    sort.insertionSort(listavertices,great)
    indegree_list=lt.subList(listavertices,1,3)
    iterador=it.newIterator(indegree_list)
    while it.hasNext(iterador):
        element=it.next(iterador)["Estacion"]
        entry=m.get(citibike["Estaciones"],element)

        if entry is not None:
            value=me.getValue(entry)
            nombre=value["Nombre"]
            lista.append(nombre)
   
    sort.insertionSort(listavertices,great2)
    outdegree_=lt.subList(listavertices,1,3)
    iterador2=it.newIterator(outdegree_)
    while it.hasNext(iterador2):
        element=it.next(iterador2)["Estacion"]
        entry=m.get(citibike["Estaciones"],element)
        if entry is not None:
            value=me.getValue(entry)
            nombre=value["Nombre"]
            lista.append(nombre)

    sort.insertionSort(listavertices,less)
    menor_u_=lt.subList(listavertices,1,3)
    iterador3=it.newIterator(menor_u_)
    while it.hasNext(iterador3):
        element=it.next(iterador3)["Estacion"]
        entry=m.get(citibike["Estaciones"],element)
        if entry is not None:
            value=me.getValue(entry)
            nombre=value["Nombre"]
            lista.append(nombre)

    return lista 
    

def Recomendar_rutas(grafo,rango_edad):
    
    mayor_salida=0
    mayor_llegada=0
    estacion_salida=None
    estacion_llegada=None
    lista=m.keySet(grafo["Estaciones"])
    iterador=it.newIterator(lista)
    while it.hasNext(iterador):
        elemento=it.next(iterador)
        entry=m.get(grafo["Estaciones"],elemento)
        
        valor=me.getValue(entry)
        
        entry_salida=om.get(valor["Edades_salida"],rango_edad)
        entry_llegada=om.get(valor["Edades_llegada"],rango_edad)
        cant_edades_salida=None
        cant_edades_llegada=None 
        if entry_salida is not None:
            cant_edades_salida=me.getValue(entry_salida)
        if entry_llegada is not None:
            cant_edades_llegada=me.getValue(entry_llegada)
        if cant_edades_salida is not None:
            if cant_edades_salida>=mayor_salida:
                mayor_salida=cant_edades_salida
                estacion_salida=elemento
        if cant_edades_llegada is not None:
            if cant_edades_llegada>=mayor_llegada:
                mayor_llegada=cant_edades_llegada
                estacion_llegada=elemento
    
    if estacion_salida == None and estacion_llegada == None:
        return None,None,None,None
    else:
        path=djk.Dijkstra(grafo["graph"],estacion_salida)
        path_=djk.pathTo(path,estacion_llegada)
        costo=djk.distTo(path,estacion_llegada)
        
        estaciones=grafo["Estaciones"]
    
        entry_sal=m.get(estaciones,estacion_salida)
        entry_lle=m.get(estaciones,estacion_llegada)
    
        estacion_sali=me.getValue(entry_sal)["Nombre"]
        estacion_lleg=me.getValue(entry_lle)["Nombre"]
    
        lista2=lt.newList("ARRAY_LIST",comparar_esta)
        while (not st.isEmpty(path_)):
                stop = st.pop(path_)
                entryA=m.get(estaciones,stop["vertexA"])
                estacion_1=me.getValue(entryA)["Nombre"]
                if lt.isPresent(lista2,estacion_1) == 0:
                    lt.addLast(lista2,estacion_1)
                
                entryB=m.get(estaciones,stop["vertexB"])
                estacion_2=me.getValue(entryB)["Nombre"]
                if lt.isPresent(lista2,estacion_2) == 0:
                
                    lt.addLast(lista2,estacion_2)
            
        
        
    if estacion_sali == estacion_lleg:
        return 0, estacion_sali,estacion_lleg,costo
    else: 
        return lista2,estacion_sali,estacion_lleg,costo


def Ruta_interes_turistico(grafo,latitud1,longitud1,latitud2,longitud2):

    Latitud1 = float(latitud1)/57.29577951
    Longitud1=float(longitud1)/57.29577951
    Latitud2=float(latitud2)/57.29577951
    Longitud2=float(longitud2)/57.29577951
   
    menor=None
    menor_dist=10000000000
    menor2=None
    menor_dist2=10000000000
    estaciones=grafo["Estaciones"]
    entry=m.keySet(estaciones)
    iterador=it.newIterator(entry)
    while it.hasNext(iterador):
        elemento=it.next(iterador)
        entry=m.get(estaciones,elemento)
        valor=me.getValue(entry)
        latitud= float(valor["Latitud"])/57.29577951
        longitud= float(valor["Longitud"])/57.29577951
        dis_estacion_salida= 3963.0 * math.acos(math.sin(Latitud1)*math.sin(latitud)+math.cos(Latitud1)*math.cos(latitud)*math.cos( longitud- Longitud1))
        dis_estacion_llegada= 3963.0 * math.acos(math.sin(Latitud2)*math.sin(latitud)+math.cos(Latitud2)*math.cos(latitud)*math.cos(longitud - Longitud2))
        if dis_estacion_salida<=menor_dist:
            menor=elemento
            menor_dist=dis_estacion_salida
        if dis_estacion_llegada<=menor_dist2:
            menor2=elemento
            menor_dist2=dis_estacion_llegada
    
    lista=lt.newList("ARRAY_LIST",comparar_esta)
    path=djk.Dijkstra(grafo["graph"],menor)
    path_=djk.pathTo(path,menor2)
    costo=djk.distTo(path,menor2)
    estaciones=grafo["Estaciones"]
    
    entry_sal=m.get(estaciones,menor)
    entry_lle=m.get(estaciones,menor2)
    
    estacion_sali=me.getValue(entry_sal)["Nombre"]
    estacion_lleg=me.getValue(entry_lle)["Nombre"]
    
    while (not st.isEmpty(path_)):
            stop = st.pop(path_)
            entryA=m.get(estaciones,stop["vertexA"])
            estacion_1=me.getValue(entryA)["Nombre"]
            if lt.isPresent(lista,estacion_1) == 0:
                lt.addLast(lista,estacion_1)
            
            entryB=m.get(estaciones,stop["vertexB"])
            estacion_2=me.getValue(entryB)["Nombre"]
            if lt.isPresent(lista,estacion_2) == 0:
                lt.addLast(lista,estacion_2)
            
    
    return lista,estacion_sali,estacion_lleg,costo

def Ruta_turistica_circular(graph,tiempo,estacion_inicio):

    Tiempo=float(tiempo)*60 
    kosa=scc.KosarajuSCC(graph["graph"])
    est_k_idscc= kosa["idscc"]
    dfs_recor=dfs.DepthFirstSearchsSCC(graph["graph"],estacion_inicio,est_k_idscc)
    
    Lista=m.keySet(dfs_recor["visited"])
    iterador=it.newIterator(Lista)
    L2=lt.newList()
    while it.hasNext(iterador):
        element=it.next(iterador)
        camino=None
        if  dfs.hasPathTo(dfs_recor,element):
            vertices=gr.adjacents(graph["graph"],element)
            
            it2=it.newIterator(vertices)
            while it.hasNext(it2):
                elemento2=it.next(it2)
                if elemento2  == estacion_inicio:
                    camino=dfs.pathTo(dfs_recor,element)
            if camino != None:
                lt.addLast(L2,camino)
    
    
    lista_rutas=lst=lt.newList("ARRAY_LIST")
    iterador2=it.newIterator(L2)
    while it.hasNext(iterador2):
        elemento=it.next(iterador2)
        lst=[]
        while (not st.isEmpty(elemento)):
            stop= st.pop(elemento)
            lst.append(stop)
        lt.addLast(lista_rutas,lst)
    
    lista_final=lt.newList()
    iterador_fin=it.newIterator(lista_rutas)
    while it.hasNext(iterador_fin):
        lista_pe=it.next(iterador_fin)
        
        total=0
        total+=(len(lista_pe)-1)*20*60
        edge=gr.getEdge(graph["graph"],lista_pe[len(lista_pe)-1],lista_pe[0])
        peso=float(edge["weight"])
        total+=peso
        i=0
        while  i<len(lista_pe):
            estacion=lista_pe[i]
            j=i+1
            while j !=0 and i<((len(lista_pe))-1): 
                estacion2=lista_pe[j]
                edge2=gr.getEdge(graph["graph"],estacion,estacion2)
                peso2=float(edge2["weight"])
                total+=peso2
                j=0
            i+=1
        
        lista_parcial=[]
        ruta={"Peso":round(total,2), "ruta":None}
        if total <= Tiempo:
            i=0
            while i<len(lista_pe):
                estacion1=lista_pe[i]
                entry=m.get(graph["Estaciones"],estacion1)
                valor=me.getValue(entry)
                nombre=valor["Nombre"]
                lista_parcial.append(nombre)
                i+=1
            
            ruta["ruta"]=lista_parcial
            lt.addLast(lista_final,ruta)

    return lista_final 


# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def comparar_esta(estacion1,estacion2):
    if estacion1 == estacion2:
        return 0
    else:
        return 1

def great(elemento1,elemento2):
    if elemento1["indegree"]>elemento2["indegree"]:
        return True
def great2(elemento1,elemento2):
    if elemento1["outdegree"]>elemento2["outdegree"]:
        return True
def less(elemento1,elemento2):
    if elemento1["menor_ut"]<elemento2["menor_ut"]:
        return True
def compareStations(station, keyvaluestation):
    """
    Compara dos estaciones
    """
    code = keyvaluestation['key']
    if (station == code):
        return 0
    elif (station > code):
        return 1
    else:
        return -1



def compararEstaciones(E1, E2):
   
    entry = me.getKey(E2)
    if (E1 == entry):
        return 0
    elif (E1 > entry):
        return 1
    else:
        return -1

def compararEdades(Edad1, Edad2):
   
    
    if (Edad1 == Edad2):
        return 0
    elif (Edad1 > Edad2):
        return 1
    else:
        return -1