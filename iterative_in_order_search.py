
class Node(object):

  def __init__(self, value):
    self.value = value
    self._left = None
    self._right = None
    self.parent = None

  @property
  def left(self):
    return self._left

  @left.setter
  def left(self, node):
    self._left = node
    node.parent = self

  @property
  def right(self):
    return self._right

  @right.setter
  def right(self, node):
    self._right = node
    node.parent = self


def InOrderSearch(node):
  node = Least(node)
  while node:
    yield node.value
    node = Successor(node)


def Least(node):
  while node.left:
    node = node.left
  return node


def Successor(node):
  if node.right:
    return Least(node.right)
  else:
    return RightAncestor(node)


def RightAncestor(node):
  while node.parent:
    if node.parent.left == node:
      return node.parent
    node = node.parent
  return None


import unittest


class TestInOrderSearch(unittest.TestCase):

  def test_LeftTree(self):
    root = Node(5)
    root.left = Node(4)
    root.left.left = Node(3)
    root.left.left.left = Node(2)

    expected = [2, 3, 4, 5]
    actual = [n for n in InOrderSearch(root)]
    self.assertEqual(expected, actual)

  def test_RightTree(self):
    root = Node(5)
    root.right = Node(6)
    root.right.right = Node(7)
    root.right.right.right = Node(8)

    expected = [5, 6, 7, 8]
    actual = [n for n in InOrderSearch(root)]
    self.assertEqual(expected, actual)

  def test_ZigZag(self):
    root = Node(1)
    root.right = Node(9)
    root.right.left = Node(2)
    root.right.left.right = Node(8)

    expected = [1, 2, 8, 9]
    actual = [n for n in InOrderSearch(root)]
    self.assertEqual(expected, actual)

  def test_FullTree(self):
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(7)
    root.right.left = Node(6)
    root.right.right = Node(8)

    expected = [2, 3, 4, 5, 6, 7, 8]
    actual = [n for n in InOrderSearch(root)]
    self.assertEqual(expected, actual)

  def test_Empty(self):
    root = None

    expected = []
    actual = []
    self.assertEqual(expected, actual)
