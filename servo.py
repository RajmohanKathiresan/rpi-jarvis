#!/usr/bin/env python
 
import time

from grove.display.jhd1802 import JHD1802
from seeed_dht import DHT
 
from grove.grove_servo import GroveServo
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton
 
def display_in_lcd(lcd, row, message):
    if len(message) > 16:
        display_message = message[0:15]
    else:
        display_message = message
    lcd.setCursor(row, 0)
    print(display_message)
    lcd.write(display_message)


def main():
    
    value = "Jarvis Focus"

    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    display_in_lcd(lcd, 0, value)

    # Grove - Servo connected to PWM port
    servo = GroveServo(12)

    # Grove - LED Button connected to port D5
    button = GroveLedButton(18)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            print('single click')
            button.led.light(True)
            servo.setAngle(180)
            display_in_lcd(lcd,0,"ON : 180")
            display_in_lcd(lcd, 1, "")
        elif event & Button.EV_EV_LONG_PRESS:
            print('long press')
            button.led.light(False)
            servo.setAngle(0)
            display_in_lcd(lcd,0,"OFF : 0")
            display_in_lcd(lcd, 1, "")

    button.on_event = on_event

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
