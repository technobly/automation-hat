#!/usr/bin/env python3

import time

import automationhat

print("""
Press CTRL+C to exit.
""")

while True:
    one = automationhat.analog.one.read()
    two = automationhat.analog.two.read()
    three = automationhat.analog.three.read()
    four = automationhat.analog.four.read()
    print("ANALOG_1:", one, "| ANALOG_2:", two, "| ANALOG_3:", three, "| ANALOG_4:", four)
    time.sleep(0.5)
