

def find_dice_order(sentence, dices):
  permutation_indices = []
  def inner(sentence_tail, dices, permutation_indices):
    if len(sentence_tail) == 0:
      return []
    for dice_index, dice in enumerate(dices):
      if dice_index in permutation_indices:
        continue
      if sentence_tail[0] in dice:
        permutation_indices.append(dice_index)
        dice_tail = inner(sentence_tail[1:], dices, permutation_indices)
        if dice_tail is not None:
          return [dice] + dice_tail
    return None
  return inner(sentence, dices, permutation_indices)


print(find_dice_order('hello', ['oo', 'll', 'll', 'ee', 'hh']))
