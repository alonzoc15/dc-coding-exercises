message = input('Please provide a message: ')

caesar_message = []
OFFSET = -1

alphabet_lower = [chr(i) for i in range(ord('a'),ord('z')+1)]
""" alphabet_upper = [chr(i).upper() for i in range(ord('a'),ord('z')+1)]
alphabet = [' '] + alphabet_lower + alphabet_upper """

for char in range(0, len(message)):
    caesar_message.append(alphabet_lower[(alphabet_lower.index(message[char]) + OFFSET) % 26]) if (message[char] in alphabet_lower) else caesar_message.append(message[char])

print(''.join(caesar_message))