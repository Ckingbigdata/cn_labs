'''#Read in 10 numbers from the user. '''
numbs = input("please enter 10 numbers: ")
#Place all 10 numbers into an list in the order they were received.
lnumbs = numbs.split()
print(lnumbs)

#Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
print(lnumbs[1::2] + lnumbs[-2::-2])


#Then print out the 9th, 7th, 5th, 3rd, and 1st.

#Example input: 1,2,3,4,5,6,7,8,9,10
#Example output: 2,4,6,8,10,9,7,5,3,1