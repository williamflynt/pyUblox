from unittest import TestCase
from unittest.mock import patch

"""
Test code to mock out the need for the UBlox class to actually be connected ¨
the the EVK 8N device.
"""


class UBloxTest(TestCase):
    
    @patch('ublox.UBlox')
    def test_ublox(self, UBloxMock):
        dev = UBloxMock()
        dev.name.return_value = "MockDevice"

        self.assertIsNotNone(dev.name())