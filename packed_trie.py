
class TrieNode(object):

  def __init__(self):
    self.packed_path = ''
    self.next_letters = {}
    self.data = None

  def Find(self, string):
    if self.packed_path:
      if string.find(self.packed_path) == 0:
        if len(string) == len(self.packed_path):
          return self
        elif string[len(self.packed_path)] in self.next_letters:
          return self.next_letters[string[len(self.packed_path)]].Find(
              string[len(self.packed_path)+1:])
        else:
          return None
      else:
        return None
    else:
      return self.next_letters[string[0]].Find(string[1:])

  def Add(self, string):
    if len(self.packed_path) == 0 and len(self.next_letters) == 0:
      self.packed_path = string
      return

    largest_common_prefix = LargestCommonPrefix(self.packed_path, string)

    if largest_common_prefix != self.packed_path:
      old_packed_path = self.packed_path[len(largest_common_prefix):]

      node = TrieNode()
      node.Add(old_packed_path[1:])
      node.next_letters = self.next_letters

      self.packed_path = largest_common_prefix
      self.next_letters = {old_packed_path[0]: node}

    new_packed_path = string[len(largest_common_prefix):]
    if new_packed_path[0] not in self.next_letters:
      self.next_letters[new_packed_path[0]] = TrieNode()
    self.next_letters[new_packed_path[0]].Add(new_packed_path[1:])

  def __repr__(self):
    return '\n'.join(self.Lines())

  def Lines(self):
    lines = ['[{}]: {}'.format(self.packed_path, self.data)]
    for next_letter, next_node in self.next_letters.iteritems():
      letter_lines = next_node.Lines()
      lines.append('  {}:'.format(next_letter))
      lines.extend(['  '+line for line in letter_lines])
    return lines


def LargestCommonPrefix(a, b):
  i, j = 0, 0
  while i < len(a) and j < len(b) and a[i] == b[j]:
    i += 1
    j += 1
  return a[:i]


import unittest


class TestTrieNode(unittest.TestCase):

  def test_Example(self):
    root = TrieNode() 
    root.Add('facebook')
    root.Add('facelift')
    root.Add('facebookers')
    root.Add('google')
    print '\n', root
    node = root.Find('facelift')
    self.assertIsNotNone(node)
    node.data = 'Yea!'
    print '\n', root
