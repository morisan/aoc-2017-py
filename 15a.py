a = 634
b = 301
a_factor = 16807
b_factor = 48271
divider = 2147483647
i = 40000000

num_matches = 0
while i > 0:
  a = a * a_factor % divider
  b = b * b_factor % divider

  if bin(a)[-16:] == bin(b)[-16:]:
    num_matches += 1

  i -= 1

print(num_matches)
