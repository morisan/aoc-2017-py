f = open('./18.input')
input = f.read().rstrip()

def solve(input):
  program = input.split('\n')
  pc = 0

  regs = {}
  last_snd = None

  while True:
    instr = program[pc]
    instr_parts = instr.split()
    op = instr_parts[0]
    reg_name = instr_parts[1]
    operand_val = None

    if len(instr_parts) > 2:
      operand = instr_parts[2]
      try:
        int(operand)
        operand_val = int(operand)
      except ValueError:
        operand_val = regs[operand]

    if op == 'set':
      regs[reg_name] = operand_val
      pc += 1
    elif op == 'add':
      if reg_name in regs:
        regs[reg_name] += operand_val
      else:
        regs[reg_name] = operand_val
      pc += 1
    elif op == 'mul':
      if reg_name in regs:
        regs[reg_name] *= operand_val
      else:
        regs[reg_name] = 0
      pc += 1
    elif op == 'mod':
      if reg_name in regs:
        regs[reg_name] %= operand_val
      else:
        regs[reg_name] = 0
      pc += 1
    elif op == 'snd':
      if reg_name in regs:
        last_snd = regs[reg_name]
      pc += 1
    elif op == 'rcv':
      if reg_name in regs and regs[reg_name] != 0:
        return last_snd
      pc += 1
    elif op == 'jgz':
      if reg_name in regs and regs[reg_name] > 0:
        pc += operand_val
      else:
        pc += 1
    else:
      return regs

print(solve(input))
