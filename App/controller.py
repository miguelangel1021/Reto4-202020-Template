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

import config as cf
from App import model
import csv
import os

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def iniciar_catalog():
    catalog= model.new_graph()
    return catalog
       

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadTrips(citibike):
    for filename in os.listdir(cf.data_dir):
        if filename.endswith('.csv'):
            print('Cargando archivo: ' + filename)
            loadFile(citibike, filename)
    return citibike
    

def loadFile(citibike, tripfile):
    """
    """
    tripfile = cf.data_dir + tripfile
    input_file = csv.DictReader(open(tripfile, encoding="utf-8"),
                                delimiter=",")
    for trip in input_file:
        model.addTrip(citibike, trip)
    
    return citibike

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def  totalConnections(catalog):
    return model.num_edges(catalog)

def totalStops(catalog):
    return model.num_vertices(catalog)

def num_scc(catalog):
    return model.numSCC(catalog)

def scc_1(catalog,station1,station2):
    return model.sameCC(catalog,station1,station2)

def estaciones_criticas(catalog):
    return model.estaciones_criticas(catalog)

def ruta_interes(catalog,latitud1,longitud1,latitud2,longitud2):
    path_,estacion_salida,estacion_llegada,costo=model.Ruta_interes_turistico(catalog,latitud1,longitud1,latitud2,longitud2)
    return path_,estacion_salida,estacion_llegada,costo

def recomendar_rutas(catalog,Rango):
    path_,estacion_salida,estacion_llegada,costo=model.Recomendar_rutas(catalog,Rango)
    return path_,estacion_salida,estacion_llegada,costo


def ruta_circular(grafo,tiempo,estacion_inicio):
    dfs=model.Ruta_turistica_circular(grafo,tiempo,estacion_inicio)
    return dfs