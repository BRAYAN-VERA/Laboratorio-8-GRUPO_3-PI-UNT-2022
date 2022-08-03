# Escribir un programa que mediante voz pregunte los datos de una persona, para
# luego crear un archivo csv con los datos consultados. Si una nueva persona quiere
# registrar sus datos, el programa debe anexar estos en el mismo archivo csv.
from ast import Str
from asyncore import write
import py_compile
from numpy import source
import pyttsx3
import speech_recognition
engine = pyttsx3.init()
recognizer = speech_recognition.Recognizer()
peticion=input('¿quiere ingresar sus  datos?.  (y/n)')
if 'y' in peticion:
    engine.say('Dime tu nombre')
    engine.runAndWait()
    with speech_recognition.Microphone() as source:
        audio=recognizer.listen(source)
        NOMBRE=recognizer.recognize_google(audio,language='es')
    engine.say('Dime tu edad')
    engine.runAndWait()
    with speech_recognition.Microphone() as source:
        audio=recognizer.listen(source)
        EDAD=recognizer.recognize_google(audio,language='es')
    engine.say('Dime tu profecion')
    engine.runAndWait()
    with speech_recognition.Microphone() as source:
        audio=recognizer.listen(source)
        PROF=recognizer.recognize_google(audio,language='es')
    Str(NOMBRE)
    Str(EDAD)
    Str(PROF)
    engine.say('OK.TU NOMBRE ES:')
    engine.say(NOMBRE)
    engine.say('TIENES')
    engine.say(EDAD)
    engine.say('AÑOS DE EDAD, Y ERES')
    engine.say(PROF)
    engine.say('ESO ES TODO, tus datos ya fueron ingresados, GRACIAS')
    engine.runAndWait()
import csv
import random
with open('Datos_personales.csv','a', newline = "") as file:
    writer=csv.writer(file, delimiter=";",)
    writer.writerow([NOMBRE,EDAD,PROF])