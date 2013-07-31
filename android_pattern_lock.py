
def PatternCount(num_dots):
  c, s, o = 1, 1, 1
  for _ in xrange(1, num_dots):
    c_ = 4 * s + o
    s_ = 4 * c + 2 * s + o
    o_ = 4 * c + 4 * s
    c, s, o = c_, s_, o_
  return 4 * c + 4 * s + o


import unittest


class TestPatternCount(unittest.TestCase):

  def test_Examples(self):
    tests = [(1, 9),
             (2, 56),
             (3, 360),
             (4, 2280),
             (5, 14544),
             (6, 92448),
             (7, 588672),
             (8, 3745152)]
    for num_dots, expected_count in tests:
      self.assertEqual(expected_count, PatternCount(num_dots))
