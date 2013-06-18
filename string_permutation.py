
def StringPermutation(s):
  for p in Permutation(list(s)):
    yield ''.join(p)


def Permutation(s):
  if len(s) <= 1:
    yield s
  else:
    for i in xrange(len(s)):
      Swap(s, 0, i)
      for p in Permutation(s[1:]):
        yield [s[0]] + p
      Swap(s, 0, i)
    

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
    expected = ['abb', 'abb', 'bab', 'bba', 'bba', 'bab'] 
    self.assertEqual(actual, expected)
