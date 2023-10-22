import sys


def flatten(seq, N):
    flattened = []
    for i in range(N):
        cp = seq[i]
        for j in range(2):
            flattened.append(cp[j])
    return flattened

def solution():
    """ Read inputs """
    # N for number of couples, Q for number of instructions
    N, Q = map(int, input().split())
    # [['amelia', 'bubba'], ['kiryu', 'coco'], ['ollie', 'udin']]
    names = [sys.stdin.readline().strip().split() for cp in range(N)]
    # print(names)
    partners = {}
    # Pair each couple into dict
    for i in range(N):
        cp = names[i]
        partners[cp[0]] = cp[1]
        partners[cp[1]] = cp[0]
    inst = input()

    # Assign initial parameters
    mic_pos = 0
    yell_names = []
    congo = flatten(names, N)

    # Proceed instructions
    for i in inst:
        if i == 'F':
            # The mic holder will pass the mic to the person in front of them.
            mic_pos -= 1
            pass
        elif i == 'B':
            # The mic holder will pass the mic to the person behind them.
            mic_pos += 1
            pass
        elif i == 'R':
            mic_holder = congo.pop(mic_pos)
            congo.append(mic_holder)
            if mic_pos >= len(congo)-1:
                mic_pos = 0
            pass
        elif i == 'C':
            mic_holder = congo.pop(mic_pos)
            for pos, name in enumerate(congo):
                if name == partners[mic_holder]:
                    # Move to partner's back
                    congo.insert(pos + 1, mic_holder)
            if mic_pos >= len(congo)-1:
                mic_pos = 0
            pass
        elif i == 'P':
            # The mic holder will yell their partner’s name into the mic.
            yell_names.append(partners[congo[mic_pos]])
            pass

    for name in yell_names:
        print(name)
    print()
    for name in congo:
        print(name)

solution()