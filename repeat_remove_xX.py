
def IsXx(a, b):
  return a.lower() == b.lower() and (
      a.isupper() and b.islower() or
      b.isupper() and a.islower())


def remove(s):
  if len(s) <= 1:
    return s
  t = remove(s[1:])
  if IsXx(s[0], t[0]):
    return t[1:]
  else:
    return s[0] + t


def iter_remove(s):
  output = ''
  i = 0
  j = 1
  while j < len(s):
    if IsXx(s[i], s[j]):
      if i > 0:
        i -= 1
        j += 1
      else:
        i += 2
        j += 2
    else:
      output += s[i]
      i += 1
      j += 1
  if i < len(s):
    output += s[i]
  return output


for test in [
    'abcCkDdppGGa',
    'abCcBk',
  ]:
  print('{} -> {}'.format(test, remove(test)))
  print('{} -> {}'.format(test, iter_remove(test)))
