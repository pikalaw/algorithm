
def Select(items, rank, key=lambda x: x):
  return InternalSelect(items, 0, len(items), rank, key)


def InternalSelect(items, i, j, rank, key):
  # Base.
  if j - i <= 5:
    return BaseSelect(items, i, j, rank, key)

  # Recursion.
  k = Partition(items, i, j, key)
  if rank == k:
    return items[k]
  elif rank < k:
    return InternalSelect(items, i, k, rank, key)
  else:
    return InternalSelect(items, k + 1, j, rank, key)


def BaseSelect(items, i, j, rank, key):
  InsertSort(items, i, j, key)
  return items[rank]


def InsertSort(items, i, j, key):
  for p in xrange(i, j):
    for q in xrange(p, i, -1):
      if key(items[q-1]) > key(items[q]):
        Swap(items, q-1, q)


def Swap(items, i, j):
  temp = items[i]
  items[i] = items[j]
  items[j] = temp


def Partition(items, i, j, key):
  median_of_medians = MedianOfMedians(items, i, j, key)
  p = i
  q = j
  k = i
  while k < q:
    if key(items[k]) < median_of_medians:
      Swap(items, k, p)
      p += 1
      k += 1
    elif key(items[k]) > median_of_medians:
      Swap(items, k, q - 1)
      q -= 1
    else:
      k += 1
  return int((p+q)/2)


def MedianOfMedians(items, i, j, key):
  medians = []
  while i < j:
    start = i
    end = min(i+5, j)
    middle = (start + end) / 2
    medians.append(InternalSelect(items, start, end, middle, key))
    i += 5
  return Select(medians, int(len(medians)/2), key)


import unittest
import random
import copy


class TestSelect(unittest.TestCase):

  def test_Random(self):
    original = [random.randint(1, 100) for _ in xrange(10)] 
    a_copy = copy.deepcopy(original)
    select = Select(a_copy, 5)
    self.assertEqual(sorted(original)[5], select)

  def test_Increasing(self):
    original = [x for x in xrange(100)] 
    a_copy = copy.deepcopy(original)
    select = Select(a_copy, 5)
    self.assertEqual(sorted(original)[5], select)

  def test_Decreasing(self):
    original = [x for x in xrange(100)]
    original.reverse()
    a_copy = copy.deepcopy(original)
    select = Select(a_copy, 5)
    self.assertEqual(sorted(original)[5], select)

  def test_Constant(self):
    original = [1 for _ in xrange(10)] 
    a_copy = copy.deepcopy(original)
    select = Select(a_copy, 5)
    self.assertEqual(sorted(original)[5], select)
