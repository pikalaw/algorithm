
def SolveSudoku(grid):
  """Solve a Sudoku.

  Args:
    grid: 9 by 9 array of values. Missing values are None.

  Returns:
    9 by 9 array of a solution. None if no solution.
  """
  solution = [[col for col in row] for row in grid]
  if _Solve(grid, solution, 0, 0):
    return solution
  else:
    return None


def _Solve(grid, solution, i, j):
  p, q = NextCell(i, j)
  candidates = CandidatesAt(solution, i, j)
  for candidate in candidates:
    solution[i][j] = candidate
    if p is None or _Solve(grid, solution, p, q):
      return True
  solution[i][j] = grid[i][j]
  return False


def NextCell(i, j):
  if j < 8:
    return i, j + 1
  else:
    if i < 8: 
      return i + 1, 0
    else:
      return None, None


def CandidatesAt(solution, i, j):
  if solution[i][j] is not None:
    return [solution[i][j]]

  c = [True for _ in range(9)]
  for k in range(9): 
    if solution[i][k] is not None:
      c[solution[i][k] - 1] = False
    if solution[k][j] is not None:
      c[solution[k][j] - 1] = False
  i_3 = i - i%3
  j_3 = j - j%3
  for p in range(3):
    for q in range(3):
      if solution[i_3+p][j_3+q] is not None:
        c[solution[i_3+p][j_3+q] - 1] = False
  return [h + 1 for h, v in enumerate(c) if v]


import unittest


class TestSolveSudoku(unittest.TestCase):

  def test_Example(self):
    grid = [
        [ 5, 3, None, None, 7, None, None, None, None ],
        [ 6, None, None, 1, 9, 5, None, None, None ],
        [ None, 9, 8, None, None, None, None, 6, None ],
        [ 8, None, None, None, 6, None, None, None, 3 ],
        [ 4, None, None, 8, None, 3, None, None, 1 ],
        [ 7, None, None, None, 2, None, None, None, 6 ],
        [ None, 6, None, None, None, None, 2, 8, None ],
        [ None, None, None, 4, 1, 9, None, None, 5 ],
        [ None, None, None, None, 8, None, None, 7, 9 ]
    ]
    self.assertEqual(
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]],
        SolveSudoku(grid))
