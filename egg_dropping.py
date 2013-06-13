
def MinEggDrops(floors, eggs):
  """Returns the minimum egg drops from m floors with n eggs where
  1 <= m <= floors and 1 <= n <= eggs.

  See http://en.wikipedia.org/wiki/Dynamic_programming#Egg_dropping_puzzle

  Args:
    floors: Number of floors.
    eggs: Number of eggs.

  Returns:
    Doubly array d where d[m][n] is the minimum drops for m floors and n eggs.
  """
  INF = float('Inf')
  min_egg_drops = [[None for _ in range(floors+1)] for _ in range(eggs+1)]

  # Solutions for 1 egg for all floors.
  for num_floors in range(floors+1):
    min_egg_drops[1][num_floors] = num_floors

  # Solutions for > 1 eggs.
  for num_eggs in range(2, eggs+1):
    min_egg_drops[num_eggs][1] = 1
    for num_floors in range(2, floors+1):
      drop_counts = [INF for _ in range(num_floors+1)]
      for at_floor in range(1, num_floors+1):
        drop_counts[at_floor] = 1 + max([
            min_egg_drops[num_eggs-1][at_floor-1],
            min_egg_drops[num_eggs][num_floors-at_floor]])
      min_egg_drops[num_eggs][num_floors] = min(drop_counts)

  return min_egg_drops


import unittest


class TestMinEggDrops(unittest.TestCase):

  def setUp(self):
    self.longMessage = True

  def test_Example(self):
    tests = [
      {'expected': 1, 'floors': 1, 'eggs': 1},
      {'expected': 2, 'floors': 2, 'eggs': 1},
      {'expected': 3, 'floors': 3, 'eggs': 1},
      {'expected': 2, 'floors': 3, 'eggs': 2},
      {'expected': 3, 'floors': 4, 'eggs': 2},
      {'expected': 3, 'floors': 5, 'eggs': 2},
      {'expected': 3, 'floors': 6, 'eggs': 2},
      {'expected': 4, 'floors': 7, 'eggs': 2},
      {'expected': 4, 'floors': 10, 'eggs': 2},
      {'expected': 5, 'floors': 15, 'eggs': 2},
      {'expected': 14, 'floors': 100, 'eggs': 2},
      {'expected': 9, 'floors': 100, 'eggs': 3},
      {'expected': 8, 'floors': 100, 'eggs': 4},
      {'expected': 7, 'floors': 100, 'eggs': 5},
      {'expected': 7, 'floors': 100, 'eggs': 6},
      {'expected': 7, 'floors': 100, 'eggs': 7},
      {'expected': 7, 'floors': 100, 'eggs': 8},
      {'expected': 7, 'floors': 100, 'eggs': 9},
      {'expected': 7, 'floors': 100, 'eggs': 10},
    ]
    min_drops = MinEggDrops(floors=100, eggs=10)
    for test in tests:
      self.assertEqual(test['expected'],
                       min_drops[test['eggs']][test['floors']],
                       msg='Test was {}'.format(test))
