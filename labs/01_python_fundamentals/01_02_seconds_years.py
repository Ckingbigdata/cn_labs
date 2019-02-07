'''

From the previous example, move your calculation of how many seconds in a year to a python executable script.

'''

print(((60 * 60) * 24) * 365)
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
