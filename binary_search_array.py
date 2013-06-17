
def BinarySearch(values, key):
  left, right = 0, len(values)
  while left < right:
    mid = (left + right) / 2
    if key < values[mid]:
      right = mid
    elif key > values[mid]:
      left = mid + 1
    else:
      return (mid, True)
  else:
    if left == 0:
      return (0, False)
    if left == len(values):
      return (len(values) - 1, False)
    else:
      if abs(values[left-1] - key) < abs(values[left] - key): 
        return (left - 1, False)
      else:
        return (left, False)


import unittest


class TestBinarySearch(unittest.TestCase):

  def test_Example(self):
    values = [10, 50, 90]

    self.assertEqual((0, True), BinarySearch(values, 10))
    self.assertEqual((1, True), BinarySearch(values, 50))
    self.assertEqual((2, True), BinarySearch(values, 90))

    self.assertEqual((0, False), BinarySearch(values, 9))
    self.assertEqual((0, False), BinarySearch(values, 11))
    self.assertEqual((1, False), BinarySearch(values, 49))
    self.assertEqual((1, False), BinarySearch(values, 51))
    self.assertEqual((2, False), BinarySearch(values, 89))
    self.assertEqual((2, False), BinarySearch(values, 91))
