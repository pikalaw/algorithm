
def MaximumSubarray(xs, start, end):
  if start == end:
    return None, None, None
  if end - start == 1:
    return start, end, 0

  mid = (start + end) / 2

  left_start, left_end, left_reach = MaximumSubarray(xs, start, mid)
  right_start, right_end, right_reach = MaximumSubarray(xs, mid, end)
  cross_start, cross_end, cross_reach = MaximumCrossArray(xs, start, mid, end)

  if left_reach >= right_reach and left_reach >= cross_reach:
    return left_start, left_end, left_reach
  elif right_reach >= cross_reach:
    return right_start, right_end, right_reach
  else:
    return cross_start, cross_end, cross_reach


def MaximumCrossArray(xs, start, mid, end):
  left_min = left_index = None
  right_max = right_index = None

  for i in xrange(start, mid):
    if left_min is None or xs[i] < left_min:
      left_min = xs[i]
      left_index = i

  for i in xrange(mid, end):
    if right_max is None or xs[i] > right_max:
      right_max = xs[i]
      right_index = i

  if right_max is not None and left_min is not None:
    return left_index, right_index + 1, right_max - left_min
  else:
    return None, None, None


def MaximumSubarrayDivide(xs):
  return MaximumSubarray(xs, 0, len(xs))


def MaximumSubarraySquare(xs):
  # Brute force search. O(n^2).
  left_index = right_index = max_reach = None
  for i in xrange(len(xs)):  
    for j in xrange(len(xs)):  
      if i <= j:
        if xs[j] - xs[i] > max_reach:
          left_index = i
          right_index = j
          max_reach = xs[j] - xs[i]
  return (left_index,
          right_index + 1 if right_index is not None else None,
          max_reach)


import unittest

class TestMaximumArray(unittest.TestCase):

  def setUp(self):
    self.longMessage = True
    self.tests = [
      ([1,2,3], (0,3, 2)), 
      ([2,1,3], (1,3, 2)), 
      ([0,10,1,2,3,1,11], (0,7, 11)), 
      ([2,1], (0,1, 0)), 
      ([], (None,None, None)), 
    ] 

  def test_Square(self):
    for test in self.tests:
      self.assertEqual(test[1], MaximumSubarraySquare(test[0]),
                       msg='list was {0}'.format(test[0]))

  def test_Divide(self):
    for test in self.tests:
      self.assertEqual(test[1], MaximumSubarrayDivide(test[0]),
                       msg='list was {0}'.format(test[0]))

