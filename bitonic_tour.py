import math
import sys


class Point(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return '({},{})'.format(self.x, self.y)


def SqDistance(point_a, point_b):
  return (point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2


class Result(object):

  def __init__(self, point_index, previous_index, sq_distance, predecessor):
    self.point_index = point_index
    self.previous_index = previous_index
    self.sq_distance = sq_distance
    self.predecessor = predecessor

  def __str__(self):
    return '[{}:{}:{}]'.format(
        self.point_index, self.previous_index, self.sq_distance)

  def __repr__(self):
    return self.__str__()


def Pretty(results):
  return '\n'.join([''] + [str(row) for row in results])


def BitonicTour(points):
  results = [[None for _ in points] for _ in points]
  results[0][0] = Result(0, None, 0, None)
  if len(points) > 1:
    results[1][0] = Result(1, 0, SqDistance(points[1], points[0]),
                           results[0][0])
  result = _BitonicTour(points, results, len(points)-1, len(points)-2)
  top, bottom = ComposeSolution(result, len(points) - 1)
  (bottom if top[-1] == len(points) - 1 else top).append(len(points) - 1)
  print Pretty(results)
  return top, bottom


def _BitonicTour(points, results, i, j):
  if results[i][j]:
    return results[i][j]

  if i - j > 1:
    predecessor = _BitonicTour(points, results, i-1, j)
    result = Result(
        i, i - 1,
        predecessor.sq_distance + SqDistance(points[i-1], points[i]),
        predecessor)
  else:
    min_sq_distance = sys.maxint
    min_predecessor = None
    min_k = None
    for k in xrange(i-1):
      predecessor = _BitonicTour(points, results, i-1, k)
      sq_distance = (predecessor.sq_distance + 
                     SqDistance(points[k], points[i]))
      if sq_distance < min_sq_distance:
        min_sq_distance = sq_distance
        min_predecessor = predecessor
        min_k = k
    result = Result(i, min_k, min_sq_distance, min_predecessor)

  results[i][j] = result
  return result


def ComposeSolution(result, final_index):
  if not result.predecessor:
    return [result.point_index], [result.point_index]

  top, bottom = ComposeSolution(result.predecessor, final_index)

  if top[-1] == result.previous_index:
    top.append(result.point_index)
  elif bottom[-1] == result.previous_index:
    bottom.append(result.point_index)

  return top, bottom


import unittest


class TestBitonicPath(unittest.TestCase):

  def test_Example(self):
    points = [Point(0,6), Point(1,0), Point(2,3), Point(5,4), Point(6,1),
              Point(7,5), Point(8,2)]
    self.assertEqual(([0, 1, 4, 6], [0, 2, 3, 5, 6]), BitonicTour(points))
