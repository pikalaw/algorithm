
class Result(object):

  def __init__(self, current_investment, previous_investment, payoff):
    self.current_investment = current_investment
    self.previous_investment = previous_investment
    self.payoff = payoff

  def __str__(self):
    return '[{}->{}:{}]'.format(
        self.previous_investment, self.current_investment, self.payoff)

  def __repr__(self):
    return self.__str__()


def CormenInvestment(returns, stay_fee, change_fee, capital):
  # Doubly array [y][i], the best payoff if the last investment is i ending in
  # year y.
  results = [[None for investment in year] for year in returns]
  num_year = len(returns)
  num_investment = len(returns[0])

  # First year best payoffs.
  results[0] = [Result(i, None, capital * rate)
                for i, rate in enumerate(returns[0])]

  for year in xrange(1, num_year):
    for this_investment in xrange(num_investment):
      this_year_payoff = []
      for previous_investment in xrange(num_investment):
        payoff = results[year-1][previous_investment].payoff * returns[year][this_investment]
        fee = stay_fee if previous_investment == this_investment else change_fee
        this_year_payoff.append((previous_investment, payoff - fee))
      largest_payoff = -float('Inf')
      largest_previous_investment = None
      for investment, payoff in this_year_payoff:
        if payoff > largest_payoff:
          largest_payoff = payoff
          largest_previous_investment = investment
      results[year][this_investment] = Result(
          this_investment, largest_previous_investment, largest_payoff)

  print results

  largest_result = None
  for result in results[-1]:
    if largest_result is None or result.payoff > largest_result.payoff:
      largest_result = result

  return largest_result.payoff, ComposeSolution(
      largest_result.current_investment, num_year - 1, results)


def ComposeSolution(investment, year, results):
  if results[year][investment].previous_investment is None:
    return [results[year][investment].current_investment]

  prior_solution = ComposeSolution(
      results[year][investment].previous_investment,
      year - 1,
      results)

  return prior_solution + [results[year][investment].current_investment]


import unittest


class TestCormenInvestment(unittest.TestCase):

  def setUp(self):
    self.longMessage = True

  def test_Example15_10(self):
    returns = [
        [1., 2.],
        [2., 1.],
    ] 
    payoff, strategy = CormenInvestment(returns, 100., 150., 100000)
    self.assertEqual([1, 0], strategy, msg=strategy)
    self.assertEqual(399850., payoff)
