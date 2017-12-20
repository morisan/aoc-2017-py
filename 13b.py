f = open('./13.input')
input = f.read().rstrip()

def find_scanner_pos(r, ps):
  pos = 0
  direction = 'down'

  cycle = r + (r - 2)
  ps %= cycle

  while ps > 0:
    if direction == 'down':
      pos += 1
      ps  -= 1
      if pos == r-1:
        direction = 'up'
    elif direction == 'up':
      pos -= 1
      ps  -= 1
      if pos == 0:
        direction = 'down'

  return pos

def solve(input):
  layers = input.split('\n')

  layer_map = {}
  deepest_layer = 0
  for layer in layers:
    parts = layer.split(': ')
    d = int(parts[0])
    r = int(parts[1])
    layer_map[d] = r
    if d > deepest_layer:
      deepest_layer = d

  test_ps = 0
  while True:
    hit = False

    ps = test_ps
    d = 0
    while d <= deepest_layer:
      if d in layer_map:
        r = layer_map[d]
        if find_scanner_pos(r, ps) == 0:
          hit = True
          break
      ps += 1
      d += 1

    if hit:
      test_ps += 1
    else:
      return test_ps

print(solve(input))
