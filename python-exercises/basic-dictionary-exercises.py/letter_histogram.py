'''
Write a letter_histogram program that asks the user for input
and prints a dictionary containing the tally of how many times 
each letter in the alphabet was used in the word. For example:

Please enter a word: banana
{'a': 3, 'b': 1, 'n': 2}
'''

message = input('Enter a word, expression, or message to see its character frequencies: ')

unique_chars = []
frequency_dict = {}

alphabet_lower = [chr(i) for i in range(ord('a'),ord('z')+1)]
alphabet_upper = [chr(i).upper() for i in range(ord('a'),ord('z')+1)]
alphabet = alphabet_lower + alphabet_upper

for char in message:
    if (char not in unique_chars) and (char in alphabet):
        unique_chars.append(char)

for char in unique_chars:
    frequency_dict[char] = message.count(char)

print(frequency_dict)