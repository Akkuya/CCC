x = int(input())
t = 0
s = 0
for i in range(x):
  string = input().lower()

  t += string.count("t")
  s += string.count("s")


if s>=t:
  print("French")
else:
  print("English")
