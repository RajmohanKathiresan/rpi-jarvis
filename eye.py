from picamera import PiCamera
import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton


def capture():
    now = int(time.time())
    camera = PiCamera()
    camera.capture(f'/home/pi/Pictures/{now}.jpg')

def main():
    print("Initializing")
    now = int(time.time())
    # Grove - LED Button connected to port D5
    button = GroveLedButton(16)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            print(f"Button Clicked")
            capture()

    button.on_event = on_event

    print("Registering event for button")

    while True:
        now = int(time.time())
        time.sleep(1)

if __name__ == '__main__':
    main()
