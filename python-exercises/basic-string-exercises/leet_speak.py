leet_letters = ['A', 'E', 'G', 'I', 'O', 'S', 'T']
leet_numbers = [4, 3, 6, 1, 0, 5, 7]

# Use list comprehension as noted in the following link to make each number a string:
# link: https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers

leet_numbers_as_strings = [str(num) for num in leet_numbers]

leet_dict = dict(zip(leet_letters, leet_numbers_as_strings))

print(leet_dict)

user_paragraph = input('Please provide a paragraph in order to see the "leetspeak" version of it: ').upper()

def leet_converter(letter):
    return leet_dict.get(letter,letter)

leet_paragraph = []

for char in range(0, len(user_paragraph)):
    leet_paragraph.append(leet_converter(user_paragraph[char]))

print(''.join(leet_paragraph))