x = int(input())
y =int(input())
z=int(input())
a=int(input())

if x<y<z<a:
    print("Fish Rising")
elif x>y>z>a:
    print("Fish Diving")
elif x==y==z==a:
    print("Fish At Constant Depth")
else:
    print("No Fish")
