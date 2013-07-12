
def MaxFetch(coins):
  """http://leetcode.com/2011/02/coins-in-line.html"""
  num_coins = len(coins)
  ans = [[0 for _ in xrange(num_coins+1)] for _ in xrange(num_coins+1)]
  sides = [[None for _ in xrange(num_coins+1)] for _ in xrange(num_coins+1)]
  for i in xrange(num_coins-1, -1, -1):
    for j in xrange(i+1, num_coins+1):
      left_pick = coins[i] + sum(coins[i+1:j]) - ans[i+1][j]
      right_pick = coins[j-1] + sum(coins[i:j-1]) - ans[i][j-1]
      if left_pick > right_pick:
        ans[i][j] = left_pick
        sides[i][j] = 'L'
      else:
        ans[i][j] = right_pick
        sides[i][j] = 'R'
  return ans[0][num_coins], PickPath(coins, sides, 0, num_coins)


def PickPath(coins, sides, i, j):
  path = []
  k = 0
  while sides[i][j] is not None:
    if sides[i][j] == 'L':
      if k % 2 == 0:
        path = [coins[i]] + path
      i += 1
    elif sides[i][j] == 'R':
      if k % 2 == 0:
        path = [coins[j-1]] + path
      j -= 1
    else:
      assert False, 'Unknown side at {},{}: {}'.format(i, j, sides)
    k += 1
  return path


import unittest


class TestMaxFetch(unittest.TestCase):

  def test_Example(self):
    self.assertEqual((9, [1,3,5]), MaxFetch([1,2,3,4,5]))
    self.assertEqual((8, [3,2,3]), MaxFetch([3,2,2,3,1,2]))
