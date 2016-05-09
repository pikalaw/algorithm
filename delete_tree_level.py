"""Delete a level of a BST.

Space requirement: 2N.
Running time: 2N.

TODO: Write an in-place version.

$ python delete_tree_level.py 
Orignal tree
                            19
            11                              27
       7            15              23              31
   3     9      13      17      21      25      29      33
 1   5  8 10  12  14  16  18  20  22  24  26  28  30  32  34
0 2 4 6

-------------------
Without level 0
                          18
          10                              27
      6           14              23              31
   3    8     12      16      21      25      29      33
 1   5 7 9  11  13  15  17  20  22  24  26  28  30  32  34
0 2 4

-------------------
Without level 1
                        18
         9                              26
     5          14              22              31
   3   7    12      16      20      24      29      33
 1  4 6 8 10  13  15  17  19  21  23  25  28  30  32  34
0 2

-------------------
Without level 2
                     17
       8                             26
   3         12              21              30
 1   5   10      14      19      24      28      33
0 2 4 6 9  11  13  16  18  20  22  25  27  29  32  34

-------------------
Without level 3
                      19
       8                              30
   4          14              24          32
 1   6    11      16      22      27    31  34
0 2 5 7 10  12  15  18  20  23  26  28

-------------------
Without level 4
               19
       11              27
   4       15      23      31
 2   7   13  17  21  25  29  33
0 3 6 9

-------------------
Without level 5
                        19
        11                              27
   7            15              23              31
 3   9      13      17      21      25      29      33
1 5 8 10  12  14  16  18  20  22  24  26  28  30  32  34
"""


class Node(object):
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right


def RootIndex(values, start, end):
  """Compute the index of the root of a complete BST.

  The values of the tree are from the sorted list `values` in [start, end).
  """
  num_values = end - start
  tree_size = 1
  level_size = 1
  while True:
    next_level_size = level_size * 2
    next_tree_size = tree_size + next_level_size
    if next_tree_size > num_values:
      break
    tree_size, level_size = next_tree_size, next_level_size
  left_over = num_values - tree_size
  return (start + int((tree_size - 1) / 2) +
          min(left_over, int(next_level_size / 2)))


def _CompleteTree(values, start, end):
  """Helper function to return the root node of a complete BST.

  The values of the tree are from the sorted list `values` in [start, end).
  """
  if start >= end:
    return None
  root_index = RootIndex(values, start, end)
  assert start <= root_index < end, 'start = {} root = {} end = {}'.format(
      start, root_index, end)
  return Node(values[root_index],
              _CompleteTree(values, start, root_index), 
              _CompleteTree(values, root_index + 1, end))


def CompleteTree(values):
  """Compute the complete BST from sorted list `values`."""
  return _CompleteTree(values, 0, len(values))


def InOrderDFS(node, level, process):
  """Generic algorithm to run a DFS."""
  if not node:
    return
  InOrderDFS(node.left, level + 1, process)
  process(node, level)
  InOrderDFS(node.right, level + 1, process)


def LinearizeTreeWithoutLevel(root, omit_level):
  """Compute a list of values from a BST without a level.

  The level is an index starting from 0 represeting the root level.
  """
  values = []
  def AppendIfNotAtLevel(node, level):
    if level != omit_level:
      values.append(node.value)
  InOrderDFS(root, 0, AppendIfNotAtLevel)
  return values


def DeleteTreeLevel(root, delete_level):
  """Compute a complete BST from a BST without a certain level.

  The level is an index starting from 0 represeting the root level.
  """
  return CompleteTree(LinearizeTreeWithoutLevel(root, delete_level))


def PrintBinaryTree(root):
  """Pretty print a BST."""
  rows = []
  seq = 0
  def PrintNode(node, level):
    nonlocal seq
    if len(rows) <= level:
      rows.extend([''] * (level - len(rows) + 1))
    if len(rows[level]) < seq:
      rows[level] += ' ' * (seq - len(rows[level]))
    node_value_str = str(node.value)
    rows[level] += node_value_str
    seq += len(node_value_str)
  InOrderDFS(root, 0, PrintNode)
  for row in rows:
    print(row)


# Main.
tree = CompleteTree(range(35))
print('Orignal tree')
PrintBinaryTree(tree)
for delete_level in range(6):
  print('\n-------------------\nWithout level {}'.format(delete_level))
  PrintBinaryTree(DeleteTreeLevel(tree, delete_level))
