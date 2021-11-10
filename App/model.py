"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    info = {"UFOS": None,
             "cities": None           
                        }

    info["UFOS"] = lt.newList('SINGLE_LINKED')
    info["cities"] = om.newMap(omaptype='RBT')

    return info

def addUfo(info,ufo):
    lt.addLast(info['UFOS'], ufo)

# Funciones de consulta

# Requisito 1
def avistamientosCiudad(info,ciudad):
    AvistamientosCiudad = om.newMap(omaptype="RBT")
    mapCiudades = mp.newMap(160,maptype='PROBING',loadfactor=0.50)
    for avistamiento in lt.iterator(info['UFOS']):
        if not(mp.contains(mapCiudades, avistamiento["city"])):
            mp.put(mapCiudades, avistamiento["city"],0)
        if avistamiento["city"] == ciudad:
            datos = avistamiento["datetime"].split(" ")
            hora = (datos[1]).split(":")
            fecha = (datos[0]).split("-")
            tiempo = fecha + hora
            om.put(AvistamientosCiudad,tiempo,avistamiento)
    return AvistamientosCiudad,mapCiudades

# Requisito 2
def avistamientosDuracion(info,segundos):
    AvistamientosPorDuracion = om.newMap(omaptype="RBT")
    duracionMaxima = -1
    for avistamiento in lt.iterator(info["UFOS"]):
        tiempo = float(avistamiento["duration (seconds)"])
        if tiempo > duracionMaxima:
            duracionMaxima = tiempo
        if segundos[0] <= tiempo and segundos[1] >= tiempo:
            om.put(AvistamientosPorDuracion,[tiempo,avistamiento["city"],avistamiento["country"],avistamiento["datetime"]],avistamiento)

    contador = 0
    for avistamiento in lt.iterator(info["UFOS"]):
        tiempo = float(avistamiento["duration (seconds)"])
        if tiempo == duracionMaxima:
            contador += 1

    return AvistamientosPorDuracion,duracionMaxima,contador


# Requisito 5
def avistamientos_zona(info,lat,long):
    info_avistamiento = om.newMap(omaptype="RBT")
    for avistamiento in lt.iterator(info["UFOS"]):
        Latitud = float(avistamiento["latitude"])
        Longitud = float(avistamiento["longitude"])
        datos = avistamiento["datetime"].split(" ")
        hora = (datos[1]).split(":")
        fecha = (datos[0]).split("-")
        tiempo = fecha + hora
        if Latitud > lat[0] and Latitud < lat[1] and Longitud > long[0] and Longitud < long[1]:
            om.put(info_avistamiento,[float(avistamiento["latitude"]),float(avistamiento["longitude"]),tiempo],avistamiento)
    return info_avistamiento

        





# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

