wins = 0
for i in range(6):
    outcome = input()
    if outcome == "W":
        wins+=1
        
if wins in [1,2]:
    print("3")
    
elif wins in [3,4]:
    print("2")
    
elif wins in [5,6]:
    print("1")
    
elif wins==0:
    print("-1")
