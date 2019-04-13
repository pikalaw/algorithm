from collections import defaultdict


def _compute_bag(word):
  bag = defaultdict(int)
  for letter in word:
    bag[letter] += 1
  return bag


def _match_bags(from_bag, to_bag):
  match_count = 0
  for letter in from_bag:
    if letter in to_bag and from_bag[letter] == to_bag[letter]:
      match_count += 1
  return match_count


def find_permutated(text, word):
  if len(text) < len(word):
    return
  # Setup the invariants.
  head, tail = 0, len(word) - 1
  word_bag = _compute_bag(word)
  text_bag = _compute_bag(text[head:(tail+1)])
  num_word_bag_matched = _match_bags(word_bag, text_bag)
  if num_word_bag_matched == len(word_bag):
    yield head

  # Begin.
  while tail < len(text) - 1:
    # Lose the left character.
    if text[head] in word_bag:
      if text_bag[text[head]] == word_bag[text[head]]:
        num_word_bag_matched -= 1
      text_bag[text[head]] -= 1
      if text_bag[text[head]] == word_bag[text[head]]:
        num_word_bag_matched += 1
    head += 1

    # Gain the right character.
    tail += 1
    if text[tail] in word_bag:
      if text_bag[text[tail]] == word_bag[text[tail]]:
        num_word_bag_matched -= 1
      text_bag[text[tail]] += 1
      if text_bag[text[tail]] == word_bag[text[tail]]:
        num_word_bag_matched += 1

    if num_word_bag_matched == len(word_bag):
      yield head


for test_input in [
    ('dacbeacfabc', 'abc'),
    ('d', 'abc'),
    ('xyzzzz', 'abc'),
    ('abcba', 'abc'),
  ]:
  text, word = test_input
  print('\n{} in {}'.format(word, text))
  for i in find_permutated(text, word):
    print('FOUND AT', i)
