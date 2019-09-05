bill_amount = float(input('Total bill amount? '))
service_level = input('Level of service (good, fair, bad)? ')
split_bill_num = int(input('How many ways would you like to split the bill? '))

def tip_based_on_service(service_level):
    return {
        'good': 0.2,
        'fair': 0.15,
        'bad': 0.1
    }[service_level]

tip_amount = tip_based_on_service(service_level) * bill_amount
total_amount = bill_amount + tip_amount
amount_per_split = total_amount / split_bill_num

print('Tip amount: $%.2f' % (tip_amount))
print('Total amount: $%.2f' % (total_amount))
print('Amount per person: $%.2f' % (amount_per_split))