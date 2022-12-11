speedLimit = int(input())
speed = int(input())

fine = 0

if speed >= speedLimit+31:
    fine = 500
elif speed <= speedLimit+30 and speed >= speedLimit+21:
    fine = 270
elif speed <= speedLimit+20 and speed >= speedLimit+1:
    fine = 100

if speed <= speedLimit:
    print("Congratulations, you are within the speed limit!")
else:
    print(f"You are speeding and your fine is ${fine}.")
    

