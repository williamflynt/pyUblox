from setuptools import setup, find_packages

NAME = "py-ublox"
VERSION = "0.1"
REQS = [
    "pyserial==3.*",
    "numpy==1.14.*",
    "scipy==1.1.*",
    "matplotlib==2.2.*",
    "bitstring==3.1.*",
    # pybayes with basic, untested Python3 conversion
    "git+git://github.com/Python3pkg/PyBayes.git",
]

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQS,
    description="python uBlox module",
    author_email="william@williamflynt.com",
    url="https://github.com/williamflynt/pyUblox",
    keywords=["uBlox", "ublox", "ubx", "py-ublox", "pyublox"],
    packages=['ublox'],
    include_package_data=True,
    long_description=""" """
)
