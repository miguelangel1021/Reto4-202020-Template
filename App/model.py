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
import config
from DISClib.Algorithms.Graphs import scc
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.DataStructures import edge as e
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
# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================

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