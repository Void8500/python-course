days = int(input("How many days do you want to predict: "))
weather = []
for i in range(days):
    day = input("Enter weather for day (s for sunny, r for rainy): ")
    weather.append(day)
    
weather = tuple(weather)
print(weather)

sunny = 0
rainy = 0

for i in range(len(weather)):
    if weather[i] == "r":
        rainy += 1
    else:
        sunny +=1
        
if sunny > rainy:
    print("Good Weather")
else:
    print("Bad weather")