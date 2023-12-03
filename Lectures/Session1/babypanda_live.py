# there are TWO subtle bugs introduced in this code

# the longer version

n, m = map(int, input().split())
sneeze = 0
while m > 0:
    m /= 2
    if m%2 == 1:
        sneeze -= 1
print(sneeze)


# the one liner version
# print(bin(int(input().split()[0])).count('0'))
