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

    value = "Jarvis Sense"

    # Grove - 16x2 LCD(White on Blue) connected to I2C port
    lcd = JHD1802()

    display_in_lcd(lcd, 0, value)
    time.sleep(2)
    display_in_lcd(lcd, 0, "Light-Moisture")
    display_in_lcd(lcd, 1, "Temp-Humidity")
    time.sleep(2)
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

        row_one = f"L:{light_sensor_output} - M:{moisture} "
        row_two = f"H:{humi} - T:{temp}C "
        display_in_lcd(lcd, 0, row_one)
        display_in_lcd(lcd, 1, row_two)
        time.sleep(2)

if __name__ == '__main__':
    main()
