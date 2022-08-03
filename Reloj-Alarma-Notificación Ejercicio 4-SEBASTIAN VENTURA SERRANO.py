from datetime import datetime, timedelta
import pyttsx3
import os
dt = datetime.now() 
print("Hora actual")
print("{}:{}".format(dt.hour, dt.minute))
from win10toast import ToastNotifier
print("Estableza una hora y minuto")
Hora= int(input("Hora: "))
Minuto= int(input("Minuto: "))
         
def notificacion():
 os.chdir(os.path.dirname(os.path.realpath(__file__)))
 toast=ToastNotifier() 
 titulo="Recordatorio - Alarma" 
 mensaje="En 5 minutos sera la hora programada"
 time=10
 icon=None
    
 toast.show_toast(titulo, mensaje, icon_path=icon, duration=time, threaded=True)
 print ("Se esta mostrando una notificación en Windows")
while True:
 import datetime
 tiempo=datetime.datetime.now()
 tiempo_5_minutos_antes= tiempo+timedelta(minutes=5)
 if Hora==datetime.datetime.now().hour and Minuto==tiempo_5_minutos_antes.minute:
     notificacion()
     break
        