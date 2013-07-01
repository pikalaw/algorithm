INF = float('Inf')


class NetworkFlow(object):

  def __init__(self):
    self.edges = {}

  def Link(self, from_node, to_node, capacity):
    for node in [from_node, to_node]:
      if node not in self.edges:
        self.edges[node] = []

    forward_edge, reverse_edge = EdgePair(from_node, to_node, capacity)
    self.edges[from_node].append(forward_edge)
    self.edges[to_node].append(reverse_edge)

  def MaximumFlow(self, from_node, to_node):
    total_flow = 0
    while True:
      visited = {node: False for node in self.edges}
      edge_path, flow = _DFSAugmentingPath(
          from_node, to_node, self.edges, visited)
      if edge_path:
        self._Flood(edge_path, flow)
        total_flow += flow
      else:
        return total_flow

  @property
  def capacity_str(self):
    return self._GraphStr(True)

  @property
  def flow_str(self):
    return self._GraphStr(False)

  def _Flood(self, edge_path, flow):
    for edge in edge_path:
      edge.capacity -= flow
      edge.reverse.capacity += flow

  def _GraphStr(self, original):
    s = []
    for from_node in self.edges:
      header = '{} {} '.format(from_node, '->' if original else '<-')
      line = []
      for edge in self.edges[from_node]:
        if edge.original == original and edge.capacity > 0:
          line.append('{} [{}]'.format(edge.to_node, edge.capacity))
      s.append(header + ', '.join(line))
    return '\n'.join(s)


class Edge(object):

  def __init__(self, to_node, capacity, original):
    self.to_node = to_node
    self.capacity = capacity
    self.reverse = None
    self.original = original
  

def EdgePair(from_node, to_node, capacity):
  forward_edge = Edge(to_node, capacity, True)
  reverse_edge = Edge(from_node, 0, False)
  forward_edge.reverse = reverse_edge
  reverse_edge.reverse = forward_edge
  return forward_edge, reverse_edge


def _DFSAugmentingPath(node, to_node, edges, visited):
  if node == to_node:
    return [], INF

  visited[node] = True
  for edge in edges[node]:
    next_node = edge.to_node
    capacity = edge.capacity
    if not visited[next_node] and capacity > 0:
      path, flow = _DFSAugmentingPath(next_node, to_node, edges, visited)
      if path is not None:
        flow = min([flow, capacity])
        return [edge] + path, flow
  return None, None


import math
import unittest


class TestNetworkFlow(unittest.TestCase):

  def test_Example(self):
    network = NetworkFlow()
    network.Link('s', 'v1', 16) 
    network.Link('s', 'v2', 13) 
    network.Link('v2', 'v1', 4) 
    network.Link('v1', 'v3', 12) 
    network.Link('v3', 'v2', 9) 
    network.Link('v2', 'v4', 14) 
    network.Link('v4', 'v3', 7) 
    network.Link('v3', 't', 20) 
    network.Link('v4', 't', 4) 
    print 'Capacity Graph:\n', network.capacity_str
    self.assertEqual(23, network.MaximumFlow('s', 't'))
    print 'Flow Graph:\n', network.flow_str

  def test_Diamond(self):
    network = NetworkFlow()
    network.Link('s', 'u', 1000000) 
    network.Link('u', 't', 1000000) 
    network.Link('s', 'v', 1000000) 
    network.Link('v', 't', 1000000) 
    network.Link('u', 'v', 1) 
    self.assertEqual(2000000, network.MaximumFlow('s', 't'))

  def test_Irrational(self):
    r = (math.sqrt(5) - 1) / 2
    m = 2
    network = NetworkFlow()
    network.Link('v4', 'v3', r)
    network.Link('v2', 'v3', 1)
    network.Link('v2', 'v1', 1)
    network.Link('s', 'v1', m)
    network.Link('s', 'v2', m)
    network.Link('s', 'v4', m)
    network.Link('v1', 't', m)
    network.Link('v3', 't', m)
    network.Link('v4', 't', m)
    self.assertEqual(2*m + 1, network.MaximumFlow('s', 't'))
