import numpy as np
import pandas as pd
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os
import phonenumbers
import folium
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
from datetime import datetime
from numberLocation import *



clave=[]
filas=[]
columnas=[]
def agregarPalabra():
    print("Ingrese su Palabra")
    pala=input()
    clave.append(pala)
    os.system("cls")

def listarPalabra():
    cont=0
    for reg in clave:
        print(cont,") ",reg)
        cont+=1

def eliminarPalabra():
    print("Ingrese el numero")
    num=int(input())
    clave.remove(num)

def agregarContacto():
    print("Ingresa su Nombre")
    nombre=input()
    nombre.append(filas)
    print("Ingresa tu numero")
    numero=input()
    numero.append(columnas)
    serie=pd.Series(data = filas , index= columnas)
    print(serie)


def Activar(text):
    for i in clave:
        if i in text:
            ubicacion()
            pywhatkit.sendwhatmsg("+56982044516", "Hola Mundo", 23, 26)
            print("Mensaje Enviado")
