spots = int(input())

day1 = input()
day2 = input()
count = 0

for i in range(spots):
    if day1[i] == day2[i] == 'C':
        count += 1

print(count)
