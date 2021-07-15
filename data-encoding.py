# import csv

# with open("homes.csv") as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(row)

# with open("homes.csv", 'r') as file:
#      csv_file = csv.DictReader(file)
#      for row in csv_file:
#          print(row['Baths'])
         
# with open('people.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',')

#     writer.writerow(['first_name', 'surname', 'age'])
#     writer.writerow(['Joe', 'Bloggs', 40])
#     writer.writerow(['Jane', 'Smith', 50])


# with open('people.csv', mode='a') as file:
#     writer = csv.writer(file, delimiter=',')

#     writer.writerow(['Mike', 'Wazowski', 40])

    
# with open('people.csv', mode='w') as file:
#     fieldnames = ['firstname', 'lastname', 'age']
#     writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'firstname': 'Joe', 
#     'age':40,
#     'lastname':'Bloggs'
#     })

import json

# with open('example.json') as json_file:
#     data = json.load(json_file)
#     # print(data)
#     # print(data['menu']['items'])
#     for item in data['menu']['items']:
#         print(item['id'])

data = {
    'president': {
        'name': 'Zaphod Beeblebrox',
        'species': 'Betelgeusian'
    }
}

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)