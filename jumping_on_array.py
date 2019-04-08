from typing import List


def num_ways_to_jump(array_length: int, jumps: List[int]):
  num_ways = [0]*array_length
  num_ways[0] = 1
  for i in range(array_length):
    for jump in jumps:
      if i - jump >= 0:
        num_ways[i] += num_ways[i-jump]
  return num_ways[-1]


# Test.
for jumps in [[1,2], [1,2,3], [2,3]]:
  print('jumps:', jumps)
  for i in range(1, 10):
    print('array of size {} has {} ways to jump.'.format(
        i, num_ways_to_jump(i, jumps)))


def ways_to_jump(location: int, jumps: List[int]):
  if location == 0:
    yield ['Done']
    return
  for jump in jumps:
    if location - jump >= 0:
      for tail_ways in ways_to_jump(location - jump, jumps):
        yield [location - jump] + tail_ways


# Test.
for jumps in [[1,2], [1,2,3], [2,3]]:
  print('jumps:', jumps)
  for i in range(1, 10):
    print('ways to jump from {}'.format(i))
    for way in ways_to_jump(i, jumps):
      print('\t', way)
