
class Interval(object):

  @classmethod
  def Discrete(cls, x):
    return Interval(x, x)

  def __init__(self, a, b):
    self.a = a
    self.b = b

  def __repr__(self):
    return '[{}, {}]'.format(self.a, self.b)

  def __le__(self, other):
    return not other.b < self.a


def FuzzySort(intervals):
  IntervalFuzzySort(intervals, 0, len(intervals))


def IntervalFuzzySort(intervals, p, q):
  if q - p <= 1:
    return  # Done.

  pivot = FindFuzzyPivot(intervals, p, q)
  r, s = PartitionFuzzy(intervals, p, q, pivot)
  IntervalFuzzySort(intervals, p, r)
  IntervalFuzzySort(intervals, s, q)


def FindFuzzyPivot(intervals, p, q):
  pivot = copy.deepcopy(intervals[p])
  for i in xrange(p + 1, q):
    if intervals[i].a <= pivot.b and intervals[i].b >= pivot.a:
      pivot.a = max(pivot.a, intervals[i].a)
      pivot.b = min(pivot.b, intervals[i].b)
  return pivot


def PartitionFuzzy(intervals, p, q, pivot):
  r = p
  s = q
  i = p
  while i < s:
    if intervals[i].b < pivot.a:
      Swap(intervals, i, r)
      r += 1
      i += 1
    elif intervals[i].a > pivot.b:
      Swap(intervals, i, s - 1)
      s -= 1
    else:
      i += 1
  return r, s


def Swap(items, i, j):
  temp = items[i]
  items[i] = items[j]
  items[j] = temp


import unittest
import random
import copy


class TestFuzzySort(unittest.TestCase):

  def assertSorted(self, sorted_items, original_items):
    self.longMessage = True
    last = Interval(-1, -1) 
    for item in sorted_items:
      self.assertLessEqual(last, item, msg="""
Unsorted: {}
Sorted: {}""".format(original_items, sorted_items))
      last = item
    
  def test_discrete(self):
    items = [Interval.Discrete(random.randint(1, 100))
        for _ in range(10)]

    original_items = copy.deepcopy(items)
    FuzzySort(items)

    self.assertSorted(items, original_items)

  def test_random(self):
    items = []
    for _ in range(10):
      a = random.randint(1, 100)
      b = random.randint(a, 100)
      items.append(Interval(a, b))

    original_items = copy.deepcopy(items)
    FuzzySort(items)

    self.assertSorted(items, original_items)
