import math

input = 368078

def get_next_d_pos(d_pos):
  return (d_pos + 1) % 4

def solve(input):
  curr_num = 1

  directions = ['RIGHT', 'UP', 'LEFT', 'DOWN']
  d_pos = 0
  x_pos = 0
  y_pos = 0
  mag = 1
  mag_cnt = 0

  if input == 1:
    return 0

  while curr_num < input:
    curr_direction = directions[d_pos]

    if curr_direction == 'RIGHT':
      for _ in range(mag):
        curr_num += 1
        x_pos += 1
        if curr_num == input:
          return int(math.fabs(x_pos) + math.fabs(y_pos))

    if curr_direction == 'UP':
      for _ in range(mag):
        curr_num += 1
        y_pos += 1
        if curr_num == input:
          return int(math.fabs(x_pos) + math.fabs(y_pos))

    if curr_direction == 'LEFT':
      for _ in range(mag):
        curr_num += 1
        x_pos -= 1
        if curr_num == input:
          return int(math.fabs(x_pos) + math.fabs(y_pos))

    if curr_direction == 'DOWN':
      for _ in range(mag):
        curr_num += 1
        y_pos -= 1
        if curr_num == input:
          return int(math.fabs(x_pos) + math.fabs(y_pos))

    d_pos = (d_pos + 1) % 4
    mag_cnt += 1
    if mag_cnt == 2:
      mag += 1
      mag_cnt = 0

  return curr

print(solve(input))
