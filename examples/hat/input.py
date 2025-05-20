#!/usr/bin/env python3

import time

import automationhat

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

    print("INPUT_1,2,3 are always high on Tachyon due to pull up resistors on the 40-pin gpio level shifters")
    print("You can still control the INPUT_1,2,3 LEDs manually though to have more indicators:")
    print("automationhat.input.one.light.on() / .off() / .toggle() / .write(0|1)")
    inputs = automationhat.input.read()
    print(inputs)

    print("""
    Press CTRL+C to exit.
    """)

    print("  ANALOG_1      ANALOG_2      ANALOG_3        ANALOG_4")
while True:
    analogs = automationhat.analog.read()
    print(analogs)

    time.sleep(0.5)
