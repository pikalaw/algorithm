from collections import defaultdict


def build_name_graph(N):
  last_name_map = defaultdict(list)
  name_graph = {}

  for name in N:
    first, last = name
    last_name_map[last].append(name)
    name_graph[name] = []

  for name in N:
    first, last = name
    for node in last_name_map[first]:
      name_graph[node].append(name)
  return name_graph


def dfs(name, name_graph, visited, visiting, unvisited, solutions):
  visiting.add(name)
  solutions[name] = [name]
  for next_name in name_graph[name]:
    if next_name in visiting:
      candidate_solution = [name]
    elif next_name in visited:
      candidate_solution = [name] + solutions[next_name]
    else:
      dfs(next_name, name_graph, visited, visiting, unvisited, solutions)
      candidate_solution = [name] + solutions[next_name]
    if len(candidate_solution) > len(solutions[name]):
      solutions[name] = candidate_solution
  visited.add(name)
  unvisited.remove(name)


def longest_name_chain(N):
  name_graph = build_name_graph(N)
  unvisited = set(name_graph.keys())
  visited = set()
  solutions = {}
  while unvisited:
    name = next(iter(unvisited))
    visiting = set()
    dfs(name, name_graph, visited, visiting, unvisited, solutions)
  max_solution = []
  for solution in solutions.values():
    if len(solution) > len(max_solution):
      max_solution = solution
  return max_solution


for test_input in [
    [('a', 'b'), ('b', 'c'), ('c', 'd'),],
    [('a', 'b'), ('b', 'c'), ('c', 'd'),('d','a')],
    [],
    [('a', 'b'), ('b', 'c'), ('d', 'e'),('e','f'),('f','g')],
    ]:
  solution = longest_name_chain(test_input)
  print('{} has longest chain {}'.format(test_input, solution))
