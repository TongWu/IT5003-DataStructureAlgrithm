# Problem A - Metronome

A Metronome is a mechanical device used by musicians for keeping time. It is a very clever device, based on a spring, an inverted pendulum, and an escapement gear. Milo is learning to play the glockenspiel, and has purchased a metronome to help him keep time. Milo has noticed that for every complete turn (one revolution) of the key, the metronome will give four ticks. Milo wants the metronome to stop at the end of each song that he tries to play.

For a given song, how many revolutions must he wind the key?

## **Input**

The single line of input contains a single integer $n$ ($1\le n le 10^5$), which is the length of the song in ticks.

## **Output**

Output a single real number, which is the number of revolutions Milo must turn the metronome’s key so that it stops precisely at the end of the song. This number must be accurate to two decimal places.

## Sample

| Sample Input 1 | Sample Output 1 |
| -------------- | --------------- |
| `16 `          | `4.0 `          |

| Sample Input 2 | Sample Output 2 |
| -------------- | --------------- |
| `99 `          | `24.75`         |

## Solution

```python
t = int(input())
r = t / 4
print(f"{r:.2f}")
```



# Problem B - Code to Save Lives

Daenerys and her fellow friends decided to go on a magical adventure to find the mystical scientist to cure her village of disease. On her adventure she faces the winter and desert until she finally found the genius scientist, and while Daenerys explained her dire situation to the scientist, the scientist agreed to save her village under one condition.

She must prove her village is worthy of saving by solving the following problem: given that numbers are observing numerical distancing, which means they each need a space in between each digit, provide the sum of two numerically distanced numbers. For example, the numerically distanced numbers $3 \ 4 \ 5$ and $5\ 6\ 7$ sum to $9\ 1\ 2$

## Input

The input consists of 3 different segments:

1. The first line will have the number of test cases $t$, where $1≤t≤10$.
2. The first line of each case will contain the first positive numerically distanced whole number, which will have the number’s digits, $0 – 9$, be space-separated. The amount of digits in this line is $m$, where $1≤m≤9$.
3. The second line of each case will contain the second positive numerically distanced whole number, which will have the number’s digits, $0 – 9$, be space-separated. The amount of digits in this line is $n$, where $1≤n≤9$.

## Output

Output the sum of the numerically distanced numbers for each of the test cases on one line each.

## Sample

| Sample Input 1             | Sample Output 1 |
| -------------------------- | --------------- |
| `2 3 4 5 5 6 7 6 1 3 2 5 ` | `9 1 2 3 8 6 `  |

| Sample Input 2         | Sample Output 2 |
| ---------------------- | --------------- |
| `1 1 4 8 0 5 4 3 8 4 ` | `1 9 1 8 9 `    |

| Sample Input 3                 | Sample Output 3   |
| ------------------------------ | ----------------- |
| `3 4 4 5 7 6 6 2 7 8 2 0 2 3 ` | `4 9 7 0 3 8 4 3` |

## Solution

```python
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
```



# Problem C Adding Trouble

Your friend Bob is really bad at adding numbers, and he’d like some help to make sure he’s doing it correctly! Can you help Bob make sure he is adding correctly? Given 3 integers $A,\ B,\ C$ make sure that $A+B=C$, and that Bob indeed added $A$ and $B$ correctly.

## Input

The input consists of a single line with 3 integers $A,\ B,\ C$ where $−10^9≤A,B,C≤10^9$.

## Output

Output either `correct!` if $A+B=C$, or `wrong!` if $A+B≠C$.

| Sample Input 1 | Sample Output 1 |
| -------------- | --------------- |
| `2 3 5 `       | `correct! `     |

| Sample Input 2 | Sample Output 2 |
| -------------- | --------------- |
| `1 1 3 `       | `wrong! `       |

| Sample Input 3 | Sample Output 3 |
| -------------- | --------------- |
| `-1 1 0 `      | `correct!`      |

## Solution

```python
A, B, C = map(int, input().split())
if A + B == C:
    print("correct!")
else:
    print("wrong!")
```

# Problem D International Dates

You read a lot of documents that come from the United States, Europe, and other countries around the world. The issue is that their date formats aren’t consistent! The US formats their dates as MM/DD/YYYY while in Europe they format it as DD/MM/YYYY. That is, in the US the month comes before the day, while in Europe the day comes first. Given a date, can you determine if its *definitely* the US format, for sure European, or could be either? (Note that there are even more date formats, but luckily since the year is guaranteed to be last in this case, we only have to worry about these 2 formats.)

## Input

The input consists of a single string comprised of 3 integers separated by forward slashes, as $AA/BB/CCCC$, where $1≤AA$,$BB≤31$, and $0≤CCCC≤9999$. It is guaranteed that the given string will be a valid date for at least one of the formats. You can assume that all 12 months have exactly 31 days, so there is no need to worry about months with 30 days, or February.

## Output

Output either `US` if the date doesn’t conform to the European format, or `EU` if the date doesn’t conform to the US format. Otherwise, output `either` if there is no way to know for sure which format the date follows.

## Sample

| Sample Input 1 | Sample Output 1 |
| -------------- | --------------- |
| `25/03/2023 `  | `EU `           |

| Sample Input 2 | Sample Output 2 |
| -------------- | --------------- |
| `04/02/2023 `  | `either `       |

| Sample Input 3 | Sample Output 3 |
| -------------- | --------------- |
| `07/23/1972 `  | `US`            |

## Solution

```python
A, B, C = map(int, input().split('/'))
if A > 12 and 31 >= B > 0:
    print("EU")
elif B > 12 and 31 >= A > 0:
    print("US")
else:
    print("either")
```

# Problem E Undead or Alive

Now that zombies have learned to use SMS messaging, it is imperative to develop software for detecting zombies over text. After many long months of study, the top scientists have figured out how to do it. The key observation is that humans only use smiley faces, represented by the exact substring `:)`, and zombies only use frowny faces, represented by the exact substring `:(`. However, upon realizing this, double agents were trained to use both kinds of emoticons at once! Your job is to write a program to determine who a given message is from.

## Input

The input will consist of a single line of text, no longer than 160 characters, containing letters, numbers, spaces, and any of the following symbols: `.,'!?:)(`.

## Output

- If the line contains only smiley faces and no frowny faces, then output `alive`.
- If the line contains only frowny faces and no smiley faces, then output `undead`.
- If the line contains both smiley faces and frowny faces, then output `double agent`.
- Otherwise, output `machine`.

## Sample

| Sample Input 1            | Sample Output 1 |
| ------------------------- | --------------- |
| `Hello, how are you? :) ` | `alive `        |

| Sample Input 2                 | Sample Output 2 |
| ------------------------------ | --------------- |
| `Hey there! :( What's up? :( ` | `undead `       |

| Sample Input 3                                               | Sample Output 3 |
| ------------------------------------------------------------ | --------------- |
| `::(Braaaains... are very useful for programming contests:)) ` | `double agent ` |

| Sample Input 4                             | Sample Output 4 |
| ------------------------------------------ | --------------- |
| `Sandy, when will my order be delivered? ` | `machine `      |

| Sample Input 5                                  | Sample Output 5 |
| ----------------------------------------------- | --------------- |
| `Firing up EmoticonBot... (:  : (  ):  :D  c: ` | `machine`       |

## Solution

```python
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
```

# Problem F Election Paradox

In Oddland, the leader of the country is determined by a democratic election. The country is divided into an odd number of regions, in which each region has an odd number of voters.

There are two (an even number!) political parties in Oddland, and the winning party is the one that wins the most number of regions. A party wins a region if it receives more votes than the other party in that region.

Under this system, it is possible that the losing party receives more votes than the winning party. For example, if there are three regions with 11, 3, and 3 people, respectively, then a party could receive 8, 1, and 1 votes and lose the election. In this case, the losing party received the majority of the votes in the total population.

Determine the largest number of votes a party can receive and still lose the election.

## Input

The first line of input contains an odd integer $N$ $(3≤N≤999)$, which is the number of regions in Oddland.

The next line contains $N$ odd integers $p_i$ $(1≤p_i≤999)$, which are the populations of the N cities.

## Output

Display the largest number of votes a party can receive and still lose the election.

## Sample

| Sample Input 1 | Sample Output 1 |
| -------------- | --------------- |
| `3 11 3 3 `    | `13`            |

## Solution

```python
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
```

# Problem G Digit Product

Consider a positive integer $x$. Multiply its nonzero digits and you get another integer $y$. Repeating this process, you eventually arrive at a single digit between $1$ and $9$. Write a program that reads $x$ and outputs the resulting digit.

## Input

An integer $x$ with $10≤x≤1000$.

## Output

Print a digit between $1$ and $9$, the result of repeatedly multiplying the nonzero digits of $x$ as described above.

## Explanation of Sample Inputs

In Sample Input 1, we have $x=808$. Multiplying $8$ and $8$, we arrive at $64.$ Then we get $6⋅4=24$, and finally $2⋅4=8$, which is the sample output.

In Sample Input 2, there is only a single nonzero digit, $2$. The product of all digits in a set containing only a single element is the digit itself. Thus the answer is $2$.

## Sample

| Sample Input 1 | Sample Output 1 |
| -------------- | --------------- |
| `808 `         | `8 `            |

| Sample Input 2 | Sample Output 2 |
| -------------- | --------------- |
| `20 `          | `2`             |

## Solution

```python
ori_num = str(input())
while len(ori_num) > 1:
    rounded_num = 1
    for i in range(len(ori_num)):
        rounded_num *= int(ori_num[i]) if int(ori_num[i]) > 0 else 1
    ori_num = str(rounded_num)
print(int(ori_num))
```

# Problem H Coffee Cup Combo

Jonna is a university student who attends $n$ lectures every day. Since most lectures are way too simple for an algorithmic expert such as Jonna, she can only stay awake during a lecture if she is drinking coffee. During a single lecture she needs to drink exactly one cup of coffee to stay awake.

Some of the lecture halls have coffee machines, so Jonna can always make sure to get coffee there. Furthermore, when Jonna leaves a lecture hall, she can bring at most two coffee cups with her to the following lectures (one cup in each hand). But note that she cannot bring more than two coffee cups with her at any given time.

Given which of Jonna’s lectures have coffee machines, compute the maximum number of lectures during which Jonna can stay awake.

## Input

The first line contains the integers $n$ $(1≤n≤105)$, the number of lectures Jonna attends.

The second line contains a string $s$ of length $n$. The $i$’th letter is `1` if there is a coffee machine in the $i$’th lecture hall, and otherwise it is `0`.

## Output

Print one integer, the maximum number of lectures during which Jonna can stay awake.

## Sample

| Sample Input 1   | Sample Output 1 |
| ---------------- | --------------- |
| `10 0100010100 ` | `8 `            |

| Sample Input 2   | Sample Output 2 |
| ---------------- | --------------- |
| `10 1100000000 ` | `4 `            |

| Sample Input 3 | Sample Output 3 |
| -------------- | --------------- |
| `1 0 `         | `0`             |