person = ['Đạt', 96, 'Viettel', 1, False, True]

# dictionary, object, map,...
person = {
    'name': 'Đạt', 
    'yob': {
        'year': 1996, 
        'month': 1,
        'day': 1
    },
    'company': ['Viettel', 'Vinaphone'],
    'key': None
}
# READ
print(person['yob'] ['year'])
print(len(person['company']))

person['relationship'] = True  # CREATE
person['yob']['month'] = 4    # UPDATE
del person['key']           # DELETE

for key in person:
    print(key, person[key])