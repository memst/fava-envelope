"""
This type stub file was generated by pyright.
"""

import unittest

"""
Tests for distribution.
"""
__copyright__ = ...
__license__ = ...
class TestDistributionBase(unittest.TestCase):
    def assertDist(self, dist, mode, min, max): # -> None:
        ...
    


class TestDistribution(TestDistributionBase):
    def test_distribution(self): # -> None:
        ...
    


class TestDistributionUpdateFrom(TestDistributionBase):
    def test_update_from(self): # -> None:
        ...
    


if __name__ == '__main__':
    ...