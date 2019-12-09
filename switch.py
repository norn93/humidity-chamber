from gpiozero import LED
from time import sleep

PRESS_TIME = 0.5

on = LED(14, active_high = False)
set = LED(15, active_high = False)
off = LED(18, active_high = False)

def press(button):
    button.on()
    sleep(PRESS_TIME)
    button.off()
    sleep(PRESS_TIME)

def tap_on():
    press(on)
    press(set)
    press(set)

def tap_off():
    press(off)

while True:
    tap_on()
    print("ON")
    sleep(1)
    tap_off()
    print("OFF")
    sleep(1)
