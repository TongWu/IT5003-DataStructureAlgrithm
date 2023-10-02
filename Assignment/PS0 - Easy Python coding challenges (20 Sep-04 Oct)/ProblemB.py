testcase = int(input())
distance = []
for _ in range(testcase):
    lst1 = list(input().replace(' ', ''))
    lst2 = list(input().replace(' ', ''))
    numbers = [int(''.join(map(str, lst1))), int(''.join(map(str, lst2)))]
    distance.append(str(numbers[1] + numbers[0]))
for i in range(len(distance)):
    for j in range(len(distance[i])):
        if j != len(distance[i])-1:
            print(distance[i][j] + ' ', end='')
        else:
            print(distance[i][j])