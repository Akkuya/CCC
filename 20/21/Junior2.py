bidders = int(input())
highestbid = 0
currentWinner = None

for i in range(bidders):
    bidderName = input()
    bidAmount = int(input())
    if bidAmount > highestbid:
        highestbid = bidAmount
        currentWinner = bidderName

print(currentWinner)
