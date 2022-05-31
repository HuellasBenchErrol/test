import time
from playsound import playsound
from datetime import datetime
alarmtime= "11:39"
while True:
    currenttime= datetime.now().strftime('11:39')
    if currenttime == alarmtime:
        print("Wake up!!")
        playsound("alarm.wav")
        break
    else:
        print("not yet")
        time.sleep(10)
