week_day_nums = []

for i in range(0, 7):
    week_day_nums.append(i)

days_of_week = dict(zip(week_day_nums, ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']))

day = int(input('Day (0-6)? '))

# Use a ternary operator to see if the day supplied is a weekend day (0 or 6) or a weekday (1 through 5)

print('Go to work!') if (1 <= day <= 5) else print('Go to sleep!')