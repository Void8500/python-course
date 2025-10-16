import math

angle = float(input("Enter the angle in degrees: "))

radians = math.radians(angle)
sinv = math.sin(radians)
cosv = math.cos(radians)
tanv = math.tan(radians)

print("Sine value:", sinv)
print("Cosine value:", cosv)
print("Tangent value:", tanv)
