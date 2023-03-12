import sys
from sys import maxsize

def createStack(input):
    newStack = []
    newStack = input.split()
    return newStack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1)
     
    return stack.pop()

def peek(stack):
    if (isEmpty(stack)):
        return str(-maxsize -1) # return minus infinite
    return stack[len(stack) - 1]

def search(stack, item):
    index = 0
    for i in stack:
        if i == item:
            return index
        index += 1
    return -1
    
def checkBracket(input, check):
    for i in input:
        if i == check:
            
            return True
    return False

def compute(op, inNum1, inNum2):
    if op[1:2] == '+':
        return str(int(inNum1) + int(inNum2[0:1]))
    elif op[1:2] == '-':
        return str(int(inNum1) - int(inNum2[0:1]))
    elif op[1:2] == '*':
        return str(int(inNum1) * int(inNum2[0:1]))
    elif op[1:2] == '/':
        return str(int(inNum1) / int(inNum2[0:1]))
    else:
        raise ValueError(f"Invalid operator: {op}")    

def evaluate(stack):
    index = len(stack)
    hold = str()
    for i in reversed(stack):

        if checkBracket(i, ')'):

            if checkBracket(stack[len(stack) - (index + 3)], '('):
                
                num2 = pop(stack)
                num1 = pop(stack)
                op = pop(stack)

                result = compute(op, num1, num2)
                
                push(stack, str(result))

                if bool(hold) != "":
                    push(stack, hold)
                    hold = str()

            else:
                hold = pop(stack)

        if len(stack) == 1:
            return str(stack[0])
        
        index -= 1

    return str(stack[0])


if __name__ == '__main__':
    conInput = sys.argv[1]
    stack = createStack(conInput)
    result = evaluate(stack)
    result = result.replace(")","")
    print(result)
    