
class InvalidRank(Exception):
  pass

class InvalidNode(Exception):
  pass

class Node(object):

  def __init__(self, value):
    self._left = None
    self._right = None
    self.parent = None
    self.size = 1
    self.value = value

  @property
  def left(self):
    return self._left

  @left.setter
  def left(self, node):
    self._left = node 
    if node:
      node.parent = self
    
  @property
  def right(self):
    return self._right

  @right.setter
  def right(self, node):
    self._right = node
    if node:
      node.parent = self

  def __str__(self):
    return '{}'.format(self.value)

  def __repr__(self):
    return 'Node({})'.format(self.value)

  def _UpdateSize(self):
    self.size = (
        (self.left.size if self.left else 0) +
        1 +
        (self.right.size if self.right else 0)
    )


class Tree(object):

  def __init__(self, root=None):
    self.root = root

  def __str__(self):
    left_tree = str(Tree(self.root.left)) if self.root.left else None
    this_node = str(self.root) if self.root else None
    right_tree = str(Tree(self.root.right)) if self.root.right else None
    return ','.join(NoNone(left_tree, this_node, right_tree))

  @property
  def least(self):
    if not self.root:
      return None
    elif self.root.left:
      return Tree(self.root.left).least
    else:
      return self.root

  @property
  def greatest(self):
    if not self.root:
      return None
    elif self.root.right:
      return Tree(self.root.right).greatest
    else:
      return self.root

  def Insert(self, node):
    if not self.root:
      self.root = node
      node.parent = None
    elif node.value < self.root.value:
      self.root.size += 1
      if not self.root.left:
        self.root.left = node
      else:
        Tree(self.root.left).Insert(node)
    else:
      self.root.size += 1
      if not self.root.right:
        self.root.right = node
      else:
        Tree(self.root.right).Insert(node)

  def PersistentInsert(node):
    raise NotImplementedError()
    
  def Find(self, value):
    if self.root.value == value:
      return self.root
    elif value < self.root.value:
      if self.root.left:
        return Tree(self.root.left).Find(value)
      else:
        return None
    else:
      if self.root.right:
        return Tree(self.root.right).Find(value)
      else:
        return None

  def Delete(self, node):
    if node.left is None:
      self._Transplant(node, node.right)
      lowest_size_changed_node = node.right
    elif node.right is None:
      self._Transplant(node, node.left)
      lowest_size_changed_node = node.left
    else:
      substitute = Tree(node.right).least
      if substitute != node.right:
        self._Transplant(substitute, substitute.right)
        substitute.right = node.right
        lowest_size_changed_node = substitute.right
      else:
        lowest_size_changed_node = substitute
      self._Transplant(node, substitute)
      substitute.left = node.left

    if lowest_size_changed_node and lowest_size_changed_node.parent:
      self._UpdateSize(lowest_size_changed_node.parent)

  def Select(self, rank):
    if not self.root:
      raise InvalidRank(rank)

    max_left_rank = self.root.left.size if self.root.left else 0
    if rank <= max_left_rank:
      return Tree(self.root.left).Select(rank)

    self_rank = max_left_rank + 1
    if self_rank == rank:
      return self.root

    return Tree(self.root.right).Select(rank - self_rank)

  def Rank(self, node):
    left_size = node.left.size if node.left else 0
    right_size = node.right.size if node.right else 0

    if node == self.root:
      return left_size + 1
    elif node.parent.left == node:
      return self.Rank(node.parent) - right_size - 1
    else:  # Right child of parent.
      return self.Rank(node.parent) + left_size + 1

  def Successor(self, node):
    if node.right:
      return Tree(node.right).least
    else:
      return self.RightAncestor(node)
      
  def Predecessor(self, node):
    if node.left:
      return Tree(node.left).greatest
    else:
      return self.LeftAncestor(node) 

  def RightAncestor(self, node):
    if not node.parent:
      return None
    elif node.parent.left and node.parent.left == node:
      return node.parent
    else:
      return self.RightAncestor(node.parent)

  def LeftAncestor(self, node):
    if not node.parent:
      return None
    elif node.parent.right and node.parent.right == node:
      return node.parent
    else:
      return self.LeftAncestor(node.parent)

  def DepthFirst(self, callback):
    if self.root:
      Tree(self.root.left).DepthFirst(callback)
      callback(self.root)
      Tree(self.root.right).DepthFirst(callback)

  def BreadthFirst(self, callback):
    queue = []
    if self.root:
      queue.append(self.root)
    while queue:
      node = queue.pop(0)
      callback(node)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)

  def IterativeDeepening(self, callback):
    level = 0
    while self._DepthFirstWithLevel(callback, level):
      level += 1

  def _DepthFirstWithLevel(self, callback, level):
    if self.root:
      left_visited = Tree(self.root.left)._DepthFirstWithLevel(callback,
                                                               level - 1)
      if level == 0:
        callback(self.root)
        self_visited = True
      else:
        self_visited = False
      right_visited = Tree(self.root.right)._DepthFirstWithLevel(callback,
                                                                 level - 1)
      return left_visited or self_visited or right_visited
    else:
      return False

  def _Transplant(self, out_node, in_node):
    if out_node == self.root:
      in_node.parent = self.root.parent
      self.root = in_node
    elif out_node == out_node.parent.left:
      out_node.parent.left = in_node
    else:
      out_node.parent.right = in_node

  def _UpdateSize(self, from_node):
    while True:
      from_node._UpdateSize()
      if from_node == self.root:
        return
      from_node = from_node.parent
    
  def Dump(self, level=0):
    if level == 0:
      print
    print '    ' * level, '{} [{}]: {}, {}'.format(
        self.root.value, self.root.size,
        self.root.left.value if self.root.left else None,
        self.root.right.value if self.root.right else None)
    if self.root.left:
      Tree(self.root.left).Dump(level + 1)
    if self.root.right:
      Tree(self.root.right).Dump(level + 1)


def NoNone(*items):
  return [x for x in items if x is not None]


import unittest
import mox


class TestTree(unittest.TestCase):

  def test_str(self):
    tree = Tree()
    tree.root = Node(0)
    tree.root.left = Node(-1)
    tree.root.right = Node(5)
    tree.root.left.left = Node(-2)
    tree.root.right.left = Node(1)
    tree.root.right.right = Node(10)
    self.assertEqual('-2,-1,0,1,5,10', str(tree))

  def test_Insert(self):
    tree = Tree()

    tree.Insert(Node(0))
    self.assertEqual('0', str(tree))

    tree.Insert(Node(1))
    self.assertEqual('0,1', str(tree))

    tree.Insert(Node(-1))
    self.assertEqual('-1,0,1', str(tree))

    tree.Insert(Node(-2))
    self.assertEqual('-2,-1,0,1', str(tree))

    tree.Insert(Node(2))
    self.assertEqual('-2,-1,0,1,2', str(tree))

  def test_Find(self):
    tree = Tree()
    tree.Insert(Node(0)) 
    tree.Insert(Node(5)) 
    tree.Insert(Node(-5))
    tree.Insert(Node(1))
    tree.Insert(Node(-1))
    tree.Insert(Node(10))
    tree.Insert(Node(-10))
    self.assertEqual('-10,-5,-1,0,1,5,10', str(tree))

    self.assertEqual(0, tree.Find(0).value)
    self.assertEqual(5, tree.Find(5).value)
    self.assertEqual(-10, tree.Find(-10).value)

  def test_least_greatest(self):
    tree = Tree()
    tree.Insert(Node(0)) 
    tree.Insert(Node(5)) 
    tree.Insert(Node(-5))
    tree.Insert(Node(1))
    tree.Insert(Node(-1))
    tree.Insert(Node(10))
    tree.Insert(Node(-10))
    self.assertEqual(10, tree.greatest.value)
    self.assertEqual(-10, tree.least.value)

  def test_SuccessorPredecessor(self):
    tree = Tree()
    tree.Insert(Node(0))
    tree.Insert(Node(-1))
    tree.Insert(Node(5))
    tree.Insert(Node(-2))
    tree.Insert(Node(1))
    tree.Insert(Node(10))
    tree.Insert(Node(2))
    self.assertEqual('-2,-1,0,1,2,5,10', str(tree))

    self.assertEqual(tree.Find(-1), tree.Successor(tree.Find(-2)))
    self.assertEqual(tree.Find(0), tree.Successor(tree.Find(-1)))
    self.assertEqual(tree.Find(1), tree.Successor(tree.Find(0)))
    self.assertEqual(tree.Find(2), tree.Successor(tree.Find(1)))
    self.assertEqual(tree.Find(5), tree.Successor(tree.Find(2)))
    self.assertEqual(tree.Find(10), tree.Successor(tree.Find(5)))
    self.assertEqual(None, tree.Successor(tree.Find(10)))

    self.assertEqual(None, tree.Predecessor(tree.Find(-2)))
    self.assertEqual(tree.Find(-2), tree.Predecessor(tree.Find(-1)))
    self.assertEqual(tree.Find(-1), tree.Predecessor(tree.Find(0)))
    self.assertEqual(tree.Find(0), tree.Predecessor(tree.Find(1)))
    self.assertEqual(tree.Find(1), tree.Predecessor(tree.Find(2)))
    self.assertEqual(tree.Find(2), tree.Predecessor(tree.Find(5)))
    self.assertEqual(tree.Find(5), tree.Predecessor(tree.Find(10)))

  def test_Delete(self):
    tree = Tree()
    tree.Insert(Node(0)) 
    tree.Insert(Node(5)) 
    tree.Insert(Node(-5))
    tree.Insert(Node(1))
    tree.Insert(Node(-1))
    tree.Insert(Node(10))
    tree.Insert(Node(-10))
    self.assertEqual('-10,-5,-1,0,1,5,10', str(tree))

    # Delete right leaf.
    node10 = tree.Find(10)
    self.assertIsNotNone(node10)
    tree.Delete(node10)
    self.assertEqual('-10,-5,-1,0,1,5', str(tree))

    # Delete left leaf.
    node_10 = tree.Find(-10)
    self.assertIsNotNone(node_10)
    tree.Delete(node_10)
    self.assertEqual('-5,-1,0,1,5', str(tree))

    # Delete middle left.
    node_1 = tree.Find(-1)
    self.assertIsNotNone(node_1)
    tree.Delete(node_1)
    self.assertEqual('-5,0,1,5', str(tree))

    # Delete middle right.
    node1 = tree.Find(1)
    self.assertIsNotNone(node1)
    tree.Delete(node1)
    self.assertEqual('-5,0,5', str(tree))

    # Delete root.
    tree.Delete(tree.root)
    self.assertEqual('-5,5', str(tree))

  def test_DeletePivotedWithRight(self):
    tree = Tree()
    tree.root = Node(0)
    tree.root.left = Node(-1)
    tree.root.right = Node(5)
    tree.root.left.left = Node(-2)
    tree.root.right.left = Node(1)
    tree.root.right.right = Node(10)
    tree.root.right.left.right = Node(2)
    self.assertEqual('-2,-1,0,1,2,5,10', str(tree))

    tree.Delete(tree.root)
    self.assertEqual('-2,-1,1,2,5,10', str(tree))

  def test_Select(self):
    tree = Tree()
    tree.Insert(Node(0))
    tree.Insert(Node(-1))
    tree.Insert(Node(5))
    tree.Insert(Node(-2))
    tree.Insert(Node(1))
    tree.Insert(Node(10))
    tree.Insert(Node(2))
    self.assertEqual('-2,-1,0,1,2,5,10', str(tree))

    self.assertEqual(tree.Find(-2), tree.Select(1))
    self.assertEqual(tree.Find(-1), tree.Select(2))
    self.assertEqual(tree.Find(0), tree.Select(3))
    self.assertEqual(tree.Find(1), tree.Select(4))
    self.assertEqual(tree.Find(2), tree.Select(5))
    self.assertEqual(tree.Find(5), tree.Select(6))
    self.assertEqual(tree.Find(10), tree.Select(7))

    with self.assertRaises(InvalidRank):
      tree.Select(0)
    with self.assertRaises(InvalidRank):
      tree.Select(8)

  def test_Rank(self):
    tree = Tree()
    tree.Insert(Node(0))
    tree.Insert(Node(-1))
    tree.Insert(Node(5))
    tree.Insert(Node(-2))
    tree.Insert(Node(1))
    tree.Insert(Node(10))
    tree.Insert(Node(2))
    self.assertEqual('-2,-1,0,1,2,5,10', str(tree))

    self.assertEqual(1, tree.Rank(tree.Find(-2)))
    self.assertEqual(2, tree.Rank(tree.Find(-1)))
    self.assertEqual(3, tree.Rank(tree.Find(0)))
    self.assertEqual(4, tree.Rank(tree.Find(1)))
    self.assertEqual(5, tree.Rank(tree.Find(2)))
    self.assertEqual(6, tree.Rank(tree.Find(5)))
    self.assertEqual(7, tree.Rank(tree.Find(10)))

  def test_DepthFirst(self):
    tree = Tree()
    tree.Insert(Node(0))
    tree.Insert(Node(-1))
    tree.Insert(Node(5))
    tree.Insert(Node(-2))
    tree.Insert(Node(1))
    tree.Insert(Node(10))
    tree.Insert(Node(2))
    self.assertEqual('-2,-1,0,1,2,5,10', str(tree))

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__(mox.Func(IsNode(-2)))
    mock_visit.__call__(mox.Func(IsNode(-1)))
    mock_visit.__call__(mox.Func(IsNode(0)))
    mock_visit.__call__(mox.Func(IsNode(1)))
    mock_visit.__call__(mox.Func(IsNode(2)))
    mock_visit.__call__(mox.Func(IsNode(5)))
    mock_visit.__call__(mox.Func(IsNode(10)))
    m.ReplayAll()

    tree.DepthFirst(mock_visit)
    m.VerifyAll()

  def test_BreadthFirst(self):
    tree = Tree()
    tree.root = Node(0)
    tree.root.left = Node(1)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.right.right = Node(6)

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__(mox.Func(IsNode(0)))
    mock_visit.__call__(mox.Func(IsNode(1)))
    mock_visit.__call__(mox.Func(IsNode(2)))
    mock_visit.__call__(mox.Func(IsNode(3)))
    mock_visit.__call__(mox.Func(IsNode(4)))
    mock_visit.__call__(mox.Func(IsNode(5)))
    mock_visit.__call__(mox.Func(IsNode(6)))
    m.ReplayAll()

    tree.BreadthFirst(mock_visit)
    m.VerifyAll()

  def test_IterativeDeepening(self):
    tree = Tree()
    tree.root = Node(0)
    tree.root.left = Node(1)
    tree.root.right = Node(2)
    tree.root.left.left = Node(3)
    tree.root.right.left = Node(4)
    tree.root.right.right = Node(5)
    tree.root.right.right.right = Node(6)

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__(mox.Func(IsNode(0)))
    mock_visit.__call__(mox.Func(IsNode(1)))
    mock_visit.__call__(mox.Func(IsNode(2)))
    mock_visit.__call__(mox.Func(IsNode(3)))
    mock_visit.__call__(mox.Func(IsNode(4)))
    mock_visit.__call__(mox.Func(IsNode(5)))
    mock_visit.__call__(mox.Func(IsNode(6)))
    m.ReplayAll()

    tree.IterativeDeepening(mock_visit)
    m.VerifyAll()


def IsNode(value):

  def VerifyNode(node):
    return node.value == value

  return VerifyNode
