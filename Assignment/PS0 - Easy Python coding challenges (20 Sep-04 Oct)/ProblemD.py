A, B, C = map(int, input().split('/'))
if A > 12 and 31 >= B > 0:
    print("EU")
elif B > 12 and 31 >= A > 0:
    print("US")
else:
    print("either")