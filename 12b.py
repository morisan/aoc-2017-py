f = open('./12.input')
input = f.read().rstrip()

def solve(input):
  lines = input.split('\n')

  pipings = {}
  for line in lines:
    parts = line.split(' <-> ')
    pipings[int(parts[0])] = parts[1].split(', ')

  num_groups = 0
  group_ids = ['0']
  len_pipings = len(pipings)

  while len(pipings) > 0:
    for src_id, dest_ids in sorted(pipings.iteritems()):
      if src_id in group_ids:
        for dest_id in dest_ids:
          group_ids.append(int(dest_id))

        del pipings[src_id]

    if len_pipings == len(pipings):
      num_groups += 1
      group_ids = [min(pipings)]
    else:
      len_pipings = len(pipings)

  return num_groups

print(solve(input))
