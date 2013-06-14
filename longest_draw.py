#!/usr/bin/env python

import copy
import math


def Distance(p, q):
  return math.hypot(p[0] - q[0], p[1] - q[1])


def Reaches(node):
  i, j = node
  for di in [-2, -1, 0, 1, 2]:
    for dj in [-2, -1, 0, 1, 2]:
      if di % 2 == 0 and dj % 2 == 0:
        continue
      else:
        fi = i + di
        fj = j + dj
        if not (0 <= fi <= 2 and 0 <= fj <= 2):
          continue
        else:
          yield fi, fj


def LongestDraw():
  """Find the longest Security Pattern on Android.

  The Android lock screen has 9 dots:

      x  x  x
      x  x  x
      x  x  x

  You draw the correct pattern to unlock the screen.

  This function finds the longest pattern you can draw.
  """
  solution = {'path': [], 'length': 0}
  for root in [(0, 0), (0, 1), (1, 1)]:
    visited = {}
    for i in range(3):
      for j in range(3):
        visited[(i, j)] = False
    this_path = {'path': [], 'length': 0}
    DFS(root, root, visited, solution, this_path)
  return solution


def DFS(parent_node, node, visited, solution, this_path):
  is_leaf = True

  visited[node] = True
  segment_length = Distance(parent_node, node)
  this_path['path'].append(node)
  this_path['length'] += segment_length

  for next_node in Reaches(node):
    if not visited[next_node]:
      is_leaf = False
      DFS(node, next_node, visited, solution, this_path)

  if is_leaf:
    if this_path['length'] > solution['length']:
      solution['path'] = copy.deepcopy(this_path['path'])
      solution['length'] = this_path['length']

  visited[node] = False
  this_path['path'].pop()
  this_path['length'] -= segment_length


import unittest


class TestLongestDraw(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(
        [(0,1), (2,2), (1,0), (0,2), (2,1), (0,0), (1,2), (2,0), (1,1)],
        LongestDraw()['path'])
