def assign_inequality(n, s):
  """Assign a list of numbers interleaving another list of inequality signs.

  Args:
    n: list of numbers
    s: list of chars '<' or '>'

  Returns:
    a list of reordered numbers that will interleave into the signs logically.
  """
  assert len(n) == len(s) + 1
  n.sort()
  i, j = 0, len(n) - 1
  k = 0
  y = []
  while i < j:
    if s[k] == '<':
      y.append(n[i])
      i += 1
    else:
      y.append(n[j])
      j -= 1
    k += 1
  y.append(n[i])
  return y


import itertools
import random
import unittest


def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = itertools.tee(iterable)
  next(b, None)
  return itertools.izip(a, b)


def print_chain(n, s):
  first = True
  for (x, y), c in zip(pairwise(n), s):
    if first:
      print x,
      first = False
    print c, y,
  print


class TestAssign(unittest.TestCase):

  def test_fix(self):
    self.assertEqual([1, 2, 3], assign_inequality([1, 2, 3], ['<', '<']))
    self.assertEqual([3, 2, 1], assign_inequality([1, 2, 3], ['>', '>']))
    self.assertEqual([1, 3, 2], assign_inequality([1, 2, 3], ['<', '>']))
    self.assertEqual([3, 1, 2], assign_inequality([1, 2, 3], ['>', '<']))

  def test_random(self):
    n = range(45)
    for _ in range(1000):
      s = ['<' if random.random() < .5 else '>' for _ in range(len(n) - 1)]
      m = assign_inequality(n, s)
      for (x, y), c in zip(pairwise(m), s):
        if c == '<':
          self.assertLess(x, y)
        elif c == '>':
          self.assertGreater(x, y)
        else:
          assert False, 'Bad comparitor {}'.format(c)
      print_chain(m, s)
