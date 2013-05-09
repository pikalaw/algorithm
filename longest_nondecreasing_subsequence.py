import sys


def LongestNondecreasingSubsequence(xs):
  # tail x of the LIS of length i+1 with the smallest tail.
  vs = [sys.maxint for _ in xs]
  # index of the tail x of the LIS of length i+1 with the smallest tail.
  ts = [None for _ in xs]
  # index of the predecessor x[i].
  ps = [None for _ in xs]
  # index of the longest sequence in ts.
  longest = -1

  for i, x in enumerate(xs):
    vi = FindGreatestLIS(vs, x)
    next_vi = vi + 1
    vs[next_vi] = x
    ts[next_vi] = i
    if vi >= 0:
      ps[i] = ts[vi]
    if next_vi > longest:
      longest = next_vi

  return ComposeSolution(xs, ps, ts[longest]) if longest >= 0 else []


def FindGreatestLIS(vs, x):
  i, j = 0, len(vs)
  while True:
    k = (i+j)/2
    if j - i == 0:
      return i - 1
    if vs[k] > x:
      j = k
    else:
      i = k + 1
       

def ComposeSolution(xs, ps, i):
  solution = []
  while True:
    solution.append(xs[i])
    if ps[i] is not None:
      i = ps[i]
      continue
    else:
      solution.reverse()
      return solution


import unittest


class TestLongest(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(
        [1, 2, 3, 4],
        LongestNondecreasingSubsequence([1, 9, 2, 9, 3, 0, 4]))
    self.assertEqual(
        [1, 1, 1, 1],
        LongestNondecreasingSubsequence([1, 1, 1, 1]))
    self.assertEqual(
        [],
        LongestNondecreasingSubsequence([]))
    self.assertEqual(
        [1, 2, 3, 4],
        LongestNondecreasingSubsequence([1, 2, 3, 4]))
    self.assertEqual(
        [1],
        LongestNondecreasingSubsequence([4, 3, 2, 1]))
