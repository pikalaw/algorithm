
class Node(object):

  def __init__(self):
    self.adj_node_ids = []


class Graph(object):

  def __init__(self):
    self.nodes = {}

  def Link(self, from_node_id, to_node_id):
    for node_id in [from_node_id, to_node_id]:
      if node_id not in self.nodes:
        self.nodes[node_id] = Node()
    self.nodes[from_node_id].adj_node_ids.append(to_node_id)

  def __str__(self):
    s = ''
    for node_id, node in self.nodes.items():
      if hasattr(node, 'member_node_ids'):
        s += '{} -> {}\n'.format(node.member_node_ids, node.adj_node_ids)
      else:
        s += '{} -> {}\n'.format(node_id, node.adj_node_ids)
    return s


WHITE = 0
GRAY = 1
BLACK = 2


def SCC(graph):
  """Find the strongly connected components graph of a graph.

  Args:
    graph: Graph object

  Returns:
    SCC graph of `graph` 
  """
  scc_graph = Graph()

  graph_t = GraphTranspose(graph)
  colors = {node_id: WHITE for node_id in graph.nodes}
  for node_id in reversed(TopologicalSort(graph)):
    if colors[node_id] == WHITE:
      scc_graph.nodes[node_id] = Node()
      scc_graph.nodes[node_id].member_node_ids = []
      DFSBuildSCC(node_id, graph_t, colors, node_id, scc_graph)

  return scc_graph


def DFSBuildSCC(node_id, graph_t, colors, set_node_id, scc_graph):
  colors[node_id] = GRAY
  scc_graph.nodes[set_node_id].member_node_ids.append(node_id)
  graph_t.nodes[node_id].set_node_id = set_node_id
  for next_node_id in graph_t.nodes[node_id].adj_node_ids:
    if colors[next_node_id] == WHITE:
      DFSBuildSCC(next_node_id, graph_t, colors, set_node_id, scc_graph)
    elif colors[next_node_id] == BLACK:
      source_set_node_id = graph_t.nodes[next_node_id].set_node_id
      if (source_set_node_id != set_node_id and
          # This is a linear search. Could we do better?
          set_node_id not in scc_graph.nodes[source_set_node_id].adj_node_ids):
        scc_graph.nodes[source_set_node_id].adj_node_ids.append(set_node_id)
  colors[node_id] = BLACK


def GraphTranspose(graph):
  graph_t = Graph()
  graph_t.nodes = {node_id: Node() for node_id in graph.nodes}
  for node_id, node in graph.nodes.items():
    for next_node_id in node.adj_node_ids:
      graph_t.nodes[next_node_id].adj_node_ids.append(node_id)
  return graph_t


def TopologicalSort(graph):
  sorted_node_ids = []
  
  colors = {node_id: WHITE for node_id in graph.nodes}
  for node_id in graph.nodes:
    if colors[node_id] == WHITE:
      DFSSort(node_id, graph, colors, sorted_node_ids)

  return sorted_node_ids


def DFSSort(node_id, graph, colors, sorted_node_ids):
  colors[node_id] = GRAY
  for next_node_id in graph.nodes[node_id].adj_node_ids:
    if colors[node_id] == WHITE:
      DFSSort(node_id, graph, colors, sorted_node_ids)
  colors[node_id] = BLACK
  sorted_node_ids.insert(0, node_id)


import unittest


class TestSCC(unittest.TestCase):

  def setUp(self):
    g = Graph()
    g.Link('a', 'b')
    g.Link('b', 'c')
    g.Link('b', 'e')
    g.Link('b', 'f')
    g.Link('c', 'd')
    g.Link('c', 'g')
    g.Link('d', 'c')
    g.Link('d', 'h')
    g.Link('e', 'a')
    g.Link('e', 'f')
    g.Link('f', 'g')
    g.Link('g', 'f')
    g.Link('g', 'h')
    g.Link('h', 'h')
    self.graph = g

  def test_Example(self):
    print '\n', self.graph
    scc_graph = SCC(self.graph)
    print '\n', scc_graph

