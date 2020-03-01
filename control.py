import switch
import data
import time, datetime
from datetime import date, timedelta
import os, sys
from sendEmail import sendEmail

DELAY_TIME = 60

HOME_DIR = os.path.abspath(os.path.dirname(sys.argv[0])) + "/"
LOG_FILE = HOME_DIR + "log.log"
SETPOINT_FILE = HOME_DIR + "setpoint.txt"
WARNING_HUMIDITY = 50
WARNING_TEMPERATURE = 30

flag_over_temperature = False
flag_under_humidity = False

with open(SETPOINT_FILE, "r") as f:
    REQUIRED_HUMIDITY = int(f.read())

def loop():
    global flag_over_temperature, flag_under_humidity
    today = str(datetime.datetime.now())
    t, h = data.get_temperature_humidity()
    temperature = str(round(t, 2))
    humidity = str(round(h, 2))
    print(temperature, humidity)
    with open(LOG_FILE, "a+") as f:
        f.write(today + ", " + temperature + ", " + humidity + "\n")
    if h < REQUIRED_HUMIDITY:
        switch.tap_on_off()
    if h < WARNING_HUMIDITY and flag_under_humidity == False:
        flag_under_humidity = True
        sendEmail.send(["george.knowlden@gmail.com"], "WARNING: Mushrooms", "Humidity is too low...")
    if t > WARNING_TEMPERATURE and flag_over_temperature == False:
        flag_over_temperature = True
        sendEmail.send(["george.knowlden@gmail.com"], "WARNING: Mushrooms", "Temperature is too high...")
    minute = datetime.datetime.now().minute
    if minute == 0: # Reset the flags
        flag_under_humidity = False
        flag_over_temperature = False

while True:
    loop()
    time.sleep(DELAY_TIME)
