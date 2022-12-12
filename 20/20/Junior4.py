t = input()
s = input()
x = False
for i in range(len(s)):
  if s in t:
    print("yes")
    x = True
    break
  s = s[1:] + s[0]
if x == False:
    print("no")
