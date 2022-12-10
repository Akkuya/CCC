adjectives = int(input())
nouns = int(input())

ad = []
no = []

for i in range(adjectives):
    x = input()
    ad.append(x)

for j in range(nouns):
    y = input()
    no.append(y)

for k in range(len(ad)):
    for l in range(len(no)):
        print(f"{ad[k]} as {no[l]}")
