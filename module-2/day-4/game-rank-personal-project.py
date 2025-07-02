print("What your Osu rank says about you!")
rank = (input("Enter your rank in Osu in numbers: "))
if len(rank) == 9:
    print("You are a 9 digit in ranked (100 Millions). You definetly used this not for Osu rank.")
elif len(rank) == 8:
    print("You are a 8 digit in ranked (10 Millions). Try playing more than once.")
elif len(rank) == 7:
    print("You are a 7 digit in ranked (1 Millions). It doesnt take much time to get to 6 digit. Good luck!")
elif len(rank) == 6:
    print("You are a 6 digit in ranked (100 Thousands). You can comfortably set plays above 100pp. Good job!")
elif len(rank) == 5:
    print("You are a 5 digit in ranked (10 Thousands). This is where it starts to get competitive. Download all the farm maps in your skillset")
elif len(rank) == 4:
    print("You are a 4 digit in ranked (1 Thousands). This is around the rank where some players start to become well known. ")
elif len(rank) == 3:
    print("You are a 3 digit in ranked (1 Hundreds). Keep Pushing! Youre close to to the peak of the Mountain. There isnt a comma in your rank anymore.")
elif len(rank) == 2:
    print("You are a 2 digit in ranked (Tens). You can now consider yourself a top player.")
elif rank == "1":
    print("You are top 1 in ranked. You are truly the best who overcame all challenges and climbed to the top of the mountain. Don't give up this rank so soon.")
elif rank == "0":
    print("This feat was only achieved by player Saturos in July 30, 2008. You are not rank 0.")
elif len(rank) == 1:
    print("You are a 1 digit in ranked. You are among the best of the best and can set absolutely groundbreaking scores with ease. I doubt you are actually in this rank range but good job. ")
else:
    print("Liar.")