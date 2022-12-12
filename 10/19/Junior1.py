a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

a_score = ((a*3)+(b*2)+(c*1))

b_score = ((d*3)+(e*2)+(f*1))

if (a_score < b_score):
    print("B")
elif (a_score == b_score):
    print("T")
elif (a_score > b_score):
    print("A")
