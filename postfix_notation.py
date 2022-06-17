print("Post-fix Calculator")
print("For help, type \"help\" or \"?\"")

while True:
    str_in = input("> ")
    tokens = str_in.split(" ")
    stack = []

    if tokens[0] == "help" or tokens[0] == "?":
        print ("Post-fix calculator takes in post-fix formatted equations and evaluates them.")
        print ("Input should be formatted in such a way that the equation can be evaluated fully.")
        print ("Ex. \"1 2 + 4 *\" equals \"12\"")

    elif tokens[0] == "quit" or tokens[0] == "q":
        break

    else:
        while len(tokens) > 0:
            item = tokens.pop(0)

            if item.isdigit():
                stack.append(int(item))

            elif item == "+":
                if len(stack) > 1:
                    stack.append(stack.pop() + stack.pop())
                else:
                    #ERROR
                    print ("ERROR: Invalid expression. Not enough input.")
                    break

            elif item == "-":
                if len(stack) > 1:
                    tmp = stack.pop()
                    stack.append(stack.pop() - tmp)
                else:
                    #ERROR
                    print ("ERROR: Invalid expression. Not enough input.")
                    break

            elif item == "*":
                if len(stack) > 1:
                    stack.append(stack.pop() * stack.pop())
                else:
                    #ERROR
                    print ("ERROR: Invalid expression. Not enough input.")
                    break

            elif item == "/":
                if len(stack) > 1:
                    tmp = stack.pop()
                    stack.append(stack.pop() / tmp)
                else:
                    #ERROR
                    print ("ERROR: Invalid expression. Not enough input.")
                    break

            elif item == "^":
                if len(stack) > 1:
                    tmp = stack.pop()
                    stack.append(pow(stack.pop(), tmp))
                else:
                    #ERROR
                    print ("ERROR: Invalid Expression. Not enough input.")
                    break

            else:
                #ERROR
                break

        print (stack.pop())
