
import sys


class Matrix(object):

  def __init__(self, m, n):
    self.m = m
    self.n = n

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    return 'Matrix({}, {})'.format(self.m, self.n)
 

class Pair(object):

  def __init__(self, ops=0, left=0, mid=0, right=0):
    self.ops = ops
    self.left = left
    self.mid = mid
    self.right = right

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    return 'Pair({}, {}, {}, {})'.format(
        self.left, self.mid, self.right, self.ops)


def DPFindStrategy(matrices):
  pairs = [[Pair(0, i, i, i) for i in xrange(len(matrices))]
           for j in xrange(len(matrices))]
  for num_factors in xrange(2, len(matrices) + 1):
    for head in xrange(0, len(matrices) - num_factors + 1):
      tail = head + num_factors
      min_ops = sys.maxint
      min_mid = None
      for mid in xrange(head + 1, tail):
        this_ops = (pairs[mid-head-1][head].ops + pairs[tail-mid-1][mid].ops +
                    CountOps(matrices[head].m,
                             matrices[mid].m,
                             matrices[tail-1].n))
        if this_ops < min_ops:
          min_ops = this_ops
          min_mid = mid
      pairs[num_factors-1][head] = Pair(min_ops, head, min_mid, tail)
  return pairs


def MatrixMultiplyStrategy(matrices):
  VerifyMultiplicable(matrices)
  pairs = DPFindStrategy(matrices)
  solution = pairs[len(matrices)-1][0]
  return solution.ops, SolutionString(solution, pairs, matrices)


def SolutionString(solution, pairs, matrices):
  if solution.ops == 0:
    return '{}'.format(matrices[solution.left])
  
  left_solution = pairs[solution.mid - solution.left - 1][solution.left]
  left_string = WrappableSolutionString(left_solution, pairs, matrices)
  
  right_solution = pairs[solution.right - solution.mid - 1][solution.mid]
  right_string = WrappableSolutionString(right_solution, pairs, matrices)

  return '{} * {}'.format(left_string, right_string)


def WrappableSolutionString(solution, pairs, matrices):
  solution_string = SolutionString(solution, pairs, matrices)
  if solution.ops > 0:
    solution_string = '({})'.format(solution_string)
  return solution_string


def CountOps(left, mid, right):
  return left * right * mid


def VerifyMultiplicable(matrices):
  for i in xrange(1, len(matrices)):
    if matrices[i-1].n != matrices[i].m:
      raise ValueError('Incompatible multiplication {} * {}'.format(
          matrices[i-1], matrices[i]))


import unittest


class TestMatrixMultiplyStrategy(unittest.TestCase):

  def test_Example(self):
    matrices = [Matrix(2,2), Matrix(2,2), Matrix(2,3)]
    ops, solution = MatrixMultiplyStrategy(matrices)
    self.assertEqual('(Matrix(2, 2) * Matrix(2, 2)) * Matrix(2, 3)', solution)
    self.assertEqual(20, ops)

  def test_Example2(self):
    matrices = [Matrix(9,3), Matrix(3,4), Matrix(4,5)]
    ops, solution = MatrixMultiplyStrategy(matrices)
    self.assertEqual('Matrix(9, 3) * (Matrix(3, 4) * Matrix(4, 5))', solution)
    self.assertEqual(195, ops)

  def test_InvalidMultiplication(self):
    with self.assertRaisesRegexp(ValueError, 'Incompatible multiplication'):
      MatrixMultiplyStrategy([Matrix(1,2), Matrix(3,4)])
