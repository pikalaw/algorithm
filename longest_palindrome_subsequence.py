
class Result(object):

  def __init__(self, max_length, new_letter, previous_result=None):
    self.max_length = max_length
    self.new_letter = new_letter
    self.previous_result = previous_result


def LongestPalindromeSubsequence(word):
  # Bottom-up dynamic programming.
  results = [[None for _ in range(len(word)+1)] for _ in range(len(word)+1)]
  for length in range(len(word) + 1):
    for i in range(len(word) - length + 1):
      j = i + length
      if j == i:
        results[i][j] = Result(0, '')
      elif j - i == 1:
        results[i][j] = Result(1, word[i])
      else:
        if word[i] == word[j-1]:
          results[i][j] = Result(
              results[i+1][j-1].max_length + 2, word[i], results[i+1][j-1])
        elif results[i+1][j].max_length > results[i][j-1].max_length:
          results[i][j] = Result(
              results[i+1][j].max_length, '', results[i+1][j])
        else:
          results[i][j] = Result(
              results[i][j-1].max_length, '', results[i][j-1])

  return ConstructSolution(results)


def ConstructSolution(results):
  # Reconstruct the solution.
  result = results[0][-1]
  solution = result.new_letter
  while result.previous_result:
    result = result.previous_result  
    solution += result.new_letter

  if result.max_length == 0:
    return solution + solution[::-1]
  else:
    return solution[:-1] + solution[-1] + solution[-2::-1]


def RecursiveLongestPalindromeSubsequence(word):
  # Meorized version.
  results = [[None for _ in range(len(word)+1)] for _ in range(len(word)+1)]
  _RecursiveLongestPalindromeSubsequence(word, 0, len(word), results)
  return ConstructSolution(results)


def _RecursiveLongestPalindromeSubsequence(word, i, j, results):
  # Meorized case.
  if results[i][j]:
    return results[i][j]

  # Base case.
  if i == j:
    results[i][j] = Result(0, '')
    return results[i][j]
  if j - i == 1:
    results[i][j] = Result(1, word[i])
    return results[i][j]

  # Recursion case.
  if word[i] == word[j-1]:
    mid_result = _RecursiveLongestPalindromeSubsequence(
        word, i+1, j-1, results)
    results[i][j] = Result(mid_result.max_length + 2, word[i], mid_result)
    return results[i][j]

  left_result = _RecursiveLongestPalindromeSubsequence(
      word, i, j-1, results)
  right_result = _RecursiveLongestPalindromeSubsequence(
      word, i+1, j, results)
  if left_result.max_length > right_result.max_length:
    results[i][j] = Result(left_result.max_length, '', left_result)
    return results[i][j]
  else:
    results[i][j] = Result(right_result.max_length, '', right_result)
    return results[i][j]


import unittest


class TestLongestPalindromeSubsequence(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(
        'aba',
        LongestPalindromeSubsequence('aba'))
    self.assertEqual(
        'carac',
        LongestPalindromeSubsequence('character'))
    self.assertEqual(
        '',
        LongestPalindromeSubsequence(''))
    self.assertEqual(
        'a',
        LongestPalindromeSubsequence('a'))
    self.assertEqual(
        'aa',
        LongestPalindromeSubsequence('aa'))
    self.assertEqual(
        'aaa',
        LongestPalindromeSubsequence('aaa'))

  def test_Recursive(self):
    self.assertEqual(
        'aba',
        RecursiveLongestPalindromeSubsequence('aba'))
    self.assertEqual(
        'carac',
        RecursiveLongestPalindromeSubsequence('character'))
    self.assertEqual(
        '',
        RecursiveLongestPalindromeSubsequence(''))
    self.assertEqual(
        'a',
        RecursiveLongestPalindromeSubsequence('a'))
    self.assertEqual(
        'aa',
        RecursiveLongestPalindromeSubsequence('aa'))
    self.assertEqual(
        'aaa',
        RecursiveLongestPalindromeSubsequence('aaa'))
