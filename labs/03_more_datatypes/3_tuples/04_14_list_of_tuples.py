"""
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

"""

input = "hello world"

# t = tuple(input)
# print(t)
# for i in t:
#     if i  == (' '):
#         continue
# print(t)


# print(mylist)


chunks = []
x = 0
chunks.append([])  # create an empty chunk to which we'd append in the loop
for i in input:
    if i != ' ':
        chunks[x].append(i)
    else:
        x += 1
        chunks.append([])

print(tuple((chunks)))


# print(x)
# t = tuple(list(x))
# print(t)









