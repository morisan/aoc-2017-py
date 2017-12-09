import re

f = open('./9.input')
input = f.read().rstrip()

def solve(input):
  input = re.sub(r"!.", "", input)
  input = re.sub(r"<[^>]*>", "", input)

  total_score = 0
  depth = 0
  for c in input:
    if c == '{':
      depth += 1
    if c == '}':
      total_score += depth
      depth -= 1

  return total_score

print(solve(input))
