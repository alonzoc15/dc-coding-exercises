'''
Write a word_histogram program that asks the user for a sentence as its input 
and prints a dictionary containing the tally of how many times each word in 
the alphabet was used in the text. For example:

Please enter a sentence: To be or not to be
{'to': 2, 'be': 2, 'or': 1, 'not': 1}
'''

message = input('Enter a word, expression, or message to see the frequency with which each word occurs: ').lower()

unique_words = []
frequency_dict = {}

for word in message.split(' '):
    if word not in unique_words:
        unique_words.append(word)

for word in unique_words:
    frequency_dict[word] = message.count(word)

# begin bonus challenge

frequency_dict_sorted = sorted(frequency_dict.items(), key=lambda kv: kv[1], reverse = True)
print(frequency_dict_sorted)

# for key, value in frequency_dict.items():
#     if value in top_frequency_values: