"""Minimum path of letter replacements to translate from one string to another.

First solution is A*search.
Second solution is much faster and simpler.
"""

from typing import List, Set, Dict, Callable, TypeVar, Tuple
import string


T = TypeVar('T')


class PathData(object):
  def __init__(self, parent: T, pre_dist: int):
    # The parent of this node on the shortest path so far.
    self.parent = parent
    # The distance from start to this node on the shortest path so far.
    self.pre_dist = pre_dist


class PendingData(object):
  def __init__(self, node: T, post_dist: int):
    # Node pending for expansion.
    self.node = node
    # A*Search heuristic distance from this node to the end.
    self.post_dist = post_dist


def retrace_path(paths: PathData, end: T) -> List[T]:
  """Shortest path from start to end given the computation from A*Search."""
  route = [end]
  node = end
  while True:
    parent = paths[node].parent
    if not parent:
      return route
    route.insert(0, parent)
    node = parent


def update_pending(pending: List[PendingData], node: T, post_dist: int) -> None:
  """Add a newly discovered node for expansion later."""
  i = 0
  while i < len(pending):
    if pending[i].post_dist >= post_dist:
      break
    i += 1
  pending.insert(i, PendingData(node, post_dist))


def update_paths(
    paths: Dict[T, PathData], parent: T, child: T, edge_dist: int) -> None:
  """Update the shortest paths given a new found edge."""
  new_pre_dist = (paths[parent].pre_dist if parent in paths else 0) + edge_dist
  if child not in paths:
    paths[child] = PathData(parent, new_pre_dist)
  elif paths[child].pre_dist > new_pre_dist:
    paths[child].parent = parent
    paths[child].pre_dist = new_pre_dist


def a_star_search(
    start: T, end: T, expand: Callable[[T], List[Tuple[T,int]]],
    a_star_distance: Callable[[T, T], int]):
  """Generic A*Search from start to end."""
  paths = {start: PathData(parent=None, pre_dist=0)}
  expanded: Set[T] = set()
  pending = [PendingData(node=start, post_dist=a_star_distance(start, end))]

  num_explored = 0
  while pending:
    parent = pending.pop(0).node
    num_explored += 1
    if parent == end:
      return retrace_path(paths, end), num_explored

    for child, dist in expand(parent):
      if child in expanded:
        continue
      update_pending(pending, child, a_star_distance(child, end))
      update_paths(paths, parent, child, dist)

    expanded.add(parent)

  # Could not find a path.
  return [], 0


def substitute(node: str, original_letter: str, new_letter: str) -> str:
  return node.replace(original_letter, new_letter)


def letter_set(node: str) -> Set[str]:
  return set(list(node))


def my_expand(node: str) -> List[Tuple[str, int]]:
  """Find all possible transformed string over a single substitution."""
  children = []
  for original_letter in letter_set(node):
    for new_letter in string.ascii_lowercase:
      if new_letter == original_letter:
        continue
      children.append((substitute(node, original_letter, new_letter), 1))
  return children


def my_a_star_distance(a: str, b: str) -> int:
  """Heuristic distance function for the letter substitution graph."""
  assert len(a) == len(b)
  return sum(c != d for c, d in zip(a, b))


# Tests.
tests = [
    ('a', 'b'),
    ('ab', 'ba'),
    ('abc', 'ccc'),
    ('abc', 'bca'),
    ('abc', 'baa'),
    ('aab', 'abc'),
]

for start, end in tests:
  path, num_explored = a_star_search(start, end, my_expand, my_a_star_distance)
  if path:
    print('{} -> {} needs {} steps {}, explored {} nodes'.format(
      start, end, len(path) - 1, path, num_explored))
  else:
    print('{} -> {} is impossible.'.format(start, end))


