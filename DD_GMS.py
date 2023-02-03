# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 12:06:49 2023

@author: Gabriela Matamoros
"""


print("     Bienvenidos al conversos de coordenadas     ")

print("       Tipos de conversión a realizar       ")
print("  1.Grados, Minutos y Segundos a Decimales")
print("  2.Decimales a Grados, Minutos y Segundos")

conver1=float(input("     Seleccione el número del tipo de conversión a realizar: >>   "))

if conver1 == 1:
    print("     Has seleccionado convertir GMS a DD     ")
    print("ingrese primero los valores de longitud y despues los valores de latitud")
    
    long_grd= float(input("\nIngrese el valor de los grados en longitud >  "))
    long_minu= float(input("Ingrese el valor de los minutos en longitud >  "))
    long_seg =float(input("Ingrese el valor de los segundos en longitud >  "))
    
    
    long_minu_1 = long_seg/60 + long_minu
    long_grd_1 = (long_minu_1) / 60 + long_grd
    
    
    if long_grd_1 >=0:
        hem_lon_grd = "E"
    else:
        hem_lon_grd = "W"
        
            
    lati_grd= float(input("\nIngrese el valor de los grados en latitud >  "))
    lati_minu= float(input("Ingrese el valor de los minutos en latitud >  "))
    lati_seg =float(input("Ingrese el valor de los segundos en latitud >  "))
    
    
    lati_minu_1 = lati_seg/60 + lati_minu
    lati_grd_1 = (lati_minu_1) / 60 + lati_grd
    
    
    if lati_grd_1 >=0:
        hem_lat_grd = "N"
    else:
        hem_lat_grd = "S"
        
    print("\n-->Las coordenadas son: >> ", lati_grd_1, hem_lat_grd, "  <<")
    print("\n-->Las coordenadas son: >> ", long_grd_1, hem_lon_grd, "  <<")
    
    
elif conver1 == 2:
     
    print("     Has seleccionado convertir DD a GMS     ")
    
    lon= float(input("\nIngrese el valor de la longitud >  "))
    lat= float(input("Ingrese el valor de la latitud >  "))
    
    
    
    lon_grd = int(abs(lon))
    lon_min = (abs(lon)-lon_grd) * 60
    lon_min_in = int(lon_min)
    lon_sec = (lon_min - lon_min) * 60
        
    if lon >=0:
        hem_lon = "E"
    else:
        hem_lon = "W"
            
        #x= f"{lon_grd}° {lon_min_in}' {lon_sec:.2f}'' {hem_lon}"
        
    lat_grd = int(abs(lat))
    lat_min = (abs(lat)-lat_grd) * 60
    lat_min_int = int(lat_min)
    lat_sec = (lat_min -lat_min_int) * 60
        
    if lat >=0:
        hem_lat= "N" 
    else:
        hem_lat= "S"
        
        
    print("\n--> Las coordenadas en Grados, Minuto y Segundos equivalen a: ")
    print(lon_grd,"°", lon_min_in,"'",  lon_sec,"´´", hem_lon)
    print(lat_grd,"°", lat_min_int,"'", lat_sec,"´´", hem_lat)
        
        