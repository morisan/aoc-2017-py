import math

input = 368078

def get_next_d_pos(d_pos):
  return (d_pos + 1) % 4

def get_next_num(history, x_pos, y_pos):
  res = 0
  if x_pos - 1 in history:
    print('-1')
    if y_pos - 1 in history[x_pos - 1]:
      print('a')
      res += history[x_pos - 1][y_pos - 1]
    if y_pos in history[x_pos - 1]:
      print('b')
      res += history[x_pos - 1][y_pos]
    if y_pos + 1 in history[x_pos - 1]:
      print('c')
      res += history[x_pos - 1][y_pos + 1]

  if x_pos in history:
    print('0')
    if y_pos - 1 in history[x_pos]:
      res += history[x_pos][y_pos - 1]
    if y_pos in history[x_pos]:
      res += history[x_pos][y_pos]
    if y_pos + 1 in history[x_pos]:
      res += history[x_pos][y_pos + 1]

  if x_pos + 1 in history:
    print('1')
    if y_pos - 1 in history[x_pos + 1]:
      res += history[x_pos + 1][y_pos - 1]
    if y_pos in history[x_pos + 1]:
      res += history[x_pos + 1][y_pos]
    if y_pos + 1 in history[x_pos + 1]:
      res += history[x_pos + 1][y_pos + 1]

  return res

def solve(input):
  history = {}
  history[0] = {}
  history[0][0] = 1

  curr_num = 1

  directions = ['RIGHT', 'UP', 'LEFT', 'DOWN']
  d_pos = 0
  x_pos = 0
  y_pos = 0
  mag = 1
  mag_cnt = 0

  if input == 1:
    return 1

  while curr_num <= input:
    curr_direction = directions[d_pos]

    if curr_direction == 'RIGHT':
      for _ in range(mag):
        x_pos += 1
        curr_num = get_next_num(history, x_pos, y_pos)

        if curr_num > input:
          return curr_num

        if x_pos not in history:
          history[x_pos] = {}

        history[x_pos][y_pos] = curr_num

    if curr_direction == 'UP':
      for _ in range(mag):
        y_pos += 1
        curr_num = get_next_num(history, x_pos, y_pos)

        if curr_num > input:
          return curr_num

        history[x_pos][y_pos] = curr_num

    if curr_direction == 'LEFT':
      for _ in range(mag):
        x_pos -= 1
        curr_num = get_next_num(history, x_pos, y_pos)

        if curr_num > input:
          return curr_num

        if x_pos not in history:
          history[x_pos] = {}

        history[x_pos][y_pos] = curr_num

    if curr_direction == 'DOWN':
      for _ in range(mag):
        y_pos -= 1
        curr_num = get_next_num(history, x_pos, y_pos)

        if curr_num > input:
          return curr_num

        history[x_pos][y_pos] = curr_num

    d_pos = (d_pos + 1) % 4
    mag_cnt += 1
    if mag_cnt == 2:
      mag += 1
      mag_cnt = 0

print(solve(input))
