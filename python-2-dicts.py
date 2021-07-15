car = {
'brand': 'Ford',
'model': 'Mustang',
'year' : 1964,
'isNew': False
}

# 1
# car['colour'] = 'silver'
# print(car['colour'])
# print(car.get('colour'))

# 2
# car['model'] = 'Porsche'
# print(car['model'])

# 3
# del car['model']
# print(car)

# 4
for key, value in car.items():
    print(f'key: {key}, value: {value}')
# for key, value in car.items():
#     print(f'key: {key}, value: {value}')


