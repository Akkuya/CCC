x = int(input())
y = int(input())
z = int(input())

if x+y+z != 180:
    print("Error")
elif x!=y and y!=z and x!=z:
    print("Scalene")
elif x==y==z==60:
    print("Equilateral")
else:
    print("Isosceles")
