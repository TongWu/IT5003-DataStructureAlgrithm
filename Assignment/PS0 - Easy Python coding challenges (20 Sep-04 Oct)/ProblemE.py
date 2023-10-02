sms = str(input())

if ':)' in sms:
    if ':(' not in sms:
        print("alive")
    else:
        print("double agent")
elif ':(' in sms:
    print('undead')
else:
    print("machine")
