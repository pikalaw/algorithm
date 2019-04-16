from typing import List


class Packing(object):
  def __init__(self, boundaries: List[int], required_capacity):
    self.boundaries = boundaries
    self.required_capacity = required_capacity

  def __repr__(self):
    return '{} with required capacity {}'.format(
        self.boundaries, 
        self.required_capacity)


def shipping_schedule(cargo_weights: List[int], num_days):
  # The m-th element is the packing strategy for cargos[:i] due in i-1 days at
  # the start of the i-loop but due in i days at the end of i-loop.
  # i = 1.
  min_packings = [Packing([0], 0)] + [None]*len(cargo_weights)
  last_package_weight = 0
  for j in range(1, len(cargo_weights)+1):
    last_package_weight += cargo_weights[j-1]
    min_packings[j] = Packing([j], last_package_weight)

  steps = 0

  # i > 1.
  for i in range(2, num_days+1):
    next_min_packings = [Packing([0], 0)] + [None]*len(cargo_weights)
    for j in range(1, len(cargo_weights)+1):
      min_boundaries = None
      min_required_capacity = float('inf')
      last_package_weight = 0
      for k in range(j-1, -1, -1):
        last_package_weight += cargo_weights[k]
        candidate_min = max(
            min_packings[k].required_capacity, last_package_weight)
        if candidate_min < min_required_capacity:
          min_required_capacity = candidate_min
          min_boundaries = min_packings[k].boundaries + [j]
          if min_required_capacity <= last_package_weight:
            break
        steps += 1
      next_min_packings[j] = Packing(min_boundaries, min_required_capacity)
    min_packings = next_min_packings

  return min_packings[len(cargo_weights)], steps


for test_case in [
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 2),
    ([1, 2, 3, 4, 5], 3),
    ([1, 2, 3, 4, 5], 5),
    ]:
  cargo_weights, num_days = test_case
  solution, steps = shipping_schedule(cargo_weights, num_days)
  print('Shipping cargos {} in {} days has solution {} '
        'computed in {} steps.'.format(
    cargo_weights, num_days, solution, steps))
