import json

input = '4  1 15  12  0 9 9 5 5 8 7 3 14  5 12  3'

def solve(input):
  banks = input.split()
  banks = map(int, banks)

  history = {}
  history[json.dumps(banks)] = 1

  res = 0

  times_looped = 0
  first_looped_at = None

  while True:
    res += 1

    # Find block to redistribute
    most_blocks = 0
    bank_num = 0
    for i, blocks in enumerate(banks):
      if blocks > most_blocks:
        most_blocks = blocks
        bank_num = i

    # Redistribute blocks
    banks[bank_num] = 0
    while most_blocks > 0:
      bank_num = (bank_num + 1) % len(banks)
      banks[bank_num] += 1
      most_blocks -= 1

    if json.dumps(banks) in history:
      history[json.dumps(banks)] += 1

      if not first_looped_at:
        first_looped_at = res

      if history[json.dumps(banks)] == 3:
        break;
    else:
      history[json.dumps(banks)] = 1

  return res - first_looped_at

print(solve(input))
