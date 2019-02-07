'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4

'''

string_input = input("please type a string of words: ")
letter_input = input("please type a letter included somewhere in your string: ")
finder = string_input.find(letter_input)
print(f'Your letter first occurs in the {finder}th postion')
#or by index
finder = string_input.index(letter_input)
print(f'Your letter first occurs in the {finder}th position.')


