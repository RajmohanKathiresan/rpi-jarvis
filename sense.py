import time

from grove.display.jhd1802 import JHD1802
from seeed_dht import DHT
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_moisture_sensor import GroveMoistureSensor


def display_in_lcd(lcd, row, message):
    if len(message) > 16:
        display_message = message[0:15]
    else:
        display_message = message
    lcd.setCursor(row, 0)
    print(display_message)
    lcd.write(display_message)


def main():

    value = "Jarivs - Initializing"

    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    display_in_lcd(lcd, 0, value)

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

        value = f"Light:{light_sensor_output} {humi}-{temp}-{moisture}"

        display_in_lcd(lcd, 1, value)
        time.sleep(20)


if __name__ == '__main__':
    main()
