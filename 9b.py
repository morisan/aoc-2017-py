import re

f = open('./9.input')
input = f.read().rstrip()

def solve(input):
  input = re.sub(r"!.", "", input)

  total_chars = 0

  r = re.compile("<(<*[^>]*)>")
  for match in r.finditer(input):
    total_chars += len(match.group(1))

  return total_chars

print(solve(input))
