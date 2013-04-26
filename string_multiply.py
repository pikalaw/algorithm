
m_table = {"00": "00", "01": "00", "02": "00", "03": "00", "04": "00",
           "05": "00", "06": "00", "07": "00", "08": "00", "09": "00",
           "10": "00", "11": "10", "12": "20", "13": "30", "14": "40",
           "15": "50", "16": "60", "17": "70", "18": "80", "19": "90",
           "20": "00", "21": "20", "22": "40", "23": "60", "24": "80",
           "25": "01", "26": "21", "27": "41", "28": "61", "29": "81",
           "30": "00", "31": "30", "32": "60", "33": "90", "34": "21",
           "35": "51", "36": "81", "37": "12", "38": "42", "39": "72",
           "40": "00", "41": "40", "42": "80", "43": "21", "44": "61",
           "45": "02", "46": "42", "47": "82", "48": "23", "49": "63",
           "50": "00", "51": "50", "52": "01", "53": "51", "54": "02",
           "55": "52", "56": "03", "57": "53", "58": "04", "59": "54",
           "60": "00", "61": "60", "62": "21", "63": "81", "64": "42",
           "65": "03", "66": "63", "67": "24", "68": "84", "69": "45",
           "70": "00", "71": "70", "72": "41", "73": "12", "74": "82",
           "75": "53", "76": "24", "77": "94", "78": "65", "79": "36",
           "80": "00", "81": "80", "82": "61", "83": "42", "84": "23",
           "85": "04", "86": "84", "87": "65", "88": "46", "89": "27",
           "90": "00", "91": "90", "92": "81", "93": "72", "94": "63",
           "95": "54", "96": "45", "97": "36", "98": "27", "99": "18"}


a_table = {"00": "00", "01": "10", "02": "20", "03": "30", "04": "40",
           "05": "50", "06": "60", "07": "70", "08": "80", "09": "90",
           "10": "10", "11": "20", "12": "30", "13": "40", "14": "50",
           "15": "60", "16": "70", "17": "80", "18": "90", "19": "01",
           "20": "20", "21": "30", "22": "40", "23": "50", "24": "60",
           "25": "70", "26": "80", "27": "90", "28": "01", "29": "11",
           "30": "30", "31": "40", "32": "50", "33": "60", "34": "70",
           "35": "80", "36": "90", "37": "01", "38": "11", "39": "21",
           "40": "40", "41": "50", "42": "60", "43": "70", "44": "80",
           "45": "90", "46": "01", "47": "11", "48": "21", "49": "31",
           "50": "50", "51": "60", "52": "70", "53": "80", "54": "90",
           "55": "01", "56": "11", "57": "21", "58": "31", "59": "41",
           "60": "60", "61": "70", "62": "80", "63": "90", "64": "01",
           "65": "11", "66": "21", "67": "31", "68": "41", "69": "51",
           "70": "70", "71": "80", "72": "90", "73": "01", "74": "11",
           "75": "21", "76": "31", "77": "41", "78": "51", "79": "61",
           "80": "80", "81": "90", "82": "01", "83": "11", "84": "21",
           "85": "31", "86": "41", "87": "51", "88": "61", "89": "71",
           "90": "90", "91": "01", "92": "11", "93": "21", "94": "31",
           "95": "41", "96": "51", "97": "61", "98": "71", "99": "81"}


def MultiplyR(a, b):
  # Base case of 1 digit by 1 digit.
  if len(a) == len(b) == 1:
    return m_table[a+b]

  mid_a = len(a) >> 1
  mid_b = len(b) >> 1 

  if len(a) == 1:
    return AddR(MultiplyR(a, b[:mid_b]), PowerR(MultiplyR(a, b[mid_b:]), mid_b))
  elif len(b) == 1:
    return AddR(MultiplyR(b, a[:mid_a]), PowerR(MultiplyR(b, a[mid_a:]), mid_a))
  else:
    return AddR(AddR(MultiplyR(a[:mid_a], b[:mid_b]),
                     PowerR(MultiplyR(a[mid_a:], b[:mid_b]), mid_a)),
                AddR(PowerR(MultiplyR(a[:mid_a], b[mid_b:]), mid_b),
                     PowerR(MultiplyR(a[mid_a:], b[mid_b:]), mid_a + mid_b)))


def AddR(a, b):
  answer = ""
  carry = False
  i = 0

  for i in xrange(max(len(a), len(b))):
    ai = a[i] if i < len(a) else "0"
    bi = b[i] if i < len(b) else "0"

    c = a_table[ai + bi]

    # Add from last carry if any.
    if carry:
      c = [z for z in c]
      c[0] = chr(ord(c[0]) + 1) 
      if c[0] > '9':
        c[0] = '0'
        c[1] = '1'

    answer += c[0]
    carry = c[1] == '1'

  # Last carry.
  if carry:
    answer += '1'

  return answer


def PowerR(a, p):
  return "0" * p + a


def Reverse(a):
  return a[::-1]


def TrimTrailingZero(a):
  for i in xrange(len(a) - 1, 0, -1):
    if a[i] != '0':
      return a[:i+1]
  return a[0]


def Multiply(a, b):
  return Reverse(TrimTrailingZero(MultiplyR(Reverse(a), Reverse(b))))


def Add(a, b):
  return Reverse(AddR(Reverse(a), Reverse(b)))


def main():
  for i in range(20):
    for j in range(20):
      print '{0} + {1} = {2}'.format(i, j, Add(str(i), str(j)))
      print '{0} * {1} = {2}'.format(i, j, Multiply(str(i), str(j)))


if __name__ == '__main__':
  main()


import itertools
import unittest


class TestUtil(unittest.TestCase):

  def test_TrimTrailingZero(self):
    self.assertEqual("0", TrimTrailingZero("0"))
    self.assertEqual("0", TrimTrailingZero("00"))
    self.assertEqual("0", TrimTrailingZero("000"))
    self.assertEqual("1", TrimTrailingZero("1"))
    self.assertEqual("1", TrimTrailingZero("10"))
    self.assertEqual("1", TrimTrailingZero("100"))


class TestAdd(unittest.TestCase):

  def test_ThreeDigit(self):
    for m, n in itertools.product(range(1000), range(1000)):
      p = Add(str(m), str(n))
      self.assertEqual(m + n, int(p), msg="{0} + {1} =? {2}".format(m, n, p))


class TestMultiply(unittest.TestCase):

  def test_ThreeDigit(self):
    for m, n in itertools.product(range(1000), range(1000)):
      p = Multiply(str(m), str(n))
      self.assertEqual(m * n, int(p), msg="{0} * {1} =? {2}".format(m, n, p))
