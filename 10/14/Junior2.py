numberOfVotes = int(input())
votes = input()
aVotes = 0
bVotes = 0
for i in range(numberOfVotes):
    if votes[i] == "A":
        aVotes+=1
    else:
        bVotes+=1
if aVotes>bVotes:
    print("A")
elif aVotes==bVotes:
    print("Tie")
else:
    print("B")

