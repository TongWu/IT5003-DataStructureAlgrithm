# there are TWO subtle bugs introduced in this code

def digit_product(x):
    ans = 1
    while x > 0:
        last_digit = x%10
        if last_digit != 0:
            ans *= last_digit
        x /= 10
    return ans
    

x = int(input())
while x > 9: # two digits or more
#for x in range(10, 1001):
    new_x = digit_product(x)
#    print(x, "->", new_x)
    assert new_x > x
    x = new_x
print(x)
