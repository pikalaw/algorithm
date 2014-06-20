
def popular_value(n):
  min_len = len(n) / 4 + 1
  for i in [min_len - 1, len(n) / 2, len(n) - min_len]:
    if upper_index(i, n) - lower_index(i, n) + 1 >= min_len:
      return n[i]
  return None


def upper_index(at, n):
  v = n[at]
  i, j = at, len(n)
  while i < j:
    k = (i + j) / 2
    if n[k] == v:
      i = k + 1
    else:
      j = k
  return i - 1


def lower_index(at, n):
  v = n[at]
  i, j = 0, at
  while i < j:
    k = (i + j) / 2
    if n[k] == v:
      j = k
    else:
      i = k + 1
  return i


import unittest


class TestPopular(unittest.TestCase):

  def test_4(self):
    self.assertEqual(1, popular_value([1, 1, 2, 3]))
    self.assertEqual(2, popular_value([1, 2, 2, 3]))
    self.assertEqual(3, popular_value([1, 2, 3, 3]))
    self.assertEqual(None, popular_value([1, 2, 3, 4]))

    self.assertEqual(1, popular_value([1, 1, 1, 2]))
    self.assertEqual(2, popular_value([1, 2, 2, 2]))
    self.assertEqual(3, popular_value([1, 3, 3, 3]))

    self.assertEqual(1, popular_value([1, 1, 1, 1]))

  def test_5(self):
    self.assertEqual(1, popular_value([1, 1, 2, 3, 4]))
    self.assertEqual(2, popular_value([1, 2, 2, 3, 4]))
    self.assertEqual(3, popular_value([1, 2, 3, 3, 4]))
    self.assertEqual(4, popular_value([1, 2, 3, 4, 4]))
    self.assertEqual(None, popular_value([1, 2, 3, 4, 5]))

    self.assertEqual(1, popular_value([1, 1, 1, 2, 3]))
    self.assertEqual(2, popular_value([1, 2, 2, 2, 3]))
    self.assertEqual(3, popular_value([1, 2, 3, 3, 3]))

    self.assertEqual(1, popular_value([1, 1, 1, 1, 2]))
    self.assertEqual(2, popular_value([1, 2, 2, 2, 2]))

    self.assertEqual(1, popular_value([1, 1, 1, 1, 1]))
