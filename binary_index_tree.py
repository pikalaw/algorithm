
class BIT(object):

  def __init__(self, xs):
    self.levels = [xs]
    l = (len(xs) + 1) / 2
    while l > 0:
      self.levels.append([0] * l)
      l = (l+1) / 2 if l > 1 else 0

    for i, x in enumerate(xs):
      self.Update(i, x)

  def Update(self, i, x):
    self.levels[0][i] = x
    i /= 2
    for l in xrange(1, len(self.levels)):
      self.levels[l][i] += x
      i /= 2

  def CummulativeSum(self, i):
    l = 0
    total = self.levels[l][i]
    while l < len(self.levels):
      j = i / 2
      if j * 2 < i:
        total += self.levels[l][i-1] 
      l += 1
      i = j
    return total

  def RangeSum(self, i, j):
    return self.CummulativeSum(j) - (
        self.CummulativeSum(i - 1) if i > 0 else 0)


import unittest


class TestBIT(unittest.TestCase):

  def test_Cummulative(self):
    bit = BIT([1, 10, 100, 1000, 10000, 100000])
    self.assertEqual(1, bit.CummulativeSum(0))
    self.assertEqual(11, bit.CummulativeSum(1))
    self.assertEqual(111, bit.CummulativeSum(2))
    self.assertEqual(1111, bit.CummulativeSum(3))
    self.assertEqual(11111, bit.CummulativeSum(4))
    self.assertEqual(111111, bit.CummulativeSum(5))

  def test_Range(self):
    bit = BIT([1, 10, 100, 1000, 10000, 100000])
    self.assertEqual(1, bit.RangeSum(0, 0))
    self.assertEqual(10, bit.RangeSum(1, 1))
    self.assertEqual(100000, bit.RangeSum(5, 5))
    self.assertEqual(110, bit.RangeSum(1, 2))

    self.assertEqual(111111, bit.RangeSum(0, 5))
