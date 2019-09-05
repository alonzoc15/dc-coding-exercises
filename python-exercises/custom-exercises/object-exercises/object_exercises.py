class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []
         self.greeting_count = 0
         self.people_greeted = []

    def __str__(self):
        return f'Person object with the following properties:\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}'

    def greet(self, other_person):
         self.greeting_count += 1
         if other_person.name not in self.people_greeted:
            self.people_greeted.append(other_person.name)
         return f'Hello {other_person.name}, I am {self.name}!'

    def num_unique_people_greeted(self):
        return len(self.people_greeted)

    def contact_info(self):
        return f'{self.name}\'s email: {self.email}, {self.name}\'s phone: {self.phone}'

    def add_friend(self, friend):
        self.friends.append(friend)

    def num_friends(self):
        return len(self.friends)

# 1. Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# 2. Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

# 3. Have Sonny greet Jordan using the greet method and print the greeting to the screen.

print(sonny.greet(jordan))

# 4. Have Jordan greet Sonny using the greet method and print the greeting to the screen.

print(jordan.greet(sonny))

# 5. Write a print statement to print the contact info (email and phone) of Sonny.

print(sonny.contact_info())

# 6. Write another print statement to print the contact info of Jordan.

print(jordan.contact_info())