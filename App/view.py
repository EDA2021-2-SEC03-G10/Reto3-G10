"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

# Requisito 1
def avistamientosCiudad():
    pass
# Requisito 2
def avistamientosDuracion():
    pass
# Requisito 3
def avistamientosSegunHora():
    pass
# Requisito 4
def avistamientosRango():
    pass
# Requisito 5
def avistamientosZona():
    pass



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar los avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una Zona Geográfica")
catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        size = lt.size(catalog["UFOS"])
        print("Total de avistamientos cargados: " + str(size))

    elif int(inputs[0]) == 2:
        tamaño = om.size(catalog["cities"])
        print("La cantidad de nodos es de: " + str(tamaño))
        altura = om.height(catalog["cities"])
        print("La altura del arbo es de: "+ str(altura))
    else:
        sys.exit(0)
sys.exit(0)
