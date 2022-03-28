import unittest
import logging

from lsst.sitcom.example_method import example_method

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.level=logging.DEBUG

class TestModel(unittest.TestCase):
    def test_example_method(self):
        multiplier=11
        value=10
        logger.debug(f'Multiplier is {multiplier}, value is {value}')
        self.assertTrue(example_method(value, multiplier=multiplier))
