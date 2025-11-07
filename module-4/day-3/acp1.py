test_dict = {'Codingal': 3, 'is': 2, 'best': 4, 'for': 2, 'Coding': 1}

K = int(input("Enter the value to check frequency: "))

print("The dictionary:", test_dict)

search = 0
for key in test_dict:
    if test_dict[key] == K:
        search += 1

print(f"The value {K} has appeared {search} times.")