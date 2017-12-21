from collections import deque
import math, copy

f = open('./21.input')
input = f.read().rstrip()

def img_to_rule(img):
  rule = []
  for line in img:

    rule.append(''.join(line))
  return '/'.join(rule)

def img_to_v_flipped_rule(img):
  rule = deque([])
  for line in img:
    rule.appendleft(''.join(line))
  return '/'.join(rule)

def img_to_h_flipped_rule(img):
  rule = []
  for line in img:
    rule.append(''.join(line)[::-1])
  return '/'.join(rule)

def rule_to_img(rule):
  img = deque([])
  rule = rule.split('/')
  for r in rule:
    img.append(deque(list(r)))
  return img

def print_img(img):
  string = []
  for line in img:
    print(''.join(line))
    string.append(''.join(line))

  return

def rotate_chunk(chunk):
  rotated_chunk = deque([])

  if len(chunk) == 2:
    rotated_chunk.append(deque([chunk[1][0], chunk[0][0]]))
    rotated_chunk.append(deque([chunk[1][1], chunk[0][1]]))
  elif len(chunk) == 3:
    line = deque([])
    line.append(chunk[2][0])
    line.append(chunk[1][0])
    line.append(chunk[0][0])
    rotated_chunk.append(line)
    line = deque([])
    line.append(chunk[2][1])
    line.append(chunk[1][1])
    line.append(chunk[0][1])
    rotated_chunk.append(line)
    line = deque([])
    line.append(chunk[2][2])
    line.append(chunk[1][2])
    line.append(chunk[0][2])
    rotated_chunk.append(line)

  return rotated_chunk

def solve(input):
  img = deque([deque(['.', '#', '.']), deque(['.', '.', '#']), deque(['#', '#', '#'])])

  lines = input.split('\n')
  rules = {}
  for l in lines:
    parts = l.split(' => ')
    rules[parts[0]] = parts[1]

  iters = 18
  for _ in range(0, iters):

    # Chunk img
    chunks = deque([])

    img_size = len(img)
    grid_size = None
    if img_size % 2 == 0:
      grid_size = 2
    elif img_size % 3 == 0:
      grid_size = 3

    num_grids = len(img) / grid_size

    # By row chunk first
    while len(img) > 0:
      rows_chunk = []
      for _ in range(0, grid_size):
        rows_chunk.append(img.popleft())

      # Then chunk the rows into squares
      while len(rows_chunk[0]) > 0:
        chunk = deque([])
        for row_i in range(0, grid_size):
          chunk.append(deque([]))
          for col_i in range(0, grid_size):
            chunk[row_i].append(rows_chunk[row_i].popleft())

        chunks.append(chunk)

    enhanced_chunks = deque([])
    for chunk in chunks:

      matched_rule = False
      for _ in range(0,4):
        if matched_rule:
          break

        if img_to_rule(chunk) in rules:
          enhanced_chunk = rule_to_img(rules[img_to_rule(chunk)])
          enhanced_chunks.append(enhanced_chunk)
          matched_rule = True
          break
        elif img_to_v_flipped_rule(chunk) in rules:
          enhanced_chunk = rule_to_img(rules[img_to_v_flipped_rule(chunk)])
          enhanced_chunks.append(enhanced_chunk)
          matched_rule = True
          break
        elif img_to_h_flipped_rule(chunk) in rules:
          enhanced_chunk = rule_to_img(rules[img_to_h_flipped_rule(chunk)])
          enhanced_chunks.append(enhanced_chunk)
          matched_rule = True
          break

        chunk = rotate_chunk(chunk)

    grid_size += 1
    num_chunks = len(enhanced_chunks)
    chunks_across = int(math.sqrt(num_chunks))

    # De-chunk img
    for chunk_i, chunk in enumerate(enhanced_chunks):
      supergrid_row = chunk_i / chunks_across

      for line_i, line in enumerate(chunk):
        insertion_row = (supergrid_row * grid_size) + line_i

        while len(img) <= insertion_row:
          img.append(deque([]))

        for c in line:
          img[insertion_row].append(c)

  return [ y for x in img for y in x].count('#')

print(solve(input))
