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

def avistamientosCiudad(info,ciudad):
    listaCiudades = lt.newList('SINGLE_LINKED')
    for avistamiento in lt.iterator(info['UFOS']):
        if not(lt.isPresent(listaCiudades,avistamiento["city"])):
            lt.addLast(listaCiudades, avistamiento["city"])
        if avistamiento["city"] == ciudad:
            datos = avistamiento["datetime"].split(" ")
            hora = (datos[1]).split(":")
            fecha = (datos[0]).split("-")
            tiempo = fecha + hora
            om.put(info["cities"],tiempo,avistamiento)
    return info["cities"],listaCiudades



# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
