'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''

# Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.
# Perimeter
# P = 2(L + W)
# Area
# A = L * W


def Area_Perim_rectangle(width, height):
 height = int(input(
  "You have given a width of 2 for the rectangle. Please enter a height so that I may calculate its area and perimeter: "))
 width = int(2)
 # calculate the Perimeter
 Perimeter = 2 * (width + height)

 # calculate the area
 Area = width * height
 # Using the "%.f" operator(floating point number).
 print(" The perimeter of rectangle with a width of 2 and the height you gave is %.f" % Perimeter)
 print("\n The area of a rectangle with a width of 2 and the height you gave is %.f" % Area)
 # or with f string
 print(f'\n The perimeter of rectangle with a width of 2 and a height of {height}')
 print(f'\n The area of a rectangle with a width of 2 and the height of {height}')


Area_Perim_rectangle(width, height)
