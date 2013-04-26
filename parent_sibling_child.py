
class Node(object):

  def __init__(self, value):
    self.value = value
    self.parent = None
    self.sibling = None
    self.child = None

  def __repr__(self):
    return 'Node({})'.format(self.value)

  def __str__(self):
    return self.__repr__()


def IterativeDeepening(root, visit):
  depth = 0
  while DepthFirst(root, visit, depth):
    depth += 1


def DepthFirst(node, visit, depth):
  if depth < 0:
    return False
  if depth == 0:
    visit(node)
    self_reached = True
  else:
    self_reached = False
  if node.child:
    child_reached = DepthFirst(node.child, visit, depth - 1)
  else:
    child_reached = False
  if node.sibling:
    sibling_reached = DepthFirst(node.sibling, visit, depth)
  else:
    sibling_reached = False
  return self_reached or child_reached or sibling_reached


def PrintNode(node):
  print 'found {}'.format(node)


import unittest
import mox
import sys


def IsNode(value):

  def VerifyNode(node):
    return node.value == value

  return VerifyNode


class TestIterativeDeepening(unittest.TestCase):

  def test_balance(self):
    root = Node(1)
    root.child = Node(2)
    root.child.sibling = Node(3)
    root.child.sibling.sibling = Node(4)
    root.child.child = Node(5)
    root.child.child.sibling = Node(6)
    root.child.sibling.child = Node(7)
    root.child.sibling.child.sibling = Node(8)

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__(mox.Func(IsNode(1)))
    mock_visit.__call__(mox.Func(IsNode(2)))
    mock_visit.__call__(mox.Func(IsNode(3)))
    mock_visit.__call__(mox.Func(IsNode(4)))
    mock_visit.__call__(mox.Func(IsNode(5)))
    mock_visit.__call__(mox.Func(IsNode(6)))
    mock_visit.__call__(mox.Func(IsNode(7)))
    mock_visit.__call__(mox.Func(IsNode(8)))
    m.ReplayAll()

    IterativeDeepening(root, mock_visit)    
    m.VerifyAll()
