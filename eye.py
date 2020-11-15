from picamera import PiCamera
import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton


def main():
    # Grove - LED Button connected to port D5
    button = GroveLedButton(5)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            camera = PiCamera()
            camera.start_preview()
            sleep(2)
            camera.capture('/tmp/picture1.jpg')
            camera.stop_preview()
    button.on_event = on_event

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()


