temperature = int(input())
x = 5*temperature-400
print(x)
if x < 100:
    print(1)
elif x == 100:
    print(0)
else:
    print(-1)
