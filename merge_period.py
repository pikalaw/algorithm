class Period(object):
  def __init__(self, start, end, status):
    self.start = start
    self.end = end
    self.status = status

  def __repr__(self):
    return '({}, {}) -> {}'.format(self.start, self.end, self.status)


def boundaries(ts):
  assert len(ts) > 0
  b = [(ts[0].start, None)]
  for t in ts:
    b.append((t.end, t.status))
  return b


def merge_timelines(ts1, ts2, merge):
  merged = []
  bs1 = boundaries(ts1)
  bs2 = boundaries(ts2)
  last_boundary = float('-inf')
  i1 = i2 = 0
  while i1 < len(bs1) and i2 < len(bs2):
    if bs1[i1][0] < bs2[i2][0]:
      merged.append(Period(last_boundary, bs1[i1][0], merge(bs1[i1][1], bs2[i2][1])))
      last_boundary = bs1[i1][0]
      i1 += 1
    elif bs1[i1][0] > bs2[i2][0]:
      merged.append(Period(last_boundary, bs2[i2][0], merge(bs1[i1][1], bs2[i2][1])))
      last_boundary = bs2[i2][0]
      i2 += 1
    else:
      merged.append(Period(last_boundary, bs2[i2][0], merge(bs1[i1][1], bs2[i2][1])))
      last_boundary = bs1[i1][0]
      i1 += 1
      i2 += 1
  while i1 < len(bs1):
    merged.append(Period(last_boundary, bs1[i1][0], merge(bs1[i1][1], None)))
    last_boundary = bs1[i1][0]
    i1 += 1
  while i2 < len(bs2):
    merged.append(Period(last_boundary, bs2[i2][0], merge(None, bs2[i2][1])))
    last_boundary = bs2[i1][0]
    i2 += 1
  return merged[1:]


def And(a, b):
  if a is not None and b is not None:
    return a and b
  elif a is not None:
    return a
  elif b is not None:
    return b
  else:
    return None


m = merge_timelines(
    [Period(1, 3, True), Period(3, 5, False), Period(5, 7, True), Period(7, 9, False),],
    [Period(2, 4, True), Period(4, 6, False), Period(6, 8, True),],
    And)
print(m)
