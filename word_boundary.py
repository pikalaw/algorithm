
def IsWord(word):
  return word in [
    'a',
    'am',
    'man',
    'is',
    'eats',
    'jumps',
    'the',
    'cow',
    'fence',
    'quietly',
  ]


def BreakWords(glob):
  """Break a string of characters, glob, into a list of words.

  Args:
    glob: A string of characters to be broken into words if possible.

  Returns:
    List of words if glob can be broken down. List can be empty if glob is ''.
    None if no such break is possible.
  """
  # Base case.
  if len(glob) == 0:
    return []

  # Find a partition.
  for i in xrange(1, len(glob) + 1):
    left = glob[:i]
    if IsWord(left):
      right = glob[i:]
      remaining_words = BreakWords(right)
      if remaining_words is not None:
        return [left] + remaining_words

  return None


import unittest


class TestBreakWords(unittest.TestCase):

  def test_Example(self):
    self.assertEqual(['a', 'man', 'jumps', 'the', 'fence'],
                     BreakWords('amanjumpsthefence'))
