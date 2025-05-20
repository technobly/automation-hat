#!/usr/bin/env python3

import time

import automationhat

print("""
Press CTRL+C to exit.
""")

if automationhat.is_automation_hat():
    automationhat.light.power.write(1)

while True:
    automationhat.relay.one.toggle()
    time.sleep(0.1)
    if automationhat.is_automation_hat():
        automationhat.relay.two.toggle()
        time.sleep(0.1)
        automationhat.relay.three.toggle()
    time.sleep(0.1)
