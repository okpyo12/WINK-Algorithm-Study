import sys

program = [[]]
stack_num = [[]]
stack = []
result = []
idx = 0
cmd = ""
while cmd != "QUIT":
    cmd = sys.stdin.readline().rstrip()
    if cmd == "QUIT":
        break
    elif cmd[:3] == "NUM":
        program[idx].append(cmd)
    elif cmd == "POP":
        program[idx].append(cmd)
    elif cmd == "INV":
        program[idx].append(cmd)
    elif cmd == "DUP":
        program[idx].append(cmd)
    elif cmd == "SWP":
        program[idx].append(cmd)
    elif cmd == "ADD":
        program[idx].append(cmd)
    elif cmd == "SUB":
        program[idx].append(cmd)
    elif cmd == "MUL":
        program[idx].append(cmd)
    elif cmd == "DIV":
        program[idx].append(cmd)
    elif cmd == "MOD":
        program[idx].append(cmd)
    elif cmd == "END":
        program[idx].append(cmd)
    elif cmd == "":
        program.append([])
    else:
        for i in range(int(cmd)):
            stack_num[idx].append(int(sys.stdin.readline()))
        stack_num.append([])
        idx += 1
del program[-1]
del stack_num[-1]

for i in range(len(stack_num)):
    for j in range(len(stack_num[i])):
        stack = []
        stack.append(stack_num[i][j])
        for k in program[i]:
            if k[:3] == "NUM":
                stack.append(int(k[3:]))
            elif k == "POP":
                if len(stack) < 1:
                    stack = "ERROR"
                    break
                else:
                    stack.pop()
            elif k == "INV":
                if len(stack) < 1:
                    stack = "ERROR"
                    break
                else:
                    stack[-1] = -stack[-1]
            elif k == "DUP":
                if len(stack) < 1:
                    stack = "ERROR"
                    break
                else:
                    stack.append(stack[-1])
            elif k == "SWP":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    stack.append(a)
                    stack.append(b)
            elif k == "ADD":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    stack.append(a+b)
            elif k == "SUB":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    stack.append(b-a)
            elif k == "MUL":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    stack.append(a*b)
            elif k == "DIV":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    if a == 0:
                        stack = "ERROR"
                        break
                    else:
                        if (a > 0 and b < 0) or (a < 0 and b > 0):
                            stack.append(-(abs(b)//abs(a)))
                        else:
                            stack.append(abs(b)//abs(a))
            elif k == "MOD":
                if len(stack) < 2:
                    stack = "ERROR"
                    break
                else:
                    a = stack[-1]
                    stack.pop()
                    b = stack[-1]
                    stack.pop()
                    if a == 0:
                        stack = "ERROR"
                        break
                    else:
                        if b < 0:
                            stack.append(-(abs(b)%abs(a)))
                        else:
                            stack.append(abs(b)%abs(a))
            elif k == "END":
                if len(stack) == 1:
                    if stack[0] > 10**9 or stack[0] < -10**9:
                        stack = "ERROR"
                else:
                    stack = "ERROR"
        result.append(stack)
    result.append("")
    
del result[-1]
for i in result:
    if i == "ERROR":
        print(i)
    elif i == "":
        print()
    else:
        for j in i:
            print(j)