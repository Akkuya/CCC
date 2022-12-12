x = int(input())

for i in range(1, x+1, 2):
  print("*"*i + " "*(x*2 - i*2) + "*"*i)

for i in range(x-2, -1, -2):
  print("*"*i + " "*(x*2 - i*2) + "*"*i)
