import wikipedia as wiki
import speech_recognition as sr
import pyttsx3 as pyt
recognizer=sr.Recognizer()
engine = pyt.init()
def Hablar(enunciado):
    engine.say(enunciado)
    engine.runAndWait()
def escuchar():
    try:
        with sr.Microphone() as source:
            print("...")
            audio= recognizer.listen(source)
            Mivoz= recognizer.recognize_google(audio, language='es')
            Mivoz= Mivoz.lower(0)
    except:
        pass
    return Mivoz
def atender():
    Hablar("¿Qué deseas saber?")
    print("Qué deseas saber?")
    Mivoz = escuchar()
    pregunta = Mivoz
    wiki.set_lang("es")
    respuesta = wiki.summary(pregunta, sentences = 2)
    print(respuesta)
    Hablar(respuesta)
atender()