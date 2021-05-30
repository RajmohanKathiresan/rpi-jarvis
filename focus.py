import time

from grove.display.jhd1802 import JHD1802
from seeed_dht import DHT
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
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
    time.sleep(2)
    display_in_lcd(lcd, 0, "Identify")
    display_in_lcd(lcd, 1, "Temp-Humi")
    time.sleep(2)
    # Grove - Light Sensor connected to port A0
    light_sensor = GroveLightSensor(0)

    # Range Sensor - D24
    ultrasonic_range_senor = GroveUltrasonicRanger(24)

    # Motion Sensor - D18
    motion_sensor = GroveMiniPIRMotionSensor(18)

    # Grove - Temperature&Humidity Sensor connected to port D5
    climate_sensor = DHT('11', 5)

    # Grove - LED Button connected to port D16
    button = GroveLedButton(16)

    def on_detect():
        print('motion detected')
        
    motion_sensor.on_detect = on_detect

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            print('single click')
            button.led.light(True)

        elif event & Button.EV_LONG_PRESS:
            print('long press')
            button.led.light(False)
    button.on_event = on_event
    
    while True:
        distance = ultrasonic_range_senor.get_distance()
        print('{} cm'.format(distance))
        light_sensor_output = light_sensor.light
        humi, temp = climate_sensor.read()
        row_one = f"L:{light_sensor_output}"
        row_two = f"H:{humi}-T:{temp}"
        display_in_lcd(lcd, 0, row_one)
        display_in_lcd(lcd, 1, row_two)
        time.sleep(2)


if __name__ == '__main__':
    main()
