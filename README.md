# pifire_remote
Scripts and apps for monitoring pifire remotely

## Objective
This project hopes to provide a front end for pifire to monitor the smoker remotely.

The primary use of the application will be through microPython running on an ESP32 device with a small TFT screen and 3 buttons. The device will mimic the TFT and 3 buttons that are on the front of the pifire.

There will be a second directory containing python scripts. These scripts will be used for testing parts of the app as needed.

## Microcontroller setup
This project relies on a few libraries in order to work. I'm using the following hardware.

https://a.co/d/6dmW2Gp

After installing the latest version of the microPython firmware, I'm using the following commands to setup the libraries.

* import network
* sta_if = network.WLAN(network.STA_IF)
* sta_if.active(True)
* sta_if.connect('\<your SSID\>', '\<your key\>')
* sta_if.isconnected()
* sta_if.ifconfig()
* import mip
* mip.install('requests')
* mip.install("github:peterhinch/micropython-nano-gui")
* mip.install("github:peterhinch/micropython-nano-gui/drivers/ili93xx")

Then you need to pull down micropython-nano-gui to your system and create a color_setup.py. Use the directions on their README for help with that.

You can use ampy to upload the color_setup.py

* ampy --port PORT put color_setup.py