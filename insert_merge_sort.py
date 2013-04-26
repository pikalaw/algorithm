

def InsertSort(xs):
  ys = []
  for x in xs:
    ys = [y for y in ys if y <= x] + [x] + [y for y in ys if y > x]
  return ys


def Merge(xs, ys):
  zs = []
  while xs and ys:
    if xs[0] < ys[0]:
      zs.append(xs[0])
      del xs[0]
    else:
      zs.append(ys[0])
      del ys[0]
  zs += xs
  zs += ys
  return zs


def MergeSort(xs):
  if len(xs) <= 1:
    return xs
  mid = len(xs) / 2
  return Merge(MergeSort(xs[:mid]), MergeSort(xs[mid:]))
   

def MergeInsertSort(xs, k=1):
  if len(xs) <= k:
    return InsertSort(xs)
  mid = len(xs) / 2
  return Merge(MergeSort(xs[:mid]), MergeSort(xs[mid:]))


def InplaceInsertSort(xs):
  for i in xrange(len(xs)):
    j = i
    while j > 0 and xs[j] < xs[j-1]:
      xs[j], xs[j-1] = xs[j-1], xs[j]
      j -= 1
  

def InplaceMerge(xs, p, r, q):
  left = xs[p:r]
  right = xs[r:q]
  i, j, k = p, 0, 0

  while j < len(left) and k < len(right):
    if left[j] < right[k]:
      xs[i] = left[j]
      j += 1
    else:
      xs[i] = right[k]
      k += 1
    i += 1

  while j < len(left):
    xs[i] = left[j]
    j += 1
    i += 1

  while k < len(right):
    xs[i] = right[k]
    k += 1
    i += 1


def InplaceMergeSort(xs, p=None, q=None):
  if p is None:
    p = 0
  if q is None:
    q = len(xs)

  if q - p <= 1:
    return
  r = (q + p) / 2
  InplaceMergeSort(xs, p, r)
  InplaceMergeSort(xs, r, q)
  InplaceMerge(xs, p, r, q)


import unittest


class TestSort(unittest.TestCase):

  def setUp(self):
    self.tests = []
    self.tests.append(([0,1,2,3,4,5,6,7,8], range(9)))
    self.tests.append(([8,7,6,5,4,3,2,1,0], range(9)))
    self.tests.append(([], []))
    self.tests.append(([1], [1]))
    self.tests.append(([1,2,1,2], [1,1,2,2]))

  def test_InsertSort(self):
    for test in self.tests:
      self.assertEqual(test[1], InsertSort(test[0]))

  def test_MergeSort(self):
    for test in self.tests:
      self.assertEqual(test[1], MergeSort(test[0]))

  def test_MergeInsertSort(self):
    for test in self.tests:
      self.assertEqual(test[1], MergeInsertSort(test[0]))

  def test_InplaceInsertSort(self):
    for test in self.tests:
      InplaceInsertSort(test[0])
      self.assertEqual(test[1], test[0])

  def test_InplaceMergeSort(self):
    for test in self.tests:
      InplaceMergeSort(test[0])
      self.assertEqual(test[1], test[0])

