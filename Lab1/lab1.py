import machine
import sys
import time

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin1 = machine.Pin(14, machine.Pin.OUT)


# Function definitions
def blink(led_pin):
    led_pin.on()
    time.sleep_ms(1000)
    led_pin.off()
    time.sleep_ms(1000)


def heartbeat(led_pin):
    led_pin.on()
    time.sleep_ms(500)
    led_pin.off()
    time.sleep_ms(150)
    led_pin.on()
    time.sleep_ms(500)
    led_pin.off()
    time.sleep_ms(1000)


# Infinite Loop
while True:
    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    # blink(led_pin1)
    heartbeat(led_pin1)

