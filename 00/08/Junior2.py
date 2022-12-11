letters = ["A", "B", "C", "D", "E"]

end = False

while end==False:
    button = int(input())
    number = int(input())
    for i in range(number):
        if button==1:
            letters.append(letters.pop(0))
        elif button==2:
            letters.insert(0, letters.pop())
        elif button==3:
            letters[0], letters[1] = letters[1], letters[0]
        elif button==4:
            end = True
            break
print(" ".join(letters))
