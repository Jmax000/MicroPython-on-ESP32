# MicroPython-in-PyCharms
## Install PyCharm
## Install MicroPython Plugin for PyCharm
After installing PyCharm and opening it, go to `PyCharm>Settings>Plugins>Marketplace` and search for MicroPython and install it. If PyCharm requires you to relaunch the program then do so.

![Figure 4](/Images/figure4.png)

## Create a New Project
After installing the MircoPython plugin, we are ready to start our MicroPython Project! Go to `Project>New Project` and name your project whatever you feel like. Ensure you are using the latest version of Python and then click `Create`.

![Figure 5](/Images/figure5.png)

As of right now, our project is a Python project. Our next goal is to change it to a MircoPython project so that we can run it on our ESP32. In your new project, go to `PyCharm>Settings>Languages & Frameworks>MicroPython`. Check `Enable MicroPython support`. Select `ESP8266` from the drop-down for device type. Click the `Detect` button next to your `Device path` which should pull up the path we found previously with one key difference: the `tty` part of the path should be replaced by 'cu'. 

However, this `Detect` button doesn't always work. If this is not working for you, copy the path found previously, paste it into the `Device path`, and change the `tty` extension to `cu`. In the end, it should look something like this:

![Figure 6](/Images/figure6.png)

Hit `OK` and close settings.

### What is the Difference between TTY and CU?
- A TTY device is used to call into a device/system, and the CU device (call-up) is used to call out of a device/system. 

## Upload a Program
Now that the MicroPython project has been set up properly, create a program by right-clicking the project folder and going to `New>Python File` and naming it `main.py`. This specific file will automatically run every time the ESP starts.

![Figure 7](/Images/figure7.png)

After opening `main.py` in your editor, PyCharm will require certain packages to be able to run MicroPython properly on your device. You can install them by clicking `Missing required MicroPython packages` in the upper-left corner of your screen.

 ![Figure 8](/Images/figure8.png)

Once the installation is complete, you can write your Python program in `main.py` and flash it to your ESP. Let’s put `print(“Hello World!”)` inside of this file and save. Then, to move the program to your ESP right-click on your `main.py` file, and go down to Run `Flash main.py`. 

 ![Figure 9](/Images/figure9.png)

You’ll see it output that it’s connected, uploading, and soft rebooting. You just put your program on your device!


## Troubleshooting


[^1]: [https://medium.com/@andymule/micropython-on-esp32-e54998966e9](https://medium.com/@andymule/micropython-in-pycharms-basic-setup-9169b497ec8a)
