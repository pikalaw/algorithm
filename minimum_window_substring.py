def minWindow(s: str, t: str) -> str:
  solutions = []
  distinct_t = set(t)
  for i in range(len(s)):
    if s[i] in distinct_t:
      found = set()
      for j in range(i, len(s)):
        if s[j] in distinct_t:
          found.add(s[j])
          if len(found) == len(distinct_t):
            solutions.append(s[i:j+1])
            break

  print('All solutions {}'.format(solutions))

  min_solution = s
  for solution in solutions:
    if len(solution) < len(min_solution):
      min_solution = solution
  return min_solution


print(minWindow("ADOBECODEBANC", "ABC"))
