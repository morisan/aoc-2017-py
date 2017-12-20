from collections import deque

input = 348

def solve(input):
  buf = deque([0])

  insert_val = 0
  end_val = 50000000
  while insert_val <= end_val:
    insert_val += 1
    buf.rotate(-input)
    buf.append(insert_val)

  zero_index = 0
  for i, val in enumerate(buf):
    if val == 0:
      zero_index = i
      break

  return buf[zero_index + 1]

print(solve(input))
