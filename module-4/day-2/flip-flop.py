tuplen = int(input("How many elements in the tuple: "))
tup2 = []
for i in range(tuplen):
    value = input("Enter element ")
    tup2.append(value)
    
if tup2 == tup2[::-1]:
    print("The tuple is a flip flop!")
else:
    print("The tuple is not a flip flop")
