# MicroPython-on-ESP32 Setup
![ESP32 Pinout](/Images/esp32-pinout.jpg)

## Install Python 3
## Make sure your board can be seen on your USB
When you plug your ESP into your computer via USB, it needs to recognize the serial connection interface. In this step, we will find where your ESP is located on your specific computer. Depending on what operating system you are using (i.e. Windows, MacOS, or Linux) this process will look differently.

On MacOS, go into System Settings > General > About and scroll down to the bottom of that page and click on the “System Report…” button. From there go to the “USB” heading under “Hardware”. Here you should see your ESP connected to one of your USB connections. Take note of the “Serial Number” listed in the information provided. In my photo below, it’s “0001”. We will use this number to identify where our ESP is located in memory in the next step.

![Figure 1](/Images/figure1.png)

## Find the location of your ESP in memory

On MacOS, go into Terminal and type ls /dev/tty.*. This will list all the USB connections on your device. Look for the USB connection with the specific serial port we noted last step. This is the location of your ESP in memory. Copy down this location as we will be needing it later

![Figure 2](/Images/figure2.png)

## Flash your ESP32 with MicroPython

You can kind of think of micropython as the operating system on your ESP, so you have to install it before you can run any programs, etc… Head on over to https://micropython.org/download/esp32 and grab the latest release.

![Figure 3](/Images/figure3.png)

Now that we have the installation on our local computer, we need to flash it to our ESP. To do this let’s navigate into the downloads folder inside the terminal. Open Terminal and type all the next lines into our command prompt:

`cd Downloads/`

Use pip to download the Python tool that will flash our esp.

`pip install esptool`

From here we need to take off the existing firmware on the ESP with the following command (The ESP location is the same location that we found in the previous step):

`esptool.py --chip esp32 --port [ESP location] erase_flash`

For me, this command looked like this: 

`esptool.py --chip esp32 --port /dev/tty.usbserial-0001 erase_flash `

Following this we can flash our installation of micropython by entering this into the command line: 

`esptool.py --chip esp32 --port [ESP Location]--baud 460800 write_flash -z 0x1000 [Installation Name]`

For me this command looked like this:

`esptool.py --chip esp32 --port /dev/tty.usbserial-0001 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-20240222-v1.22.2.bin`

## Debugging

THIS WORKS!!!! -> `screen /dev/cu.usbserial-0001 115200` (The baud rate is important! Idk why this specific one works but it does!
```
import uos
print(uos.listdir())
```
`sudo ampy --port /dev/cu.usbserial-0001 run test.py`


[^1]: https://medium.com/@andymule/micropython-on-esp32-e54998966e9
[^2]: https://learn.sparkfun.com/tutorials/micropython-programming-tutorial-getting-started-with-the-esp32-thing/repl-hello-world
[^3]: https://github.com/scientifichackers/ampy/issues/19?source=post_page-----fcef1370a2dd--------------------------------?source=post_page-----fcef1370a2dd--------------------------------#issuecomment-317126363
