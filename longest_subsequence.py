
def LongestSubsequence(a, b):
  subresults = [[None for _ in b] for _ in a]
  solution = InternalLongestSubsequence(a, b, len(a), len(b), subresults)
  print '{} vs {} subresults are {}'.format(a, b, PrettyPrint(subresults))
  return solution


def InternalLongestSubsequence(a, b, i, j, subresults):
  # Base case.
  if i <= 0 or j <= 0:
    return ''

  # Meorized case.
  if subresults[i-1][j-1] is not None:
    return subresults[i-1][j-1]

  # Recursion.
  if a[i-1] == b[j-1]:
    p = InternalLongestSubsequence(a, b, i-1, j-1, subresults) + a[i-1]
    subresults[i-1][j-1] = p
    return p
  else:
    p = InternalLongestSubsequence(a, b, i-1, j, subresults)
    q = InternalLongestSubsequence(a, b, i, j-1, subresults)
    if len(p) > len(q):
      subresults[i-1][j-1] = p
      return p
    else:
      subresults[i-1][j-1] = q
      return q


def PrettyPrint(m):
  s = '\n'
  for r in m:
    s += '{}\n'.format(r)
  return s


import unittest


class TestLongestSubsequence(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(
        'abc',
        LongestSubsequence('1a23b45c', '56a780b7698c233'))
    self.assertEqual(
        'abc',
        LongestSubsequence('abc', '56a780b7698c233'))
    self.assertEqual(
        'abc',
        LongestSubsequence('1a23b45c', 'abc'))
    self.assertEqual(
        'abc',
        LongestSubsequence('abc', 'abc'))

  def test_NoMatch(self):
    self.assertEqual('', LongestSubsequence('abc', ''))
    self.assertEqual('', LongestSubsequence('', 'abc'))
    self.assertEqual('', LongestSubsequence('', ''))
    self.assertEqual('', LongestSubsequence('abc', 'xyz'))
    
  def test_cormen_15_4_1(self):
    self.assertEqual('010101', LongestSubsequence('10010101', '010110110'))
