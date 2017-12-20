f = open('./12.input')
input = f.read().rstrip()

def solve(input):
  lines = input.split('\n')

  pipings = {}
  for line in lines:
    parts = line.split(' <-> ')
    pipings[parts[0]] = parts[1].split(', ')

  group_ids = ['0']
  len_pipings = len(pipings)

  while True:
    for src_id, dest_ids in sorted(pipings.iteritems()):
      if src_id in group_ids:
        for dest_id in dest_ids:
          group_ids.append(dest_id)

        del pipings[src_id]

    if len_pipings == len(pipings):
      break
    else:
      len_pipings = len(pipings)

  return len(list(set(group_ids)))

print(solve(input))
