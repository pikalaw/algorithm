import collections
import random

class Node(object):

  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value

  def DepthFirst(self, callback):
    if self.left:
      self.left.DepthFirst(callback)
    callback(self.value)
    if self.right:
      self.right.DepthFirst(callback)


class BinaryTree(object):

  def __init__(self, root=None):
    self.root = root

  def Insert(self, value):
    if not self.root:
      self.root = Node(value)
      return

    next_node = self.root
    while next_node:
      if value < next_node.value:
        if next_node.left:
          next_node = next_node.left
        else:
          new_node = next_node.left = Node(value)
          return
      else:
        if next_node.right:
          next_node = next_node.right
        else:
          new_node = next_node.right = Node(value)
          return

  def __str__(self):
    str = ''
    if not self.root:
      return str
    last_level = 0
    nodes = collections.deque([(last_level, None, self.root)])
    while nodes:
      level, parent_value, node = nodes.popleft()
      if level != last_level:
        str += '\n[{0}] '.format(level)
      str += '{0}:{1} '.format(parent_value, node.value)
      if node.left:
        nodes.append((level + 1, node.value, node.left))
      if node.right:
        nodes.append((level + 1, node.value, node.right))
      last_level = level
    return str
    
    
  def DepthFirst(self, callback):
    if self.root:
      self.root.DepthFirst(callback)


def Flatten(tree):
  vs = []
  tree.DepthFirst(lambda v: vs.append(v))
  return vs


def Treeify(xs):
  
  def ToNode(xs):
    # Base case.
    if len(xs) == 0:
      return None
    if len(xs) == 1:
      return Node(xs[0])

    # Induction case.
    mid = len(xs) / 2
    return Node(xs[mid], ToNode(xs[:mid]), ToNode(xs[mid+1:]))

  return BinaryTree(ToNode(xs))
  

def UnionList(xs, ys):
  zs = []
  i = j = 0
  while i < len(xs) and j < len(ys):
    if xs[i] < ys[j]:
      zs.append(xs[i])
      i += 1
    if xs[i] > ys[j]:
      zs.append(ys[j])
      j += 1
    else:
      zs.append(xs[j])
      i += 1
      j += 1
  while i < len(xs):
    zs.append(xs[i])
    i += 1
  while j < len(ys):
    zs.append(ys[j])
    j += 1
  return zs


def UnionTree(xs, ys):
  return Treeify(UnionList(Flatten(xs), Flatten(ys)))

  
def main():
  tree1 = BinaryTree()
  tree1.Insert(100)
  tree1.Insert(50)
  tree1.Insert(150)

  tree2 = BinaryTree()
  tree2.Insert(90)
  tree2.Insert(45)
  tree2.Insert(110)

  tree3 = UnionTree(tree1, tree2)

  print 'tree1 is {0}'.format(tree1)
  print
  print 'tree2 is {0}'.format(tree2)
  print
  print 'union tree is {0}'.format(tree3)
  print 'or {0}'.format(Flatten(tree3))

  tree = Treeify([int(random.uniform(0,1000)) for _ in xrange(100)])
  print
  print 'random tree:\n{0}'.format(tree)


if __name__ == '__main__':
  main()
