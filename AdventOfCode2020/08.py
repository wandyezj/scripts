def readFile(file):
    f = open(file)
    data = f.read()
    f.close()
    return data

INSTRUCTION_JUMP = "jmp"
INSTRUCTION_ACCUMULATE = "acc"
INSTRUCTION_NOOPERATION = "nop"

class Instruction:
    def __init__(self, line):
        self.text = line
        pieces = line.split(" ")
        self.operation = pieces[0]
        self.value = int(pieces[1])

    def __str__(self):
        return "{} {:+}".format(self.operation, self.value)

    def isOperation(self, op):
        return self.operation == op

    def isJump(self):
        return self.isOperation(INSTRUCTION_JUMP)
    
    def isAccumulate(self):
        return self.isOperation(INSTRUCTION_ACCUMULATE)

    def isNooperation(self):
        return self.isOperation(INSTRUCTION_NOOPERATION)
        

CODE_SEQUENTIAL = "code sequential"
CODE_LOOPS = "code loops"

class Program:
    def __init__(self, data):
        lines = data.strip().split("\n")
        self.instructions = list(map(Instruction, lines))

    def __str__(self):
        return "\n".join(map(str, self.instructions))

    def execute(self, verbose=False):
        accumulator = 0
        program_counter = 0

        # keep track of which instructions are visited
        visited = [False] * len(self.instructions)

        # Until a loop is found
        code = CODE_SEQUENTIAL
        while program_counter < len(self.instructions):

            if visited[program_counter]:
                code = CODE_LOOPS
                break

            instruction = self.instructions[program_counter]

            if verbose:
                #trace program execution
                print('{:>3} {:<8} | {} {}'.format(program_counter, str(instruction), visited[program_counter], accumulator))

            visited[program_counter] = True

            if instruction.isJump():
                program_counter += instruction.value
            elif instruction.isAccumulate():
                accumulator += instruction.value
                program_counter +=1
            elif instruction.isNooperation():
                program_counter += 1
            else:
                assert False

        return (code, accumulator, program_counter)



def constructProgram(data):
    return Program(data)


print("Part 1")
data = readFile("08.input.txt")
program = constructProgram(data)
#print(data)
#print(program)

code = program.execute()
print(code[1])

print("Part 2")
program = constructProgram(data)

# mutate instructions
replacement = Instruction('nop 0')

for i in range(len(program.instructions)):
    instruction = program.instructions[i]
    if instruction.isJump():
        program.instructions[i] = replacement

        code, accumulator, program_counter = program.execute()

        # put the original instruction back
        program.instructions[i] = instruction

        if code == CODE_SEQUENTIAL:
            print(accumulator)
            #print('replace {}  accumulator {}'.format(i, accumulator))





