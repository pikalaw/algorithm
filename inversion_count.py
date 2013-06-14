
def InversionCountSq(values):
  inversion_count = 0
  for i in xrange(len(values)):
    for j in xrange(i + 1, len(values)): 
      if values[i] > values[j]:
        inversion_count += 1
  return inversion_count


def InversionCountFast(values):
  _, inversion_count = MergeSort(values)
  return inversion_count


def MergeSort(values):
  if len(values) <= 1:
    return values, 0

  a_values, a_inversion_count = MergeSort(values[:len(values)/2])
  b_values, b_inversion_count = MergeSort(values[len(values)/2:])
  merged_values, merged_inversion_count = Merge(a_values, b_values)
  return merged_values, (
      a_inversion_count+b_inversion_count+merged_inversion_count)


def Merge(xs, ys):
  zs = []
  i = j = 0
  inversion_count = 0
  while i < len(xs) and j < len(ys):
    if xs[i] < ys[j]:
      zs.append(xs[i])
      i += 1
    else:
      zs.append(ys[j])
      j += 1
      inversion_count += len(xs) - i
  while i < len(xs):
    zs.append(xs[i])
    i += 1
  while j < len(ys):
    zs.append(ys[j])
    j += 1
  return zs, inversion_count


import unittest


class TestInversionCount(unittest.TestCase):

  def setUp(self):
    self.tests = [
      {'seq': [2, 4, 1, 3, 5], 'expected': 3},
      {'seq': [1, 2, 3, 4, 5], 'expected': 0},
      {'seq': [5, 4, 3, 2, 1], 'expected': 10},
    ]

  def test_Square(self):
    for test in self.tests:
      self.assertEqual(test['expected'], InversionCountSq(test['seq']))

  def test_Fast(self):
    for test in self.tests:
      self.assertEqual(test['expected'], InversionCountFast(test['seq']))
