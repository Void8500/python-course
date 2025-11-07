import random
user = input("What is your name? ")
if user == "":
    user = "Mr User"
    
print(f"Welcome, {user}! Guess a number between 1-20! You have 3 attempts.")

while True:
    number = random.randint(1,20)
    
    if number%2 == 0:
        print("Hint: The number is even!")
    else:
        print("Hint: The number is odd!")
    
    for i in range(1,4):
        guess = int(input("Guess a number: "))
        
        if guess == number:
            print("You guessed correctly! The number was ", number)
        elif guess > number:
            print("Too High!")
        elif guess < number:
            print("Too low!")
    else:
        print("Sorry! You ran out of attempts. The number was", number)
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Thanks for playing, {user}!")
            break