# Write a program that classifies a triangle based on its side lengths.

side1 = 3
side2 = 3
side3 = 3

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")

