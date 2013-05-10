
import sys


class Node(object):

  def __init__(self, key, pr, cost):
    self.key = key
    self.left = None
    self.right = None
    self.cost = cost
    self.pr = pr


def RecursiveOptimalBST(keys, key_prs, gap_prs):
  assert keys == sorted(keys)
  assert len(key_prs) == len(keys)
  assert len(gap_prs) == len(keys) + 1

  results = [[None for _ in range(len(keys)+1)] for _ in range(len(keys)+1)]
  return RecursiveInternalOptimalBST(
      0, len(keys), keys, key_prs, gap_prs, results)


def RecursiveInternalOptimalBST(start, end, keys, key_prs, gap_prs, results):
  # meorized case.
  if results[start][end]:
    return results[start][end]
    
  # base case.
  if start == end:
    return Node(key=None, pr=gap_prs[end], cost=gap_prs[end])

  # recursion.
  best_root = None
  best_cost = sys.maxint
  for root in range(start, end):
    left = RecursiveInternalOptimalBST(
        start, root, keys, key_prs, gap_prs, results)
    right = RecursiveInternalOptimalBST(
        root + 1, end, keys, key_prs, gap_prs, results)
    cost = (left.cost+1) * left.pr + (right.cost+1) * right.pr + key_prs[root]
    if cost < best_cost:
      best_cost = cost
      best_pr = key_prs[root] + left.pr + right.pr
      best_root = Node(keys[root], pr=best_pr, cost=best_cost)
      best_root.left = left
      best_root.right = right

  results[start][end] = best_root
  return best_root


def PrintTree(node, level=0):
  if level == 0:
    print '\n'
  print '  ' * level, '{} [{}, {}]'.format(node.key, node.cost, node.pr)
  if node.left:
    PrintTree(node.left, level+1)
  if node.right:
    PrintTree(node.right, level+1)


import unittest


class TestOptimalBST(unittest.TestCase):

  def test_Example(self):
    root = RecursiveOptimalBST([1,2,3], [.8,.05,.05], [.01,.02,.03,.05])
    PrintTree(root)

  def test_Cormen_figure_15_9(self):
    keys = [1, 2, 3, 4, 5]
    key_prs = [0.15, 0.10, 0.05, 0.10, 0.20]
    gap_prs = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    root = RecursiveOptimalBST(keys, key_prs, gap_prs)
    PrintTree(root)

  def test_Cormen_15_5_2(self):
    keys = [1, 2, 3, 4, 5, 6, 7]
    key_prs = [0.04, 0.06, 0.08, 0.02, 0.10, 0.12, 0.14]
    gap_prs = [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05]
    root = RecursiveOptimalBST(keys, key_prs, gap_prs)
    PrintTree(root)

