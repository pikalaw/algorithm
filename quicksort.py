
def QuickSort(items, key=lambda x: x):
  InternalQuickSort(items, 0, len(items), key)


def InternalQuickSort(items, i, j, key):
  # Base case.
  if j - i <= 1:
    return

  # Recursion case.
  pivot = FindPivot(items, i, j, key)
  k = Partition(items, i, j, key, pivot)
  InternalQuickSort(items, i, k, key) 
  InternalQuickSort(items, k + 1, j, key) 


def Partition(items, i, j, key, pivot):
  x = items[pivot]
  Swap(items, j - 1, pivot)
  p = q = i
  while q < j - 1:
    if key(items[q]) < x:
      Swap(items, p, q)
      p += 1
    q += 1
  Swap(items, p, j - 1)
  return p


def FindPivot(items, i, j, key):
  """Median of 3."""
  x1 = random.randint(i, j - 1)
  x2 = CyclicNext(x1, i, j)
  x3 = CyclicNext(x2, i, j)
  y1 = key(items[x1]) 
  y2 = key(items[x2]) 
  y3 = key(items[x3]) 
  if y1 <= y2:
    if y2 < y3:
      return x2
    else:
      return x3
  else:
    if y1 < y3:
      return x1
    else:
      return x3


def CyclicNext(x, i, j):
  y = x + 1
  if y >= j:
    y = i
  return y


def Swap(items, i, j):
  temp = items[i]
  items[i] = items[j]
  items[j] = temp


import unittest
import random
import copy


class TestQuickSort(unittest.TestCase):

  def test_Random(self):
    original = [random.randint(1, 100) for _ in xrange(10)] 
    actual = copy.deepcopy(original)
    QuickSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Increasing(self):
    original = [x for x in xrange(100)] 
    actual = copy.deepcopy(original)
    QuickSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Decreasing(self):
    original = [x for x in xrange(100)]
    original.reverse()
    actual = copy.deepcopy(original)
    QuickSort(actual)
    self.assertEqual(sorted(original), actual)

  def test_Constant(self):
    original = [1 for _ in xrange(10)] 
    actual = copy.deepcopy(original)
    QuickSort(actual)
    self.assertEqual(sorted(original), actual)
