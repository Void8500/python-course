word = input("Enter a word: ").lower()
char = input("Enter the character you want to find: ").lower()
for i in word:
    if i == char:
        print(f"{char} is found")
        break
    print("Character was not found.")