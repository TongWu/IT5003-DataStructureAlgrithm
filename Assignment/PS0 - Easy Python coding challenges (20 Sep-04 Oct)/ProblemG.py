ori_num = str(input())
while len(ori_num) > 1:
    rounded_num = 1
    for i in range(len(ori_num)):
        rounded_num *= int(ori_num[i]) if int(ori_num[i]) > 0 else 1
    ori_num = str(rounded_num)
print(int(ori_num))