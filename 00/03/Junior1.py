height = int(input())
spacing = int(input())
handle = int(input())

for i in range(height):
    print("*" + (" ")*spacing + "*" + (" ")*spacing + "*")

print("*"*(spacing*2+3))
for i in range(handle):
    print(" "*(spacing+1) + "*")
