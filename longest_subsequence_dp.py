def longest_subsequence(a, b):
  if len(a) < len(b):
    b, a = a, b
  ls = [''] * (len(b) + 1)
  for i in range(len(a) + 1):
    new_ls = [''] * (len(b) + 1)
    for j in range(1, len(b) + 1):
      if a[i-1] == b[j-1]:
        new_ls[j] = ls[j-1] + a[i-1]
      else:
        c1 = ls[j]
        c2 = new_ls[j-1]
        new_ls[j] = c1 if len(c1) > len(c2) else c2
    ls = new_ls
  return ls[len(b)]


import unittest


class TestLongestSubsequence(unittest.TestCase):
  def test_example(self):
    for test_case in [
        ('ADH', 'ABCDGH', 'AEDFHR'),
        ('GTAB', 'AGGTAB', 'GXTXAYB'),
      ]:
      expected, a, b = test_case
      self.assertEqual(expected, longest_subsequence(a, b))
