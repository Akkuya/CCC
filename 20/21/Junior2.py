players = int(input())
count = 0

for i in range(players):
    player_points = int(input())
    player_fouls = int(input())
    star_rating = player_points*5 - player_fouls*3

    if star_rating > 40:
        count += 1

if count == players:
    count = str(count) + '+'

print(count)

