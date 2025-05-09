total = float(input("enter total marks obtained ")) #100
physics = float(input("What is your physics mark? ")) #12.5
chemistry = float(input('What is your chemistry mark? '))
math = float(input('What is your math mark? '))
biology = float(input('What is your mark in biology? '))

subjMark = total / 4 #25 

print(f'Physics Percentage: {(physics/subjMark*100):.2f} %')
print(f'Chemistry Percentage: {(chemistry/subjMark*100):.2f} %')
print(f'Maths Percentage: {(math/subjMark*100):.2f} %')
print(f'Biology Percentage: {(biology/subjMark*100):.2f} %')

average = (math + chemistry + physics + biology) / 4
print("Average: ", average)