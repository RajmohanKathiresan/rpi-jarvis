#!/usr/bin/env python
 
import time
 
from grove.grove_servo import GroveServo
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton
 
def main():
    # Grove - Servo connected to PWM port
    servo = GroveServo(12)

    # Grove - LED Button connected to port D5
    button = GroveLedButton(18)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            print('single click')
            button.led.light(True)
            print(event)
            print(index)
            print(tm)
            servo.setAngle(180)

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
