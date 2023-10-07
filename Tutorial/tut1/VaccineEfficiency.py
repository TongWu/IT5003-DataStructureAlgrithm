def solution():
    number = int(input())
    count = 0
    A = 0
    B = 0
    C = 0
    count2 = 0
    A2 = 0
    B2 = 0
    C2 = 0
    for i in range(number):
        lst = list(input())
        if lst[0] == 'N':
            count2 += 1
            if lst[1] == 'Y':
                A2 += 1
            if lst[2] == 'Y':
                B2 += 1
            if lst[3] == 'Y':
                C2 += 1
        else:
            count += 1
            if lst[1] == 'Y':
                A += 1
            if lst[2] == 'Y':
                B += 1
            if lst[3] == 'Y':
                C += 1
    pct = lambda p, t: p/t*100
    print(format((pct(A2,count2) - pct(A,count))/(pct(A2,count2))*100, '.6f') if pct(A,count)<pct(A2,count2) else 'Not Effective')
    print(format((pct(B2,count2) - pct(B,count))/(pct(B2,count2))*100, '.6f') if pct(B,count)<pct(B2,count2) else 'Not Effective')
    print(format((pct(C2,count2) - pct(C,count))/(pct(C2,count2))*100, '.6f') if pct(C,count)<pct(C2,count2) else 'Not Effective')


solution()
