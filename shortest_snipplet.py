import copy


def ShortestSnipplet(doc, words):
  word_locations = WordLocations(doc, words)
  block = []
  candidate = [('', 0), ('', len(doc))]
  for word, location in word_locations:
    block.append((word, location))
    NormalizeBlock(block)
    if HasAllWords(block, words) and BlockLen(block) < BlockLen(candidate):
      candidate = copy.deepcopy(block)
  return Snipplet(doc, candidate)


def WordLocations(doc, words):
  """Returns a list of (word, location) in order of `location`."""
  # TODO(pikalaw): Could improve running time.
  word_locations = []
  i = 0
  while i < len(doc):
    for word in words:
      if doc[i:i+len(word)] == word:
        word_locations.append((word, i))
        i += len(word)
        break
    else:
      i += 1
  return word_locations


def NormalizeBlock(block):
  while len(block) > 1 and block[-1][0] == block[0][0]:
    del block[0]


def HasAllWords(block, words):
  # TODO(pikalaw): Could improve running time.
  block_words = [word for word, _ in block]
  for word in words:
    if word not in block_words:
      return False
  else:
    return True


def BlockLen(block):
  return block[-1][1] - block[0][1]


def Snipplet(doc, block):
  if BlockLen(block) == len(doc):
    return ''
  else:
    return doc[block[0][1]:block[-1][1] + len(block[-1][0])]
  

import unittest


class TestShortestSnipplet(unittest.TestCase):

  def test_Example(self):
    doc = 'this is a test of cat and dog and many more cat and dog'
    self.assertEqual('test of cat and',
                     ShortestSnipplet(doc, ['test', 'cat', 'and']))
    self.assertEqual('cat and dog',
                     ShortestSnipplet(doc, ['cat', 'dog']))
    self.assertEqual('this is a test',
                     ShortestSnipplet(doc, ['test', 'this']))
    self.assertEqual('more cat and dog',
                     ShortestSnipplet(doc, ['more', 'cat', 'dog']))
    self.assertEqual('cat',
                     ShortestSnipplet(doc, ['cat']))
    self.assertEqual('',
                     ShortestSnipplet(doc, ['not-in-doc']))
    self.assertEqual('',
                     ShortestSnipplet(doc, []))
