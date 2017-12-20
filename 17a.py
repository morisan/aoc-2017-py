input = 348

def solve(input):
  buf = [0]

  curr_pos = 0
  insert_val = 0
  end_val = 2017
  while insert_val <= end_val:
    insert_val += 1

    curr_pos = ((curr_pos + input) % len(buf)) + 1
    buf.insert(curr_pos, insert_val)

  return buf[buf.index(end_val)+1]

print(solve(input))
