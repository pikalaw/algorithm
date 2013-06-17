import random


class Node(object):

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
        self.left = Node(key, weight)
    else:
      if self.right:
        self.right.Insert(key, weight)
      else:
        self.right = Node(key, weight)

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


class TestWeightedBST(unittest.TestCase):

  def test_Example(self):
    root = Node(50) 
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

    TRIALS = 100000
    counts = collections.defaultdict(int)
    for i in xrange(TRIALS):
      counts[root.Random()] += 1
    self.assertAlmostEqual(5/10., counts[30]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[50]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[25]/float(TRIALS), places=2)
    self.assertAlmostEqual(2/10., counts[75]/float(TRIALS), places=2)
    self.assertAlmostEqual(1/10., counts[10]/float(TRIALS), places=2)
