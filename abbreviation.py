"""Abbreviate words like this:

aaaa -> 4xa
"""

def ForceAbbrevaiteHead(original_string, start_index):
  assert start_index < len(original_string)

  first_char = original_string[start_index]
  first_char_last_index = start_index
  for i in xrange(start_index + 1, len(original_string)):
    if original_string[i] != first_char:
      break
    first_char_last_index += 1

  token_length = first_char_last_index - start_index + 1
  return '{}x{}'.format(token_length, first_char), first_char_last_index+1
  

def _Abbreviate(original_string, start_index):
  if start_index >= len(original_string):
    return False, ''

  v1_head = original_string[start_index]
  v1_tail_is_abbreviated, v1_tail = _Abbreviate(
      original_string, start_index+1)
  if (v1_head in '0123456789' and
      (v1_tail_is_abbreviated or v1_tail and v1_tail[0] == 'x')):
    v1 = None
  else:
    v1 = v1_head + v1_tail

  v2_head, tail_index = ForceAbbrevaiteHead(original_string, start_index)
  v2_tail_is_abbreviated, v2_tail =  _Abbreviate(
      original_string, tail_index)
  v2 = v2_head + v2_tail

  if not v1:
    return True, v2
  elif len(v1) <= len(v2):
    return False, v1
  else:
    return True, v2

  
def Abbreviate(original_string):
  _, abbreviated = _Abbreviate(original_string, 0)
  return abbreviated
  

import unittest


class TestAbbreviate(unittest.TestCase):
  def test_Abbreviate(self):
    self.assertEqual('', Abbreviate(''))
    self.assertEqual('a', Abbreviate('a'))
    self.assertEqual('aa', Abbreviate('aa'))
    self.assertEqual('aaa', Abbreviate('aaa'))
    self.assertEqual('4xa', Abbreviate('aaaa'))
    self.assertEqual('ab', Abbreviate('ab'))
    self.assertEqual('aab', Abbreviate('aab'))
    self.assertEqual('aaab', Abbreviate('aaab'))
    self.assertEqual('4xab', Abbreviate('aaaab'))

    self.assertEqual('x', Abbreviate('x'))
    self.assertEqual('1x1x', Abbreviate('1x'))
    self.assertEqual('1x11x2x', Abbreviate('12x'))
    self.assertEqual('xa', Abbreviate('xa'))
    self.assertEqual('1x1xa', Abbreviate('1xa'))
    self.assertEqual('1x11x2xa', Abbreviate('12xa'))

    self.assertEqual('1', Abbreviate('1'))
    self.assertEqual('11', Abbreviate('11'))
    self.assertEqual('111', Abbreviate('111'))
    self.assertEqual('4x1', Abbreviate('1111'))
    self.assertEqual('5x1', Abbreviate('11111'))
    self.assertEqual('2x14x2', Abbreviate('112222'))
    
    self.assertEqual('2x14x2x', Abbreviate('112222x'))
