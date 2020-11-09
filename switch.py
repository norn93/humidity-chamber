from gpiozero import LED
from time import sleep

PRESS_DEPRESS_TIME = 1.0
ON_TIME = 0.0

on_button = LED(14, active_high = False)
set_button = LED(15, active_high = False)
off_button = LED(18, active_high = False)

def press(button):
    button.on()
    sleep(PRESS_DEPRESS_TIME)
    button.off()
    sleep(PRESS_DEPRESS_TIME)

def tap_on():
    press(on_button)
    press(set_button)
    press(set_button)

def tap_off():
    press(off_button)

def tap_on_off():
    tap_on()
    tap_off()

def relay_on_off():
    press(on_button)
