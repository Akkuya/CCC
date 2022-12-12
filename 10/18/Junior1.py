x = []

for i in range(4):
    x.append(int(input()))

if (x[0] == 8 or x[0] == 9) and (x[3] == 8 or x[3] == 9) and (x[1] == x[2]):
    print("ignore")
else:
    print("answer")
