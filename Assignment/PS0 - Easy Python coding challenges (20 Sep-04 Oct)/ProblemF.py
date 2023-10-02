region = int(input())
pop_input = input()
population = list(map(int, pop_input.split()))
win = region//2 if region//2 < region else region//2-1
lose = region - win
max_population = 0
for _ in range(win):
    max_population += population.pop(population.index(max(population)))
for _ in range(lose):
    max_population += population[_]//2 if population[_]//2 < population[_] else population[_]//2-1
print(max_population)