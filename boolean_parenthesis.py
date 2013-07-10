
def MaxParenthesis(tokens):
  num_tokens = len(tokens)
  ans = [[None for _ in xrange(num_tokens+1)] for _ in xrange(num_tokens+1)]
  count, _ = _MaxParenthesis(tokens, ans, 0, num_tokens)
  return count


def _MaxParenthesis(tokens, ans, i, j):
  assert i < j, 'i={}, j={}'.format(i, j)

  # Memorized case.
  if ans[i][j] is not None:
    return ans[i][j]

  # Base case.
  if j - i == 1:
    assert tokens[i] in ['true', 'false']
    ans[i][j] = (1,0) if tokens[i] == 'true' else (0,1)
    return ans[i][j]

  # Recursion case.
  max_true_count, max_false_count = 0, 0
  for k in xrange(i, j):
    token = tokens[k]
    if token in ['and', 'or', 'xor']:
      left_true_count, left_false_count = _MaxParenthesis(tokens, ans, i, k)
      right_true_count, right_false_count = _MaxParenthesis(tokens, ans, k+1, j)

      if token == 'and':
        true_count = left_true_count * right_true_count
        false_count = (
            left_false_count * (right_true_count + right_false_count) +
            right_false_count * (left_true_count + left_false_count))
      elif token == 'or':
        true_count = (
            left_true_count * (right_true_count + right_false_count) +
            right_true_count * (left_true_count + left_false_count))
        false_count = left_false_count * right_false_count
      elif token == 'xor':
        true_count = (left_true_count * right_false_count +
            right_true_count * left_false_count)
        true_count = (left_true_count * right_true_count +
            right_false_count * left_false_count)

      if true_count > max_true_count:
        max_true_count = true_count
        max_false_count = false_count

  ans[i][j] = (true_count, false_count)
  return true_count, false_count


import unittest


class TestMaxParenthesis(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(1, MaxParenthesis(['true']))
    self.assertEqual(0, MaxParenthesis(['false']))
    self.assertEqual(1, MaxParenthesis(['true', 'and', 'true']))
    self.assertEqual(0, MaxParenthesis(['true', 'and', 'false']))
    self.assertEqual(1, MaxParenthesis(['true', 'or', 'false']))
    self.assertEqual(1, MaxParenthesis(['true', 'or', 'false', 'and', 'true']))
    self.assertEqual(2, MaxParenthesis(['true', 'or', 'false', 'or', 'true']))
