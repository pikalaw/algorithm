def one_item(s):
  item = ''
  i = 0
  while i < len(s):
    if s[i] == '{':
      break
    item += s[i]
    i += 1
  return [item], s[i:]


def one_brace(s):
  assert s[0] == '{'
  comma_delimited_list = ''
  num_open_brace = 1
  i = 1
  while i < len(s):
    next_char = s[i]
    i += 1
    if next_char == '{':
      num_open_brace += 1
    elif next_char == '}':
      num_open_brace -= 1
    if num_open_brace == 0:
      return comma_delimited_list.split(','), s[i:]
    comma_delimited_list += next_char
  raise 'No matching braces'


def one_section(s):
  assert len(s) > 0
  if s[0] == '{':
    return one_brace(s)
  else:
    return one_item(s)


def sectionize(s):
  sections = []
  while s:
    section, s = one_section(s)
    sections.append(section)
  return sections


def expand(sections):
  if not sections:
    return []
  if len(sections) == 1:
    for item in sections[0]:
      yield [item]
  else:
    for item in sections[0]:
      for tail in expand(sections[1:]):
        yield [item] + tail


for s in [
    'abc',
    'abc{def,123,4}xyz',
    'abc{def,123,4}xyz{1,2,3}t',
    ]:
  print('{} expands to'.format(s))
  sections = sectionize(s)
  for expansion in expand(sections):
    print('\t', ''.join(expansion))
