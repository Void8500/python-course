physics = float(input("What is your physics mark? ")) #12.5
chemistry = float(input('What is your chemistry mark? '))
math = float(input('What is your math mark? '))
biology = float(input('What is your mark in biology? '))
total = physics + chemistry + math + biology

average = (total) / 4
print(f"Average: {average} total: {total}")
if total < 0 or total > 100:
    print("Invalid mark")
else:
    if total >= 70 and total <= 100:
        print("Your grade is A")
    elif total >= 60 and total <= 69:
        print("Your grade is B")
    elif total >= 50 and total <= 59:
        print("Your grade is C")
    elif total >= 40 and total <= 49:
        print("Your grade is D")
    else:
        print("Your grade is F")
