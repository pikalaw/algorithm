
def SolveHanoi(depth):
  """Solves a Hanoi Tower.

  Assumes starting position is in stack[0] and target is stack[1].
  So, stack[2] is the free stack space.

  Args:
    depth: Number of plate in the initial stack.

  Returns:
    List of moves of (from-stack, to-stack).
  """
  return _Hanoi(depth, 0, 1, 2)


def _Hanoi(depth, from_stack, to_stack, free_stack):
  # Base case.
  if depth == 1:
    return [(from_stack, to_stack)]

  # Recursion case.
  moves_a = _Hanoi(depth - 1, from_stack, free_stack, to_stack)

  permutation = [None] * 3
  permutation[from_stack] = free_stack
  permutation[free_stack] = to_stack
  permutation[to_stack] = from_stack

  moves_b = PermuteMoves(moves_a, permutation)

  return moves_a + [(from_stack, to_stack)] + moves_b


def PermuteMoves(moves, permutation):
  return [(permutation[i], permutation[j]) for i, j in moves]


import unittest


class HanoiBoard(object):

  def __init__(self, depth):
    self.depth = depth
    self.stacks = [range(depth - 1, -1, -1), [], []]

  def Move(self, from_stack, to_stack):
    if self.stacks[to_stack]:
      assert self.stacks[from_stack][-1] < self.stacks[to_stack][-1]
    self.stacks[to_stack].append(self.stacks[from_stack].pop())

  @property
  def done(self):
    return self.stacks[0] == [] and self.stacks[2] == []

  def __str__(self):
    return ('\t0: {}'.format(self.stacks[0]) +
            '\n\t1: {}'.format(self.stacks[1]) +
            '\n\t2: {}'.format(self.stacks[2]))


class TestHanoi(unittest.TestCase):

  def test_Example(self):
    for depth in xrange(1, 7):
      board = HanoiBoard(depth)
      print '\nStarting board\n{}'.format(board)

      for i, (from_stack, to_stack) in enumerate(SolveHanoi(depth)):
        board.Move(from_stack, to_stack)
        print 'Move #{}: {}->{}\n{}'.format(i + 1, from_stack, to_stack, board)

      self.assertTrue(board.done)
