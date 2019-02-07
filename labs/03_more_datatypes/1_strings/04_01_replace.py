'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

string_input = input("please type a string of words: ")
symbol_input = input("please input a symbol: ")
x = string_input[0]
new_string = string_input.replace(x, symbol_input)
print(new_string)
