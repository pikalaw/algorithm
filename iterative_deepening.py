
class Node(object):

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None 

  def __str__(self):
    return 'Node {{ value: {} }}'.format(self.value)

  def __repr__(self):
    return 'Node({})'.format(self.value)


def DepthFirst(node, depth, visit):
  if depth <= 0:
    visit(node)
    return True
  else:
    if node.left:
      left_reached = DepthFirst(node.left, depth - 1, visit)
    else:
      left_reached = False

    if node.right:
      right_reached = DepthFirst(node.right, depth - 1, visit)
    else:
      right_reached = False

    return left_reached or right_reached


def IterativeDeepening(root, visit):
  depth = 0
  while DepthFirst(root, depth, visit):
    depth += 1


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
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    root.left.left.left = Node(6)
    
    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__(mox.Func(IsNode(1)))
    mock_visit.__call__(mox.Func(IsNode(2)))
    mock_visit.__call__(mox.Func(IsNode(3)))
    mock_visit.__call__(mox.Func(IsNode(4)))
    mock_visit.__call__(mox.Func(IsNode(5)))
    mock_visit.__call__(mox.Func(IsNode(6)))
    m.ReplayAll()

    IterativeDeepening(root, mock_visit)    
    m.VerifyAll()
