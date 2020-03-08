# 3. App to calculate the hypotenuse and the area of a right-angled triangle
# Write a console programme that
# (1) Allows users to enter two numbers as length of legs
# (2) Makes sure what users entered are valid
# (3) Calculated and prints the hypotenuse and the area of the triangle
from math import sqrt

def isleg(value):
	try:
		if (float(value) > 0):
		    return True
	except ValueError:
		return False

print("Exercise 01_03: App to calculate the hypotenuse and the area of a right-angled triangle")

leg_1 = 0
leg_2 = 0

while not(isleg(leg_1)):
  leg_1 = input("Please input the number of first leg: ")
leg_1 = float(leg_1)

while not(isleg(leg_2)):
  leg_2 = input("Please input the number of second leg: ")
leg_2 = float(leg_2)

hypotenuse = sqrt(leg_1**2 + leg_2**2)
print("The hypotenuse is: {}".format(hypotenuse))

area = (leg_1 * leg_2 / 2)
print("The area of the right-angled triangle is: {}".format(area))