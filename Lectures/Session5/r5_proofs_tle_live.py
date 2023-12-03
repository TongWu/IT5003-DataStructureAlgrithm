# proofs
# the TLE version... if you attended the live recitation, you will know what two lines that have to be "minimally" edited in order to solve this problem

n = int(input())

has_been_proven = [] # wrong data structure :O, do you understand why?

for line in range(1, n+1):
    assumptions, conclusion = input().split('-> ')
    assumptions = assumptions.rstrip()
    if len(assumptions) > 0:
        # print("'", assumptions, "', '", c, "'", sep='')
        for a in assumptions.split(' '):
            # print(" > ", a, sep='')
            if not a in has_been_proven: # O(n) if the data structure is wrong
                print(line) # print the 1-based line number
                exit(0) # stop the entire program

    has_been_proven.append(conclusion)

print("correct")
