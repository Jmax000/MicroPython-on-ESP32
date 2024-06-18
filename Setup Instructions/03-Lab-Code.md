# Lab 1

```
import machine
import sys
import time

# Pin definitions
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
led_pin = machine.Pin(14, machine.Pin.OUT)


# Function definitions
def blink():
    led_pin.on()
    time.sleep_ms(1000)
    led_pin.off()
    time.sleep_ms(1000)


def heartbeat():
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

    # blink()
    heartbeat()
```

# Lab 2
## Pre-Lab

```
from machine import Pin
import sys

# Pin definitions
repl_button = Pin(0, Pin.IN, Pin.PULL_UP)
led_1 = Pin(14, Pin.OUT)
led_2 = Pin(27, Pin.OUT)
led_3 = Pin(26, Pin.OUT)
led_4 = Pin(25, Pin.OUT)
led_5 = Pin(32, Pin.OUT)

button_1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
button_2 = Pin(16, Pin.IN, Pin.PULL_DOWN)
button_3 = Pin(17, Pin.IN, Pin.PULL_DOWN)
button_4 = Pin(5, Pin.IN, Pin.PULL_DOWN)
button_5 = Pin(18, Pin.IN, Pin.PULL_DOWN)

# Infinite Loop
while True:
    # If button 0 is pressed, drop to REPL
    if repl_button.value() == 0:
        print("Dropping to REPL")
        sys.exit()

    if button_1.value() == 1:
        led_1.on()
    else:
        led_1.off()

    if button_2.value() == 1:
        led_2.on()
    else:
        led_2.off()

    if button_3.value() == 1:
        led_3.on()
    else:
        led_3.off()

    if button_4.value() == 1:
        led_4.on()
    else:
        led_4.off()

    if button_5.value() == 1:
        led_5.on()
    else:
        led_5.off()
```
