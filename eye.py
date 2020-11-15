from picamera import PiCamera
import time

from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton


def main():
    print("Initializing")
    now = int(time.time())
    # Grove - LED Button connected to port D5
    button = GroveLedButton(16)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            now = int(time.time())
            print(f"Button Clicked {now}")
            camera = PiCamera()
            camera.start_preview()
            time.sleep(2)
            camera.capture(f'/tmp/{now}.jpg')
            camera.stop_preview()
    button.on_event = on_event

    print("Registering event for button")

    while True:
        now = int(time.time())
        time.sleep(1)
        print(f"Time @  {now}")


if __name__ == '__main__':
    main()
