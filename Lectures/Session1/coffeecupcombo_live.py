# there are TWO subtle bugs introduced in this code

n = int(input())
s = input()
awake = ['0']*(n+1)
for i in range(n):
    if s[i] == '1': # a coffee machine here
        awake[i] = '1'
        awake[i+1] = '1'
        awake[i+2] = '1'
        # awake[i] = awake[i+1] = awake[i+2] = '1' # doing these multiple assignments is also possible
print(awake[:-2].count('0')) # the answer
