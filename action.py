#!/usr/bin/env python

import time

from grove.grove_relay import GroveRelay

def main():

    # Grove - Relay connected to port D16
    relay = GroveRelay(16)
    number = 5
    while number < 5:
        relay.on()
        print('relay on')
        time.sleep(10)

        relay.off()
        print('relay off')
        time.sleep(5)
        number = number + 1

if __name__ == '__main__':
    main()
