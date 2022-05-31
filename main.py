import time
from playsound import playsound
from datetime import datetime
alarmtime= "9:21"
while True:
    currenttime= datetime.now().strftime("9:21")
    if currenttime == alarmtime:
        print("Wake up!!")
        playsound("alarm.wav")
        break
    else:
        print("not yet")
        time.sleep(10)
