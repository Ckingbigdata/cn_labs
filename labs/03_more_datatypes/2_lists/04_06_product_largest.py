'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.

'''

numbs = input("please enter 10 numbers: ")
lnumbs = numbs.split()

#calculate the sum

print("Calculating sum of element of input list")
sum = 0
for num in lnumbs:
    sum += int(num)
print("Sum of list = ",sum)


# Also, find the largest number in the list.
lnumbs.sort(key=int)

print("Highest number in list = ", lnumbs[-1])