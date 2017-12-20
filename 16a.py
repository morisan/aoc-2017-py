f = open('./16.input')
input = f.read().rstrip()

def solve(input):
  line = list('abcdefghijklmnop')
  moves = input.split(',')

  for move in moves:
    move_code = move[0]
    move_props = move[1:]

    if move_code == 's':
      line = line[len(line)-int(move_props):] + line[:len(line)-int(move_props)]
    if move_code == 'x':
      swap_positions = move_props.split('/')
      for i, pos in enumerate(swap_positions):
        swap_positions[i] = int(pos)
      swap_positions.sort()
      swap_vals = [line[swap_positions[0]], line[swap_positions[1]]]

      line[swap_positions[0]] = swap_vals[1]
      line[swap_positions[1]] = swap_vals[0]

    if move_code == 'p':
      swap_vals = move_props.split('/')
      swap_positions = [line.index(swap_vals[0]), line.index(swap_vals[1])]

      line[swap_positions[0]] = swap_vals[1]
      line[swap_positions[1]] = swap_vals[0]

  return ''.join(line)

print(solve(input))
