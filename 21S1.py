x = int(input())

vertical = input().split()
vertical = [int(y) for y in vertical]

horizontal = input().split()
horizontal = [int(z) for z in horizontal]

area = 0

for i in range(0, len(horizontal)):
    area += (horizontal[i] * (vertical[i] + vertical[i+1])/2)
    print(area)

            

