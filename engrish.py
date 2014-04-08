#!/usr/bin/env python

import collections
import itertools
import random
import re
import urllib2


def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = itertools.tee(iterable)
  next(b, None)
  return itertools.izip(a, b)


def WebPageLines(url):
  for line in urllib2.urlopen(url):
    yield line


def WordSequence(lines):
  """Return a list of words and punctuations ',.!?; in order of the text.
  
  Args:
    url: Source of text.
    
  Returns:
    See description.
  """
  irrelevant_char_re = re.compile(r"[^a-zA-Z'\s,.!?;]")
  word_boundary_re = re.compile(r"[\w']+|[.,!?;]")
  for line in lines:
    clean_line = irrelevant_char_re.sub('', line)
    for word in word_boundary_re.findall(clean_line):
      if len(word):
        yield word


def BuildProb(word_sequence):
  """Compute conditional probability of a char given another from word seq.

  Args:
    word_sequence: List of words and punctuations in order.

  Returns:
    2-D dict A so that A[x][y] = P(y|x).
  """
  p = collections.defaultdict(lambda: collections.defaultdict(int))
  for pre_word, post_word in pairwise(word_sequence):
    p[pre_word][post_word] += 1
  return p


def RandomWordAfter(word, prob):
  if word not in prob:
    return None
  next_word_prob = prob[word]

  total = sum([count for count in next_word_prob.itervalues()])
  choice = random.randint(1, total)
  cumm = 0

  for next_word, count in next_word_prob.iteritems():
    cumm += count
    if choice <= cumm:
      return next_word
  assert False, 'WTF!'


def JoinSentence(words):
  return ' '.join(words)  


def EngrishSentence(prob, end_of_sentence_chars):
  words = []
  current_word = '.'
  while not words or end_of_sentence_chars.find(current_word) == -1:
    next_word = RandomWordAfter(current_word, prob)
    if not next_word:
      break
    words.append(next_word)
    current_word = next_word
  return words


def EngrishEssay(prob, num_words=100):
  num_words_generated = 0
  end_of_sentence_chars = '.?!'
  while num_words_generated < num_words:
    words = EngrishSentence(prob, end_of_sentence_chars)
    num_words_generated += len(words)
    yield JoinSentence(words)

  
def main():
  text_url = 'http://www.gutenberg.org/files/45343/45343-0.txt'
  text_file = 'great_expectation.txt'
  with open(text_file) as f:
    prob = BuildProb(WordSequence(f))
  for line in EngrishEssay(prob, num_words=500):
    print line


if __name__ == '__main__':
  main()
