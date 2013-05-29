
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
  i = CandiateUniversalSink(adj_mat)
  return i < len(adj_mat) and IsUniversalSink(adj_mat, i)


def CandiateUniversalSink(adj_mat):
  i = j = 0
  V = len(adj_mat)
  while j < V:
    if adj_mat[i][j] == 0:
      j += 1
    else:
      if i == j:
        i += 1
        j += 1
      else:
        i = j
  return i


def IsUniversalSink(adj_mat, i):
  for e in adj_mat[i]:
    if e != 0:
      return False
  for j in xrange(len(adj_mat)):
    if i != j and adj_mat[j][i] != 1:
      return False
  return True


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
        (False, [[0, 0, 1],
                 [0, 0, 1],
                 [0, 0, 1]]),
        (False, [[0, 0, 1],
                 [0, 0, 1],
                 [1, 1, 1]]),
    ]

  def test_all(self):
    self.longMessage = True
    for expected, mat in self.tests:
      self.assertEqual(expected, HasUniversalSink(mat), msg=mat)
