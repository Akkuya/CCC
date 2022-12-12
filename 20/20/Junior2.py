threshold = int(input())
starting_people = int(input())
infections = int(input())

day = 0
done = False
infected = starting_people

while done == False:
    infected += starting_people*infections
    print(starting_people)
    starting_people = starting_people*infections
    print(starting_people)
    print(f'Day {day}: {infected} infected')
    day+=1
    if infected > threshold:
        done = True


print(day)
