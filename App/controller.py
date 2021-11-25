﻿"""
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

# Inicialización del Analizador 

def init():
    analyzer = model.newAnalyzer()
    return analyzer


# Funciones para la carga de datos

def loadServices(analyzer):
    routesfile = cf.data_dir + "routes_full.csv"
    input_file1 = csv.DictReader(open(routesfile, encoding="utf-8"),
                                delimiter=",")
    lastroute = None
    airportsfile = cf.data_dir +  "airports_full.csv"
    input_file2 = csv.DictReader(open(airportsfile, encoding="utf-8"),
                                delimiter=",")
    citiesfile = cf.data_dir + "worldcities.csv"
    input_file3 = csv.DictReader(open(citiesfile, encoding="utf-8"),
                                delimiter=",")
    for airport in input_file2 : 
        model.addAirportbyCode(analyzer,airport)
    for route in input_file1:
        model.addRoute(analyzer,route)
        model.addRoute_2(analyzer,route)
    for city in input_file3 : 
        model.addCity(analyzer,city)
    
    airports_1 = model.totalAirports(analyzer['routes'])
    airports_2 = model.totalAirports(analyzer['routes_2'])
    return analyzer,airports_1,airports_2
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
