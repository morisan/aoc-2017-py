import json

input = '4  1 15  12  0 9 9 5 5 8 7 3 14  5 12  3'

def solve(input):
  banks = input.split()
  banks = map(int, banks)

  history = {}
  history[json.dumps(banks)] = 1

  res = 0

  while True:
    res += 1

    # Find block to redistribute
    most_blocks = 0
    j = 0
    for i, blocks in enumerate(banks):
      if blocks > most_blocks:
        most_blocks = blocks
        j = i

    # Redistribute blocks
    banks[j] = 0
    while most_blocks > 0:
      j = (j + 1) % len(banks)
      banks[j] += 1
      most_blocks -= 1

    if json.dumps(banks) in history:
      break;
    else:
      history[json.dumps(banks)] = 1

  return res

print(solve(input))
