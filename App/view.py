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
from DISClib.ADT import map as mp
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
def avistamientosDuracion(catalog,segundos):
    return controller.avistamientosDuracion(catalog,segundos)
# Requisito 3
def avistamientosSegunHora():
    pass
# Requisito 4
def avistamientosRango():
    pass
# Requisito 5
def avistamientos_zona(catalog,lat,long):
    return controller.avistamientos_zona(catalog,lat,long)



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print(chr(27)+"[1;32m")
    print("Bienvenido")
    print(chr(27)+"[0;37m")
    print(chr(27)+"[4;32m"+"1" + chr(27)+ "[0;37m" + "- Cargar información en el catálogo")
    print(chr(27)+"[4;32m"+ "2" + chr(27)+ "[0;37m" + "- Contar los avistamientos en una ciudad")
    print(chr(27)+"[4;32m"+ "3" + chr(27)+ "[0;37m" + "- Contar los avistamientos por duración")
    print(chr(27)+"[4;32m"+ "4" + chr(27)+ "[0;37m" + "- Contar avistamientos por Hora/Minutos del día")
    print(chr(27)+"[4;32m"+ "5" + chr(27)+ "[0;37m" + "- Contar los avistamientos en un rango de fechas")
    print(chr(27)+"[4;32m"+ "6" + chr(27)+ "[0;37m" + "- Contar los avistamientos de una Zona Geográfica")

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
        cuenta0 = 1
        for i in range(1,11):
            listaUfos = lt.getElement(catalog["UFOS"], cuenta0)
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
            cuenta0 += 1
            if cuenta0 == 6:
                cuenta0 = size - 4


    elif int(inputs[0]) == 2:
        ciudad = input("Escriba el nombre de la ciudad: ")
        avistamientos,listaCiudades = avistamientosCiudad(catalog,ciudad)
        cantidad = om.size(avistamientos)
        numeroCiudades = mp.size(listaCiudades)
        print("El total de ciudades con reportes es de:", str(numeroCiudades))
        print("Se han reportado" , str(cantidad) , "avistamientos en la ciudad")
        print("\n")

        cuenta1 = 0
        if cantidad >= 6:
            print(chr(27)+"[1;44m"+"Primeros 3 y últimos 3 avistamientos de la cuidad "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,6):
                if i <= 2:
                    pos = i
                else:
                    pos = int(cantidad)-3+cuenta1
                    cuenta1 += 1
                llave = om.select(avistamientos,pos)
                informacion = om.get(avistamientos,llave)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacion["datetime"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacion["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacion["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacion["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacion["shape"])

        elif cantidad != 0:
            print(chr(27)+"[1;44m"+"Avistamientos de la cuidad "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,cantidad):
                llave = om.select(avistamientos,i)
                informacion = om.get(avistamientos,llave)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacion["datetime"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacion["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacion["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacion["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacion["shape"])
                print("\n")

        else:
            print("No se encontraron avistamientos en el rango")

        print("\n")
        tamaño = om.size(avistamientos)
        print("La cantidad de nodos es de: " + str(tamaño))
        altura = om.height(avistamientos)
        print("La altura del arbol es de: "+ str(altura))

    elif int(inputs[0]) == 3:
        segMin = float(input("Ingrese el tiempo minimo en segundos: "))
        segMax = float(input("Ingrese el tiempo maximo en segundos: "))
        mapPorDuracion, duracionMaxima, numMayorDuracion = avistamientosDuracion(catalog,[segMin,segMax])
        tamañoMap = int(om.size(mapPorDuracion))
        print("\n")
        print("La duracion maxima fue: "+ str(duracionMaxima))
        print("El numero total de avistamientos con duracion maxima es de: "+ str(numMayorDuracion))
        print("La cantidad de avistamientos en el rango es: "+ str(tamañoMap))
        print("\n")

        cuentaReq2 = 0
        if tamañoMap >= 6:
            print(chr(27)+"[1;44m"+"Primeros 3 y últimos 3 avistamientos por duracion "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,6):
                if i <= 2:
                    pos = i
                else:
                    pos = int(tamañoMap)-3+cuentaReq2
                    cuentaReq2 += 1
                llaveReq2 = om.select(mapPorDuracion,pos)
                informacionReq2 = om.get(mapPorDuracion,llaveReq2)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacionReq2["datetime"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacionReq2["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacionReq2["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacionReq2["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacionReq2["shape"])
                print("\n")

        elif tamañoMap != 0:
            print(chr(27)+"[1;44m"+"Avistamientos por duracion "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,tamañoMap):
                llaveReq2 = om.select(mapPorDuracion,i)
                informacionReq2 = om.get(mapPorDuracion,llaveReq2)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacionReq2["datetime"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacionReq2["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacionReq2["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacionReq2["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacionReq2["shape"])
                print("\n")

        else:
            print("No se encontraron avistamientos en el rango")


    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        lat_min = float(input("Ingrese la latitud mínima: "))
        lat_max = float(input("Ingrese la latitud máxima: "))
        long_min = float(input("Ingrese la longitud mínima: "))
        long_max = float(input("Ingrese la longitud máxima: "))
        lat =[lat_min,lat_max]
        long= [long_min,long_max]
        Datos = avistamientos_zona(catalog,lat,long)
        tamaño = om.size(Datos)
        print("El número de avistamientos de la zona es: " + str(tamaño))
        print("\n")
        
        contador = 0
        if tamaño >= 10:
            print(chr(27)+"[1;44m"+"Los Primeros 5 y últimos 5 avistamientos de la zona: "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,10):
                if i <= 4:
                    pos = i
                else:
                    pos = int(tamaño)-5+contador
                    contador += 1
                llave = om.select(Datos,pos)
                informacion = om.get(Datos,llave)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacion["datetime"],
                chr(27)+"[1;34m"+", longitude: " + chr(27)+"[0;37m"+informacion["longitude"],
                chr(27)+"[1;34m"+", latitude: " + chr(27)+"[0;37m"+informacion["latitude"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacion["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacion["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacion["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacion["shape"])
                print("\n")

        elif tamaño != 0:
            print(chr(27)+"[1;44m"+"Avistamientos de la zona: "+chr(27)+"[0;37m")
            print("\n")
            for i in range(0,tamaño):
                llave = om.select(Datos,i)
                informacion = om.get(Datos,llave)["value"]
                print(chr(27)+"[1;34m"+"Datetime: " + chr(27)+"[0;37m"+informacion["datetime"],
                chr(27)+"[1;34m"+", longitude: " + chr(27)+"[0;37m"+informacion["longitude"],
                chr(27)+"[1;34m"+", latitude: " + chr(27)+"[0;37m"+informacion["latitude"],
                chr(27)+"[1;34m"+", City: " + chr(27)+"[0;37m"+informacion["city"],
                chr(27)+"[1;34m"+", Country: " + chr(27)+"[0;37m"+informacion["country"],
                chr(27)+"[1;34m"+", Duration (seconds): " + chr(27)+"[0;37m"+informacion["duration (seconds)"],
                chr(27)+"[1;34m"+", Shape: " + chr(27)+"[0;37m"+informacion["shape"])
                print("\n")
        else:
            print("No se encuentran avistamientos en el rango")



            
    else:

        sys.exit(0)
sys.exit(0)
