
class DAG(object):

  def __init__(self):
    self.nodes = {}

  def Link(self, from_node_id, to_node_id):
    for node_id in [from_node_id, to_node_id]:
      if node_id not in self.nodes:
        self.nodes[node_id] = []
    self.nodes[from_node_id].append(to_node_id)

  def __str__(self):
    s = ''
    for node_id, next_nodes in sorted(self.nodes.items()):
      s += '{}: '.format(node_id) + ', '.join(sorted(next_nodes)) + '\n'
    return s


WHITE = 1
GRAY = 2
BLACK = 3


def TopologicalSort(dag):
  sorted_list = []

  def PrependList(node_id):
    sorted_list[:0] = [node_id]

  colors = {node_id: WHITE for node_id in dag.nodes}
  for node_id in dag.nodes:
    if colors[node_id] == WHITE:
      DFS(node_id, dag, colors, PrependList)
  return sorted_list


def DFS(node_id, dag, colors, visit):
  colors[node_id] = GRAY
  for next_node_id in dag.nodes[node_id]:
    if colors[next_node_id] == GRAY:
      raise Exception('dag has cycle')
    elif colors[next_node_id] == WHITE:
      DFS(next_node_id, dag, colors, visit)
  colors[node_id] = BLACK
  visit(node_id)
  return True


def SimplePathCount(dag, from_node_id, to_node_id):
  if from_node_id not in dag.nodes or to_node_id not in dag.nodes:
    return 0

  path_count = {node_id: 0 for node_id in dag.nodes}
  path_count[to_node_id] = 1

  sorted_list = TopologicalSort(dag)

  for i in xrange(sorted_list.index(to_node_id) - 1, 
                  sorted_list.index(from_node_id) - 1, -1):
    this_node_id = sorted_list[i]
    for next_node_id in dag.nodes[this_node_id]:
      path_count[this_node_id] += path_count[next_node_id]

  return path_count[from_node_id]

  
import unittest


class TestSimplePathCount(unittest.TestCase):

  def setUp(self):
    dag = DAG()
    dag.Link('m', 'q')
    dag.Link('m', 'x')
    dag.Link('m', 'r')
    dag.Link('n', 'q')
    dag.Link('n', 'u')
    dag.Link('n', 'o')
    dag.Link('o', 'r')
    dag.Link('o', 'v')
    dag.Link('o', 's')
    dag.Link('p', 'o')
    dag.Link('p', 's')
    dag.Link('p', 'z')
    dag.Link('q', 't')
    dag.Link('r', 'u')
    dag.Link('r', 'y')
    dag.Link('s', 'r')
    dag.Link('u', 't')
    dag.Link('v', 'x')
    dag.Link('v', 'w')
    dag.Link('w', 'z')
    dag.Link('y', 'v')
    self.dag = dag

  def test_Example(self):
    print self.dag

  def test_TopologicalSort(self):
    self.assertEqual(
        ['p', 'n', 'o', 's', 'm', 'r', 'y', 'v', 'w', 'z', 'u', 'x', 'q', 't'],
        TopologicalSort(self.dag))

  def test_SimplePathCount(self):
    self.assertEqual(4, SimplePathCount(self.dag, 'p', 'v'))
    self.assertEqual(1, SimplePathCount(self.dag, 'm', 'q'))
    self.assertEqual(0, SimplePathCount(self.dag, 'q', 'm'))
    self.assertEqual(0, SimplePathCount(self.dag, 'no-such-node', 'm'))
    self.assertEqual(0, SimplePathCount(self.dag, 'm', 'no-such-node'))
    self.assertEqual(0, SimplePathCount(
        self.dag, 'no-such_node-1', 'no-such-node-2'))
    self.assertEqual(1, SimplePathCount(self.dag, 'm', 'm'))
