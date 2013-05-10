
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
