#!/usr/bin/env python3

import time

import automationhat

print("""
Press CTRL+C to exit.
""")

print("  ANALOG_1      ANALOG_2      ANALOG_3        ANALOG_4")

while True:
    if automationhat.is_automation_hat():
        automationhat.light.power.toggle()
        time.sleep(0.1)
        automationhat.light.comms.toggle()
        time.sleep(0.1)
        automationhat.light.warn.toggle()

    automationhat.relay.one.toggle()
    time.sleep(0.05)

    if automationhat.is_automation_hat():
        automationhat.relay.two.toggle()
        time.sleep(0.05)
        automationhat.relay.three.toggle()

    automationhat.input.three.light.toggle()
    time.sleep(0.05)
    automationhat.input.two.light.toggle()
    time.sleep(0.05)
    automationhat.input.one.light.toggle()
    time.sleep(0.05)

    automationhat.output.three.toggle()
    time.sleep(0.05)
    automationhat.output.two.toggle()
    time.sleep(0.05)
    automationhat.output.one.toggle()

    print(automationhat.analog.read())
