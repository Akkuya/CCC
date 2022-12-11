daytime_minutes = int(input())
evening_minutes = int(input())
weekend_minutes = int(input())


a_daytime = (daytime_minutes-100)*25
if a_daytime < 0:
    a_daytime = 0

a_evening = evening_minutes*15
a_weekend = weekend_minutes*20

b_daytime = (daytime_minutes-250)*45
if b_daytime < 0:
    b_daytime = 0

b_evening = evening_minutes*35
b_weekend = weekend_minutes*25


a_cost = format((a_daytime + a_evening + a_weekend) / 100, '.2f')
b_cost = format((b_daytime + b_evening + b_weekend) / 100, '.2f')

print(f'Plan A costs {a_cost}')
print(f'Plan B costs {b_cost}')

if a_cost > b_cost:
    print('Plan B is cheapest.')
elif a_cost < b_cost:
    print('Plan A is cheapest.')
else:
    print('Plan A and B are the same price.')
