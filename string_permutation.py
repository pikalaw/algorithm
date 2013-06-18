
def StringPermutation(s):
  s = list(s)
  s.sort()
  for p in Permutation(s):
    yield ''.join(p)


def Permutation(s):
  # s must be sorted for duplicates to be ignored.
  if len(s) <= 1:
    yield s
  else:
    last = None
    for i in xrange(len(s)):
      if s[i] == last:
        continue
      Swap(s, 0, i)
      for p in Permutation(s[1:]):
        yield [s[0]] + p
      Swap(s, 0, i)
      last = s[i]
    

def Swap(a, i, j):
  t = a[i]
  a[i] = a[j]
  a[j] = t


import unittest


class TestStringPermutation(unittest.TestCase):

  def test_Unique(self):
    actual = list(StringPermutation('abc'))
    expected = ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
    self.assertEqual(actual, expected)

  def test_Duplicate(self):
    actual = list(StringPermutation('abb'))
    expected = ['abb', 'bab', 'bba'] 
    self.assertEqual(actual, expected)
