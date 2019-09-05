# Consider the following dictionary that represents a mapping from names to phone numbers:

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

""" INSTRUCTIONS
Write code to do the following:

    1. Print Elizabeth's phone number.
    2. Add an entry to the dictionary: Kareem's number is 938-489-1234.
    3. Delete Alice's phone entry.
    4. Change Bob's phone number to '968-345-2345'.
    5. Print all the phone entries. 
"""

error_message = 'Sorry, this does not exist.'

##### 1. Print Elizabeth's phone number.

# try to access the key directly to print its value:

print(phonebook_dict['Elizabeth']) # 484-584-2923

# try to access key's value directly but provide an error message if the key does not exist:

print(phonebook_dict.get('Elizabeth',error_message)) # 484-584-2923
print(phonebook_dict.get('Jeb',error_message)) # Sorry, this does not exist.

##### 2. Add an entry to the dictionary: Kareem's number is 938-489-1234.

phonebook_dict['Kareem'] = '938-489-1234'

##### 3. Delete Alice's phone entry.

phonebook_dict.pop('Alice')

##### 4. Change Bob's phone number to '968-345-2345'.

phonebook_dict.update({'Bob': '968-345-2345'})

##### 5. Print all the phone entries. 

phone_entries = list(phonebook_dict.values())