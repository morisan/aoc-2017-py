from collections import deque

input = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"

def solve(input):
  num_list = deque(range(0,256))
  num_list_len = len(num_list)

  i = 0
  skip_size = 0
  lengths = input.split(',')
  for l in lengths:
    l = int(l)
    span = deque([])

    num_list.rotate(-1*i)

    for j in range(0, l):
      span.append(num_list.popleft())

    while len(span) > 0:
      num_list.appendleft(span.popleft())

    num_list.rotate(i)

    i = (i + l + skip_size) % len(num_list)
    skip_size += 1

  return num_list[0] * num_list[1]

print(solve(input))
