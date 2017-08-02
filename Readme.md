# pyUblox

This Python module is a collection of various pieces of codes to read and communicate with uBlox devices


## Requirements

1. Python 3
2. uBlox device properly connected


## Test the device

On OSX/Linux you can test it like this:
```
$ source venv/bin/activate
# Note that you need to find the correct port/device where the uBlox device is connected
$ python ublox_capture.py --port=/dev/cu.usbmodem144141 --dot
```

If connected and able to read you should get a bunch of dots on your screen. You could also experiment with the '--show' to get more verbose output for debuging / testing purposes.

