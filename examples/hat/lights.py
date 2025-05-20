#!/usr/bin/env python3

import signal

import automationhat

print("Analog, Output, Input, Power, Comms, and Warn LEDs should be ON")

print("""
Press CTRL+C to exit.
""")

# Relay lights will not light up when this is False,
# but it helps us force on other lights without those inputs being active
automationhat.enable_auto_lights(False)

# automationhat.light.power.on()
# automationhat.light.comms.on()
# automationhat.light.warn.on()
# Turn on all 3 with
automationhat.light.on()

for analog in automationhat.analog:
    analog.light.on()

for output in automationhat.output:
    output.light.on()

for input in automationhat.input:
    input.light.on()

signal.pause()
