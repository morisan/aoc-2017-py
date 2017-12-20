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

  lowest_particle = None
  for i in range(0, 500):

    lowest_distance = None
    for p_i, particle in particles.iteritems():
      particle['v'][0] += particle['a'][0]
      particle['v'][1] += particle['a'][1]
      particle['v'][2] += particle['a'][2]
      particle['p'][0] += particle['v'][0]
      particle['p'][1] += particle['v'][1]
      particle['p'][2] += particle['v'][2]
      particles[p_i] = particle

      m_distance = abs(particle['p'][0]) + abs(particle['p'][1]) + abs(particle['p'][2])
      if lowest_distance == None:
        lowest_distance = m_distance
        lowest_particle = p_i
      elif m_distance < lowest_distance:
        lowest_distance = m_distance
        lowest_particle = p_i

  return lowest_particle

print(solve(input))
