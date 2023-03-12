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
    print(item + " pushed to stack ")

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
    hold = ""
    for i in reversed(stack):

        print("We Go Agian with: " +str(stack) + "  and were at: " + str(i))
        if checkBracket(i, ')'):

            print("*find index: " + str(len(stack)) + " - (" + str(index) + "+ 3 = " + str(len(stack) - (index + 3)))

            if checkBracket(stack[len(stack) - (index + 3)], '('):
                
                num2 = pop(stack)
                num1 = pop(stack)
                op = pop(stack)

                print("calculate: " + num1 + op + num2)

                result = compute(op, num1, num2)
                
                push(stack, str(result + ")"))
                print(str(stack))

                if bool(hold) != "":
                    print("This is in hold: " + str(hold))
                    push(stack, hold)
                    hold = str()

            else:
                hold = pop(stack)
                print("**putting this on hold: " + str(hold))

        print("stack length: " +str(len(stack)))
        if len(stack) == 1:
            return str(stack[0])
        
        index -= 1

    return str(stack[0])


if __name__ == '__main__':
    conInput = sys.argv[1]
    stack = createStack(conInput)
    print(stack)
    result = evaluate(stack)
    print("input: " + conInput + " = " + result)
    