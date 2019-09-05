from pprint import pprint
from characters import characters
from houses import houses

# for character in characters:
#     if character['name'][0] == 'A':
#         pprint(character['name'])
#     if character['name'].startswith('A') == True:
#         pprint(character['name'])


# How many characters names start with "A"? # 168

def character_starts_with_a_num():
    characters_starting_with_a = []
    for character in characters:
        if character['name'][0] == 'A':
            characters_starting_with_a.append(character)
    return len(characters_starting_with_a)

# How many characters names start with "Z"? ### 8

def character_starts_with_z_num():
    characters_starting_with_z = []
    for character in characters:
        if character['name'][0] == 'Z':
            characters_starting_with_z.append(character)

    return len(characters_starting_with_z)

# How many characters are dead? ### 553

def dead_characters_num():
    dead_characters = []
    for character in characters:
        if character['died'] != '':
            dead_characters.append(character)
    
    return len(dead_characters)

# Who has the most titles? ### Balon Greyjoy with 7 titles

def character_with_most_titles():
    most_titles = 0
    character_with_most_titles = ['']
    for character in characters:
        if len(character['titles']) > most_titles:
            most_titles = len(character['titles'])
            character_with_most_titles[0] = character['name']
    
    return character_with_most_titles[0], most_titles

# How many are Valyrian? ### 57

def valyrian_num():
    valyrian_characters = []
    for character in characters:
        if character['culture'] == 'Valyrian':
            valyrian_characters.append(character)
    
    return len(valyrian_characters)

# What actor plays "Hot Pie" (and don't use IMDB)?

def actor_for_hot_pie():
    for character in characters:
        if character['name'] == 'Hot Pie':
            return character['playedBy']

# How many characters are *not* in the tv show? # 197

def characters_not_in_show_num():
    characters_not_in_show = []
    for character in characters:
        if character['tvSeries'][0] != '':
            characters_not_in_show.append(character)
    return len(characters_not_in_show)

# Produce a list of characters with the last name "Targaryen" ### 49

def targaryen_last_name_list():
    characters_last_name_targaryen = []
    for character in characters:
        if character['name'].split(' ')[-1] == 'Targaryen':
            characters_last_name_targaryen.append(character)

    return len(characters_last_name_targaryen)

# Create a histogram of the houses (it's the "allegiances" key)

def histogram_of_houses():
    unique_allegiances = []
    for character in characters:
        for allegiance in character['allegiances']:
            if allegiance not in unique_allegiances:
                unique_allegiances.append(allegiance)
    allegiance_starter_values = [0 for allegiance in unique_allegiances]
    allegiance_frequency_dict = dict(zip(unique_allegiances, allegiance_starter_values))
    for character in characters:
        for allegiance in character['allegiances']:
            allegiance_frequency_dict[allegiance] += 1
    
    return allegiance_frequency_dict

# allegiance_frequency_dict = histogram_of_houses()
# print(sorted(allegiance_frequency_dict.items(), key=lambda kv: kv[1], reverse = True))

# Actually printing the names of the houses

def histogram_of_houses_stretch():
    unique_allegiances = []
    for character in characters:
        for allegiance in character['allegiances']:
            if allegiance not in unique_allegiances:
                unique_allegiances.append(allegiance)


    allegiance_house_names = [houses[allegiance] for allegiance in unique_allegiances]
    allegiance_starter_values = [0 for allegiance in allegiance_house_names]
    allegiance_frequency_dict = dict(zip(allegiance_house_names, allegiance_starter_values))

    for character in characters:
        for allegiance in character['allegiances']:
            allegiance_frequency_dict[houses[allegiance]] += 1
    
    return allegiance_frequency_dict

print(histogram_of_houses())

# allegiance_frequency_houses_dict = histogram_of_houses_stretch()
# sorted_allegiances = sorted(allegiance_frequency_houses_dict.items(), key=lambda kv: kv[1], reverse = True)

# print('Allegiances     ||     House     ')
# for i in range(len(sorted_allegiances)):
#     print('%d     |     %s     ' % (sorted_allegiances[i][1], sorted_allegiances[i][0]))











# print(len(characters))

# # print out the key names individually
# for k in jon_snow:
#    print(k)

# # print out just the values
# for key in jon_snow:
#    print(jon_snow[key])

# # print both the key and the value
# for k in characters.jon_snow:
#    print("%s: %s" % (k, jon_snow[k]))