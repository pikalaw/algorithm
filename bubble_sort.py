
def BubbleSort(values):
  while True:
    swapped = False
    for j in xrange(1, len(values)):
      if values[j - 1] > values[j]:
        temp = values[j - 1]
        values[j - 1] = values[j]
        values[j] = temp
        swapped = True
    if not swapped:
      return


def OptimizedBubbleSort(values):
  for i in xrange(len(values), 0, -1):
    swapped = False
    for j in xrange(1, i):
      if values[j - 1] > values[j]:
        temp = values[j - 1]
        values[j - 1] = values[j]
        values[j] = temp
        swapped = True
    if not swapped:
      return


import unittest
import random
import copy


class TestBubbleSort(unittest.TestCase):

  def RunTest(self, bubble, range, size):
    values = [random.randint(1, range) for _ in xrange(size)]
    original_values = copy.deepcopy(values)
    bubble(values)
    self.assertEqual(sorted(original_values), values,
                     msg='original={} sorted={}'.format(original_values,
                                                        values))

  def test_BubbleSort(self):
    self.RunTest(BubbleSort, 5, 100)
    self.RunTest(BubbleSort, 1000, 10)

  def test_OptimizedBubbleSort(self):
    self.RunTest(OptimizedBubbleSort, 5, 100)
    self.RunTest(OptimizedBubbleSort, 1000, 10)
