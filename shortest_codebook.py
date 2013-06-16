
def ShortestCodebook(digits):
  """Produce the shortest codebook for codes of a fixed number of  digits.

  Args:
    digits: Number of digits in each code.

  Returns:
    Shortest codebook.
  """
  num_codes = 10**digits
  root = 0
  visited = [False for _ in xrange(num_codes)]
  codebook = [0] * (digits-1) + DFS(root, visited, 0, num_codes)
  return ''.join([str(x) for x in codebook])


def DFS(code, visited, num_codes_reached, num_codes):
  num_codes_reached += 1
  if num_codes_reached == num_codes:
    return [code % 10]

  visited[code] = True
  for next_code in AdjacentCodes(code, num_codes):
    if not visited[next_code]:
      codebook = DFS(next_code, visited, num_codes_reached, num_codes)
      if codebook is not None:
        return [code % 10] + codebook
  visited[code] = False
  return None


def AdjacentCodes(code, num_codes):
  base = (code % (num_codes / 10)) * 10 
  for i in range(10):
    yield base + i


import sys
import unittest


class TestShortestCodebook(unittest.TestCase):

  def VerifyAllCodes(self, codebook, digits):
    visited = [False for _ in xrange(10**digits)]
    i = 0
    while i + digits <= len(codebook):
      visited[int(codebook[i:i+digits])] = True
      i += 1
    for i, v in enumerate(visited):
      self.assertTrue(v, msg='{} is not in the codebook'.format(i))

  def test_Example(self):
    for digits in range(1, 5):
      sys.setrecursionlimit(10**digits + 1000)
      codebook = ShortestCodebook(digits)
      print '{} digits requires {} length codebook (first 100): {}'.format(
          digits, len(codebook), codebook[:100])
      self.assertEqual(10**digits + digits - 1, len(codebook))
      self.VerifyAllCodes(codebook, digits)
