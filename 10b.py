from collections import deque

input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"

def solve(input):
  num_list = deque(range(0,256))

  i = 0
  skip_size = 0
  chars = list(input)
  lengths = []
  for c in chars:
    lengths.append(ord(c))

  lengths.extend([17, 31, 73, 47, 23])
  lengths *= 64

  for l in lengths:
    span = deque([])

    num_list.rotate(-1*i)

    for j in range(0, l):
      span.append(num_list.popleft())

    while len(span) > 0:
      num_list.appendleft(span.popleft())

    num_list.rotate(i)

    i = (i + l + skip_size) % len(num_list)
    skip_size += 1

  res = 0
  dense_hash = []
  for i, n in enumerate(num_list):
    res ^= n
    if i % 16 == 15:
      dense_hash.append(res)
      res = 0

  hex_str = ''
  for d in dense_hash:
    h = hex(d)[2:]
    if len(h) == 1:
      h = '0' + h

    hex_str += h

  return hex_str

print(solve(input))
