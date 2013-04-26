#!/usr/bin/env python

import itertools
import math


def ComputeDistance(p, q):
  return math.hypot(p[0] - q[0], p[1] - q[1])


def BuildDistances(ps):
  num_p = len(ps)
  ds = [[0 for _ in range(num_p)] for _ in range(num_p)]
  for i, j in itertools.product(range(num_p), repeat=2):
    ds[i][j] = ComputeDistance(ps[i], ps[j])
  return ds


def ComputePathLength(path, ds):
  path_len = 0.
  for i, j in itertools.product(path[:-1], path[1:]):
    path_len += ds[i][j]
  return path_len 


def main():
  ps = [(x, y) for x, y in itertools.product(range(3), range(3))]
  ds = BuildDistances(ps)

  paths = []
  for path in itertools.permutations(range(len(ps))):
    paths.append((path, ComputePathLength(path, ds)))
    #print path, ComputePathLength(path, ds)

  paths.sort(key=lambda x: x[1])

  print paths[-5:]


if __name__ == '__main__':
  main()
