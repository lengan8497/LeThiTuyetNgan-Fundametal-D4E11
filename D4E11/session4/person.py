person = ['Đạt', 96, 'Viettel', 1, False, True]

# dictionary, object, map
# person = {
#     'name': 'Đạt', 
#     'yob': 96, 
#     'company': 'Viettel'
# }
# print(person)



# person = {
#     'name': 'Đạt', 
#     'yob': 96, 
#     'company': 'Viettel',
#     'key': None
# }
# name = person['name']
# print(person['name'])



# person = {
#     'name': 'Đạt', 
#     'yob': {
#         'year': 1996,
#         'month': 1,
#         'day': 1
#     }, 
#     'company': ['Viettel', 'Vinaphone'],
#     'key': None
# }
# name = person['name']
# print(person['yob']['year'])
# print(len(person['company']))



# person = {
#     'name': 'Đạt', 
#     'yob': {
#         'year': 1996,
#         'month': 1,
#         'day': 1
#     }, 
#     'company': ['Viettel', 'Vinaphone'],
#     'key': None
# }
# name = person['name']

# for key in person:
#     print(key)



person = {
    'name': 'Đức',
    'name': 'Đạt', 
    'yob': {
        'year': 1996,
        'month': 1,
        'day': 1
    }, 
    'company': ['Viettel', 'Vinaphone'],
    'key': None
}
name = person['name']
for key in person:   # READ
    print(key, person[key])
person['relationship'] = True   # CREATE
person['yob']['month'] = 4   # UPDATE
del person['key']   # DELETE
for key in person:   # READ
    print(key, person[key])
