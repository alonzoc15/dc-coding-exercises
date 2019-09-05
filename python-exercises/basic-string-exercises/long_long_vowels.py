vowels = ['a', 'e', 'i', 'o', 'u']

# Extend the vowels array to include upper- and lower-case vowels

for char in range(0, len(vowels)):
    vowels.append(vowels[char].upper())


user_expression = input('Please enter a word or phrase to see its long-long vowel version: ')

long_long_vowel_expression = []

for char in range(0, len(user_expression) - 1):
    if (user_expression[char] in vowels) and (user_expression[char] == user_expression[char+1]):
        long_long_vowel_expression.append(4 * user_expression[char])
    else:
        long_long_vowel_expression.append(user_expression[char])

long_long_vowel_expression.append(user_expression[len(user_expression)-1])

print(''.join(long_long_vowel_expression))
