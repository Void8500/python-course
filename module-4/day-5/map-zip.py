def find_cube(number):
    return number**3

list1 = [3, 5, 4]
cube = list(map(find_cube, list1))

print(cube)

zipped = zip(list1, cube)
print(list(zipped))