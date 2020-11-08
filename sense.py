import time

from grove.display.jhd1802 import JHD1802
from grove.grove_temperature_humidity_sensor import DHT
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_moisture_sensor import GroveMoistureSensor


def display_in_lcd(lcd, message):
    if len(message) > 32:
        display_message = message[0:31]
    else:
        display_message = message
    lcd.setCursor(0, 0)
    print(display_message)
    # lcd.write(display_message)


def main():

    value = "Jarivs - Initializing"

    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    display_in_lcd(lcd, value)

    # Grove - Light Sensor connected to port A0
    light_sensor = GroveLightSensor(0)

    # Grove - Moisture Sensor connected to port A2
    moisture_sensor = GroveMoistureSensor(2)

    # Grove - Temperature&Humidity Sensor connected to port D5
    climate_sensor = DHT('11', 5)

    while True:
        light_sensor_output = light_sensor.light
        humi, temp = climate_sensor.read()
        moisture = moisture_sensor.moisture

        value = f"{light_sensor_output}-{humi}-{temp}-{moisture}"

        display_in_lcd(lcd, value)
        time.sleep(20)


if __name__ == '__main__':
    main()