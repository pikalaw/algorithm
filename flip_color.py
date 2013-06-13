
def MinFlipColor(cards):
  """Find the minimum flips to produce an alternating color sequence.

  Args:
    cards: string of 'B' (black) and 'W' (white). 

  Returns:
    String of 1 and 0 where 1 = flip 0 = no flip. Same length as `cards`.
  """
  colors = 'BW'
  flips = [1 if color == colors[i % 2] else 0 for i, color in enumerate(cards)]
  return ''.join(
    ['1' if x else '0' for x in flips] if sum(flips) <= len(cards) / 2 else
    ['0' if x else '1' for x in flips])


import unittest


class TestFlipColor(unittest.TestCase):

  def test_Example(self):
    self.assertEqual('',
        MinFlipColor(''))
    self.assertEqual('0',
        MinFlipColor('B'))
    self.assertEqual('0',
        MinFlipColor('W'))
    self.assertEqual('01',
        MinFlipColor('WW'))
    self.assertEqual('10',
        MinFlipColor('BB'))
    self.assertEqual('010',
        MinFlipColor('WWW'))
    self.assertEqual('010',
        MinFlipColor('BBB'))
    self.assertEqual('0100',
        MinFlipColor('BBBW'))
    self.assertEqual('00000',
        MinFlipColor('WBWBW'))
    self.assertEqual('010101010',
        MinFlipColor('WWWWWWWWW'))
    self.assertEqual('1000011111001000000011100',
        MinFlipColor('BBWBWWBWBWWBBBWBWBWBBWBBW'))
