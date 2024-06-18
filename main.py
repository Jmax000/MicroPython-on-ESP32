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
