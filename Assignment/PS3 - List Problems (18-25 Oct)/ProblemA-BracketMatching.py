def solution():
    n = int(input())
    s = list(input())
    pair = {')': '(', ']': '[', '}': '{'}
    # Create a (fake) stack (FILO) to store left_side bracket
    lst = []
    for char in s:
        # If the char is left_side bracket, put it in stack
        if char in '({[':
            lst.append(char)
        # If the char is right_side bracket
        else:
            # Check two conditions:
            # 1. There are no left bracket in stack
            # 2. The top (last) element of the stack is not the paired left_side
            if not lst or lst[-1] != pair[char]:
                print("Invalid")
                return
            # Pop out the top if it is paired
            lst.pop()
    # Check the stack at final, if rest char, print invalid
    print("Valid" if not lst else "Invalid")
    return


solution()
