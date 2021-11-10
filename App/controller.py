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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog
# Funciones para la carga de datos
def loadData(catalog):
    loadUfo(catalog)

def loadUfo(catalog):
    ufoFile = cf.data_dir + "UFOS/UFOS-utf8-large.csv"
    input_file = csv.DictReader(open(ufoFile, encoding='utf-8'))
    for ufo in input_file:
        model.addUfo(catalog, ufo) 
         
# Funciones para la carga de datos

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

# Requisito 1
def avistamientosCiudad(info,ciudad):
    return model.avistamientosCiudad(info,ciudad)
# Requisito 2
def avistamientosDuracion(catalog,segundos):
    return model.avistamientosDuracion(catalog,segundos)
# Requisito 3
def avistamientos_tiempo(info,tiempo_min,tiempo_max):
    return model.avistamientos_tiempo(info,tiempo_min,tiempo_max)
# Requisito 4
def avistamientosRango(info,fecha_min,fecha_max):
    return model.avistamientosRango(info,fecha_min,fecha_max)
# Requisito 5
def avistamientos_zona(info,lat,long):
    return model.avistamientos_zona(info,lat,long)
