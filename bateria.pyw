import time
import psutil
from win10toast import ToastNotifier

toast = ToastNotifier()
toast.show_toast("andando", " ", None, 10)
while True:
    try:
        time.sleep(10)
        bateria = psutil.sensors_battery()
        if bateria.percent > 90 and bateria.power_plugged:
            toast.show_toast("desconecta la computadora", "la bateria es de " + str(bateria.percent), None, 10)
        
    except:
        pass