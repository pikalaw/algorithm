
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
    if node:
      node._parent = self

  @property
  def right(self):
    return self._right

  @right.setter
  def right(self, node):
    self._right = node
    if node:
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


def Delete(root, node):
  if node.left is None:
    root = Transplant(root, node, node.right)
  elif node.right is None:
    root = Transplant(root, node, node.left)
  else:
    new_head = LeastElement(node.right)
    if node.right != new_head:
      root = Transplant(root, new_head, new_head.right)
      new_head.right = node.right
    root = Transplant(root, node, new_head)
    new_head.left = node.left
  return root


def Transplant(root, old, new):
  if old == root:
    return new
  if old.parent.left == old:
    old.parent.left = new
  else:
    old.parent.right = new
  return root
  

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

  def test_DeleteRoot(self):
    root = Node(0)
    self.assertEqual(None, Delete(root, root))

  def test_DeleteLeftLineTail(self):
    root = Node(0)
    left = Node(-1)
    Insert(root, left)
    self.assertEqual([0], Linearize(Delete(root, left)))

  def test_DeleteLeftLineHead(self):
    root = Node(0)
    left = Node(-1)
    Insert(root, left)
    self.assertEqual([-1], Linearize(Delete(root, root)))

  def test_DeleteLeftLineMiddle(self):
    root = Node(0)
    middle = Node(-1)
    left = Node(-2)
    Insert(root, middle)
    Insert(root, left)
    self.assertEqual([-2, 0], Linearize(Delete(root, middle)))

  def test_DeleteRightLineTail(self):
    root = Node(0)
    right = Node(1)
    Insert(root, right)
    self.assertEqual([0], Linearize(Delete(root, right)))

  def test_DeleteRightLineHead(self):
    root = Node(0)
    right = Node(1)
    Insert(root, right)
    self.assertEqual([1], Linearize(Delete(root, root)))

  def test_DeleteRightLineMiddle(self):
    root = Node(0)
    middle = Node(1)
    right = Node(2)
    Insert(root, middle)
    Insert(root, right)
    self.assertEqual([0, 2], Linearize(Delete(root, middle)))

  def test_DeleteNonrootNodeWithBothChildren(self):
    root = Node(0)
    left = Node(-1)
    Insert(root, left)
    right = Node(1)
    Insert(root, right)
    right_right = Node(2)
    Insert(root, right_right)
    right_left = Node(0.5)
    Insert(root, right_left)
    self.assertEqual([-1, 0, 0.5, 2], Linearize(Delete(root, right)))

  def test_DeleteNonrootNodeWithBothChildren2(self):
    root = Node(0)
    left = Node(-1)
    Insert(root, left)
    right = Node(1)
    Insert(root, right)
    right_right = Node(2)
    Insert(root, right_right)
    self.assertEqual([-1, 0, 2], Linearize(Delete(root, right)))
