from collections import deque
import time

# input = 'flqrgnkx'
input = 'wenycdww' # not 1165

def do_knot_hash(input):
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

def solve(input):
  rows = []
  for i in range(0,128):
    rows.append('')

    kh = do_knot_hash(input + '-' + str(i))
    row = []
    for c in kh:
      b = bin(int(c,16))[2:]
      while len(b) < 4:
        b = '0' + b
      row.extend(list(b.replace('1','#').replace('0','.')))
    rows[i] = row


  num_regions = 0
  r_start = 0
  c_start = 0
  r_scout = 0
  c_scout = 0

  for i, r in enumerate(rows):
    for j, c in enumerate(r):
      if c != '#':
        continue
      else:
        # Catch the stragglers that the Scout didn't cover

        curr_region = None
        # N
        if i-1 >= 0 and rows[i-1][j] not in ['#', '.']:
          curr_region = rows[i-1][j]
        # E
        elif j+1 < len(rows[i][j]) and rows[i][j+1] not in ['#', '.']:
          curr_region = rows[i][j+1]
        # S
        elif i+1 < len(rows[i]) and rows[i+1][j] not in ['#', '.']:
          curr_region = rows[i+1][j]
        # W
        elif j-1 >= 0 and rows[i][j-1] not in ['#', '.']:
          curr_region = rows[i][j-1]

        if not curr_region:
          num_regions += 1
          curr_region = str(num_regions)

        r_start = i
        c_start = j
        rows[i][j] = str(curr_region)

        r_scout = i
        c_scout = j
        has_moved = False
        give_up = False
        # print("give_up: "+str(give_up))
        direction = 'E'
        directions = ['E','S','W','N']
        while True:
          if give_up or (has_moved and r_start == r_scout and c_start == c_scout):
            break

          d_i = directions.index(direction)
          trys = [directions[(d_i + 3) % 4], directions[d_i], directions[(d_i + 1) % 4], directions[(d_i + 2) % 4]]

          for t_i, t in enumerate(trys):
            if t == 'N' and r_scout-1 >= 0 and rows[r_scout-1][c_scout] in ['#', curr_region] :
              r_scout -= 1
              rows[r_scout][c_scout] = curr_region

              has_moved = True
              direction = 'N'
              break

            elif t == 'E' and c_scout+1 < len(rows[r_scout]) and rows[r_scout][c_scout+1] in ['#', curr_region]:
              c_scout += 1
              rows[r_scout][c_scout] = curr_region

              has_moved = True
              direction = 'E'
              break

            elif t == 'S' and r_scout+1 < len(rows[r_scout]) and rows[r_scout+1][c_scout] in ['#', curr_region]:
              r_scout += 1
              rows[r_scout][c_scout] = curr_region

              has_moved = True
              direction = 'S'
              break

            elif t == 'W' and c_scout-1 >= 0 and rows[r_scout][c_scout-1] in ['#', curr_region]:
              c_scout -= 1
              rows[r_scout][c_scout] = curr_region

              has_moved = True
              direction = 'W'
              break


            if t_i+1 == len(trys) and not has_moved:
              give_up = True
              break


  # TODO: Better way to do this rather than have this cleanup function... :-/
  did_cleanup = False
  first_loop = True
  while (first_loop or did_cleanup):
    first_loop = False
    did_cleanup = False

    for i, r in enumerate(rows):
      for j, c in enumerate(r):
        if rows[i][j] == '.':
          continue

        # N
        if i-1 >= 0 and rows[i-1][j] != '.' and rows[i][j] != rows[i-1][j]:
          if rows[i][j] > rows[i-1][j]:
            rows[i][j] = rows[i-1][j]
            did_cleanup = True
          else:
            rows[i-1][j] = rows[i][j]
            did_cleanup = True
        # E
        if j+1 < len(rows[i][j]) and rows[i][j+1] != '.' and rows[i][j] != rows[i][j+1]:
          if rows[i][j] > rows[i][j+1]:
            rows[i][j] = rows[i][j+1]
            did_cleanup = True
          else:
            rows[i][j+1] = rows[i][j]
            did_cleanup = True
        # S
        if i+1 < len(rows[i]) and rows[i+1][j] != '.' and rows[i][j] != rows[i+1][j]:
          if rows[i][j] > rows[i+1][j]:
            rows[i][j] = rows[i+1][j]
            did_cleanup = True
          else:
            rows[i+1][j] = rows[i][j]
            did_cleanup = True
        # W
        if j-1 >= 0 and rows[i][j-1] != '.' and rows[i][j] != rows[i][j-1]:
          if rows[i][j] > rows[i][j-1]:
            rows[i][j] = rows[i][j-1]
            did_cleanup = True
          else:
            rows[i][j-1] = rows[i][j]
            did_cleanup = True

  result = []
  for r in rows:
    result.extend(r)
    # Print
    # row = []
    # for c in r:
    #   while len(c) < 4:
    #     c = ' ' + c
    #   row.append(c)
    # print('|'.join(row)[:525])

  return len(list(set(result))) - 1

print(solve(input))
