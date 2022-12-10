x = int(input())
y = int(input())

counter = 0

for i in range(x, y+1):
    divisors = 0
    for j in range(1, i+1):
        if i%j == 0:
            divisors += 1
    
    if divisors==4:
        counter+=1

print(f"The number of RSA numbers between {x} and {y} is {counter}")
