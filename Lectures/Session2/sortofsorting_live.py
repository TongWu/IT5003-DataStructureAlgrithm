# Sort of Sorting
# there are two subtle bugs inside

def first_two_characters(a): # custom named function, but this takes a few more lines
    return a[:2]

while True:
    n = int(input())
    if n == 1: break
    names = [input() for _ in range(n)]
    names.sort(key = lambda x : x[:3]) # alternatively, you can use your own custom named function, but doing so uses a bit more lines
    print(*names, sep='\n')
    print() # always print a blank like *after* each TC (forgiven by Kattis)
