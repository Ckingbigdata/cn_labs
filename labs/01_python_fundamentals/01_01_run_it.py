'''
1 - Write and execute a script that prints "hello world" to the console.

2 - Using the interpreter, print "hello world!" to the console.

3 - Explore the interpreter.
	- Execute lines with syntax error and see what the response is.
        * What happens if you leave out a quotation or parentheses?
        * How helpful are the error messages?
	- Use the help() function to explore what you can do with the interpreter.
        For example execute help('print').
        press q to exit.
	- Use the interpreter to perform simple math.
	- Calculate how many seconds are in a year.

'''
# 1 - Write and execute a script that prints "hello world" to the console.
print('hello world')

# 2 - Using the interpreter, print "hello world!" to the console.

# 3 - Explore the interpreter.
# 	- Execute lines with syntax error and see what the response is.
#         * What happens if you leave out a quotation or parentheses?
#         * How helpful are the error messages?
# 	- Use the help() function to explore what you can do with the interpreter.
#         For example execute help('print').
help('print')
#         press q to exit.
# 	- Use the interpreter to perform simple math.
# 	- Calculate how many seconds are in a year.




# From the previous example, move your calculation of how many seconds in a year to a python executable script.
print("How many seconds in a year? Let's find out!")
a = int(input("Enter the number of seconds in a minute "))
b = int(input("Enter the number of minutes in an hour "))
c = int(input("Enter the number of hours in a day "))
d = int(input("Enter the number of days in a year "))
print("The answer is " + str(((a * b) * c) * d))
# have trouble adding "seconds" to end of statement

print("How many seconds in a year? Let's find out!")
a = int(input("Enter the number of seconds in a minute "))
b = int(input("Enter the number of minutes in an hour "))
c = int(input("Enter the number of hours in a day "))
d = int(input("Enter the number of days in a year "))
answer = ((a * b) * c) * d
print(f'The answer is {answer:,d} seconds.')

# Write the necessary code to display the follow message to the console

#     I'm a programmer now.
#     Yeehaw!
#     Coding here I come!


print("I'm a programmer now. \nYeehaw! \nCoding here I come!")

# Write the necessary code to print the result of the following formula:
print(float((15.7 * 3.6) - (34.9 * 0.9)) / (68.9 - 2.1))

# (15.7 * 3.6 - 34.9 * 0.9) / (68.9 - 2.1)

# Write the necessary code to print out the result of the following:

# 2 + 4 + 6 + 8 + 9 + 10 + 12 + 14 + 16 + 18
print(2 + 4 + 6 + 8 + 9 + 10 + 12 + 14 + 16 + 18)

# Write the necessary code to display "Hello World!" 5 times.
print(5 * "Hello World! ")


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
