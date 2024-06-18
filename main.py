import machine
import sys

repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin = machine.Pin(14, machine.Pin.OUT)

# Infinite Loop
while True:
    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

