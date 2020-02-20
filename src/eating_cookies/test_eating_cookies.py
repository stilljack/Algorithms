import unittest
from src.eating_cookies.eating_cookies import *
class Test(unittest.TestCase):

  def test_eating_cookies_small_n(self):
    self.assertEqual(eating_cookies(0), 1)
    self.assertEqual(eating_cookies(1), 1)
    self.assertEqual(eating_cookies(2), 2)
  def test_eating_cookies_small_5(self):
    self.assertEqual(eating_cookies(5), 13)
  def test_eating_cookies_small_10(self):
      self.assertEqual(eating_cookies(10), 274)

  def test_eating_cookies_large_50(self):
    print(eating_cookies(50))
    self.assertEqual(eating_cookies(50), 10562230626642)
  def test_eating_cookies_large_100(self):
    print(eating_cookies(100))
    self.assertEqual(eating_cookies(100), 180396380815100901214157639)
  def test_eating_cookies_large_500(self):
    print(eating_cookies(500))
    self.assertEqual(eating_cookies(500), 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527)


if __name__ == '__main__':
  unittest.main()
