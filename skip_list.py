import random

class SkipList(object):

  def __init__(self, depth=10):
    assert depth > 0
    self.min_node = SkipNode(None, None)
    self.max_node = SkipNode(None, None)
    self.min_node.next_nodes = [self.max_node] * depth
    self.depth = depth

  def find(self, key):
    parent_nodes, steps = self._find_parents(key)
    candidate_node = parent_nodes[0].next_nodes[0]
    if candidate_node is not self.max_node and candidate_node.key == key:
      return candidate_node, steps
    else:
      raise KeyError('key {} is not found.'.format(key))
    
  def insert(self, key, value=None):
    parent_nodes, steps = self._find_parents(key)
    new_node = SkipNode(key, value)
    level = 0
    while level < self.depth:
      new_node.next_nodes.append(parent_nodes[level].next_nodes[level])
      parent_nodes[level].next_nodes[level] = new_node
      if random.randint(0, 1) == 1:
        level += 1
      else:
        break
    return steps

  def delete(self, key):
    parent_nodes, steps = self._find_parents(key)
    level = 0
    while (level < self.depth and
        parent_nodes[level].next_nodes[level].key == key):
      deleting_node = parent_nodes[level].next_nodes[level]
      parent_nodes[level].next_nodes[level] = deleting_node.next_nodes[level]
      level += 1
    return steps

  def level_nodes(self, level):
    assert level < self.depth
    node = self.min_node.next_nodes[level]
    while node is not self.max_node:
      yield node
      node = node.next_nodes[level]

  def _find_parents(self, key):
    parent_nodes = [None] * self.depth
    level = self.depth
    node = self.min_node
    steps = 0
    while level > 0:
      level -= 1
      while (node.next_nodes[level] is not self.max_node and
          node.next_nodes[level].key < key):
        node = node.next_nodes[level]
        steps += 1
      parent_nodes[level] = node
    return parent_nodes, steps
    

class SkipNode(object):

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next_nodes = []

  @property
  def start_iteration(self):
    node = self
    while node.next_nodes:
      yield node
      node = node.next_nodes[0]
    

import itertools
import math
import unittest


def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = itertools.tee(iterable)
  next(b, None)
  return itertools.izip(a, b)


def print_list(skip_list):
  for level in range(skip_list.depth):
    print_level(skip_list, level)


def print_level(skip_list, level):
  print 'Level', level
  for node in skip_list.level_nodes(level):
    print node.key,
  print
  

class TestSkipList(unittest.TestCase):

  def check_list_ordering(self, skip_list):
    for level in range(skip_list.depth):
      for x, y in pairwise(skip_list.level_nodes(level)):
        self.assertLessEqual(x.key, y.key)
      
  def test_random_insertion_deletion(self):
    for size in [10, 100, 1000]:
      inputs = range(size)
      random.shuffle(inputs)
      depth = int(math.log(size, 2))

      print '==============================================='
      print 'Size = {}, depth = {}'.format(size, depth)
      print 'Log(N) = {:.2f}'.format(math.log(size, 2))

      print 'Inserting...'
      total_steps = 0
      skip_list = SkipList(depth)
      for input in inputs:
        total_steps += skip_list.insert(input, None)
        self.check_list_ordering(skip_list)
      print 'Average steps to insert: {}'.format(
          float(total_steps) / size)

      print 'Searching...'
      total_steps = 0
      for input in sorted(inputs):
        node, steps = skip_list.find(input)
        total_steps += steps
      print 'Average steps in find: {}'.format(
          float(total_steps)/len(inputs))

      print 'Deleting...'
      total_steps = 0
      for input in inputs:
        total_steps += skip_list.delete(input)
        self.check_list_ordering(skip_list)
      print 'Average steps in delete: {}'.format(
          float(total_steps)/len(inputs))

  def test_iterable(self):
    inputs = range(10)
    skip_list = SkipList()
    for input in inputs:
      skip_list.insert(input, None)

    i = 5
    start_node, _ = skip_list.find(i)
    for node in start_node.start_iteration:
      self.assertEqual(i, node.key)
      i += 1
