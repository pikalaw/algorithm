
WHITE = 0
GRAY = 1
BLACK = 2


class Node(object):

  def __init__(self):
    self.color = WHITE
    self.next_edge = None

  def Link(self, node_id):
    new_edge = Edge(node_id)
    new_edge.next_edge = self.next_edge
    self.next_edge = new_edge
    
  def __str__(self):
    return 'c({})->{}'.format(
        self.color, self.next_edge.node_id if self.next_edge else None)


class Edge(object):

  def __init__(self, node_id):
    self.node_id = node_id
    self.next_edge = None

  def __str__(self):
    return '{}~{}'.format(
        self.node_id, self.next_edge.node_id if self.next_edge else None)


def IsSinglyConnected(nodes):
  """Determine if a directed graph is singly connected.

  Args:
    nodes: adjacency lists representation of a directed graph, a list of Node.

  Returns:
    True: if `nodes` is singly connected.
    False: otherwise.
  """
  for node_id, _ in enumerate(nodes):
    if HasForwardOrCrossLink(nodes, node_id):
      return False
  return True


def HasForwardOrCrossLink(nodes, node_id):
  """Do DFS staring at node_id to find a forward or cross link."""
  Color(nodes, WHITE)
  return DFSForForwardOrCrossLink(nodes, node_id)


def DFSForForwardOrCrossLink(nodes, node_id):
  nodes[node_id].color = GRAY
  edge = nodes[node_id].next_edge
  while edge:
    child_node_id = edge.node_id
    child_node = nodes[child_node_id]
    if child_node.color == WHITE:
      if DFSForForwardOrCrossLink(nodes, child_node_id):
        return True
    elif child_node.color == BLACK:
      return True
    edge = edge.next_edge
  nodes[node_id].color = BLACK
  return False


def Color(nodes, color):
  for node in nodes:
    node.color = color


import unittest


class TestNode(unittest.TestCase):

  def test_ChainEdges(self):
    nodes = [Node()]
    nodes[0].Link(1)
    nodes[0].Link(2)

    self.assertEqual(2, nodes[0].next_edge.node_id)
    self.assertEqual(1, nodes[0].next_edge.next_edge.node_id)
    self.assertIsNone(nodes[0].next_edge.next_edge.next_edge)
     

class TestIsSinglyConnected(unittest.TestCase):

  def test_NotSingly(self):
    """0 -> 1 -> 2, 0 ->2"""
    nodes = [Node(), Node(), Node()]
    nodes[0].Link(1)
    nodes[0].Link(2)
    nodes[1].Link(2)
    self.assertEqual(False, IsSinglyConnected(nodes))

  def test_Singly(self):
    """0 -> 1 -> 2, 0 ->2"""
    nodes = [Node(), Node(), Node()]
    nodes[0].Link(1)
    nodes[0].Link(2)
    self.assertEqual(True, IsSinglyConnected(nodes))

  def test_FullTree(self):
    nodes = [Node() for _ in xrange(7)]
    nodes[0].Link(1)
    nodes[0].Link(2)
    nodes[1].Link(3)
    nodes[1].Link(4)
    nodes[2].Link(5)
    nodes[2].Link(6)
    self.assertEqual(True, IsSinglyConnected(nodes))

    # Cross link.
    nodes[6].Link(1)
    self.assertEqual(False, IsSinglyConnected(nodes))

  def test_Circle(self):
    nodes = [Node() for _ in xrange(3)]
    nodes[0].Link(1)
    nodes[1].Link(2)
    nodes[2].Link(0)
    self.assertEqual(True, IsSinglyConnected(nodes))

    # Back link.
    nodes[1].Link(0)
    self.assertEqual(False, IsSinglyConnected(nodes))
