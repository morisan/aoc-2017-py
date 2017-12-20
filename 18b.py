from collections import deque

f = open('./18.input')
input = f.read().rstrip()

def solve(input):
  program = input.split('\n')

  pc = [0,0]
  regs = [{'p': 0},{'p': 1}]
  rcv_q = [deque([]),deque([])]
  pid = 0

  cnt_snd_1 = 0

  while True:
    instr_parts = program[pc[pid]].split()
    op = instr_parts[0]
    reg_name = instr_parts[1]
    operand_val = None

    if len(instr_parts) > 2:
      operand = instr_parts[2]
      try:
        int(operand)
        operand_val = int(operand)
      except ValueError:
        operand_val = regs[pid][operand]

    if op == 'set':
      regs[pid][reg_name] = operand_val
      pc[pid] += 1
    elif op == 'add':
      if reg_name in regs[pid]:
        regs[pid][reg_name] += operand_val
      else:
        regs[pid][reg_name] = operand_val
      pc[pid] += 1
    elif op == 'mul':
      if reg_name in regs[pid]:
        regs[pid][reg_name] *= operand_val
      else:
        regs[pid][reg_name] = 0
      pc[pid] += 1
    elif op == 'mod':
      if reg_name in regs[pid]:
        regs[pid][reg_name] %= operand_val
      else:
        regs[pid][reg_name] = 0
      pc[pid] += 1
    elif op == 'jgz':
      sneaky_operand = reg_name
      try:
        int(sneaky_operand)
        sneaky_operand_val = int(sneaky_operand)
      except ValueError:
        sneaky_operand_val = regs[pid][sneaky_operand]

      if sneaky_operand_val > 0:
        pc[pid] += operand_val
      else:
        pc[pid] += 1
    elif op == 'snd':
      if reg_name in regs[pid]:
        rcv_q[pid^1].append(regs[pid][reg_name])
      else:
        rcv_q[pid^1].append(0)

      pc[pid] += 1

      if pid == 1:
        cnt_snd_1 += 1
    elif op == 'rcv':
      if len(rcv_q[pid]) > 0:
        regs[pid][reg_name] = rcv_q[pid].popleft()
        pc[pid] += 1
      else:
        pid ^= 1

        # Deadlock
        if len(rcv_q[pid]) == 0 and program[pc[pid]].split()[0] == 'rcv':
          return cnt_snd_1

print(solve(input))
