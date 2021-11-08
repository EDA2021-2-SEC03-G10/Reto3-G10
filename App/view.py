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
def avistamientosCiudad(catalog,ciudad):
    return controller.avistamientosCiudad(catalog,ciudad)
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
        
        print("\n")
        print(chr(27)+"[1;44m"+"Primeros 5 y últimos 5 avistamientos cargados "+chr(27)+"[0;37m")
        cuenta = 1
        for i in range(1,11):
            listaUfos = lt.getElement(catalog["UFOS"], cuenta)
            print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+listaUfos["datetime"],
                    chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+listaUfos["city"],
                    chr(27)+"[1;34m"+", State: " + chr(27)+"[0;37m"+listaUfos["state"],
                    chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+listaUfos["country"],
                    chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+listaUfos["shape"],
                    chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+listaUfos["duration (seconds)"],
                    chr(27)+"[1;34m"+", Comments: " + chr(27)+"[0;37m"+listaUfos["comments"],
                    chr(27)+"[1;34m"+", Date posted: " + chr(27)+"[0;37m"+listaUfos["date posted"]
                    )
            print("\n")
            cuenta += 1
            if cuenta == 6:
                cuenta = size - 4


    elif int(inputs[0]) == 2:
        tamaño = om.size(catalog["cities"])
        print("La cantidad de nodos es de: " + str(tamaño))
        altura = om.height(catalog["cities"])
        print("La altura del arbo es de: "+ str(altura))

        ciudad = input("Escriba el nombre de la ciudad: ")
        avistamientos,listaCiudades = avistamientosCiudad(catalog,ciudad)
        cantidad = om.size(avistamientos)
        numeroCiudades = lt.size(listaCiudades)
        print("El total de ciudades con reportes es de:", str(numeroCiudades))
        print("Se han reportado" , str(cantidad) , "avistamientos en la ciudad")

        print("\n")
        print(chr(27)+"[1;44m"+"Primeros 3 y últimos 3 avistamientos de la cuidad "+chr(27)+"[0;37m")
        contador = 0
        for i in range(0,6):
            if i <= 2:
                pos = i
            else:
                pos = int(cantidad)-3+contador
                contador += 1
            llave = om.select(avistamientos,pos)
            informacion = om.get(avistamientos,llave)["value"]
            print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacion["datetime"],
            chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacion["city"],
            chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacion["country"],
            chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacion["duration (seconds)"],
            chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacion["shape"]
            )
        
    else:
        sys.exit(0)
sys.exit(0)
