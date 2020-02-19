import unittest
from src.stock_prices.stock_prices import *


class Test(unittest.TestCase):

  def test_find_max_profit(self):
    self.assertEqual(find_max_profit([10, 7, 5, 8, 11, 9]), 6)
  def test_find_max_profit1(self):
    self.assertEqual(find_max_profit([100, 90, 80, 50, 20, 10]), -10)
  def test_find_max_profit2(self):
    self.assertEqual(find_max_profit([1050, 270, 1540, 3800, 2]), 3530)
  def test_find_max_profit3(self):
    self.assertEqual(find_max_profit([100, 55, 4, 98, 10, 18, 90, 95, 43, 11, 47, 67, 89, 42, 49, 79]), 94)
  

if __name__ == '__main__':
  unittest.main()
