f = open('./19.input')
input = f.read().rstrip()

def solve(input):
  lines = input.split('\n')

  diagram = []
  for line in lines:
    diagram.append(list(line))

  directions = ['N', 'E', 'S', 'W']
  direction = 'S'
  r = 0
  c = diagram[0].index('|')

  steps = 0

  while True:
    steps  += 1

    curr_char = diagram[r][c]

    if direction == 'N':
      r -= 1
    if direction == 'E':
      c += 1
    if direction == 'S':
      r += 1
    if direction == 'W':
      c -= 1

    if r < len(diagram) and c < len(diagram[r]) and diagram[r][c] != ' ':
      next_char = diagram[r][c]
      if next_char == '+':
        if direction == 'N' or direction == 'S':
          if (c-1) < len(diagram[r]) and diagram[r][c-1] != ' ':
            direction = 'W'
          elif (c+1) < len(diagram[r]) and diagram[r][c+1] != ' ':
            direction = 'E'
        elif direction == 'E' or direction == 'W':
          if (r-1) < len(diagram) and c < len(diagram[r-1]) and diagram[r-1][c] != ' ':
            direction = 'N'
          elif (r+1) < len(diagram) and c < len(diagram[r+1]) and diagram[r+1][c] != ' ':
            direction = 'S'
    else:
      return steps

print(solve(input))
