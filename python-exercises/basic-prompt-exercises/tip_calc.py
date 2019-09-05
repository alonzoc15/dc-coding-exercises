bill_amount = float(input('Total bill amount? '))
service_level = input('Level of service (good, fair, bad)? ')

# Use a "switch-statement"-ish construction for Python; see the link below for more on this:
# link: https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python

def tip_based_on_service(service_level):
    return {
        'good': 0.2,
        'fair': 0.15,
        'bad': 0.1
    }[service_level]

tip_amount = tip_based_on_service(service_level) * bill_amount
total_amount = bill_amount + tip_amount

print('Tip amount: $%.2f' % (tip_amount))
print('Total amount: $%.2f' % (total_amount))

