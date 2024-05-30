# MicroPython-in-PyCharm
## Install PyCharm
## Install MicroPython Plugin for PyCharm
After installing PyCharm and opening it, go to `PyCharm>Settings>Plugins>Marketplace` and search for MicroPython and install it. If PyCharm requires you to relaunch the program then do so.

![Figure 4](/Images/figure04.png)

## Create a New Project
After installing the MircoPython plugin, we are ready to start our MicroPython Project! Go to `Project>New Project` and name your project whatever you feel like. Ensure you are using the latest version of Python and then click `Create`.

![Figure 5](/Images/figure05.png)

As of right now, our project is a Python project. Our next goal is to change it to a MircoPython project so that we can run it on our ESP32. In your new project, go to `PyCharm>Settings>Languages & Frameworks>MicroPython`. Check `Enable MicroPython support`. Select `ESP8266` from the drop-down for device type. Click the `Detect` button next to your `Device path` which should pull up the path we found previously with one key difference: the `tty` part of the path should be replaced by 'cu'. 

However, this `Detect` button doesn't always work. If this is not working for you, copy the path found previously, paste it into the `Device path`, and change the `tty` extension to `cu`. In the end, it should look something like this:

![Figure 6](/Images/figure06.png)

Hit `OK` and close settings.

### What is the Difference between TTY and CU?
- A TTY device is used to call into a device/system, and the CU device (call-up) is used to call out of a device/system. 

## Upload a Program
Now that the MicroPython project has been set up properly, create a program by right-clicking the project folder and going to `New>Python File` and naming it `main.py`. This specific file will automatically run every time the ESP starts.

![Figure 7](/Images/figure07.png)

After opening `main.py` in your editor, PyCharm will require certain packages to be able to run MicroPython properly on your device. You can install them by clicking `Missing required MicroPython packages` in the upper-left corner of your screen.

 ![Figure 8](/Images/figure08.png)

Once the installation is complete, you can write your Python program in `main.py` and flash it to your ESP. Let’s put `print("Hello World!")` inside of this file and save. Then, to move the program to your ESP right-click on your `main.py` file, and go down to Run `Flash main.py`. 

 ![Figure 9](/Images/figure09.png)

You’ll see it output that it’s connected, uploading, and soft rebooting. You just put your program on your device!

 ![Figure 10](/Images/figure10.png)

### Error: Cannot Enter Into Raw Repel Mode

For most people, the first upload won't work. It will give you this error:

 ![Figure 11](/Images/figure11.png)

 This is because for you to upload to your ESP, the device needs to enter "raw repl" mode. Without a `main.py` on the device, this should happen by default. The way your computer checks if the ESP has entered "raw repl" mode is by checking the output of your ESP. Normally in "raw repl" mode, you should see 3 arrows (`>>>`) to indicate that it is looking for input. However, most ESPs spit out some garbage values while they are rebooting so your computer first sees the garbage values instead of the 3 arrows and infers that the device isn't in "raw repl" mode. 

 To make sure this is your problem enter the following into your terminal (make sure to input the proper device path):

```
screen <device path> 115200
```

If this is your error you should see something similar to this (notice the garbage values before entering "raw repel" mode):

 ![Figure 12](/Images/figure12.png)

 To fix this we need to give your ESP time to bootup before checking if it is in "raw repl" mode. To accomplish this, inside your project folder go into `.venv>lib>python3.9>site-packages>ampy>pyboard.py` or click on the last link in your error message (it should say pyboard.py at the very end of the link). Scroll down to the following code:
 ```
 n = self.serial.inWaiting()
 while n > 0:
     self.serial.read(n)
     n = self.serial.inWaiting()
```
 After the while loop add this line of code:
```
time.sleep(2)
```
At the end, the whole section should look like this:
```
 n = self.serial.inWaiting()
 while n > 0:
     self.serial.read(n)
     n = self.serial.inWaiting()
 time.sleep(2)
```
Following this, when you flash your code you should no longer get this error message. If you still get this error you can increase the sleep time.

## Connect to your Device

Once these steps are complete you can see your "Hellow World!" message by entering the following code into your terminal (make sure to input the proper device path):
```
screen <device path> 115200
```
 ![Figure 14](/Images/figure14.png)

## Troubleshooting


[^1]: [https://medium.com/@andymule/micropython-on-esp32-e54998966e9](https://medium.com/@andymule/micropython-in-pycharms-basic-setup-9169b497ec8a)
