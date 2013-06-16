import random


class Maze(object):

  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.nodes = [[[] for _ in xrange(columns)] for _ in xrange(rows)]
    self.entrance = (0, 0)
    self.exit = (None, None)
    self.exit_distance = 0

  def Link(self, from_node, to_node):
    self.nodes[from_node[0]][from_node[1]].append(to_node)
    self.nodes[to_node[0]][to_node[1]].append(from_node)

  def __str__(self):
    s = []
    for i in xrange(self.rows):
      for j in xrange(self.columns):
        s.append('({}, {}) -> {}'.format(i, j, self.nodes[i][j]))
    return '\n'.join(s)


def GenerateMaze(rows, columns):
  """Generate a maze of size rows by columns."""
  maze = Maze(rows, columns)
  visited = [[False for _ in xrange(columns)] for _ in xrange(rows)]
  DFS(maze.entrance, visited, maze, 1)
  return maze


def DFS(node, visited, maze, depth):
  # Check for possible exit.
  if NodeIsAtEdgeOfMaze(node, maze):
    if depth > maze.exit_distance:
      maze.exit_distance = depth
      maze.exit = node

  visited[node[0]][node[1]] = True
  deltas = [(1,0), (-1,0), (0,1), (0,-1)]
  random.shuffle(deltas)
  for delta in deltas:
    next_node = (node[0] + delta[0], node[1] + delta[1])
    if InMaze(next_node, maze) and not visited[next_node[0]][next_node[1]]:
      maze.Link(node, next_node)
      DFS(next_node, visited, maze, depth + 1)


def InMaze(node, maze):
  return 0 <= node[0] < maze.rows and 0 <= node[1] < maze.columns


def NodeIsAtEdgeOfMaze(node, maze):
  return (node[0] == 0 or node[0] == maze.rows - 1 or
          node[1] == 0 or node[1] == maze.columns)


import unittest


class TestMaze(unittest.TestCase):

  def test_Example(self):
    maze = GenerateMaze(10, 10)
    print
    print maze
    print 'exit {}, distance {}'.format(maze.exit, maze.exit_distance)
