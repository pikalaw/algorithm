
class Node(object):

  def __init__(self, value):
    self.value = value
    self._parent = None
    self._left = None
    self._right = None

  @property
  def left(self):
    return self._left

  @left.setter
  def left(self, node):
    self._left = node
    node._parent = self

  @property
  def right(self):
    return self._right

  @right.setter
  def right(self, node):
    self._right = node
    node._parent = self

  @property
  def parent(self):
    return self._parent

  def __str__(self):
    return '|'.join([str(x) for x in Linearize(self)])


def Insert(root, node):
  if node.value < root.value:
    if root.left:
      Insert(root.left, node)
    else:
      root.left = node
  else:
    if root.right:
      Insert(root.right, node)
    else:
      root.right = node


def Linearize(node):
  left = Linearize(node.left) if node.left else []
  middle = [node.value]
  right = Linearize(node.right) if node.right else []
  return left + middle + right
  

def Successor(node):
  if node.right:
    return LeastElement(node.right)
  else:
    return RightAncestor(node)


def LeastElement(node):
  if node.left:
    return LeastElement(node.left)
  else:
    return node


def RightAncestor(node):
  if not node.parent:
    return None
  elif node.parent.left == node:
    return node.parent
  else:
    return RightAncestor(node.parent)


def IterativeRightAncestor(node):
  while True:
    if not node.parent:
      return None
    elif node.parent.left == node:
      return node.parent
    else:
      node = node.parent


import unittest


class TestTree(unittest.TestCase):

  def setUp(self):
    self.values = [0, -2, -3, -1, -1.5, 5, 2, 7, 1, 10, 15]
    self.nodes = {}
    for i, value in enumerate(self.values):
      self.nodes[value] = Node(value)
      if i == 0:
        self.root = self.nodes[value]
      else:
        Insert(self.root, self.nodes[value])

  def test_Example(self):
    print '{}'.format(self.root)

  def test_Linearize(self):
    self.assertEqual(sorted(self.values), Linearize(self.root))

  def test_Successor(self):
    sorted_values = sorted(self.values)
    for i in xrange(len(sorted_values) - 1):
      self.assertEqual(sorted_values[i + 1],
                       Successor(self.nodes[sorted_values[i]]).value)
    self.assertIsNone(Successor(self.nodes[15]))
