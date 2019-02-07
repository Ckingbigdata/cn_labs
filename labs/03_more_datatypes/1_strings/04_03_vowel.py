'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''
string_input = input("please type a string of words: ")
vowels = 'a,e,i,o,u'
print(type(vowels))
counter = 0
for i in string_input.lower():
   if i in vowels:
    counter += 1
print(f'Vowels are used {counter} times in the string given')
