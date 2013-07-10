import copy


def BalancedPartition(xs):
  _, left_bag = Knapsack(xs, sum(xs) / 2)
  right_bag = ArrayMinus(xs, left_bag)
  return left_bag, right_bag, abs(sum(left_bag) - sum(right_bag))


def Knapsack(xs, limit):
  if limit <= 0:
    return 0, []

  max_sum = 0
  max_bag = []
  for i, x in enumerate(xs):
    sub_sum, sub_bag = Knapsack(xs[:i] + xs[i+1:], limit - x)
    new_sum = sub_sum + x
    if new_sum <= limit and new_sum > max_sum:
      max_sum = sub_sum + x
      max_bag = [x] + sub_bag
  return max_sum, max_bag


def ArrayMinus(a, b):
  """Returns a - b as arrays."""
  c = copy.deepcopy(a)
  for x in b:
    c.remove(x)
  return c


import unittest


class TestBalancedPartition(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(1, BalancedPartition([1, 2, 3, 4, 5])[2])
    self.assertEqual(1, BalancedPartition([1, 1, 1, 1, 1])[2])
    self.assertEqual(0, BalancedPartition([])[2])
