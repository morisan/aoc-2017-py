f = open('./13.input')
input = f.read().rstrip()

def find_scanner_pos(r, ps):
  pos = 0
  direction = 'down'

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

  severity = 0

  ps = 0
  while ps <= deepest_layer:
    d = ps
    if d in layer_map:
      r = layer_map[d]
      if find_scanner_pos(r, ps) == 0:
        severity += (d*r)
    ps += 1

  return severity

print(solve(input))
