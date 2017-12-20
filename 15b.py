from collections import deque

a = 634
b = 301
a_factor = 16807
b_factor = 48271
a_multiple = 4
b_multiple = 8
divider = 2147483647
i = 5000000

a_q = deque([])
b_q = deque([])
num_matches = 0
while i > len(a_q) or i > len(b_q):
  a = a * a_factor % divider
  b = b * b_factor % divider

  if (a % a_multiple) == 0:
    a_q.append(a)
  if (b % b_multiple) == 0:
    b_q.append(b)

while len(a_q) > 0 and len(b_q) > 0:
  a_test = bin(a_q.popleft())[-16:]
  b_test = bin(b_q.popleft())[-16:]
  if a_test == b_test:
    num_matches += 1

print(num_matches)
