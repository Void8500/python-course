temperature = int(input("Enter the temperature in celsius: "))

if temperature >= 25:
    print("Its warm. You can wear light clothes.")
elif temperature >= 15:
    print("Its a bit cold. You can wear a light jacket.")
else:
    print("Its cold. Wear heavy clothes like a hoodie or jacket.")