student_scores = {"Alice": 95,"Bob": 91,"Charlie": 72,"Diana": 91}
K = int(input("Enter search key: "))

print("The dictionary: ", student_scores)

search = 0
for key in student_scores:
    if student_scores[key] == K:
        search += 1

print(f"{K} has appeared {search} times.")