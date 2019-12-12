import switch
import data
import time, datetime
import os, sys

DELAY_TIME = 60

HOME_DIR = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
LOG_FILE = HOME_DIR + "log.log"
SETPOINT_FILE = HOME_DIR + "setpoint.txt"

with open(SETPOINT_FILE, "r") as f:
    REQUIRED_HUMIDITY = int(f.read())

def loop():
    today = str(datetime.datetime.now())
    t, h = data.get_temperature_humidity()
    temperature = str(round(t, 2))
    humidity = str(round(h, 2))
    print(temperature, humidity)
    with open(LOG_FILE, "a+") as f:
        f.write(today + ", " + temperature + ", " + humidity + "\n")
    if h < REQUIRED_HUMIDITY:
        print("boosting!")
        switch.tap_on_off()

while True:
    loop()
    time.sleep(DELAY_TIME)
