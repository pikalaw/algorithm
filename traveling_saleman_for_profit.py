from collections import defaultdict
from typing import List, Dict


Matrix = List[List[int]]


def is_square_matrix(m: Matrix):
  num_row = len(m)
  for row_index, row in enumerate(m):
    if len(row) != num_row:
      return False
  return True


class GainPath(object):
  def __init__(self):
    self.path = []
    self.gain = 0
  
  def __repr__(self):
    return '(gain:{} path:{})'.format(self.gain, self.path)


def max_profit_route(revenue: Matrix, travel_cost: Matrix):
  assert len(revenue) == len(travel_cost)
  assert is_square_matrix(travel_cost)
  assert len(revenue) > 0

  num_times = len(revenue[0])
  num_cities = len(revenue)

  start_time = num_times - 1
  gain_paths = [GainPath() for _ in range(num_cities)]

  max_gain = gain_paths[0].gain = revenue[0][start_time]
  max_path = gain_paths[0].path = [0]

  for i in range(1, num_cities):
    gain_paths[i].gain = revenue[i][start_time]
    gain_paths[i].path = [i]
    if gain_paths[i].gain > max_gain:
      max_gain = gain_paths[i].gain
      max_path = gain_paths[i].path

  for start_time in range(num_times - 2, -1, -1):
    new_gain_paths = [GainPath() for _ in range(num_cities)]
    for city in range(num_cities):
      for next_city in range(num_cities):
        test_gain = (revenue[city][start_time] + gain_paths[next_city].gain -
            travel_cost[city][next_city])
        if test_gain > new_gain_paths[city].gain:
          max_gain = new_gain_paths[city].gain = test_gain
          max_path = new_gain_paths[city].path = (
              [city] + gain_paths[next_city].path)
    gain_paths = new_gain_paths

  return max_gain, max_path


print(max_profit_route(
    [[1,2,99],
     [4,99,6]],
    [[0,2],
     [3,0]]))
