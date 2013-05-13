
def RecursiveKnapsack(values, weights, capacity):
  assert len(values) == len(weights)
  results = {}
  return _RecursiveKnapsack(values, weights, capacity, len(values), results)
  
  
def _RecursiveKnapsack(values, weights, capacity, n, results):
  if capacity in results and n in results[capacity]:
    return results[capacity][n]
  
  if n == 0:
    result = [], 0., 0.
  else:
    # Without the last item.
    content_wo, value_wo, weight_wo = _RecursiveKnapsack(
        values, weights, capacity, n-1, results)

    # With the last item.
    if weights[n-1] <= capacity:
      content_w, value_w, weight_w = _RecursiveKnapsack(
          values, weights, capacity - weights[n-1], n-1, results)
      content_w += [n-1]
      value_w += values[n-1]
      weight_w += weights[n-1]
    else:
      value_w = -1.

    if value_w > value_wo:
      result = content_w, value_w, weight_w
    else:
      result = content_wo, value_wo, weight_wo

  results[capacity] = {n: result}
  return result


import unittest


class TestKnapsack(unittest.TestCase):

  def test_Example(self):
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    self.assertEqual(
        ([1, 2], 220.0, 50.0),
        RecursiveKnapsack(values, weights, capacity))
