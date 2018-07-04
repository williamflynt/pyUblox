# pyUblox

This Python module is a collection of various pieces of codes to read and communicate with uBlox devices.
It may or may not work. The code itself is a bit of a Frankenstein and there's no documentation. Good luck!


## Requirements

1. Python 3
2. uBlox device properly connected

In addition, see the requirements.txt file.

Of note, pybayes is a Python2 package ported automatically to Python3. It may not work.


## Installation

You can use pip to install this package by referencing this repo.
~~~
# Looks like: pip install git+<<myrepo.git>>
pip install git+https://github.com/williamflynt/pyUblox.git
~~~


## Test the device

On OSX/Linux you can test it like this:
```
$ source venv/bin/activate
# Note that you need to find the correct port/device where the uBlox device is connected
$ python ublox_capture.py --port=/dev/cu.usbmodem144141 --dot
```

If connected and able to read you should get a bunch of dots on your screen. You could also experiment with the '--show' to get more verbose output for debuging / testing purposes.

