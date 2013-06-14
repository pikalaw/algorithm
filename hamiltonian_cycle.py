
class Node(object):

  def __init__(self, id):
    self.id = id
    self.adj_nodes = []
    self.visited = False


class Graph(object):

  def __init__(self):
    self.nodes = {}

  def Link(self, node_a, node_b):
    for node in [node_a, node_b]:
      if node not in self.nodes:
        self.nodes[node] = Node(node)
    self.nodes[node_a].adj_nodes.append(node_b)
    self.nodes[node_b].adj_nodes.append(node_a)
    

def HamiltonianCycleGraph(graph, root_id):
  if root_id not in graph.nodes:
    return None
  path = DFSGraph(graph, root_id, root_id, len(graph.nodes))
  if path is not None:
    return [root_id] + path
  else:
    return None


def DFSGraph(graph, node_id, root_id, length_to_root):
  node = graph.nodes[node_id]
  node.visited = True
  try:
    for next_node_id in node.adj_nodes:
      if next_node_id == root_id and length_to_root == 1:
        return [root_id]
      if not graph.nodes[next_node_id].visited:
        next_path = DFSGraph(graph, next_node_id, root_id, length_to_root - 1)
        if next_path:
          return [next_node_id] + next_path
    if node_id == root_id and length_to_root == 1:
      return []
    else:
      return None
  finally:
    node.visited = False


import unittest


class TestHamiltonianCycleGraph(unittest.TestCase):

  def GoodGraph(self):
    # (0)--(1)--(2)
    #  |   / \   |
    #  |  /   \  | 
    #  | /     \ |
    # (3)-------(4)
    graph = Graph()
    graph.Link(0, 1)
    graph.Link(1, 2)
    graph.Link(0, 3)
    graph.Link(1, 3)
    graph.Link(1, 4)
    graph.Link(2, 4)
    graph.Link(3, 4)
    return graph

  def BadGraph(self):
    # (0)--(1)--(2)
    #  |   / \   |
    #  |  /   \  | 
    #  | /     \ |
    # (3)      (4) 
    graph = Graph()
    graph.Link(0, 1)
    graph.Link(1, 2)
    graph.Link(0, 3)
    graph.Link(1, 3)
    graph.Link(1, 4)
    graph.Link(2, 4)
    return graph

  def test_GoodGraph(self):
    self.assertEqual([0, 1, 2, 4, 3, 0],
                     HamiltonianCycleGraph(self.GoodGraph(), 0))

  def test_BadGraph(self):
    self.assertIsNone(HamiltonianCycleGraph(self.BadGraph(), 0))

  def test_SingleNode(self):
    graph = Graph()
    graph.nodes[0] = Node(0)
    self.assertEqual([0], HamiltonianCycleGraph(graph, 0))

  def test_EmptyGraph(self):
    self.assertIsNone(HamiltonianCycleGraph(Graph(), 0))

  def test_NoSuchNode(self):
    self.assertIsNone(HamiltonianCycleGraph(self.GoodGraph(), 99))
