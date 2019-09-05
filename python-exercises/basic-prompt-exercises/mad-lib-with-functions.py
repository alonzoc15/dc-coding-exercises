person = input('What is your name? ')
subject = input('What is your favorite subject? ')

def fix_name(person):
    return person.capitalize()

def make_mad_lib(person, subject):
    fixed_name = fix_name(person)
    mad_lib = print('Your name is %s and your favorite subject is %s.' % (fixed_name, subject))

    return mad_lib

make_mad_lib(person,subject)