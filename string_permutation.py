
def StringPermutation(string, visit):
  _StringPermutation(list(string), visit, 0)


def _StringPermutation(string, visit, i):
  if i == len(string):
    visit(''.join(string))
  else:
    prior_character = None
    for j in xrange(i, len(string)):
      if prior_character != string[j]:
        Swap(string, i, j)
        _StringPermutation(string, visit, i + 1)
        Swap(string, i, j)
        prior_character = string[j]
    

def Swap(a, i, j):
  t = a[i]
  a[i] = a[j]
  a[j] = t


import mox
import unittest


class TestStringPermutation(unittest.TestCase):

  def test_Unique(self):
    test_string = 'abc'

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__('abc')
    mock_visit.__call__('acb')
    mock_visit.__call__('bac')
    mock_visit.__call__('bca')
    mock_visit.__call__('cba')
    mock_visit.__call__('cab')
    m.ReplayAll()

    StringPermutation(test_string, mock_visit)
    m.VerifyAll()

  def test_Duplicate(self):
    test_string = 'aac'

    m = mox.Mox()
    mock_visit = m.CreateMockAnything()
    mock_visit.__call__('aac')
    mock_visit.__call__('aca')
    mock_visit.__call__('caa')
    m.ReplayAll()

    StringPermutation(test_string, mock_visit)
    m.VerifyAll()
