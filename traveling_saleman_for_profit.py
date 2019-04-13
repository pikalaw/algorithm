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
  def __init__(self, city=None, gain=None):
    self.next_city = city
    self.gain = gain
  
  def __repr__(self):
    return '(next:{} gain:{})'.format(self.next_city, self.gain)


def construct_path(gain_paths: Dict[int, Dict[int, GainPath]], start_city: int):
  path = [start_city]
  time = 0
  current_city = start_city
  assert len(gain_paths) > 0
  while time + 1 < len(gain_paths[0]):
    next_city = gain_paths[current_city][time].next_city
    path.append(next_city)
    current_city = next_city
    time += 1
  return path


def max_profit_route(revenue: Matrix, travel_cost: Matrix):
  assert len(revenue) == len(travel_cost)
  assert is_square_matrix(travel_cost)
  assert len(revenue) > 0

  num_times = len(revenue[0])
  num_cities = len(revenue)

  gain_paths = defaultdict(lambda: defaultdict(GainPath))

  # First round of dynamic programming..
  for c in range(num_cities):
    gain_paths[c][num_times - 1] = GainPath(
        city=None, gain=revenue[c][num_times - 1])

  for t in range(num_times - 2, -1, -1):
    for c in range(num_cities):
      gain = -99
      for d in range(num_cities):
        this_gain = revenue[c][t] + gain_paths[d][t+1].gain - travel_cost[c][d]
        if this_gain > gain:
          gain_paths[c][t] = GainPath(city=d, gain=this_gain)
          gain = this_gain

  # Construct the path.
  i = 0
  for j in range(i+1, len(gain_paths)):
    if gain_paths[j][0].gain > gain_paths[i][0].gain:
      i = j
  return gain_paths[i][0].gain, construct_path(gain_paths, i)


print(max_profit_route(
    [[1,2,99],
     [4,5,6]],
    [[0,2],
     [3,0]]))
