# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

import sys


def solution():
    # Initiate
    global_scope = {}  # Store {name: (type, level)}
    scopes = [set()]  # Store variable name for each scope
    current_level = 0  # Start with global scope dict
    output = []
    n = int(input())
    for _ in range(n):
        command = sys.stdin.readline().strip()
        # For { means entering a new scope
        if command == '{':
            current_level += 1
            scopes.append(set())
        # For } means exiting scope
        elif command == '}':
            # Remove variables declared for this scope
            for var in scopes.pop():
                if global_scope[var][-1][1] == current_level:
                    global_scope[var].pop()
                    if not global_scope[var]:
                        del global_scope[var]
            current_level -= 1
        else:
            # For ACTION_CMD <identifier> <type>(only in DECLARE)
            parts = command.split()
            action_cmd = parts[0]
            identifier = parts[1]

            if action_cmd == 'DECLARE':
                # Check for multiple declarations
                # Current scope stored in the last dict
                if identifier in scopes[-1]:
                    output.append("MULTIPLE DECLARATION")
                    return output
                else:
                    scopes[-1].add(identifier)
                    # Create/Add key-value pair in global
                    if identifier not in global_scope:
                        global_scope[identifier] = []
                    global_scope[identifier].append((parts[2], current_level))
            elif action_cmd == 'TYPEOF':
                if identifier in global_scope:
                    # Check type from inner to outer
                    for type_level in reversed(global_scope[identifier]):
                        if type_level[1] <= current_level:
                            output.append(type_level[0])
                            break
                    else:
                        output.append("UNDECLARED")
                else:
                    output.append("UNDECLARED")

    return output


for result in solution():
    print(result)
