import sys


def RecursiveExchangeCoins(amount, coins):
  results = {}
  coins.sort()
  result = _RecursiveExchangeCoins(amount, coins, results)
  return ComposeSolution(result)


class Result(object):

  def __init__(self, coin, coin_count, next_result):
    self.coin = coin
    self.coin_count = coin_count
    self.next_result = next_result


def _RecursiveExchangeCoins(amount, coins, results):
  # Memorized case.
  if amount in results:
    return results[amount]

  # Base case.
  if amount < coins[0]:
    return Result(0, 0, None) 

  # Recursion case.
  min_coin_count = sys.maxint
  min_result = Result(0, 0, None) 
  for coin in coins:
    if coin <= amount:
      remaining_result = _RecursiveExchangeCoins(amount - coin, coins, results)
      coin_count = 1 + remaining_result.coin_count
      if coin_count < min_coin_count:
        min_coin_count = coin_count
        min_result = Result(coin, coin_count, remaining_result)

  results[amount] = min_result
  return min_result


def IterativeExchangeCoins(amount, coins):
  results = []
  results[0] = Result(0, 0, None)
  for subamount in xrange(amount + 1):
    min_coin_count = sys.maxint
    min_result = results[0]
    for coin in coins:
      if coin <= subamount:
        remaining_result = results[subamount - coin]
        coin_count = 1 + remaining_result.coin_count
        if coin_count < min_coin_count:
          min_coin_count = coin_count
          min_result = Result(coin, coin_count, remaining_result)
    results[subamount] = min_result
  return ComposeSolution(results[-1])


def ComposeSolution(result):
  coins = []
  while result:
    if result.coin > 0:
      coins.append(result.coin)
    result = result.next_result
  coins.sort()
  return coins


import unittest


class TestExchangeCoins(unittest.TestCase):

  def setUp(self):
    self.tests = [
        ([1, 10, 15], 20, [10, 10]),
        ([1, 5, 10, 25], 99, [1, 1, 1, 1, 10, 10, 25, 25, 25]),
    ]
      
  def test_Recursive(self):
    for test in self.tests:
      self.assertEqual(test[2], RecursiveExchangeCoins(test[1], test[0]))
      
  def test_Iterative(self):
    for test in self.tests:
      self.assertEqual(test[2], IterativeExchangeCoins(test[1], test[0]))
