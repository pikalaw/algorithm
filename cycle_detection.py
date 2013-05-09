
class Node(object):

  def __init__(self, id):
    self.id = id
    self.next = None

def BuildChain(ids, loop_at_id):
  first_node = Node(ids[0])
  this_node = first_node
  loop_node = first_node if ids[0] == loop_at_id else None

  for id in ids[1:]:
    this_node.next = Node(id)
    this_node = this_node.next
    if id == loop_at_id:
      loop_node = this_node

  # last node to loop back.
  this_node.next = loop_node

  return first_node 


def AdvanceNode(node, steps):
  while steps:
    node = node.next
    steps -= 1
  return node


def DetectCycle(head_node):
  # Find first collision.
  fast_runner = slow_runner = head_node
  while True:
    fast_runner = AdvanceNode(fast_runner, 2)
    slow_runner = AdvanceNode(slow_runner, 1)
    if fast_runner == None:
      return None
    if fast_runner == slow_runner:
      break

  # Find Cycle entry point.
  fast_runner = head_node
  while fast_runner != slow_runner:
    fast_runner = AdvanceNode(fast_runner, 1)
    slow_runner = AdvanceNode(slow_runner, 1)
  return fast_runner


import unittest


class TestDetectCycle(unittest.TestCase):

  def setUp(self):
    self.longMessage = True

  def test_Example(self):
    CYCLE_SIZE = 6
    for i in xrange(CYCLE_SIZE):
      path = BuildChain(range(CYCLE_SIZE), i)
      cycle_entry = DetectCycle(path)
      self.assertIsNotNone(cycle_entry, msg='{}'.format(i))
      self.assertEqual(i, cycle_entry.id, msg=i)

  def test_NoLoop(self):
    path = BuildChain(range(10), 99)
    cycle_entry = DetectCycle(path)
    self.assertIsNone(cycle_entry)
