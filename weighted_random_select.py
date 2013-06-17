import random


class WeightedList(object):

  def __init__(self, weights):
    for i in xrange(1, len(weights)):
      weights[i] += weights[i-1]
    self.weights = weights

  def Random(self):
    key = random.uniform(0, self.weights[-1])
    left, right = 0, len(self.weights) 
    while True:
      mid = (left + right) / 2
      if key < self.weights[mid - 1] if mid > 0 else 0.:
        right = mid
        continue
      elif key >= self.weights[mid]:
        left = mid + 1
        continue
      else:
        return mid


class WeightedNode(object):

  def __init__(self, key, weight=1):
    self.key = key
    self.weight = weight
    self.left = None
    self.right = None

  def Insert(self, key, weight=1):
    assert weight > 0
    self.weight += weight
    if self.key == key:
      return
    elif key < self.key:
      if self.left:
        self.left.Insert(key, weight)
      else:
        self.left = WeightedNode(key, weight)
    else:
      if self.right:
        self.right.Insert(key, weight)
      else:
        self.right = WeightedNode(key, weight)

  def Random(self):
    key = random.uniform(0, self.weight)
    node = self
    while True:
      if node.left and key < node.left.weight:
        node = node.left
      elif node.right and key >= node.weight - node.right.weight:
        key -= node.weight - node.right.weight
        node = node.right
      else:
        return node.key

  def __str__(self):
    s = ''
    s += '{} [{}]: '.format(self.key, self.weight)
    for node in [self.left, self.right]:
      if node:
        s += '{} [{}] '.format(node.key, node.weight)
    s += '\n'
    for node in [self.left, self.right]:
      if node:
        s += '{}'.format(node)
    return s


import collections
import unittest


class TestWeightList(unittest.TestCase):

  def test_Example(self):
    wa = WeightedList([1, 2, 3])
    self.assertEqual([1, 3, 6], wa.weights)

    TRIALS = 100000
    counts = collections.defaultdict(int)
    for i in xrange(TRIALS):
      counts[wa.Random()] += 1

    self.assertAlmostEqual(1/6., counts[0]/float(TRIALS), places=2)
    self.assertAlmostEqual(2/6., counts[1]/float(TRIALS), places=2)
    self.assertAlmostEqual(3/6., counts[2]/float(TRIALS), places=2)


class TestWeightedNode(unittest.TestCase):

  def test_Example(self):
    root = WeightedNode(50) 
    root.Insert(25) 
    root.Insert(75) 
    root.Insert(75) 
    root.Insert(10) 
    root.Insert(30) 
    root.Insert(30) 
    root.Insert(30) 
    root.Insert(30) 
    root.Insert(30) 
    print '\n', root

    self.assertEqual(10, root.weight)

    TRIALS = 200000
    counts = collections.defaultdict(int)
    for i in xrange(TRIALS):
      counts[root.Random()] += 1

    self.assertAlmostEqual(5/10., counts[30]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[50]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[25]/float(TRIALS), places=2)
    self.assertAlmostEqual(2/10., counts[75]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[10]/float(TRIALS), places=2)
