from setuptools import setup

NAME = "py-ublox"
VERSION = "0.1"
REQS = [
    "pyserial==3.*",
    "numpy==1.14.*",
    "scipy==1.1.*",
    "matplotlib==2.2.*",
    "bitstring==3.1.*",
    "pynmea2",
]

# pybayes with basic, untested Python3 conversion
LINKS = [
    "git+git://github.com/Python3pkg/PyBayes.git",
]

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQS,
    dependency_links=LINKS,
    description="python uBlox module",
    author_email="william@williamflynt.com",
    url="https://github.com/williamflynt/pyUblox",
    keywords=["uBlox", "ublox", "ubx", "py-ublox", "pyublox"],
    packages=['ublox'],
    include_package_data=True,
    long_description=""" """
)
