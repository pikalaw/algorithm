
def InsertSort(items, key=lambda x: x):
  for p in xrange(0, len(items)):
    for q in xrange(p, 0, -1):
      if items[q-1] > items[q]:
        Swap(items, q-1, q)


def Swap(items, i, j):
  temp = items[i]
  items[i] = items[j]
  items[j] = temp


import unittest
import random
import copy


class TestInsertSort(unittest.TestCase):

  def test_Random(self):
    original = [random.randint(1, 100) for _ in xrange(10)] 
    actual = copy.deepcopy(original)
    InsertSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Increasing(self):
    original = [x for x in xrange(100)] 
    actual = copy.deepcopy(original)
    InsertSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Decreasing(self):
    original = [x for x in xrange(100)]
    original.reverse()
    actual = copy.deepcopy(original)
    InsertSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Constant(self):
    original = [1 for _ in xrange(10)] 
    actual = copy.deepcopy(original)
    InsertSort(actual)
    self.assertEqual(sorted(original), actual)
