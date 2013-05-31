
class Node(object):

  def __init__(self, id):
    self.id = id
    self.prev = self.next = self.child = None

  def LinkAsSibling(self, node):
    sibling = self.next
    if sibling:
      node.next = sibling
      sibling.prev = node
    self.next = node
    node.prev = self

  def LinkAsChild(self, node):
    self.child = node


class Tree(object):

  def __init__(self, root=None):
    self.root = root

  def __eq__(self, other):
    self_node = self.root
    other_node = other.root
    while True:
      if self_node is None and other_node is None:
        return True
      elif self_node is None or other_node is None:
        return False

      if self_node.id != other_node.id:
        return False

      if self_node.child and other_node.child:
        if Tree(self_node.child) != Tree(other_node.child):
          return False
      elif self_node.child or other_node.child:
        return False

      self_node = self_node.next
      other_node = other_node.next

  def __ne__(self, other):
    return not self == other

  def __str__(self):
    s = ''
    pending = [(None, self.root)]
    while pending:
      parent, node = pending.pop(0)
      s += '{}: '.format(parent)
      while node:
        if node.child:
          pending.append((node.id, node.child))
          s += '{}->{} '.format(node.id, node.child.id)
        else:
          s += '{} '.format(node.id)
        node = node.next
      s += '\n'
    return s


class List(object):

  def __init__(self, root):
    self.root = root

  def __str__(self):
    s = ''
    node = self.root
    while node:
      s += '{} '.format(node.id)
      node = node.next
    return s

  def __eq__(self, other):
    self_node = self.root
    other_node = other.root
    while True:
      if self_node is None and other_node is None:
        return True
      if self_node is None or other_node is None:
        return False
      
      if self_node.id != other_node.id:
        return False

      self_node = self_node.next
      other_node = other_node.next


def Flatten(tree):
  head_node = tree.root
  tail_node = _Tail(head_node)
  while head_node:
    if head_node.child:
      _Graft(head_node.child, tail_node)
      tail_node = _Tail(tail_node)
    head_node = head_node.next
  return List(tree.root)


def Deflatten(list):
  node = _Tail(list.root)
  while node:
    if node.child:
      _BreakPriorLinks(node.child)
    node = node.prev
  return Tree(list.root)
  

def _Tail(node):
  while node.next:
    node = node.next
  return node


def _Graft(branch_node, tree_node):
  tree_node.next = branch_node
  branch_node.prev = tree_node


def _BreakPriorLinks(node):
  prior = node.prev
  if prior:
    prior.next = None
  node.prev = None


import copy
import unittest


class TestFlatten(unittest.TestCase):

  def setUp(self):
    nodes = [Node(i) for i in xrange(15)]
    nodes[0].LinkAsSibling(nodes[1])
    nodes[0].LinkAsSibling(nodes[2])
    nodes[0].LinkAsChild(nodes[3])
    nodes[3].LinkAsSibling(nodes[4])
    nodes[3].LinkAsSibling(nodes[5])
    nodes[1].LinkAsChild(nodes[6])
    nodes[6].LinkAsSibling(nodes[7])
    nodes[6].LinkAsSibling(nodes[8])
    nodes[4].LinkAsChild(nodes[9])
    nodes[9].LinkAsSibling(nodes[10])
    nodes[7].LinkAsChild(nodes[11])
    nodes[11].LinkAsSibling(nodes[12])
    nodes[8].LinkAsChild(nodes[13])
    nodes[13].LinkAsSibling(nodes[14])

    tree = Tree(nodes[0])

    self.nodes = nodes
    self.tree = tree

  def test_Example(self):
    tree = copy.deepcopy(self.tree)
    print '\n', tree
    list = Flatten(tree)
    print list, '\n'
    tree = Deflatten(list)
    print tree
    self.assertEqual(self.tree, tree)
