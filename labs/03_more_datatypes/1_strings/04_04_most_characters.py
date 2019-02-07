'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

st_1 = input("Please write a sentence: ")
st_2 = input("Now write a different sentence: ")
st_3 = input("One more sentence, please, different than the other two: ")

 max(st_1, st_2, st_3, key = len)
#or
if len(st_1) > (len(st_2)and len(st_3)):
    print("The first sentence has the most characters")
if len(st_2) > (len(st_1) and len(st_3)):
    print("The second sentence has the most characters")
if len(st_3) > (len(st_1) and len (st_2)):
    print ("The third sentence has the most characters")