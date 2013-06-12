
def MinFlipColor(cards):
  """Find the minimum flips to produce an alternating color sequence.

  Args:
    cards: string of 'B' (black) and 'W' (white). 

  Returns:
    String of 1 and 0 where 1 = flip 0 = no flip. Same length as `cards`.
  """
  w = MinFlipWithStartColor(cards, 'W')
  b = MinFlipWithStartColor(cards, 'B')
  return ''.join([str(x) for x in (w if sum(w) < sum(b) else b)])


def FlipColor(color):
  return 'W' if color == 'B' else 'B'


def MinFlipWithStartColor(cards, start_color):
  flips = []
  color = start_color
  for card_color in cards:
    if card_color != color:
      flips.append(1)
    else:
      flips.append(0)
    color = FlipColor(color)
  return flips


import unittest


class TestFlipColor(unittest.TestCase):

  def test_Example(self):
    self.assertEqual('', MinFlipColor(''))
    self.assertEqual('0', MinFlipColor('B'))
    self.assertEqual('0', MinFlipColor('W'))
    self.assertEqual('10', MinFlipColor('WW'))
    self.assertEqual('01', MinFlipColor('BB'))
    self.assertEqual('010', MinFlipColor('WWW'))
    self.assertEqual('010', MinFlipColor('BBB'))
    self.assertEqual('0100', MinFlipColor('BBBW'))
    self.assertEqual('00000', MinFlipColor('WBWBW'))
    self.assertEqual('010101010', MinFlipColor('WWWWWWWWW'))
    self.assertEqual('1000011111001000000011100',
                     MinFlipColor('BBWBWWBWBWWBBBWBWBWBBWBBW'))
