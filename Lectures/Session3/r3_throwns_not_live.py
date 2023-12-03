# Game of Throwns
# there are two subtle bugs in this code

n, k = map(int, input().split())
action = list(input().split()) # read all as list of strings first
i, egg = 0, 0
stack = [] # use the back side as the top of stack
for _ in range(k): # there will be k commands
    if action[i] == "undo": # undo m (two tokens)
        m = int(action[i+1])
        i += 2
        for _ in range(m): # undo m times
            egg = stack.pop() # go back to this position
    else: # an integer, either positive or negative
        p = int(action[i])
        i += 1
        egg = (egg+n+p)%n
        stack.append(egg) # push this *new* location to the stack
print(egg) # the final location of the egg
