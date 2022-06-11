from ast import If
import os
import speech_recognition as sr
import pyttsx3
from Funciones import *

respuesta=0
while respuesta!=6:
    print("================")
    print(" WOMEN SECURITY ")
    print("================")
    print("1) Agregar Palabra Claves")
    print("2) Listar Palabras Claves")
    print("3) Eliminar Palabras Claves")
    print("4) Agregar Contacto")
    print("5) Activar Bot")
    print("6) Salir")
    opcion = int(input("Ingrese Opcion "))

    if opcion == 1:
        print("================")
        print(" WOMEN SECURITY ")
        print("================")
        agregarPalabra()

    if opcion == 2:
        print("================")
        print(" WOMEN SECURITY ")
        print("================")
        listarPalabra()     
    if opcion == 3:
        print("================")
        print(" WOMEN SECURITY ")
        print("================")
        eliminarPalabra()
    if opcion == 4:
        print("================")
        print(" WOMEN SECURITY ")
        print("================")
        agregarContacto()
    if opcion == 5:
        os.system("cls")
        #Guardamos la funcion de reconocimiento de voz en la variable Reco
        reco = sr.Recognizer()
        #Iniciamos nuestra libreria que convierte texto a voz
        engine = pyttsx3.init() 
        #Configuracion de la velocidad de habla de nuestro bot
        rate = engine.getProperty('rate')
        engine.setProperty('rate',170)
        try:
            #Con el Microfono seleccionado haga lo siguiente:
            with sr.Microphone() as micro:
                #Limitamos el ruido de Ambiente
                reco.adjust_for_ambient_noise(micro)
                print("!Di Algo!")    
                #Guarda lo que se hablo en la variable voz
                voz= reco.listen(micro)    
                #Guardamos el texto de lo que hablamos
                tex= reco.recognize_google(voz).lower()
                try:
                    os.system("cls")
                    print("El reconocimiento de voz de Google cree que dijiste: " + tex)
                    Activar(tex)
                except sr.UnknownValueError:
                    print("El reconocimiento de voz de Google no pudo entenderte")
                    engine.say("El reconocimiento de voz de Google no pudo entenderte")
                    engine.runAndWait()
                    engine.stop()
                except sr.RequestError as e:
                    print("No se pudieron solicitar los resultados del servicio de reconocimiento de voz de Google; {0}".format(e))
        except:
            rate = engine.getProperty('rate')
            engine.setProperty('rate',170)
            engine.say("Algo Salio Mal!")
            engine.runAndWait()
            engine.stop()
    if opcion == 6:
        respuesta = 6