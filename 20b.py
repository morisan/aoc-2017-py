import re

f = open('./20.input')
input = f.read().rstrip()

def solve(input):
  lines = input.split('\n')
  particles = {}

  for p_i, l in enumerate(lines):
    parts = l.split(', ')

    particle = {}
    for part in parts:
      regex = re.compile("^(\w)=<([-]?\d+),([-]?\d+),([-]?\d+)>")
      matches = regex.search(part)
      particle[matches.group(1)] = [int(matches.group(2)), int(matches.group(3)), int(matches.group(4))]

    particles[p_i] = particle

  for i in range(0, 500):
    hits = {}
    for p_i, particle in particles.iteritems():
      particle['v'][0] += particle['a'][0]
      particle['v'][1] += particle['a'][1]
      particle['v'][2] += particle['a'][2]
      particle['p'][0] += particle['v'][0]
      particle['p'][1] += particle['v'][1]
      particle['p'][2] += particle['v'][2]

      pos = ''.join(str(p_i) for p_i in particle['p'])
      if pos in hits:
        hits[pos].append(p_i)
      else:
        hits[pos] = [p_i]

    for pos, p_is in hits.iteritems():
      if len(p_is) > 1:
        for p_i in p_is:
          del particles[p_i]

  return len(particles)

print(solve(input))
