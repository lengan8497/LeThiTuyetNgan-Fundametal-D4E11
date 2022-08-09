from pymongo import MongoClient

client = MongoClient()   # Tao ra ket noi voi MongoDB qua bien client

db = client.get_database('d4e11')   # Tu bien client/hoac nhung gi co san de tao ra database

collection = db.get_collection('members')   # tu database da lay/tao ra de lay/tao ra collection

# collection.insert_one({   # CREATE
#     'name': 'Đạt',
#     'age': 24,
#     'gender': True
# })


# collection.insert_many(
#   [
#     {  
#     'name': 'Đạt1',
#     'age': 24,
#     'gender': True
#     },
#     {  
#     'name': 'Đạt2',
#     'age': 24,
#     'gender': True
#     },
#     {  
#     'name': 'Đạt3',
#     'age': 24,
#     'gender': True
#     },
#   ]
# )


members = collection.find()
for member in members:
    print(member)

