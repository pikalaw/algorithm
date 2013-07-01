import itertools


INF = float('Inf')


class NetworkFlow(object):

  def __init__(self):
    self.capacities = {}

  def Link(self, from_node, to_node, capacity):
    for node in [from_node, to_node]:
      if node not in self.capacities:
        self.capacities[node] = {}

    self.capacities[from_node][to_node] = capacity
    self.capacities[to_node][from_node] = 0

  def MaximumFlow(self, from_node, to_node):
    total_flow = 0
    while True:
      visited = {node: False for node in self.capacities}
      path, flow = _DFSAugmentingPath(
          from_node, to_node, self.capacities, visited)
      if path:
        self._Flood(path, flow)
        total_flow += flow
      else:
        return total_flow

  def Flow(self, from_node, to_node): 
    # The capacity of the reverse edge is the flow of that edge.
    return self.capacities[to_node][from_node]

  def Capacity(self, from_node, to_node):
    return self.capacities[from_node][to_node]

  def _Flood(self, path, flow):
    for from_node, to_node in pairwise(path):
      self.capacities[from_node][to_node] -= flow
      self.capacities[to_node][from_node] += flow

  def __repr__(self):
    s = []
    for from_node in self.capacities:
      line = ['{}:'.format(from_node)]
      for to_node in self.capacities[from_node]:
        if self.capacities[from_node][to_node] > 0:
          line.append('{} [{}]'.format(
              to_node, self.capacities[from_node][to_node]))
      s.append(' '.join(line))
    return '\n'.join(s)


def _DFSAugmentingPath(node, to_node, capacities, visited):
  if node == to_node:
    return [node], INF

  visited[node] = True
  for next_node in capacities[node]:
    capacity = capacities[node][next_node]
    if not visited[next_node] and capacity > 0:
      path, flow = _DFSAugmentingPath(next_node, to_node, capacities, visited)
      if path:
        flow = min([flow, capacity])
        return [node] + path, flow
  return None, None


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


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
    self.assertEqual(23, network.MaximumFlow('s', 't'))

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
