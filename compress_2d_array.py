import collections
import random
from typing import List, Tuple


def rand_2d(m: int, n: int, a: int, b: int):
  return [[random.randint(a, b) for _ in range(n)] for _ in range(m)]


def print_2d(mat: List[List[int]]):
  for row in mat:
    print(row)


def linearize(mat: List[List[int]]):
  for i in range(len(mat)):
    for j in range(len(mat[i])):
      yield ((i, j), mat[i][j])


def find_twins_with_prev(cell: Tuple[int, int], mat: List[List[int]]):
  pending = [cell]
  visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]
  twins = [cell]
  prev_value = None
  while pending:
    i, j = pending.pop()
    for k in range(len(mat[i])):
      if k == j:
        continue
      if visited[i][k]:
        continue
      visited[i][k] = True
      if mat[i][k] < mat[i][j] and (
          prev_value is None or mat[i][k] > prev_value):
        prev_value = mat[i][k]
      if mat[i][k] == mat[i][j]:
        pending.append((i,k))
        twins.append((i,k))
    for k in range(len(mat)):
      if k == i:
        continue
      if visited[k][j]:
        continue
      visited[k][j] = True
      if mat[k][j] < mat[i][j] and (
          prev_value is None or mat[k][j] > prev_value):
        prev_value = mat[k][j]
      if mat[k][j] == mat[i][j]:
        pending.append((k,j))
        twins.append((k,j))
  return twins, prev_value


def compress_2d(mat: List[List[int]]):
  done_cells = set()
  for cell, value in sorted(linearize(mat), key=lambda x: x[1]):
    if cell in done_cells:
      continue
    twins, prev_value = find_twins_with_prev(cell, mat)
    for twin in twins:
      mat[twin[0]][twin[1]] = prev_value + 1 if prev_value is not None else 1
      done_cells.add(twin)
  return mat


print(compress_2d(
  [[1, 50],
   [51, 100]]
))

print(compress_2d(
  [[10, 30, 20]]
))

print(compress_2d(
  [[10, 30, 20, 30, 40]]
))
