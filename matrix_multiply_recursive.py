import sys

class Matrix(object):

  def __init__(self, m, n):
    self.m = m
    self.n = n

  def __str__(self):
    return self.__repr__()

  def __repr__(self):
    return 'Matrix({}, {})'.format(self.m, self.n)
 

def DPRecursive(matrices, i, j, subproblems):
  # Meorized case.
  if subproblems[i][j]:
    return subproblems[i][j]

  # Base case.
  if j - i <= 1:
    return 0, '{}'.format(matrices[i])

  # Recursion case.
  min_cost = sys.maxint
  min_solution = None
  for k in xrange(i+1, j):
    left_cost, left_solution = DPRecursive(matrices, i, k, subproblems)
    right_cost, right_solution = DPRecursive(matrices, k, j, subproblems)
    cost = (left_cost + right_cost +
            matrices[i].m * matrices[k].m * matrices[j-1].n)
    if cost < min_cost:
      min_cost = cost
      min_solution = SolutionString(left_solution, right_solution, i, k, j)

  subproblems[i][j] = (min_cost, min_solution)
  return min_cost, min_solution


def SolutionString(left, right, i, k, j):
  if k - i > 1:
    left = '({})'.format(left)
  if j - k > 1:
    right = '({})'.format(right)
  return '{} * {}'.format(left, right)


def MatrixMultiplyStrategy(matrices):
  VerifyMultiplicable(matrices)
  subproblems = [[None for _ in xrange(len(matrices)+1)]
                 for _ in xrange(len(matrices))]
  return DPRecursive(matrices, 0, len(matrices), subproblems)


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

  def test_Example2(self):
    matrices = [Matrix(9,3), Matrix(3,4), Matrix(4,5), Matrix(5,15)]
    ops, solution = MatrixMultiplyStrategy(matrices)
    self.assertEqual(
        'Matrix(9, 3) * ((Matrix(3, 4) * Matrix(4, 5)) * Matrix(5, 15))',
        solution)
    self.assertEqual(690, ops)

  def test_InvalidMultiplication(self):
    with self.assertRaisesRegexp(ValueError, 'Incompatible multiplication'):
      MatrixMultiplyStrategy([Matrix(1,2), Matrix(3,4)])

