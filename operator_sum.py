
def sum_list(numbers, value):
  assert numbers

  if len(numbers) == 1:
    if numbers[0] == value:
      yield numbers
    return

  first_number, *rest = numbers
  # Addition.
  for tail_list in sum_list(rest, value - first_number):
    yield [first_number, '+'] + tail_list
  # Subtraction.
  for tail_list in sum_list(rest, value + first_number):
    yield [first_number, '-'] + tail_list
  # Concatenation.
  second_number, *rest_rest = rest
  for new_list in sum_list(
      [first_number * 10 + second_number] + rest_rest, value):
    yield new_list
    

for ans in sum_list([1,2,3,4,5,6,7,8,9], 100):
  print(' '.join([str(n) for n in ans]))
