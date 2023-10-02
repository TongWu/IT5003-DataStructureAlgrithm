classNum = int(input())
isCoffeeMachine = str(input())
coffee = [1, 1]
hold_count = 0


def fillCoffee():
    return [1, 1]


def drink(c):
    return c[:-1]


for i in range(classNum):
    if int(isCoffeeMachine[i]):
        coffee = fillCoffee()
        hold_count += 1
    else:
        if not coffee:
            break
        else:
            coffee = drink(coffee)
            hold_count += 1
print(hold_count)