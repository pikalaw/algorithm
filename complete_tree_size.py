
class Node(object):
  def __init__(self):
    self.left = None
    self.right = None
    self.index = None


def print_tree(root):
  if not root:
    print('<empty tree>')
    return
  row = [root]
  next_row = []
  while row:
    for node in row:
      print(node.index, end=' ')
      if node.left:
        next_row.append(node.left)
      if node.right:
        next_row.append(node.right)
    print()
    row = next_row
    next_row = []


def complete_tree(size):
  def _ct(node_index, size):
    if node_index > size:
      return None
    node = Node()
    node.index = node_index
    if node_index * 2 <= size:
      node.left = _ct(node_index * 2, size)
    if node_index * 2 + 1 <= size:
      node.right = _ct(node_index * 2 + 1, size)
    return node
  return _ct(1, size)


def exists(root, n):
  path = []
  while n > 1:
    if n % 2 == 0:
      path.append('L')
    else:
      path.append('R')
    n = int(n/2)
  node = root
  for direction in reversed(path):
    if direction == 'L':
      node = node.left
    else:
      node = node.right
    if not node:
      return False
  return True


tree_10 = complete_tree(10)
print_tree(tree_10)

print(exists(tree_10, 1))
print(exists(tree_10, 5))
print(exists(tree_10, 10))
print(exists(tree_10, 11))
print(exists(tree_10, 20))
print(exists(tree_10, 2000))


def complete_tree_size(root):
  if not root:
    return 0
  num_level = 0
  node = root
  while node.left:
    node = node.left
    num_level += 1
  left = 2**(num_level)
  right = 2**(num_level+1)
  while True:
    mid = int((left + right) / 2)
    if exists(root, mid):
      if exists(root, mid+1):
        left = mid + 1
      else:
        return mid
    else:
      right = mid


for s in [0,1,2,3,4,5]:
  t = complete_tree(s)
  print('Tree')
  print_tree(t)
  print('is of size {}'.format(complete_tree_size(t)))
