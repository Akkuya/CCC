rounds = int(input())
antonia = 100
david = 100

for i in range(rounds):
    x = input().split()
    x = [int(y) for y in x]

    if x[0] < x[1]:
        antonia -= x[1]
    elif x[1] < x[0]:
        david -= x[0]
    

print(antonia, david, sep="\n")
