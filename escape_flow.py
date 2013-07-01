import itertools
from network_flow import NetworkFlow


def EscapeFlow(sources, grid_size):
  return BuildNetwork(sources, grid_size).MaximumFlow('s', 't') == len(sources)
  

def BuildNetwork(sources, grid_size):  
  network = NetworkFlow()

  # Internal grid.
  for i, j in itertools.product(xrange(grid_size[0]), xrange(grid_size[1])):
    network.Link((i, j, '+'), (i, j, '-'), 1)
    for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ii, jj = i + d[0], j + d[1]
      if InGrid((ii, jj), grid_size):
        network.Link((i, j, '-'), (ii, jj, '+'), 1)

  # Source.
  for source in sources:
    network.Link('s', (source[0], source[1], '+'), 1)

  # Sink.
  for i, j in itertools.product(xrange(grid_size[0]), xrange(grid_size[1])):
    if i == 0 or j == 0 or i == grid_size[0] - 1 or j == grid_size[1] - 1:
      network.Link((i, j, '-'), 't', 1)

  return network


def InGrid(point, grid_size):
  return 0 <= point[0] < grid_size[0] and 0 <= point[1] < grid_size[1]


import unittest


class TestEscapeFlow(unittest.TestCase):

  def test_Example(self):
    self.assertTrue(
        EscapeFlow(
            [(2,0),(1,1),(2,1),(3,1),(1,3),(2,3),(3,3),(1,5),(2,5),(3,5)],
            (6, 6)))

  def test_NoEscape(self):
    self.assertFalse(
        EscapeFlow(
            [(2,0),(1,1),(2,1),(3,1),(1,3),(2,3),(3,3),(1,5),(2,5),(3,5),(2,4)],
            (6, 6)))
