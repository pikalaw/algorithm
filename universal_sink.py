
def HasUniversalSink(adj_mat):
  """Detect if there exists an universal sink, a node that has V-1 inflow but
  0 outflow in a graph G = (V, E).

  Running time is O(V).

  Args:
    adj_mat: An adjacency matrix.

  Returns:
    True if it has an universal sink.
    False otherwise.
  """
  i = j = 0
  V = len(adj_mat)
  while i < V and j < V:
    if adj_mat[i][j] == 0:
      j += 1
    else:
      if i == j:
        i += 1
        j += 1
      else:
        i = j
  if i < V:
    s = 0
    j = 0
    while j < V:
      s += adj_mat[j][i]
      j += 1
    return s == V-1
  else:
    return False


import unittest


class TestHasUniversalSink(unittest.TestCase):

  def setUp(self):
    self.tests = [
        (True, [[0, 0, 0],
                [1, 0, 0],
                [1, 0, 0]]),
        (True, [[0, 1, 0],
                [0, 0, 0],
                [0, 1, 0]]),
        (True, [[0, 0, 1],
                [0, 0, 1],
                [0, 0, 0]]),
        (False, [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]),
        (False, [[1, 1, 1],
                 [1, 1, 1],
                 [1, 1, 1]]),
        (False, [[0, 1, 0],
                 [0, 0, 1],
                 [0, 0, 0]]),
    ]

  def test_all(self):
    self.longMessage = True
    for expected, mat in self.tests:
      self.assertEqual(expected, HasUniversalSink(mat), msg=mat)
