week_day_nums = []

for i in range(0, 7):
    week_day_nums.append(i)

# Combine two arrays of equal length into a dictionary of key-value pairs (to avoid having to hardcode everything as shown below)
# See the following link for more about zipping together two arrays to make a dictionary:
# link: https://stackoverflow.com/questions/7271385/how-do-i-combine-two-lists-into-a-dictionary-in-python

days_of_week = dict(zip(week_day_nums, ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']))

""" {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday'
} """

day = int(input('Day (0-6)? '))

print(days_of_week[day])