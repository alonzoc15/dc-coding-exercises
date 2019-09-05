# Consider the following dictionary:

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

'''
INSTRUCTIONS:
Write code to do the following:

    1. Get Ramit's email address.
    2. Get the first of Ramit's interests.
    3. Get Jasmine's email address.
    4. Get the second of Jan's two interests.
'''


# 1. Get Ramit's email address.

ramit['email']

# 2. Get the first of Ramit's interests.

ramit['interests'][0]

# 3. Get Jasmine's email address.

print(ramit['friends'][0]['email'])

# 4. Get the second of Jan's two interests.

print(ramit['friends'][0]['interests'][1])