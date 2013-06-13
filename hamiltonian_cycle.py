
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
  return DFS(graph, root_id, root_id, len(graph.nodes))


def DFS(graph, node_id, root_id, length_to_root):
  node = graph.nodes[node_id]
  node.visited = True
  try:
    for next_node_id in node.adj_nodes:
      if next_node_id == root_id and length_to_root == 1:
        return [root_id]
      if not graph.nodes[next_node_id].visited:
        next_path = DFS(graph, next_node_id, root_id, length_to_root - 1)
        if next_path:
          return [next_node_id] + next_path
    return None
  finally:
    node.visited = False


def HamiltonianCycleMatrix(matrix):
  pass


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
    self.assertEqual([1, 2, 4, 3, 0],
                     HamiltonianCycleGraph(self.GoodGraph(), 0))

  def test_BadGraph(self):
    self.assertIsNone(HamiltonianCycleGraph(self.BadGraph(), 0))


class TestHamiltonianCycleMatrix(unittest.TestCase):

  def test_Example(self):
    pass
