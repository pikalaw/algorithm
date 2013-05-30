
def Diameter(graph):
  return Max(AllShortestDistance(graph))


def AllShortestDistance(graph):
  """Compute the shortest distance between all pairs of vertices.

  Args:
    graph: Adjacency matrix, where entries are non-negative distance or None
           if there is no edge between the pair of vertices.

  Returns:
    distance: where distances[i][j] = the shortest distance between V_i and V_j.
  """
  INF = float('Inf')
  V = len(graph)

  # Shortest distance between pairs of vertices with no intervening vertices.
  d = [[INF for col in row] for row in graph]
  for i in xrange(V):
    for j in xrange(V):
      if i == j:
        d[i][j] = 0
      elif graph[i][j] is None:
        d[i][j] = INF
      else:
        d[i][j] = graph[i][j]

  for k in xrange(V):
    # d has shortest distance between pairs of vertices with intervening
    # vertices in {V_n : 0 <= n < k} only.
    for i in xrange(V):
      for j in xrange(V):
        new_route = d[i][k] + d[k][j]
        if new_route < d[i][j]:
          d[i][j] = new_route

  return d


def Max(d):
  return max([max(row) for row in d]) 


import unittest


class TestAllShortestDistance(unittest.TestCase):

  def test_Example(self):
    graph = [
      [None, 1, 1, 1],
      [1, None, None, None],
      [1, None, None, None],
      [1, None, None, None],
    ]
    self.assertEqual(
        [
          [0, 1, 1, 1],
          [1, 0, 2, 2],
          [1, 2, 0, 2],
          [1, 2, 2, 0]
        ], AllShortestDistance(graph))


class TestDiameter(unittest.TestCase):

  def test_Example(self):
    graph = [
      [None, 1, 1, 1],
      [1, None, None, None],
      [1, None, None, None],
      [1, None, None, None],
    ]
    self.assertEqual(2, Diameter(graph))
