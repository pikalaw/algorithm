import collections
from itertools import tee, izip


def Pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


def IsFinalSeating(seats):
  return all([a != b for a, b in Pairwise(seats)])


def GraphChildren(parent):
  for i in xrange(len(parent) - 1):
    if parent[i] != parent[i+1]:
      yield tuple(parent[0:i] + (parent[i+1], parent[i]) + parent[i+2:])


def TranspositionPath(parents, node):
  path = [node]
  while True:
    parent = parents[node]
    if not parent:
      return path
    else:
      path = [parent] + path
      node = parent


def SwapSeats(seats):
  # Breadth first search.
  done_nodes = set()
  boundary_nodes = [seats]
  node_parents = {seats: None}

  while boundary_nodes:
    expanding_node = boundary_nodes.pop(0)
    if IsFinalSeating(expanding_node):
      return TranspositionPath(node_parents, expanding_node)
    for child in GraphChildren(expanding_node):
      if child not in done_nodes:
        boundary_nodes.append(child)
        node_parents[child] = expanding_node
    done_nodes.add(expanding_node)

  return None


import unittest


class TestHelpers(unittest.TestCase):

  def test_Final(self):
    tests = [
        [],
        [0],
        [1],
        [0, 1],
        [1, 0],
        [0, 1, 0],
        [1, 0, 1],
    ]
    for test in tests:
      self.assertTrue(IsFinalSeating(test), msg='Failed for {}'.format(test))

  def test_NonFinal(self):
    tests = [
        [1, 1],
        [0, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 0],
        [0, 1, 1],
    ]
    for test in tests:
      self.assertFalse(IsFinalSeating(test), msg='Failed for {}'.format(test))

  def test_Graph(self):
    graph = TranspositionGraph()
    self.assertEqual([], list(graph([])))
    self.assertEqual([], list(graph([0])))
    self.assertEqual([], list(graph([1])))
    self.assertEqual([[1, 0]], list(graph([0, 1])))
    self.assertEqual([[0, 1]], list(graph([1, 0])))
    self.assertEqual([], list(graph([0, 0])))
    self.assertEqual([], list(graph([1, 1])))
    self.assertEqual([[0, 1, 1], [1, 1, 0]], list(graph([1, 0, 1])))
    self.assertEqual([[1, 0, 1]], list(graph([1, 1, 0])))


class TestHelpers(unittest.TestCase):

  def test_1(self):
    self.assertEqual([(1, 0, 1, 0)], SwapSeats((1, 0, 1, 0)))
    self.assertEqual([(0, 1, 0, 1)], SwapSeats((0, 1, 0, 1)))
    self.assertEqual([(1, 1, 0, 0), (1, 0, 1, 0)], SwapSeats((1, 1, 0, 0)))
    self.assertEqual([
        (1, 1, 1, 1, 0, 0, 0, 0),
        (1, 1, 1, 0, 1, 0, 0, 0),
        (1, 1, 1, 0, 0, 1, 0, 0),
        (1, 1, 1, 0, 0, 0, 1, 0),
        (1, 1, 0, 1, 0, 0, 1, 0),
        (1, 1, 0, 0, 1, 0, 1, 0),
        (1, 0, 1, 0, 1, 0, 1, 0)], SwapSeats((1, 1, 1, 1, 0, 0, 0, 0)))
    self.assertIsNone(SwapSeats((1, 1, 1, 1, 1, 0, 0, 0)))

  def test_2(self):
    self.assertEqual([], SwapSeats((1, 1, 1, 2, 2, 2, 3, 3, 3)))
