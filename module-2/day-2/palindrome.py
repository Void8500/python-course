original = input("Enter a word: ").lower()
reverse = ''
for i in original:
    reverse = i + reverse
print(f"The original text {original}")
print(f"The reversed text {reverse}")
if original == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")